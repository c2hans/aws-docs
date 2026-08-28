---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/enabling-cloudwatch-metrics-alarms-and-dashboard.html
---

# Enabling CloudWatch metrics, alarms, and dashboard
<a name="enabling-cloudwatch-metrics-alarms-and-dashboard"></a>

There are four CloudFormation template parameters for CloudWatch functionality.

![CloudWatch Metric template parameters.](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/cloudwatch-metrics.png)

1.  **UseCloudWatchMetrics** - Setting this to `yes` enables the collection of operational metrics and creates a CloudWatch dashboard to view these metrics.

1.  **UseCloudWatchAlarms** - Setting this to `yes` enables the solution’s default alarms.

1.  **RemediationFailureAlarmThreshold** - The percentage of failing remediations in a period to raise an alarm.

1.  **EnableEnhancedCloudWatchMetrics** - Set this parameter to `yes` to collect individual metrics per control ID. By default, this parameter is set to `no`, so that only metrics on the total number of remediations across all control IDs are collected. Individual metrics and alarms per control ID incur additional cost.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
