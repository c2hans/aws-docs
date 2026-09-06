---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-browsercustom-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::BrowserCustom S3Location
<a name="aws-properties-bedrockagentcore-browsercustom-s3location"></a>

The Amazon S3 location for storing data. This structure defines where in Amazon S3 data is stored.

## Syntax
<a name="aws-properties-bedrockagentcore-browsercustom-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-browsercustom-s3location-syntax.json"></a>

```
{
  "[Bucket](#cfn-bedrockagentcore-browsercustom-s3location-bucket)" : {{String}},
  "[Prefix](#cfn-bedrockagentcore-browsercustom-s3location-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-browsercustom-s3location-syntax.yaml"></a>

```
  [Bucket](#cfn-bedrockagentcore-browsercustom-s3location-bucket): {{String}}
  [Prefix](#cfn-bedrockagentcore-browsercustom-s3location-prefix): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-browsercustom-s3location-properties"></a>

`Bucket`  <a name="cfn-bedrockagentcore-browsercustom-s3location-bucket"></a>
The name of the Amazon S3 bucket. This bucket contains the stored data.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Prefix`  <a name="cfn-bedrockagentcore-browsercustom-s3location-prefix"></a>
The prefix for objects in the Amazon S3 bucket. This prefix is added to the object keys to organize the data.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
