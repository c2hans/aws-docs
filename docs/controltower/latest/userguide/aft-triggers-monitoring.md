---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/aft-triggers-monitoring.html
---

# Monitoring and traceability
<a name="aft-triggers-monitoring"></a>

Each customization execution (whether triggered by an OU change, a manual invocation, or an account request) writes an audit record to a DynamoDB table. You can use these records to understand why a customization ran, which accounts were affected, and how the execution relates to other pipeline activity.

| Field | Description |
| --- | --- |
| execution\_id | The Step Functions execution ID |
| timestamp | When the record was created |
| target\_accounts | List of target account IDs |
| bypass\_steps | Provisioning steps that were skipped |
| customization\_triggers | Trigger context (source and destination OU) |
| trigger\_source | Why the execution ran: account\_move, manual, or account\_request |
| customization\_request\_id | Links the provisioning and customization executions for end-to-end correlation |

The `customization_request_id` allows you to correlate the triggering event with downstream pipeline execution across both Step Functions state machines. You can use this identifier to trace a single account move from initial detection through customization completion.

**Example Query audit records by trigger source**

```
aws dynamodb scan \
  --table-name aft-customizations-audit \
  --filter-expression "trigger_source = :ts" \
  --expression-attribute-values '{":ts": {"S": "account_move"}}'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
