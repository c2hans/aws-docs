---
source_url: https://docs.aws.amazon.com/streams/latest/dev/using-other-services-emr.html
---

# Read data from Kinesis Data Streams using Amazon EMR
<a name="using-other-services-emr"></a>

Amazon EMR clusters can read and process Kinesis streams directly, using familiar tools in the Hadoop ecosystem such as Hive, Pig, MapReduce, the Hadoop Streaming API, and Cascading. You can also join real-time data from Kinesis Data Streams with existing data on Amazon S3, Amazon DynamoDB, and HDFS in a running cluster. You can directly load the data from Amazon EMR to Amazon S3 or DynamoDB for post-processing activities.

For more information, see [Amazon Kinesis](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-kinesis.html) in the *Amazon EMR Release Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
