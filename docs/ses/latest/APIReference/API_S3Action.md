---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_S3Action.html
---

# S3Action
<a name="API_S3Action"></a>

When included in a receipt rule, this action saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

To enable Amazon SES to write emails to your Amazon S3 bucket, use an AWS KMS key to encrypt your emails, or publish to an Amazon SNS topic of another account, Amazon SES must have permission to access those resources. For information about granting permissions, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html).

**Note**
When you save your emails to an Amazon S3 bucket, the maximum email size (including headers) is 40 MB. Emails larger than that bounces.

For information about specifying Amazon S3 actions in receipt rules, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-s3.html).

## Contents
<a name="API_S3Action_Contents"></a>

 ** BucketName **
The name of the Amazon S3 bucket for incoming email.
Type: String
Required: Yes

 ** IamRoleArn **
 The ARN of the IAM role to be used by Amazon Simple Email Service while writing to the Amazon S3 bucket, optionally encrypting your mail via the provided customer managed key, and publishing to the Amazon SNS topic. This role should have access to the following APIs:
+  `s3:PutObject`, `kms:Encrypt` and `kms:GenerateDataKey` for the given Amazon S3 bucket.
+  `kms:GenerateDataKey` for the given AWS KMS customer managed key.
+  `sns:Publish` for the given Amazon SNS topic.
If an IAM role ARN is provided, the role (and only the role) is used to access all the given resources (Amazon S3 bucket, AWS KMS customer managed key and Amazon SNS topic). Therefore, setting up individual resource access permissions is not required.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w-]+:iam::[0-9]+:role/[\w-]+`
Required: No

 ** KmsKeyArn **
The customer managed key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. You can use the AWS managed key or a customer managed key that you created in AWS KMS as follows:
+ To use the AWS managed key, provide an ARN in the form of `arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`. For example, if your AWS account ID is 123456789012 and you want to use the AWS managed key in the US West (Oregon) Region, the ARN of the AWS managed key would be `arn:aws:kms:us-west-2:123456789012:alias/aws/ses`. If you use the AWS managed key, you don't need to perform any extra steps to give Amazon SES permission to use the key.
+ To use a customer managed key that you created in AWS KMS, provide the ARN of the customer managed key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html).
For more information about key policies, see the [AWS KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html). If you do not specify an AWS KMS key, Amazon SES does not encrypt your emails.
Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your AWS KMS keys for decryption. This encryption client is currently available with the [AWS SDK for Java](http://aws.amazon.com/sdk-for-java/) and [AWS SDK for Ruby](http://aws.amazon.com/sdk-for-ruby/) only. For more information about client-side encryption using AWS KMS managed keys, see the [Amazon S3 Developer Guide](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html).
Type: String
Required: No

 ** ObjectKeyPrefix **
The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket.
Type: String
Required: No

 ** TopicArn **
The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. You can find the ARN of a topic by using the [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) operation in Amazon SNS.
For more information about Amazon SNS topics, see the [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html).
Type: String
Required: No

## See Also
<a name="API_S3Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/S3Action)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/S3Action)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/S3Action)
