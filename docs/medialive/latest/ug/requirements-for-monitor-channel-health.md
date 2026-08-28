---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-monitor-channel-health.html
---

# Requirements for Amazon CloudWatch—monitoring channel health
<a name="requirements-for-monitor-channel-health"></a>

The AWS Elemental MediaLive console includes a page (**Channel details**) that collects CloudWatch metrics information about the health of channels and displays it directly on the MediaLive console.

You must decide if you want to give some or all of your users permission to view metrics on the console.

For a user to view this information on the MediaLive console, that user must have view permissions for metrics operations in Amazon CloudWatch. When users have these permissions, they can also view the information through the CloudWatch console, AWS CLI, or REST API.

The following table shows the actions in IAM that relate to access for monitoring channel health.

| Permissions | Service Name in IAM | Actions |
| --- | --- | --- |
| View Metrics  | CloudWatch | ListMetrics`GetMetricData`<br />`GetMetricStatistics` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
