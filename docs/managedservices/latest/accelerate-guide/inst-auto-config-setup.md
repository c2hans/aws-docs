---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/inst-auto-config-setup.html
---

# Automated instance configuration setup
<a name="inst-auto-config-setup"></a>

Assuming the prerequisites have been met, adding a specific Amazon EC2 instance tag automatically initiates the AMS Accelerate automated instance configuration. Use one of the following methods to add this tag:

1. (Strongly recommended) Use the AMS Accelerate Resource Tagger

   To configure the tagging logic for your account, see [How tagging works](acc-tag-intro.md#acc-tag-how-works). After tagging is complete, tags and automated instance configuration are handled automatically.

1. Manually add tags

   Manually add the following tag to the Amazon EC2 instances:

   Key:**ams:rt:ams-managed**, Value:**true**.

**Note**
The instance configuration service attempts to apply the required AMS configurations once the **ams:rt:ams-managed** tag is applied to the instance. The service asserts the AMS required configurations whenever an instance is started, and when a the AMS daily configuration check occurs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
