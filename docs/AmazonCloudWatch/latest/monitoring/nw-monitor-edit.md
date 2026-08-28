---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/nw-monitor-edit.html
---

# Edit a monitor
<a name="nw-monitor-edit"></a>

You can edit information for a Network Synthetic Monitor, including change the name, setting a new aggregation period, or adding or removing tags. Changing a monitor's information does not change any of its associated probes.

You can work with monitors and probes by using either the Amazon CloudWatch console or the AWS Command Line Interface. To work with Network Synthetic Monitor programmatically, see the [Network Synthetic Monitor API Reference](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html) and [networkmonitor](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/) in the AWS Command Line Interface Command Reference.

**To edit a monitor using the console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/), and then, under **Network Monitoring**, choose **Synthetic monitors**.

1. In the **Monitors** section, choose the monitor that you want to edit.

1. On the monitor dashboard page, choose **Edit**.

1. For the **Monitor name**, enter the new name for the monitor.

1. For the **Aggregation period**, choose how often you want to send metrics to CloudWatch. Valid periods are:
   + **30 seconds**
   + **60 seconds**
**Note**
A shorter aggregation period provides faster detection of network issues. However, the aggregation period that you choose can affect your billing costs. For more information about pricing, see the [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/) page.

1. (Optional) In the **Tags** section, add **Key** and **Value** pairs to further help identify this resource, allowing you to search or filter on specific information. You can also just change the **Value** of any current **Key**.

   1. Choose **Add new tag**.

   1. Enter a **Key** name and associated **Value**.

   1. Choose **Add new tag** to add the new tag.

      You can add multiple tags by choosing **Add new tag**, or you can remove a tag by choosing **Remove**.

   1. If you want to associate your tags with the monitor, keep **Add tags to probes created by monitor** checked. This adds the tags to the monitor probes, which can be helpful if you're using tag-based authentication or metering.

1. Choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
