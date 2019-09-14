# JDownloader Docker pipeline

## Run playbook

```
ansible-playbook ./playbook/main.yml \
  -i ./inventories/homelab.yml \
  --vault-password-file ~/.vault_pass.txt \
  --private-key=~/.ssh/id_rsa
```