---
source_url: https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-audit-frameworks.html
---

# Working with audit frameworks
<a name="working-with-audit-frameworks"></a>

A *framework* is a collection of controls that helps you to evaluate your backup practices. You can use pre-built, customizable controls to define your policies and evaluate whether your backup practices comply with your policies. You can also set up automatic daily reports to gain insights into the compliance status of your frameworks.

Each framework applies to a single account and AWS Region. You can deploy a maximum of 15 frameworks per account per Region. You cannot deploy duplicate frameworks (frameworks that contain the same controls and parameters).

There are two different types of frameworks:
+ The **AWS Backup framework** (recommended) – Use the AWS Backup framework to deploy all available controls to monitor your backup activity, coverage, and resources against the best practices that we recommend.
+ A **custom framework** that you define – Use a custom framework to choose one or more specific controls and to customize control parameters.

**Topics**
+ [Choosing your controls](choosing-controls.md)
+ [Turning on resource tracking](turning-on-resource-tracking.md)
+ [Creating frameworks using the AWS Backup console](creating-frameworks-console.md)
+ [Creating frameworks using the AWS Backup API](creating-frameworks-api.md)
+ [Viewing framework compliance status](viewing-frameworks.md)
+ [Finding non-compliant resources](finding-non-compliant-resources.md)
+ [Updating audit frameworks](updating-frameworks.md)
+ [Deleting audit frameworks](deleting-frameworks.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
