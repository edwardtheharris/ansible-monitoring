---
abstract: Readme for the Prometheus exporters Ansible
  role.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2025-06-27
title: exporters role
---

Install {term}`Prometheus` exporters.

## Exporters Requirements

- Target hosts running {term}`ArchLinux`.
- {term}`yay` installed on target hosts.
- A running {term}`Prometheus` instance.

## Exporters Role Variables

N/A

## Exporters Dependencies

N/A

## Exporters Example Playbook

An example playbook is given below.

```{code-block} yaml
:caption: site.yml
- hosts: all
  roles:
    - role: exporters
      tags:
        - exporters
```

## Exporters License

[Copyright (c) 2025](project:/license.md)

## Exporters Author Information

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>

```
