---
abstract: Ansible role that installs grafana.
authors:
  - name: Xander Harris
    email: xandertheharris@Gmail.com
title: grafana role
---

Install {term}`grafana` on the target hosts, configure a {term}`systemd`
service and export to {term}`Prometheus`.

## grafana Requirements

A working Python installation and the ability to write to {file}`/etc`.

## grafana Role Variables

N/A

## grafana Dependencies

N/A

## grafana Example Playbook

This can be run using a playbook similar to the one below.

```{code-block} yaml
:caption: site.yml

- hosts: servers
  become: true
  roles:
    - role: grafana
      tags:
        - grafana
      vars:
        x: 42
```

## grafana License

[Copyright (c) 2025](project:/license.md)

## grafana Author Information

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>

```

<!-- vim: set ft=markdown colorcolumn=80: -->
