---
source_url: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-delete.html
---

# Deleting connections in EventBridge
<a name="eb-target-connection-delete"></a>

You can delete a connection if you are no longer using it.

**To delete a connection using the EventBridge console**

1. Log in to AWS using an account that has permissions to manage EventBridge and open the [EventBridge console](https://console.aws.amazon.com/events).

1. In the left navigation pane, under **Integration**, choose **Connections**.

1. In the **Connections** table, choose the connection.

1. On the **Connection details** page, choose **Delete**.

**To delete a connection using the AWS CLI**
+ Use the `[delete-connection](https://docs.aws.amazon.com/cli/latest/reference/events/delete-connection.html)` command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
