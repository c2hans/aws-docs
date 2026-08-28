---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring-with-cloudwatch.html
---

# WorkSpaces Applications Metrics and Dimensions
<a name="monitoring-with-cloudwatch"></a>

Amazon WorkSpaces Applications sends the following metrics and dimension information to Amazon CloudWatch.

All of the following metrics except `InsufficientConcurrencyLimitError` apply to Always-On and On-Demand fleets. The only metrics that apply to Elastic fleets are `InUseCapacity` and `InsufficientCapacityError`.

WorkSpaces Applications sends metrics to CloudWatch one time every minute. The `AWS/AppStream` namespace includes the following metrics.

**Topics**
+ [Fleet Usage Metrics for Single-session Fleets](appstream-dimensions.md)
+ [Fleet Usage Metrics for Multi-session Fleets](usage-metrics-multi-session.md)
+ [Instance and Session Performance Metrics for Single-session and Multi-session Fleets](instance-session-metrics-single-session-multi-session.md)
+ [Dimensions for Amazon WorkSpaces Applications Metrics](dimensions-metrics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
