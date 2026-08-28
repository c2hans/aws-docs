---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring-instance-session-performance.html
---

# Viewing instance and session metrics using the console
<a name="monitoring-instance-session-performance"></a>

You can monitor Amazon WorkSpaces Applications fleet instance and session metrics using the WorkSpaces Applications console or the CloudWatch console.

These metrics are collected at a 5-minute interval. After a new session is provisioned, the first metric data point appears within 5 minutes. Subsequent metric data points are available at every 5-minute interval.

**To view instance and session in the WorkSpaces Applications console**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home).

1. In the left pane, choose **Fleets**.

1. Select a fleet and choose **View Details**.

1. View fleet utilization information under **Sessions on fleet**.

1. View the list of all active sessions under **Instances with sessions**.

1. Select a session to view the metrics.

1. You can sort and filter the table to find specific user sessions.

**To view instance and session metrics in the CloudWatch console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the left pane, choose **Metrics**.

1. Choose the **AppStream** namespace and then choose **Fleet Instance Metrics** or **Fleet Session Metrics**.

1. Select the metrics to graph.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
