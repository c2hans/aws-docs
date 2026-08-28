---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-monitor.html
---

# Monitor and troubleshoot managed external secrets
<a name="mes-monitor"></a>

Managed external secrets provide comprehensive monitoring capabilities through AWS CloudTrail logs and Amazon CloudWatch metrics. All rotation activities are logged with detailed information about success, failure, and any errors encountered during the process.

Common issues in the rotation workflow include an incorrect configuration of role permissions or the secret value. Failure to set these fields is the format specified by the integration partners can cause rotation failures, as the service will be unable to access the secret or connect with the integration partner client to update the secret. Other issues could be network connectivity problems, credential expiration, or partner service availability. The managed rotation service includes retry logic and error handling to maximize reliability

You can monitor rotation schedules, success rates, and performance metrics through Amazon CloudWatch. You can configure custom alarms through [event bridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-pattern.html) to alert you of rotation failures or other issues that require attention.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
