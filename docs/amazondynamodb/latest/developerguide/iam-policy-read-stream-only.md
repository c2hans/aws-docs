---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/iam-policy-read-stream-only.html
---

# IAM policy to grant read access for a DynamoDB stream only (not for the table)
<a name="iam-policy-read-stream-only"></a>

When you enable DynamoDB Streams on a table, information is captured about every modification to items in the table. For more information, see [Change data capture for DynamoDB Streams](Streams.md).

In some cases, you might want to prevent an application from reading data from a DynamoDB table, but still allow access to that table's streams. For example, you can configure AWS Lambda to poll a stream and invoke a Lambda function when item updates are detected, and then perform additional processing.

The following actions are available for controlling access to DynamoDB streams:
+ `dynamodb:DescribeStream`
+ `dynamodb:GetRecords`
+ `dynamodb:GetShardIterator`
+ `dynamodb:ListStreams`

The following example policy grants users permissions to access the streams of a table named `GameScores`. The wildcard character (\*) in the ARN matches any stream associated with that table.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AccessGameScoresStreamOnly",
            "Effect": "Allow",
            "Action": [
                "dynamodb:DescribeStream",
                "dynamodb:GetRecords",
                "dynamodb:GetShardIterator",
                "dynamodb:ListStreams"
            ],
            "Resource": "arn:aws:dynamodb:us-west-2:123456789012:table/GameScores/stream/*"
        }
    ]
}
```

------

Note that this policy grants access to the `GameScores` table's streams, but not to the table itself.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
