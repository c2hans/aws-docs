---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-tag-req-ins-config.html
---

# Configuring tags for EC2 instances in Accelerate
<a name="acc-tag-req-ins-config"></a>

AMS Accelerate manages agents on your Amazon EC2 instances, such as the SSM agent and the CloudWatch agent. For more information about this service offering, see [Automated instance configuration in AMS Accelerate](acc-inst-auto-config.md)

To opt-in to have your Amazon EC2 instances managed by AMS Accelerate, you must apply the following tag to your Amazon EC2 instances:

| Key | Value |
| --- | --- |
| ams:rt:ams-managed | true |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
