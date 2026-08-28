---
source_url: https://docs.aws.amazon.com/sap/latest/sap-netweaver/automation-os-patching.html
---

# Automated operating system patching
<a name="automation-os-patching"></a>

Patch management is an ongoing activity that is a key part of the SAP software lifecycle. It is a critical step in improving security, minimizing risk, remaining compliant, and reducing unplanned downtime. You can use AWS Systems Manager to automate system patching activities. Systems Manager can reduce the manual effort that is required to manage the SAP landscape, which saves time and IT resources.

An operating system patching strategy should adhere to SAP software lifecycle best practices. Patches should be applied downstream across the landscape, from development, to test, to production. This allows the patches to be tested in less-critical systems before deploying them into production. Because patching is a repeatable process, it can be automated with Systems Manager and can be documented as a standard operating procedures (SOP). This will ensure consistent patch management across the SAP landscape. The SOP should be updated continuously for future maintenance activities.

The sections below describe how to use Systems Manager to apply regular patches that are released by operating system vendors.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
