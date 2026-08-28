---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/mtgs-sdk-notifications.html
---

# Understanding Amazon Chime SDK event notifications
<a name="mtgs-sdk-notifications"></a>

The Amazon Chime SDK supports sending meeting event notifications to Amazon EventBridge, Amazon Simple Queue Service (SQS), and Amazon Simple Notification Service (SNS).

**Note**
The default Amazon Chime SDK meetings namespace uses the `ChimeSDKMeetings` endpoints. The legacy Chime namespace uses a single endpoint. For more information about the namespaces and endpoints, refer to [Migrating to the Amazon Chime SDK meetings namespace](meeting-namespace-migration.md), earlier in this guide.

## Sending notifications to EventBridge
<a name="chime-sdk-eventbridge-notifications"></a>

You can send Amazon Chime SDK Event notifications to EventBridge. For detailed information about using the Amazon Chime SDK with EventBridge, see [ Automating the Amazon Chime SDK with EventBridge ](https://docs.aws.amazon.com/chime-sdk/latest/ag/automating-chime-with-cloudwatch-events.html#events-sdk) in the *Amazon Chime SDK Administrator Guide*. For information about EventBridge, see the [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/).

## Sending notifications to Amazon SQS and Amazon SNS
<a name="chime-sdk-sqs-sns-notifications"></a>

You can use the [CreateMeeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html) API in the *Amazon Chime SDK API Reference* to send Amazon Chime SDK meeting event notifications to one Amazon SQS queue and one Amazon SNS topic per meeting. This can help reduce notification latency. For more information about Amazon SQS, see the [Amazon Simple Queue Service Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/). For more information about Amazon SNS, see the [Amazon Simple Notification Service Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/).

The notifications sent to Amazon SQS and Amazon SNS contain the same information as the notifications that the Amazon Chime SDK sends to EventBridge. The Amazon Chime SDK supports sending meeting event notifications to queues and topics in the API Region used to create a meeting. Event notifications might be delivered out of order of occurrence.

## Granting the Amazon Chime SDK access to Amazon SQS and Amazon SNS
<a name="chime-sdk-sqs-sns-permissions"></a>

Before the Amazon Chime SDK can send you notifications via an Amazon SQS queue or Amazon SNS topic, you must grant the Amazon Chime SDK permission to publish messages to the Amazon Resource Name (ARN) of the queue or topic. To do this, attach an AWS Identity and Access Management (IAM) policy to the queue or topic that grants the appropriate permissions to the Amazon Chime SDK. For more information, see [Identity and access management in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-authentication-and-access-control.html) in the *Amazon Simple Queue Service Developer Guide* and [Example cases for Amazon SNS access control ](https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-use-cases.html) in the *Amazon Simple Notification Service Developer Guide*.

**Note**
Your Amazon SQS queue or Amazon SNS topic must use the same AWS region as your Amazon Chime SDK API endpoint.

**Example Allow the Amazon Chime SDK to publish events to an Amazon SQS queue**
The following example IAM policy grants the Amazon Chime SDK permission to publish meeting event notifications to the specified Amazon SQS queue. Note the conditional statement for `aws:SourceArn` and `aws:SourceAccount`. They address potential [Confused Deputy](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) issues.
+ You can use `aws:SourceArn` or `aws:SourceAccount` when creating the policies below. You don't need to use both.
+ These examples use the `ChimeSDKMeetings` namespace and corresponding endpoint. If you use the `Chime` namespace, you must use the `chime.amazonaws.com` endpoint.
****

```
{
    "Version":"2012-10-17",
   "Id": "{{example-ID}}",
    "Statement": [
        {
            "Sid": "{{example-statement-ID}}",
            "Effect": "Allow",
            "Principal": {
                "Service": "meetings.chime.amazonaws.com"
            },
                "Action": [
                    "sqs:SendMessage",
                    "sqs:GetQueueUrl"
                ],
               "Resource": "arn:aws:sqs:{{us-east-1}}:{{111122223333}}:queueName",
               "Condition": {
                   "ArnLike": {
                   "aws:SourceArn": "arn:aws:chime:{{us-east-1}}:{{111122223333}}:*"
               },
               "StringEquals": {
               "aws:SourceAccount": "{{111122223333}}"
               }
            }
        }
   ]
}
```
This example shows an Amazon SNS policy that allows the Amazon Chime SDK to send meeting event notifications to your SNS topic.
****

```
{
    "Version":"2012-10-17",
    "Id": "{{example-ID}}",
    "Statement": [
     {
        "Sid": "{{allow-chime-sdk-access-statement-id}}",
        "Effect": "Allow",
        "Principal": {
            "Service": "meetings.chime.amazonaws.com"
    },
       "Action": [
           "SNS:Publish"
       ],
           "Resource": "arn:aws:sns:{{us-east-1}}:{{111122223333}}:topicName",
           "Condition": {
           "ArnLike": {
           "aws:SourceArn": "arn:aws:chime:{{us-east-1}}:{{111122223333}}:*"
      },
      "StringEquals": {
      "aws:SourceAccount": "{{111122223333}}"
          }
       }
     }
   ]
}
```
If the Amazon SQS queue is enabled for server-side encryption (SSE), you must take an additional step. Attach an IAM policy to the associated AWS KMS key that grants the Amazon Chime SDK permission to the AWS KMS actions needed to encrypt data added to the queue.
****

```
{
    "Version":"2012-10-17",
    "Id": "{{example-ID}}",
    "Statement": [
        {
            "Sid": "{{example-statement-ID}}",
            "Effect": "Allow",
            "Principal": {
                "Service": "meetings.chime.amazonaws.com"
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "*"
        }
    ]
}
```

**Example Allow the Amazon Chime SDK to publish events to an Amazon SNS topic**
The following example IAM policy grants the Amazon Chime SDK permission to publish meeting event notifications to the specified Amazon SNS topic.
****

```
{
    "Version":"2012-10-17",
    "Id": "{{example-ID}}",
    "Statement": [
        {
            "Sid": "allow-chime-sdk-access-statement-id",
            "Effect": "Allow",
            "Principal": {
                "Service": "meetings.chime.amazonaws.com"
            },
            "Action": [
                "SNS:Publish"
            ],
            "Resource": "arn:aws:sns:{{us-east-1}}:{{111122223333}}:topicName",
            "Condition": {
                "ArnLike": {
                "aws:SourceArn": "arn:aws:chime:{{us-east-1}}:{{111122223333}}:*"
            },
           "StringEquals": {
           "aws:SourceAccount": "{{111122223333}}"
           }
        }
     }
  ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
