---
abstract: Readme providing basic usage for the standard monitoring package
  used by the author for systesms on his network.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2025-06-27
title: Ansible Monitoring Readme
---

## Assumptions

The default configuration assumes a vault password exists at
{file}`/etc/ansible/vault`. It also assumes the inventory file is in {term}`YAML`
format and located at {file}`/etc/ansible/hosts.yml`

## Usage

You can find an example inventory file below, this inventory is intended
to house a bare metal {term}`Kubernetes` cluster with a single control
plane and three nodes. This inventory is an example only and does not
represent any actual resources.

```{code-block} yaml
:caption: /etc/ansible/hosts.yaml

all:
  hosts:
    kcp01.example.com:
      ansible_user: user
    k8s01.example.com:
      ansible_user: user
    k8s02.example.com:
      ansible_user: user
    k8s02.example.com:
      ansible_user: user
kcp:
  hosts:
    kcp01.example.com:
      ansible_user: user
kcp:
  hosts:
    kcp01.example.com:
      ansible_user: user
    kcp02.example.com:
      ansible_user: user
    kcp03.example.com:
      ansible_user: user
```
