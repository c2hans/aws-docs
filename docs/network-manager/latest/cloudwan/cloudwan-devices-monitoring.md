---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-devices-monitoring.html
---

# Monitor devices in an AWS Cloud WAN global network
<a name="cloudwan-devices-monitoring"></a>

Monitor device Amazon CloudWatch events on the AWS Cloud WAN Monitoring page.

**To monitor devices**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**.

1. Choose the **Monitoring** tab.

1. The **Monitoring** page displays data for the following:
   + **Data In**
   + **Data Out**
   + **Tunnel down count Average**

   (Optional) Metrics and events use the default time set up in the CloudWatch Events event. To set a custom time frame, choose **Custom** and then choose a **Relative** or **Absolute** time, and then choose if you want to see that date range in **UTC** or the edge location's **Local time zone**.

   Choose **Add to dashboard** to add this metric to your CloudWatch dashboard. For more information about using CloudWatch dashboards, see [Using Amazon CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) in the *Amazon CloudWatch User Guide*.
**Note**
The **Add to dashboard** option only works if your registered transit gateway is in the US West (Oregon) Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
