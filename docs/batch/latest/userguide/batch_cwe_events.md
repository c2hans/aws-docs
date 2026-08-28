---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/batch_cwe_events.html
---

# AWS Batch events
<a name="batch_cwe_events"></a>

AWS Batch sends job status change events to EventBridge. AWS Batch tracks the state of your jobs. If a previously submitted job's status changes, an event is invoked. For example, if a job in the `RUNNING` status moves to the `FAILED` status. These events are classified as job state change events.

**Note**
AWS Batch might add other event types, sources, and details in the future. If you're programmatically deserializing event JSON data, make sure that your application is prepared to handle unknown properties. This is to avoid issues if and when these additional properties are added.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
