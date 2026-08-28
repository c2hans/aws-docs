---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream KMSEncryptionConfig
<a name="aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig"></a>

The `KMSEncryptionConfig` property type specifies the AWS Key Management Service (AWS KMS) encryption key that Amazon Simple Storage Service (Amazon S3) uses to encrypt data delivered by the Amazon Kinesis Data Firehose (Kinesis Data Firehose) stream.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig-syntax.json"></a>

```
{
  "[AWSKMSKeyARN](#cfn-kinesisfirehose-deliverystream-kmsencryptionconfig-awskmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig-syntax.yaml"></a>

```
  [AWSKMSKeyARN](#cfn-kinesisfirehose-deliverystream-kmsencryptionconfig-awskmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig-properties"></a>

`AWSKMSKeyARN`  <a name="cfn-kinesisfirehose-deliverystream-kmsencryptionconfig-awskmskeyarn"></a>
The Amazon Resource Name (ARN) of the AWS KMS encryption key that Amazon S3 uses to encrypt data delivered by the Kinesis Data Firehose stream. The key must belong to the same region as the destination S3 bucket.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*:kms:[a-zA-Z0-9\-]+:\d{12}:(key|alias)/[a-zA-Z_0-9+=,.@\-_/]+`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
