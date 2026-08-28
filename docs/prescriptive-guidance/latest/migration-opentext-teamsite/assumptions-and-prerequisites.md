---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-opentext-teamsite/assumptions-and-prerequisites.html
---

# Assumptions and prerequisites
<a name="assumptions-and-prerequisites"></a>

This guide's source architecture is not hosted on virtual machines (VMs). The guide also assumes that you won't update OpenText versions during your migration. If you want to update an OpenText TeamSite version or upgrade from Open Text MediaBin to Media Management, you should carry out your migration and then implement any required upgrades or updates.

Finally, the guide assumes that there is no significant refactoring of your OpenText architecture.

Refactoring should be limited to supporting applications that might be containerized or migrated to AWS Lambda functions. We recommend that you migrate the existing application landscape and then makes changes to your workloads on the AWS Cloud.

The following table provides information about the resources that must be available for your migration project.

|
|
| Resources | Usage |
| --- |--- |
| Access to all required source infrastructure resources | Accelerate the delivery and avoid waiting for access requests to be granted |
| Infrastructure experts (for example, technical architects and system administrators) | Discovery of current infrastructure |
| Solution experts for your current OpenText or related applications | Discovery of application landscape and identify dependencies |
| A group of final users, including content contributors and final users of supported web applications | User acceptance testing (UAT) and validation of the new platform |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
