---
abstract: Ansible role that installs glances.
authors:
  - name: Xander Harris
    email: xandertheharris@Gmail.com
title: Ansible glances role
---

Install glances on the target hosts enable systemd service and
Prometheus exporter.

## Glances Requirements

A working Python installation and the ability to write to {file}`/etc`.

## Glances Role Variables

N/A

## Glances Dependencies

N/A

## Example Playbook

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

## License

MIT

## Author Information

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>

```

<!-- vim: set ft=markdown colorcolumn=80: -->
