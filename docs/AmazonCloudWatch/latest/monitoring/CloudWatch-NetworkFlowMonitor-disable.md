---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-disable.html
---

# Delete scope for Network Flow Monitor
<a name="CloudWatch-NetworkFlowMonitor-disable"></a>

If you decide that you no longer want to monitor network flows using Network Flow Monitor, you can delete your Network Flow Monitor scope. When you delete your scope, you can no longer see network performance information.

Before you can delete your scope, you must delete all monitors. Be aware that it can take about 15 minutes to complete removing monitors after you request to delete them. For more information, see [Delete a monitor in Network Flow Monitor](CloudWatch-NetworkFlowMonitor-configure-monitors-delete.md).

**To delete your scope**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the left navigation pane, under **Network Monitoring**, choose **Flow monitors**.

1. On the **Settings** tab, choose **Delete scope**.

1. In the dialog box, enter confirmation text, and then choose **Delete scope**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
