---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/monitor-task-creation.html
---

# Monitor task creation in Connect Customer
<a name="monitor-task-creation"></a>

After your connection is established, if it stops working, in Connect Customer disassociate the connection, and then re-establish it. If that doesn't solve the issue, do the following:

**Zendesk**

1. Go to the EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. Check the status of the event source connection to see if it is active.

**Salesforce**

1. Go to the Amazon AppFlow console at [https://console.aws.amazon.com/appflow)](https://console.aws.amazon.com/appflow).

1. Monitor the flow that was created for the account that was set up.

The following image shows what a flow looks like in the Amazon AppFlow console for Salesforce. It contains information about the status of the connection, and when it was last run.

![The Amazon AppFlow console for Salesforce.](http://docs.aws.amazon.com/connect/latest/adminguide/images/salesforce-appflow-flow.png)

For both Zendesk and Salesforce, you can go to the EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/) to see your connection state and see if it is active, pending, or deleted.

The following image shows an example EventBridge console.

![An example EventBridge console.](http://docs.aws.amazon.com/connect/latest/adminguide/images/eventbridge-zendesk-salesforce-connection-health.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
