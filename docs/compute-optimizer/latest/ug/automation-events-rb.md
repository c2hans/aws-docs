---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-events-rb.html
---

# Roll back automation events
<a name="automation-events-rb"></a>

You can also initiate rollback for automation events if necessary. You can select and roll back up to 10 automation events at a time. You can only initiate rollback for events with Complete status.

**To roll back an automation event**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Automation rules** under the **Automation** section.

1. Select the automation events that you want to roll back. You can select up to 10 events at a time to roll back.

1. Choose **Rollback events**.

1. Review your selected automation events to roll back.

1. Choose **Confirm all rollbacks**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
