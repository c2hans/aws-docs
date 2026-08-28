---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-s3-ts-creating.html
---

# Channel stuck in CREATING state
<a name="msk-data-delivery-s3-ts-creating"></a>
+ **Symptom:** The Channel remains in `CREATING` for an extended period and does not transition to `ACTIVE` or `FAILED`.
+ **Causes:** Provisioning is still in progress, or a transient service-side delay. Configuration errors cause the Channel to transition to `FAILED` rather than remain in `CREATING`. Examples include missing service-role permissions and a destination or DLQ bucket that doesn't exist.
+ **Resolution:** Allow provisioning to finish. Run `DescribeChannel` to check the state — if it is `FAILED`, read the failure detail (and Amazon CloudWatch Logs, if enabled) to identify the configuration problem, then delete and recreate the Channel. If the Channel stays in `CREATING` well beyond the expected time, contact AWS Support.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
