---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/view-queue-and-fleet.html
---

# View queue and fleet details in Deadline Cloud
<a name="view-queue-and-fleet"></a>

You can use the Deadline Cloud monitor to view the configuration of the queues and fleets in your farm. You can also use the monitor to see a list of the jobs in a queue or the workers in a fleet.

You must have `VIEWING` permission to view queue and fleet details. If the details don't display, contact your administrator to get the correct permissions.

**To view queue details**

1. [Open the Deadline Cloud monitor](open-deadline-cloud-monitor.md).

1. From the list of farms, choose the farm that contains the queue that you're interested in.

1. In the list of queues, choose a queue to display its details. To compare the configuration of two or more queues, select more than one check box.

1. To see a list of jobs in the queue, choose the queue name from the list of queues or from the details panel.

If the monitor is already open, you can select the queue from the **Queues** list in the left navigation pane.

**To view fleet details**

1. [Open the Deadline Cloud monitor](open-deadline-cloud-monitor.md).

1. From the list of farms, choose the farm that contains the fleet that you're interested in.

1. In **Farm resources**, choose **Fleets**.

1. In the list of fleets, choose a fleet to display its details. To compare the configuration of two or more fleets, select more than one check box.

1. To see a list of workers in the fleet, choose the fleet name from the list of fleets or from the details panel.

If the monitor is already open, you can select the fleet from the **Fleets** list in the left navigation pane.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
