# sl_viewer

A containerized vulnerability simulation environment designed for:

- CVE validation workflows
- SBOM generation and comparison
- Vulnerable package tracking
- POWER vs x86 scan testing
- Remediation workflow verification

This project intentionally includes an older `rsync` package version
to simulate real-world vulnerable container environments.

---

## 🎯 Purpose

`sl_viewer` is used to validate:

- Container vulnerability scanners
- CVE remediation pipelines
- SBOM drift analysis
- Architecture-specific vulnerability differences
- Compliance scanning integrations

---

## 🐳 Build Image

```bash
docker build -t sl-viewer .
