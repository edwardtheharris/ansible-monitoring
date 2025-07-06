---
abstract: Ansible role that installs and configures grafana.
authors:
  - name: Xander Harris
    email: xandertheharris@Gmail.com
title: grafana role
---

Install {term}`Grafana` on the target hosts, configure a {term}`systemd`
service and export to {term}`Prometheus`.

## {term}`Grafana` Requirements

This role has the following requirements.

1. A working Python installation.
2. The ability to write to {file}`/etc`.
3. A system running {term}`ArchLinux`.

## {term}`Grafana` Role Variables

|variable|description|default|
|---|---|---|
|grafana_db_pass|Password for the database|postgres|
|grafana_db_type|Type of database (`mysql`, `postgres`, `sqlite`)|postgres|
|grafana_db_url|URL of the database connection|postgres://grafana:grafana@localhost:5432/grafana|
|grafana_domain|Domain name of the Grafana instance|grafana.local|
|grafana_redis_connect|Connection information for Redis|addr=127.0.0.1:6379,pool_size=100,db=0,ssl=false|
|grafana_trusted_csrf|Accepted request origins|grafana.local localhost|

## {term}`Grafana` Dependencies

N/A

## {term}`Grafana` Example Playbook

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

## {term}`Grafana` License

[Copyright (c) 2025](project:/license.md)

## {term}`Grafana` Role Author Information

```{sectionauthor} Xander Harris <xandertheharris@gmail.com>

```

<!-- vim: set ft=markdown colorcolumn=80: -->
