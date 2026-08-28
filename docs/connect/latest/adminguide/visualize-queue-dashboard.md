---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/visualize-queue-dashboard.html
---

# Visualize historical queue data in Connect Customer
<a name="visualize-queue-dashboard"></a>

You can visualize historical queue data using time series graphs to help identify patterns, trends, and outliers such as Service Level, Contacts Queued, and Average Handle Time.

**To view queue data**

1. On the **Real-time Metrics** page, display the Queues table.

1. Select **View queue graphs** from the dropdown menu. The following image shows the dropdown menu for a queue named **test queue**.
![The view queue graphs option in the test queue dropdown menu.](http://docs.aws.amazon.com/connect/latest/adminguide/images/hmr-queue-dashboard-ui.png)

1. After you select **View queue graphs**, you are directed to the queue visualization dashboard.

1. The Queue dashboard automatically refreshes every 15 minutes. You can:
   + Configure a time range of up to 24 hours.
   + Select the channel of your choice.
   + Customize the service level thresholds.

   The following image shows an example Queue dashboard. It displays a graph of service level data for the queue. **Time range** is set to **Previous 24 hours to future 24 hours**. **Channel** is set to **All channels**. **Service level** is set to **60 seconds**.
![An example Queue dashboard, a graph of data.](http://docs.aws.amazon.com/connect/latest/adminguide/images/hmr-queue-dashboard-exp.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
