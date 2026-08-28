---
source_url: https://docs.aws.amazon.com/streams/latest/dev/sse-troubleshooting.html
---

# Verify and Troubleshoot KMS key permissions
<a name="sse-troubleshooting"></a>

After enabling encryption on a Kinesis stream, we recommend that you monitor the success of your `putRecord`, `putRecords`, and `getRecords` calls using the following Amazon CloudWatch metrics:
+  `PutRecord.Success`
+  `PutRecords.Success`
+  `GetRecords.Success`

For more information, see [Monitor Kinesis Data Streams](monitoring.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
