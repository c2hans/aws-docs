---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/troubleshooting-credential-provider.html
---

# Credential provider issue with EFO connector 1.15.2
<a name="troubleshooting-credential-provider"></a>

There is a [known issue](https://issues.apache.org/jira/browse/FLINK-29205) with Kinesis Data Streams EFO connector versions up to 1.15.2 where the `FlinkKinesisConsumer` is not respecting `Credential Provider` configuration. Valid configurations are being disregarded due to the issue, which results in the `AUTO` credential provider being used. This can cause a problem using cross-account access to Kinesis using EFO connector.

To resolve this error please use EFO connector version 1.15.3 or higher.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
