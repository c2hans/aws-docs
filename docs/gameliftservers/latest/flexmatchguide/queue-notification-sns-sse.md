---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/queue-notification-sns-sse.html
---

# Set up an SNS topic with server-side encryption
<a name="queue-notification-sns-sse"></a>

You can use server-side encryption (SSE) to store sensitive data in encrypted topics. SSE protects the contents of messages in Amazon SNS topics using keys managed in AWS Key Management Service (AWS KMS). For more information about server-side encryption with Amazon SNS, see [Encryption at rest](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html) in the *Amazon Simple Notification Service Developer Guide*.

To set up an SNS topic with server-side encryption, review the following topics:
+ [Creating key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*
+ [Enabling SSE for a topic](https://docs.aws.amazon.com/sns/latest/dg/sns-enable-encryption-for-topic.html) in the *Amazon Simple Notification Service Developer Guide*

When creating your KMS key, use the following KMS key policy:

```
{
  "Effect": "Allow",
  "Principal": {
    "Service": "gamelift.amazonaws.com"
  },
  "Action": [
      "kms:Decrypt",
      "kms:GenerateDataKey"
  ],
  "Resource": "*",
  "Condition": {
      "ArnLike": {
        "aws:SourceArn": "arn:aws:gamelift:{{your_region}}:{{your_account}}:matchmakingconfiguration/{{your_configuration_name}}"
      },
      "StringEquals": {
        "kms:EncryptionContext:aws:sns:topicArn": "arn:aws:sns:{{your_region}}:{{your_account}}:{{your_sns_topic_name}}"
      }
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
