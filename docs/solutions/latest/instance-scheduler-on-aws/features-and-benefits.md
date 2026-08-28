---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

The Instance Schedule on AWS solution provides the following features:

 **Cross-account instance scheduling**

This solution includes a template that creates the [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) (IAM) roles necessary to start and stop instances in secondary accounts. For more information, refer to the [Cross-account instance scheduling](cross-account-instance-scheduling-using-account-ids-or-aws-organization-id.md) section.

 **Automated tagging**

Instance Scheduler on AWS can automatically add tags to all instances that it starts or stops. The solution also includes macros that allow you to add variable information to the tags.

 **Configure schedules or periods using Scheduler CLI**

This solution includes a command line interface (CLI) that provides commands for configuring schedules and periods. The CLI allows customers to estimate cost savings for a given schedule. For more information, refer to the [Scheduler CLI](scheduler-cli.md).

 **Manage schedules using Infrastructure as Code (IaC)**

This solution provides an AWS CloudFormation Custom Resource that you can use to manage schedules using Infrastructure as Code (IaC). For more information, refer to [Manage Schedules Using Infrastructure as Code](manage-schedules-using-infrastructure-as-code-iac.md).

 **Integration with Systems Manager Maintenance Windows**

For Amazon EC2 instances, Instance Scheduler on AWS can integrate with [AWS Systems Manager](https://aws.amazon.com/systems-manager/) maintenance windows, defined in the same Region as those instances, to start and stop them in accordance with the maintenance window.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Instance Scheduler on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
