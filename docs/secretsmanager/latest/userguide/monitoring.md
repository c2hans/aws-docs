---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring.html
---

# Monitor AWS Secrets Manager secrets
<a name="monitoring"></a>

AWS provides monitoring tools to watch Secrets Manager secrets, report when something is wrong, and take automatic actions when appropriate. You can use the logs if you need to investigate any unexpected usage or change, and then you can roll back unwanted changes. You can also set automated checks for inappropriate usage of secrets and any attempts to delete secrets.

**Topics**
+ [Log with AWS CloudTrail](monitoring-cloudtrail.md)
+ [Monitor with CloudWatch](monitoring-cloudwatch.md)
+ [Match Secrets Manager events with EventBridge](monitoring-eventbridge.md)
+ [Monitor secrets scheduled for deletion](monitoring_cloudwatch_deleted-secrets.md)
+ [Monitor secrets for compliance](configuring-awsconfig-rules.md)
+ [Monitor Secrets Manager costs](monitor-secretsmanager-costs.md)
+ [Detect threats with GuardDuty](monitoring-guardduty.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
