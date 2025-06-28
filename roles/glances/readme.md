---
abstract: Ansible role that installs glances.
authors:
  - name: Xander Harris
    email: xandertheharris@Gmail.com
title: Ansible glances role
---

Install {term}`glances` on the target hosts, configure a {term}`systemd`
service and export to {term}`Prometheus`.

## Glances Requirements

A working Python installation and the ability to write to {file}`/etc`.

## Glances Role Variables

N/A

## Glances Dependencies

N/A

## Glances Example Playbook

This can be run using a playbook similar to the one below.

```{code-block} yaml
:caption: site.yml

- hosts: servers
  become: true
  roles:
    - role: glances
      tags:
        - glances
      vars:
        x: 42
```

## Glances License

[Copyright (c) 2025](project:/license.md)

## Glances Author Information

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>

```

<!-- vim: set ft=markdown colorcolumn=80: -->
