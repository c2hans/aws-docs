---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-customplugin-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::CustomPlugin S3Location
<a name="aws-properties-kafkaconnect-customplugin-s3location"></a>

The location of an object in Amazon S3.

## Syntax
<a name="aws-properties-kafkaconnect-customplugin-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-customplugin-s3location-syntax.json"></a>

```
{
  "[BucketArn](#cfn-kafkaconnect-customplugin-s3location-bucketarn)" : {{String}},
  "[FileKey](#cfn-kafkaconnect-customplugin-s3location-filekey)" : {{String}},
  "[ObjectVersion](#cfn-kafkaconnect-customplugin-s3location-objectversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-customplugin-s3location-syntax.yaml"></a>

```
  [BucketArn](#cfn-kafkaconnect-customplugin-s3location-bucketarn): {{String}}
  [FileKey](#cfn-kafkaconnect-customplugin-s3location-filekey): {{String}}
  [ObjectVersion](#cfn-kafkaconnect-customplugin-s3location-objectversion): {{String}}
```

## Properties
<a name="aws-properties-kafkaconnect-customplugin-s3location-properties"></a>

`BucketArn`  <a name="cfn-kafkaconnect-customplugin-s3location-bucketarn"></a>
The Amazon Resource Name (ARN) of an S3 bucket.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileKey`  <a name="cfn-kafkaconnect-customplugin-s3location-filekey"></a>
The file key for an object in an S3 bucket.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ObjectVersion`  <a name="cfn-kafkaconnect-customplugin-s3location-objectversion"></a>
The version of an object in an S3 bucket.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
