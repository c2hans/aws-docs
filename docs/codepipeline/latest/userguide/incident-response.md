---
source_url: https://docs.aws.amazon.com/codepipeline/latest/userguide/incident-response.html
---

# Logging and monitoring in CodePipeline
<a name="incident-response"></a>

You can use logging features in AWS to determine the actions users have taken in your account and the resources that were used. The log files show:
+ The time and date of actions.
+ The source IP address for an action.
+ Which actions failed due to inadequate permissions.

Logging features are available in the following AWS services:
+ AWS CloudTrail can be used to log AWS API calls and related events made by or on behalf of an AWS account. For more information, see [Logging CodePipeline API calls with AWS CloudTrail](monitoring-cloudtrail-logs.md).
+ Amazon CloudWatch Events can be used to monitor your AWS Cloud resources and the applications you run on AWS. You can create alerts in Amazon CloudWatch Events based on metrics that you define. For more information, see [Monitoring CodePipeline events](detect-state-changes-cloudwatch-events.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
