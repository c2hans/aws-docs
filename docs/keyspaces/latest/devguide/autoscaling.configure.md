---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.configure.html
---

# Configure and update Amazon Keyspaces automatic scaling policies
<a name="autoscaling.configure"></a>

You can use the console, CQL, or the AWS Command Line Interface (AWS CLI) to configure Amazon Keyspaces automatic scaling for new and existing tables. You can also modify automatic scaling settings or disable automatic scaling.

 For more advanced features like setting scale-in and scale-out cooldown times, we recommend that you use CQL or the AWS CLI to manage Amazon Keyspaces scaling policies.

**Topics**
+ [Configure permissions for Amazon Keyspaces automatic scaling](autoscaling.permissions.md)
+ [Create a new table with automatic scaling](autoscaling.createTable.md)
+ [Configure automatic scaling on an existing table](autoscaling.configureTable.md)
+ [View your table's Amazon Keyspaces auto scaling configuration](autoscaling.viewPolicy.md)
+ [Turn off Amazon Keyspaces auto scaling for a table](autoscaling.turnoff.md)
+ [View auto scaling activity for a Amazon Keyspaces table in Amazon CloudWatch](autoscaling.activity.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
