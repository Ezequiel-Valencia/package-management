# Package management (Ansible)

## Setup
`make deps` installs the `community.general` collection.

## Choosing hosts
Set `target_hosts` at the top of `site.yml` to a host, group, or pattern from `inventory.yml`
(`linux`, `mac`, `wsl`, ...). Override it for one run with `-e target_hosts=mac`.

## Per-host packages
Each host has its own `host_vars/<host>.yml`:
- `package_managers` sets the managers to try for each package type, in order of preference.
- `package_lists` names the lists from `group_vars/all/package_list_<name>.yml` that the host installs.

To add a machine, add it to `inventory.yml` and create `host_vars/<host>.yml`.

## Commands
`make run | update | configure | container_stack | stop_container_stack | status_container_stack`

You're asked for the sudo password (`become_ask_pass`). Output is logged to `ansible.log`.
## Uninstalling
To remove a package, move its entry from its package list to
`group_vars/all/package_list_uninstall.yml`. The next `make run` uninstalls it on every selected host
before installing. Packages that aren't installed are skipped.
