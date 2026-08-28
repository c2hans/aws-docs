---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-monitors-edit.html
---

# Edit a monitor in Network Flow Monitor
<a name="CloudWatch-NetworkFlowMonitor-configure-monitors-edit"></a>

You can edit a monitor at any time, to add or remove network flows.

Note that you can't change the name of a monitor after you create it.

**Important**
These steps are designed to be completed all at once. You won't be able to save any in-process work to continue later.

**To edit a monitor using the console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the left navigation pane, under **Network Monitoring**, choose **Flow monitors**.

1. On the **Monitors** tab, select a monitor, and then under the **Actions** menu, choose **Edit**.

1. Select the local or remote resources that you want add or remove for the monitor. If you have multiple accounts in your scope, specify the account where the resources are located, and then choose resources.

1. When you're finished updating the monitor, choose **Next**, to review and confirm the network flows to monitor.

1. Choose **Save monitor**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
