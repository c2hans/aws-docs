---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-events-view.html
---

# View automation events details
<a name="automation-events-view"></a>

Select an automation event ID to view more details and step history on **Event details** page.

**To view automation event details**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Automation rules** under the **Automation** section.

1. Choose the event ID of the automation event you want to get details for.

1. You can perform the following actions on the **Event details** page:

   - View details such as event status, estimated savings, created time, and completed time

   - View step history of operations performed during the automation event. Each step shows the specific action taken to modify your resource, along with its own step status, start time, and completion time.

   - Initiate a roll back for the automation event.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
