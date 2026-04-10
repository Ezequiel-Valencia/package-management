#!/usr/bin/env bash
# Security scan script for this repository.
# Uses: gitleaks, trufflehog, syft, grype, osv-scanner, trivy
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPORT_DIR="$REPO_ROOT/security_reports"
mkdir -p "$REPORT_DIR"

PASS=0
FAIL=0

# ── Helpers ─────────────────────────────────────────────────────────────────

header() { echo; echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; echo "  $1"; echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; }

require() {
    if ! command -v "$1" &>/dev/null; then
        echo "  [SKIP] '$1' not found — install it via security.py to enable this scan."
        return 1
    fi
    return 0
}

result() {
    if [ "$1" -eq 0 ]; then
        echo "  [PASS] $2"
        PASS=$((PASS + 1))
    else
        echo "  [FAIL] $2 — see $3"
        FAIL=$((FAIL + 1))
    fi
}

# ── 1. Gitleaks — secret scan across entire git history ──────────────────────

header "1/6  Gitleaks · secrets in git history"
if require gitleaks; then
    OUT="$REPORT_DIR/gitleaks.json"
    set +e
    gitleaks detect \
        --source "$REPO_ROOT" \
        --report-format json \
        --report-path "$OUT" \
        --redact \
        --no-banner \
        2>&1
    LEAKS_EXIT=$?
    set -e
    # gitleaks exits 1 when leaks are found
    if [ "$LEAKS_EXIT" -eq 0 ]; then
        result 0 "No secrets detected"
    else
        LEAKS=$(grep -c '"RuleID"' "$OUT" 2>/dev/null || true)
        LEAKS=${LEAKS:-0}
        result 1 "$LEAKS secret(s) detected" "$OUT"
    fi
fi

# ── 2. Trufflehog — deep entropy + pattern scan ───────────────────────────────

header "2/6  Trufflehog · deep secret scan"
if require trufflehog; then
    OUT="$REPORT_DIR/trufflehog.json"
    trufflehog git \
        "file://$REPO_ROOT" \
        --json \
        --no-update \
        > "$OUT" 2>&1 || true
    FINDINGS=$(grep -c '"SourceMetadata"' "$OUT" 2>/dev/null || true)
    FINDINGS=${FINDINGS:-0}
    if [ "$FINDINGS" -eq 0 ]; then
        result 0 "No secrets detected"
    else
        result 1 "$FINDINGS finding(s) detected" "$OUT"
    fi
fi

# ── 3. Syft — generate SBOM ──────────────────────────────────────────────────

header "3/6  Syft · generate SBOM"
if require syft; then
    SBOM="$REPORT_DIR/sbom.syft.json"
    syft dir:"$REPO_ROOT" \
        --output syft-json="$SBOM" \
        --quiet
    result 0 "SBOM written to $SBOM"
fi

# ── 4. Grype — scan SBOM for CVEs ────────────────────────────────────────────

header "4/6  Grype · CVE scan"
if require grype && [ -f "$REPORT_DIR/sbom.syft.json" ]; then
    OUT="$REPORT_DIR/grype.json"
    set +e
    grype "sbom:$REPORT_DIR/sbom.syft.json" \
        --output json \
        --file "$OUT" \
        --quiet
    EXIT=$?
    set -e
    # grype exits 1 when vulnerabilities are found
    if [ "$EXIT" -eq 0 ]; then
        result 0 "No CVEs found"
    else
        VULNS=$(grep -c '"matchDetails"' "$OUT" 2>/dev/null || true)
        VULNS=${VULNS:-0}
        result 1 "$VULNS CVE(s) found" "$OUT"
    fi
elif require grype; then
    echo "  [SKIP] Grype requires the Syft SBOM — run step 3 first."
fi

# ── 5. OSV-Scanner — dependency vulnerability scan ───────────────────────────

header "5/6  OSV-Scanner · dependency vulnerabilities"
if require osv-scanner; then
    OUT="$REPORT_DIR/osv.json"
    set +e
    osv-scanner \
        --format json \
        --output-file "$OUT" \
        --lockfile "pyproject.toml:$REPO_ROOT/pyproject.toml" \
        2>&1
    EXIT=$?
    set -e
    # osv-scanner exits 1 when vulnerabilities are found
    if [ "$EXIT" -eq 0 ]; then
        result 0 "No known vulnerabilities in dependencies"
    else
        VULNS=$(grep -c '"vulnId"' "$OUT" 2>/dev/null || true)
        VULNS=${VULNS:-0}
        result 1 "$VULNS vulnerability/vulnerabilities found in dependencies" "$OUT"
    fi
fi

# ── 6. Trivy — filesystem misconfiguration scan ──────────────────────────────

header "6/6  Trivy · filesystem & misconfiguration scan"
if require trivy; then
    OUT="$REPORT_DIR/trivy.json"
    set +e
    trivy fs \
        --format json \
        --output "$OUT" \
        --quiet \
        "$REPO_ROOT"
    EXIT=$?
    set -e
    # trivy exits 1 when issues are found
    if [ "$EXIT" -eq 0 ]; then
        result 0 "No issues found"
    else
        VULNS=$(grep -c '"VulnerabilityID"' "$OUT" 2>/dev/null || true)
        VULNS=${VULNS:-0}
        MISCONFS=$(grep -c '"AVDID"' "$OUT" 2>/dev/null || true)
        MISCONFS=${MISCONFS:-0}
        ISSUES=$((VULNS + MISCONFS))
        result 1 "$ISSUES issue(s) found" "$OUT"
    fi
fi

# ── Summary ──────────────────────────────────────────────────────────────────

echo
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Summary: $PASS passed · $FAIL failed"
echo "  Reports written to: $REPORT_DIR/"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

[ "$FAIL" -eq 0 ]
