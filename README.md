# JDownloader Docker pipeline

Install JDownloader via Ansible and Docker

## Prequisites

- Ubuntu host with SSH access enabled

## Configure

### 1. Create an Inventory

Create an inventory

```yaml
GROUP-NAME:  # <- change to name matching group_vars name
  children:
    jdownloader:
      hosts:
        MY-UBUNTU-HOST: # <- change to server hostname
          ansible_ssh_user: REMOTE-USER  # <- change to server username
```

### 2. Add `group_vars` directory

Add a new directory in  `group_vars` directory. Give it the same name
as the group name used in the inventory.

### 3. Create `vars.yml` for the group

Create a `vars.yml` to hold non-sensitive variables

```yaml
---
# ansible vars
jdownloader_uid: # User ID for JDownloader to use when creating files (default: 1000)
jdownloader_gid: # Group ID for JDownloader to use when creating files (default: 1000)

# docker vars
install_version: # Docker image version to use (e.g. "v1.5.2" or "latest")
container_name: # Docker container name to create (e.g. "jdownloader")
```

### 4. Create `vault.yml` for hte group

Create a `vault.yml` to hold sensitive variables

```
ansible-vault create playbook/group_vars/<MY_GROUP>/vault.yml
```

```yaml
# ansible vars
ansible_user: # remote ansible user
ansible_become_user: # (optional) privilege escalation user (e.g. "root")
ansible_become_password: # (optional) password for privilege escalation

# paths
base_data_dir: # directory for jdownload folders (e.g. "/home/my-user/jdownloader")

# MyJDownloader
# These variables will need to be set in the console
# after install is finished
my_jd_email: # email address for MyJDownloader login
my_jd_password: # password for MyJDownlaoder login
jd_device_name: # Device name.
```

## Run playbook

```
ansible-playbook ./playbook/main.yml \
  -i ./inventories/homelab.yml \
  --vault-password-file ~/.vault_pass.txt \
  --private-key=~/.ssh/id_rsa
```

## Post-Setup

JDownloader instance can be access via web console at
`http://MY-HOST:5800`

Set the username, password, and device name 

```
My.JDownloader tab -> My Account
```
