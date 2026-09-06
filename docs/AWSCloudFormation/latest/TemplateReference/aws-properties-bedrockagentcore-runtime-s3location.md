---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime S3Location
<a name="aws-properties-bedrockagentcore-runtime-s3location"></a>

The Amazon S3 location for storing data. This structure defines where in Amazon S3 data is stored.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-s3location-syntax.json"></a>

```
{
  "[Bucket](#cfn-bedrockagentcore-runtime-s3location-bucket)" : {{String}},
  "[Prefix](#cfn-bedrockagentcore-runtime-s3location-prefix)" : {{String}},
  "[VersionId](#cfn-bedrockagentcore-runtime-s3location-versionid)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-s3location-syntax.yaml"></a>

```
  [Bucket](#cfn-bedrockagentcore-runtime-s3location-bucket): {{String}}
  [Prefix](#cfn-bedrockagentcore-runtime-s3location-prefix): {{String}}
  [VersionId](#cfn-bedrockagentcore-runtime-s3location-versionid): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-s3location-properties"></a>

`Bucket`  <a name="cfn-bedrockagentcore-runtime-s3location-bucket"></a>
The name of the Amazon S3 bucket.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-bedrockagentcore-runtime-s3location-prefix"></a>
The prefix for objects in the Amazon S3 bucket.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionId`  <a name="cfn-bedrockagentcore-runtime-s3location-versionid"></a>
The version ID of the Amazon Amazon S3 object. If not specified, the latest version of the object is used.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
