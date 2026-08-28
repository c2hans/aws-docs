---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-s3bucketlogdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot S3BucketLogDestination
<a name="aws-properties-lex-bot-s3bucketlogdestination"></a>

Specifies an Amazon S3 bucket for logging audio conversations

## Syntax
<a name="aws-properties-lex-bot-s3bucketlogdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-s3bucketlogdestination-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-lex-bot-s3bucketlogdestination-kmskeyarn)" : {{String}},
  "[LogPrefix](#cfn-lex-bot-s3bucketlogdestination-logprefix)" : {{String}},
  "[S3BucketArn](#cfn-lex-bot-s3bucketlogdestination-s3bucketarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-s3bucketlogdestination-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-lex-bot-s3bucketlogdestination-kmskeyarn): {{String}}
  [LogPrefix](#cfn-lex-bot-s3bucketlogdestination-logprefix): {{String}}
  [S3BucketArn](#cfn-lex-bot-s3bucketlogdestination-s3bucketarn): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-s3bucketlogdestination-properties"></a>

`KmsKeyArn`  <a name="cfn-lex-bot-s3bucketlogdestination-kmskeyarn"></a>
The Amazon Resource Name (ARN) of an AWS Key Management Service (KMS) key for encrypting audio log files stored in an Amazon S3 bucket.
*Required*: No
*Type*: String
*Pattern*: `^arn:[\w\-]+:kms:[\w\-]+:[\d]{12}:(?:key\/[\w\-]+|alias\/[a-zA-Z0-9:\/_\-]{1,256})$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogPrefix`  <a name="cfn-lex-bot-s3bucketlogdestination-logprefix"></a>
The S3 prefix to assign to audio log files.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3BucketArn`  <a name="cfn-lex-bot-s3bucketlogdestination-s3bucketarn"></a>
The Amazon Resource Name (ARN) of an Amazon S3 bucket where audio log files are stored.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[\w\-]+:s3:::[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
