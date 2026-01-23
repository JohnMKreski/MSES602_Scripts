# Lab 2 – Ansible and Jenkins Automation

## Overview

This lab focused on using **Ansible** to automate the installation and configuration of **Jenkins** on a headless Ubuntu Server. The primary goal was to understand how configuration management tools support DevOps workflows by making system setup repeatable, auditable, and less error-prone compared to manual configuration.

All work was performed on a remote Ubuntu Server accessed via SSH. Ansible playbooks and roles were used to install required dependencies, configure the Jenkins package repository, and verify that Jenkins was running correctly. The lab emphasized understanding *why* certain steps were required, particularly around package signing and service management, rather than simply executing commands.

---

## Environment and Setup

* [Ubuntu Server](../system.md) (headless)
* Accessed via SSH
* Ansible installed using `pip --user`
* Inventory targeting the local system (`127.0.0.1`)
* Jenkins installed as a systemd service

The Ansible playbook was executed locally on the server with elevated privileges where required.

---

## Jenkins Installation with Ansible

### Package and Repository Configuration

Ansible was used to:

* Install prerequisite packages such as `ca-certificates` and `gnupg`
* Add the Jenkins APT repository using a **signed-by keyring** instead of the deprecated `apt-key` mechanism
* Update the package cache and install Jenkins from the official Jenkins repository

During this process, additional troubleshooting was required to resolve repository signature verification errors. This highlighted the importance of correctly managing GPG keys and aligning repository definitions with the expected signing keys.

### Service Verification

After installation, Jenkins was verified by:

* Confirming the Jenkins Java process was running
* Checking that Jenkins was listening on port `8080`
* Accessing the Jenkins web interface via SSH port forwarding

These checks ensured Jenkins was properly installed and running as a managed system service.

---

## Initial Jenkins Configuration

Upon first access to the Jenkins web interface, the initial setup wizard was completed. This included:

* Unlocking Jenkins using the generated admin password
* Installing the default (suggested) plugins
* Completing the initial administrator setup

Once setup was complete, the Jenkins dashboard and management options became available for further inspection.

---

## Plugin Review

The default plugin set installed by Jenkins provides a broad baseline of functionality. Key observations include:

* Core plugins support source control integration, credential management, and pipeline execution
* Additional plugins enable multibranch pipelines, notifications, and job organization
* Many installed plugins act as internal libraries or dependencies rather than direct user-facing features

Overall, the default plugin selection is sufficient for a basic self-hosted CI environment without requiring immediate customization.

---

## Use Cases for Self-Hosting CI

For a locally self-hosted CI server, the default Jenkins plugin set supports several common and practical use cases:

- **Source control–driven builds**, using Git and GitHub integrations to automatically trigger jobs on commits or pull requests  
- **Automated test execution**, with structured reporting of build and test results  
- **Credential-safe automation**, allowing secrets such as tokens or SSH keys to be injected into jobs without being stored in source code  
- **Multibranch workflows**, enabling different branches to be built and tested independently  
- **Basic access control and auditing**, suitable for personal projects or small teams  

Many installed plugins exist primarily as supporting libraries rather than standalone features. For a self-hosted learning or development environment, the default plugin set provides a solid baseline, while more specialized plugins can be evaluated and added later as requirements grow.


---

## Reflection

This lab demonstrated the value of Ansible for infrastructure provisioning tasks. Compared to scripting similar steps in Python, Ansible provides a more approachable and maintainable solution by offering declarative modules for common system operations such as package management, repository configuration, and service control.

While Python remains flexible and powerful, using it for this task would require assembling multiple libraries and writing additional logic to ensure idempotence and error handling. Ansible abstracts much of this complexity, making it better suited for repeatable DevOps workflows.

This exercise reinforced the distinction between **provisioning tools** (Ansible) and **continuous automation platforms** (Jenkins), and how they complement each other in real-world DevOps environments.

---

## References

* Regis University's MSES602 Repository: [https://github.com/RegisUniversity/MSES602_ansible.git](https://github.com/RegisUniversity/MSES602_ansible.git)

* Ansible Documentation: [https://docs.ansible.com/](https://docs.ansible.com/)
* Jenkins Documentation: [https://www.jenkins.io/doc/](https://www.jenkins.io/doc/)
* Jenkins Debian Packages: [https://pkg.jenkins.io/debian-stable/](https://pkg.jenkins.io/debian-stable/)
* Ubuntu Server Documentation: [https://ubuntu.com/server/docs](https://ubuntu.com/server/docs)

## AI Additional Tools

ChatGPT and Microsoft Copilot were used as supplemental tools for troubleshooting, documentation review, and clarification of Ansible and Jenkins concepts, consistent with modern DevOps workflows.

* OpenAI, ChatGPT: [https://openai.com/chatgpt](https://openai.com/chatgpt)
* Microsoft Copilot: [https://learn.microsoft.com/en-us/copilot/](https://learn.microsoft.com/en-us/copilot/)
