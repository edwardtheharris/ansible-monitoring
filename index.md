---
abstract: This is a collection of roles used to deploy
  a standardized monitoring package to the authors computing
  resources.
authors:
  - name: Xander Harris
    email: xandertheharris@gmail.com
date: 2025-06-27
title: Ansible Monitoring Index
---

## Roles

```{toctree}
:caption: roles

roles/exporters/readme
roles/glances/readme
roles/grafana/readme
roles/promtail/readme
```

```{index} playbooks; ca

```

## Readme and other metadata

```{toctree}
:maxdepth: 1

readme
changelog
license
security
```

```{index} metadata; repository

```

### Glossary

```{glossary}
ArchLinux
  [ArchLinux](https://archlinux.org) os A simple, lightweight distribution

glances
  [Glances](https://glances.readthedocs.io/en/latest/index.html) is a
  cross-platform monitoring tool that aims to present maximum information in
  minimal space through either a curses-based or Web-based interface. It can
  dynamically adapt the displayed information depending on the terminal size.

Grafana
  [Grafana](https://grafana.com/) is an observability tool that enables
  centralized storage and analysis of metrics and logs from external sources.

Kubernetes
  [Kubernetes](https://kubernetes.io/), also known as K8s, is an open source
  system for automating  deployment, scaling, and management of containerized
  applications.

Prometheus
  [Prometheus](https://prometheus.io/) provides open source metrics and
  monitoring for your systems and services.

promtail
  [promtail](https://grafana.com/docs/loki/latest/send-data/promtail/) is now
  deprecated in favor of Grafana Alloy.

systemd
  [systemd](https://systemd.io/) is a suite of basic building blocks for a Linux
  system. It provides a system and service manager that runs as PID 1 and
  starts the rest of the system.

YAML
  [YAML Ain't Markup Language™](https://yaml.org/) is a human-friendly data serialization
  language for all programming languages. It is much better than JSON.

yay
  [Yet Another Yogurt](https://github.com/Jguer/yay) is an AUR Helper Written in Go.
```

### Indices and tables

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`
