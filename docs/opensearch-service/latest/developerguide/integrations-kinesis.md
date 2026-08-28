---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations-kinesis.html
---

# Loading streaming data from Amazon Kinesis Data Streams
<a name="integrations-kinesis"></a>

You can load streaming data from Kinesis Data Streams to OpenSearch Service. New data that arrives in the data stream triggers an event notification to Lambda, which then runs your custom code to perform the indexing. This section includes some unsophisticated Python sample code.

## Prerequisites
<a name="integrations-kinesis-lambda-prereq"></a>

Before proceeding, you must have the following resources.

| Prerequisite | Description |
| --- | --- |
| Amazon Kinesis Data Stream | The event source for your Lambda function. To learn more, see [Kinesis Data Streams](https://docs.aws.amazon.com/kinesis/latest/dev/amazon-kinesis-streams.html). |
| OpenSearch Service Domain | The destination for data after your Lambda function processes it. For more information, see [Creating OpenSearch Service domains](createupdatedomains.md#createdomains) |
| IAM Role | This role must have basic OpenSearch Service, Kinesis, and Lambda permissions, such as the following:  JSON

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "es:ESHttpPost",
        "es:ESHttpPut",
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "kinesis:GetShardIterator",
        "kinesis:GetRecords",
        "kinesis:DescribeStream",
        "kinesis:ListStreams"
      ],
      "Resource": "*"
    }
  ]
}
```    <br />The role must have the following trust relationship:  JSON

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```    <br />To learn more, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *IAM User Guide*. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
