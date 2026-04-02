.PHONY: run
run: ##
	@echo "🚀 Installing apps."
	@python3 main.py install

.PHONY: update
update: ##
	@echo "🚀 Updating apps."
	@python3 main.py update

.PHONY: configure
configure: ##
	@echo "🚀 Configuring apps."
	@python3 main.py configure

.PHONY: container_stack
container_stack: ##
	@echo "🚀 Configuring apps."
	@python3 main.py container_stack start

.PHONY: stop_container_stack
stop_container_stack: ##
	@echo "🚀 Configuring apps."
	@python3 main.py container_stack stop

.PHONY: status_container_stack
status_container_stack: ##
	@echo "🚀 Configuring apps."
	@python3 main.py container_stack stop

.PHONY: publish
publish: ##
	@echo "🚀 Publishing Package."
	@./publish.sh

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Checking lock file consistency with 'pyproject.toml'"
	@uv lock --locked
	@echo "🚀 Linting code: Running pre-commit"
	@uv run pre-commit run -a
	@echo "🚀 Static type checking: Running mypy"
	@uv run mypy
	@echo "🚀 Checking for obsolete dependencies: Running deptry"
	@uv run deptry .

.PHONY: help
help:
	@uv run python -c "import re; \
	[[print(f'\033[36m{m[0]:<20}\033[0m {m[1]}') for m in re.findall(r'^([a-zA-Z_-]+):.*?## (.*)$$', open(makefile).read(), re.M)] for makefile in ('$(MAKEFILE_LIST)').strip().split()]"

.DEFAULT_GOAL := help