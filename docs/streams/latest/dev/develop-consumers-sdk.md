---
source_url: https://docs.aws.amazon.com/streams/latest/dev/develop-consumers-sdk.html
---

# Develop consumers with the AWS SDK for Java
<a name="develop-consumers-sdk"></a>

 You can develop custom consumers using the Amazon Kinesis Data Streams APIs. This section describes using the Kinesis Data Streams APIs with the AWS SDK for Java.

**Important**
The recommended method for developing custom Kinesis Data Streams consumers with shared throughout is to use the Kinesis Client Library (KCL). KCL helps you consume and process data from a Kinesis data stream by taking care of many of the complex tasks associated with distributed computing. For more information, see [Develop consumers with KCL in Java](develop-kcl-consumers-java.md).

**Topics**
+ [Develop shared-throughput consumers with the AWS SDK for Java](developing-consumers-with-sdk.md)
+ [Develop enhanced fan-out consumers with the AWS SDK for Java](building-enhanced-consumers-api.md)
+ [Interact with data using the AWS Glue Schema Registry](building-enhanced-consumers-glue-schema-registry.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
