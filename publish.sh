#!/bin/bash

rm -rf ./dist
VERSION=$(uv version --short)
echo "Current version is ${VERSION}"
read -p "Set new version (default is the same): " NEW_VERSION
NEW_VERSION=${NEW_VERSION:-${VERSION}}
uv version ${NEW_VERSION}
uv build
read -s -p "Token for pypi: " TOKEN
uv publish --token=${TOKEN}


