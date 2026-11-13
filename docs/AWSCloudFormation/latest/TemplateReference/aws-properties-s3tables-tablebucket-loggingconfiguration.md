---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-tablebucket-loggingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::TableBucket LoggingConfiguration
<a name="aws-properties-s3tables-tablebucket-loggingconfiguration"></a>

Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys for a table bucket.

## Syntax
<a name="aws-properties-s3tables-tablebucket-loggingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-tablebucket-loggingconfiguration-syntax.json"></a>

```
{
  "[TargetBucket](#cfn-s3tables-tablebucket-loggingconfiguration-targetbucket)" : {{String}},
  "[TargetObjectKeyFormat](#cfn-s3tables-tablebucket-loggingconfiguration-targetobjectkeyformat)" : {{TargetObjectKeyFormat}},
  "[TargetPrefix](#cfn-s3tables-tablebucket-loggingconfiguration-targetprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3tables-tablebucket-loggingconfiguration-syntax.yaml"></a>

```
  [TargetBucket](#cfn-s3tables-tablebucket-loggingconfiguration-targetbucket): {{String}}
  [TargetObjectKeyFormat](#cfn-s3tables-tablebucket-loggingconfiguration-targetobjectkeyformat): {{
    TargetObjectKeyFormat}}
  [TargetPrefix](#cfn-s3tables-tablebucket-loggingconfiguration-targetprefix): {{String}}
```

## Properties
<a name="aws-properties-s3tables-tablebucket-loggingconfiguration-properties"></a>

`TargetBucket`  <a name="cfn-s3tables-tablebucket-loggingconfiguration-targetbucket"></a>
The name of the general purpose bucket that logs are delivered to. The bucket must be in the same AWS Region and owned by the same AWS account as the table bucket. The bucket can't use SSE-KMS or DSSE-KMS default encryption, can't have S3 Object Lock enabled, and can't have Requester Pays enabled. You can deliver logs from multiple table buckets to the same target bucket. In this case, choose a different `TargetPrefix` for each table bucket so that you can tell their log objects apart.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetObjectKeyFormat`  <a name="cfn-s3tables-tablebucket-loggingconfiguration-targetobjectkeyformat"></a>
The key format of the log objects. Log object keys are always partitioned by date.
*Required*: Yes
*Type*: [TargetObjectKeyFormat](aws-properties-s3tables-tablebucket-targetobjectkeyformat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetPrefix`  <a name="cfn-s3tables-tablebucket-loggingconfiguration-targetprefix"></a>
The prefix for the keys of the log objects that are delivered to the target bucket.
*Required*: Yes
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
