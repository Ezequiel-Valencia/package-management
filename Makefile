.PHONY: deps
deps: ## Install required Ansible collections.
	@ansible-galaxy collection install -r requirements.yml

.PHONY: run
run: ## Install packages.
	@echo "🚀 Installing apps."
	@ansible-playbook playbooks/site.yml -e pm_command=install

.PHONY: update
update: ## Update packages.
	@echo "🚀 Updating apps."
	@ansible-playbook playbooks/site.yml -e pm_command=update

.PHONY: configure
configure: ## Configure packages.
	@echo "🚀 Configuring apps."
	@ansible-playbook playbooks/site.yml -e pm_command=configure

.PHONY: container_stack
container_stack: ## Start the container stack.
	@echo "🚀 Starting container stack."
	@ansible-playbook playbooks/site.yml -e pm_command=container_stack -e container_action=start

.PHONY: stop_container_stack
stop_container_stack: ## Stop the container stack.
	@echo "🚀 Stopping container stack."
	@ansible-playbook playbooks/site.yml -e pm_command=container_stack -e container_action=stop

.PHONY: status_container_stack
status_container_stack: ## Show container stack status.
	@echo "🚀 Container stack status."
	@ansible-playbook playbooks/site.yml -e pm_command=container_stack -e container_action=status

.PHONY: check
check: ## Syntax-check the playbook.
	@ansible-playbook playbooks/site.yml --syntax-check

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
