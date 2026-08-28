---
source_url: https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-deaggregation.html
---

# Process serialized data using AWS Lambda with the Amazon Kinesis Producer Library
<a name="kinesis-record-deaggregation"></a>

The [Amazon Kinesis Producer Library](https://docs.aws.amazon.com/kinesis/latest/dev/developing-producers-with-kpl.html) (KPL) aggregates small user-formatted records into larger records up to 1 MB to make better use of Amazon Kinesis Data Streams throughput. While the KCL for Java supports deaggregating these records, you need to use a special module to deaggregate records when using AWS Lambda as the consumer of your streams. You can obtain the necessary project code and instructions from GitHub at [Amazon Kinesis Producer Library Deaggregation Modules for AWS Lambda](https://github.com/awslabs/kinesis-deaggregation). The components in this project give you the ability to process KPL serialized data within AWS Lambda, in Java, Node.js and Python. These components can also be used as part of a [multi-lang KCL application](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client-multilang/src/main/java/software/amazon/kinesis/multilang/package-info.java).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
