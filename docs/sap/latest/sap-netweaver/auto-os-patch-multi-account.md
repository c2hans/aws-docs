---
source_url: https://docs.aws.amazon.com/sap/latest/sap-netweaver/auto-os-patch-multi-account.html
---

# Considerations for multiple accounts
<a name="auto-os-patch-multi-account"></a>

When you run SAP workloads in AWS, you must consider an AWS account strategy that meets the security controls of your organization. For example, you might separate SAP from non-SAP workloads and separate production from non-production environments. AWS Systems Manager does not support multi-account patching.

In every AWS account with SAP workloads, patch baselines should be created and patch execution should be performed to ensure that patching is applied to all SAP systems. In a multi-account environment, this should also follow the SAP best practice of patching in the development account, then test, and finally in the production AWS account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
