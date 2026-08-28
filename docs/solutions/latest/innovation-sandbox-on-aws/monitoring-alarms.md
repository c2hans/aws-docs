---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/monitoring-alarms.html
---

# Alarms
<a name="monitoring-alarms"></a>

Innovation Sandbox deploys Amazon CloudWatch Alarms to alert you to operational issues. By default, none of the alarms have notification actions attached. To receive notifications, subscribe an Amazon SNS topic to the alarm. For guidance, refer to [Acting on alarm changes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Acting_Alarm_Changes.html).

## Alarms deployed by the solution
<a name="solution-alarms"></a>

| Alarm | Fires when | What to do |
| --- | --- | --- |
|  **Tag resource failure**  | One or more `Organizations:TagResource` calls fail within an hour (across lease approval, cleanup, ejection, or cost-report-group updates). | Check Amazon CloudWatch Logs for entries with `logDetailType` set to `TagResourceFailed`. Common causes: the account reached the 50-tag limit (`TagSpaceExhausted`) or a transient API error (`ApiError`). |
|  **Tag activation workflow failure**  | The tag activation Step Functions workflow fails or times out without successfully activating the ISB cost allocation tag keys. | The ISB tag keys may not be active in the billing console. See [Manually activating cost allocation tags](troubleshooting.md#manually-activating-cost-allocation-tags). |
|  **Assignment processing DLQ**  | One or more lease assignment operations (granting or revoking IAM Identity Center account access) fail after all retries and land on the dead-letter queue. | Investigate the messages on the `Isb-<namespace>-AssignmentProcessingDLQ` SQS queue. Common causes: IAM Identity Center API throttling, permission set not found, or account not in the organization. |
|  **WAF blocked requests**  | AWS WAF blocks one or more requests to the Innovation Sandbox API. | Review the AWS WAF logs to determine whether the blocked requests are legitimate. A spike may indicate misconfigured WAF rules blocking valid users, or it may indicate an attack being correctly mitigated. |

You can configure additional alarms based on metrics reported by the different services within the solution. For example, you might alarm on Lambda error rates, DynamoDB throttling, or SQS dead-letter queue depth.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
