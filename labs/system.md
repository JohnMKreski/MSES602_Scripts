# System Environment

## Purpose

This document provides high-level context for the system environment used to complete the MSES602 DevOps labs. It is intended to help readers (and future reference) understand how and where the lab work was performed, while avoiding disclosure of sensitive system details.

The information here explains environmental assumptions that may affect script behavior, outputs, or configuration choices, and clarifies differences from any default classroom virtual machine referenced in the lab instructions.

---

## Hardware and Host Context

* **Platform**: Dedicated personal server (bare metal, not a virtual machine)
* **Access model**: Headless; accessed remotely via SSH
* **Primary use**: Personal DevOps lab and system experimentation

Using a bare-metal server more closely resembles real operational environments than a preconfigured course VM, particularly in terms of service management, resource visibility, and startup behavior.

---

## Operating System

* **Distribution**: Ubuntu Server
* **Interface**: Command-line only (no local GUI)
* **User model**: Non-root administrative user with `sudo` privileges

Administrative tasks were performed using `sudo` only when required. Scripts were not executed as root by default.

---

## Access and Tooling

### Remote Access

* SSH access from a local workstation
* Terminal-based workflow using standard Linux utilities

### Development and Editing

* **Python**: Installed via Ubuntu system packages
* **Git**: Installed via Ubuntu system packages
* **Editors**:

  * Terminal editors (e.g., nano) for basic edits
  * VS Code with Remote SSH for navigation and editing convenience

VS Code Remote SSH was used strictly as a remote interface. All execution, file operations, and Git actions occurred on the server itself.

---

## Python Environment

* **Python version**: System-managed Python 3
* **Package management**: `pip3`
* **Virtual environments**: Optional and not required for lab completion

Most lab scripts rely on Python’s standard library. When third-party packages were required (for example, `psutil`), they were installed in a straightforward manner to reflect common server-side workflows.

---

## Version Control Workflow

* Repositories cloned directly onto the server
* Changes committed and pushed from the server environment
* Branch protection enabled on the main branch to reduce accidental changes

This mirrors common DevOps practices where systems maintain working copies of repositories and infrastructure changes are tracked through version control.

---

## Security and Safety Considerations

* Scripts are designed to be **read-only** and non-destructive
* No credentials, secrets, hostnames, or network identifiers are committed
* Environment-specific values are externalized or excluded via ignored files

All lab work was intentionally structured to inspect system state without modifying users, services, or core configuration.

---

## Summary

The system environment was intentionally chosen to balance realism and safety. Working on a headless Ubuntu Server with standard tooling provided practical exposure to DevOps-style workflows while maintaining appropriate safeguards for a personal lab environment.

---

## References

* Ubuntu Server Documentation: [https://ubuntu.com/server/docs](https://ubuntu.com/server/docs)

## AI Additional Tools

ChatGPT and Microsoft Copilot were used as supplemental tools for research, documentation review, and clarification of concepts, consistent with professional DevOps and software engineering workflows.

* OpenAI, ChatGPT: [https://openai.com/chatgpt](https://openai.com/chatgpt)
* Microsoft Copilot: [https://learn.microsoft.com/en-us/copilot/](https://learn.microsoft.com/en-us/copilot/)
