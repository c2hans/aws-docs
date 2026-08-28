---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/dimensions-metrics.html
---

# Dimensions for Amazon WorkSpaces Applications Metrics
<a name="dimensions-metrics"></a>

The `AWS/AppStream` namespace includes the following dimensions and dimension groups.

| Dimension | Description |
| --- | --- |
| Fleet | Filters the metric data by name of the Fleet. |
| FleetName | Filters the metric data by name of the Fleet. |
| SessionId | Filters the metric data by session identifier. |
| InstanceId | Filters the metric data by instance identifier. |
| UserId | Filters the metric data by user identifier. |
| ImageBuilder | Filters the metric data by name of the image builder. |
| AppBlockBuilder | Filters the metric data by name of the app block builder. |

| Dimension | Where Available in Amazon CloudWatch Metrics |
| --- | --- |
| [Fleet] | Fleet Metrics |
| [FleetName, InstanceId] | Fleet Instance Metrics |
| [FleetName, InstanceId, SessionId] | Fleet Session Metrics |
| [UserId] | UserId |
| [FleetName, InstanceId, SessionId, UserId] | FleetName, InstanceId, SessionId, UserId |
| [ImageBuilder] | Image Builder Metrics |
| [AppBlockBuilder] | App Block Builder Metrics |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
