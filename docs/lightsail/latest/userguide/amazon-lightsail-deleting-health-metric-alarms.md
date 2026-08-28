---
source_url: https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-deleting-health-metric-alarms.html
---

# Delete or disable Lightsail metric alarms
<a name="amazon-lightsail-deleting-health-metric-alarms"></a>

You can delete an Amazon Lightsail alarm to stop notifications of when the metric being monitored by the alarm crosses a threshold. You can also disable the alarm to stop receiving notifications. For more information, see [Alarms](amazon-lightsail-alarms.md).

**Contents**
+ [Delete metric alarms using the Lightsail console](#deleting-alarms)
+ [Disable and enable metric alarms using the Lightsail console](#disable-alarms)

## Delete metric alarms using the Lightsail console
<a name="deleting-alarms"></a>

Complete the following steps to delete a metric alarm using the Lightsail console.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Instances**, **Databases**, or **Networking**.

1. Choose the name of the resource (instance, database, or load balancer) for which you want to delete an alarm.

1. Choose the **Metrics** tab on the resource’s management page.

1. Choose the metric for which you want to delete an alarm in the drop-down under the **Metrics Graphs** heading.

1. Scroll down to the **Alarms** section of the page, and choose the ellipsis icon (⋮) next to the alarm you want to delete.

1. Choose **Delete**.

1. At the prompt, choose **Delete** to confirm that you want to delete the alarm.

## Disable and enabling metric alarms using the Lightsail console
<a name="disable-alarms"></a>

Complete the following steps to disable a metric alarm using the Lightsail console.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Instances**, **Databases**, or **Networking**.

1. Choose the name of the resource (instance, database, or load balancer) for which you want to disable an alarm.

1. Choose the **Metrics** tab on the resource’s management page.

1. Choose the metric for which you want to disable an alarm in the drop-down under the **Metrics Graphs** heading.

1. Scroll down to the **Alarms** section of the page, locate the alarm you want to disable, and choose the toggle to disable it. Likewise, choose the toggle to enable it if it's disabled.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
