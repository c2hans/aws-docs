---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring-console.html
---

# Viewing Fleet Usage Using the Console
<a name="monitoring-console"></a>

You can monitor your Amazon WorkSpaces Applications fleet usage using the WorkSpaces Applications or CloudWatch console.

**To view fleet usage in the WorkSpaces Applications console**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home).

1. In the left pane, choose **Fleets**.

1. Select a fleet and choose its **Fleet Usage** tab.

1. By default, the graph displays the following metrics:
   + `ActualCapacity`, `InUseCapacity`, `DesiredCapacity`, `AvailableCapacity`, `PendingCapacity`, and `CapacityUtilization` for single-session fleets.
   + `ActualUserSessionCapacity`, `ActiveUserSessionCapacity`, `AvailableUserSessionCapacity`, `DesiredUserSessionCapacity`, `PendingUserSessionCapacity`, `CapacityUtilization`, `DrainingCapacity`, `DrainModeActiveUserSessionCapacity`, and `DrainModeUnusedUserSessionCapacity` for multi-session fleets.

**To view fleet usage in the CloudWatch console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the left pane, choose **Metrics**.

1. Choose the **AppStream** namespace and then choose **Fleet Metrics**.

1. Select the metrics to graph.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
