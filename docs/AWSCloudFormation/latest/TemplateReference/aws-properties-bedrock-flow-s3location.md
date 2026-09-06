---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow S3Location
<a name="aws-properties-bedrock-flow-s3location"></a>

The S3 location of the flow definition.

## Syntax
<a name="aws-properties-bedrock-flow-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-s3location-syntax.json"></a>

```
{
  "[Bucket](#cfn-bedrock-flow-s3location-bucket)" : {{String}},
  "[Key](#cfn-bedrock-flow-s3location-key)" : {{String}},
  "[Version](#cfn-bedrock-flow-s3location-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-s3location-syntax.yaml"></a>

```
  [Bucket](#cfn-bedrock-flow-s3location-bucket): {{String}}
  [Key](#cfn-bedrock-flow-s3location-key): {{String}}
  [Version](#cfn-bedrock-flow-s3location-version): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flow-s3location-properties"></a>

`Bucket`  <a name="cfn-bedrock-flow-s3location-bucket"></a>
The S3 bucket containing the flow definition.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-bedrock-flow-s3location-key"></a>
The object key for the S3 location containing the definition.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-bedrock-flow-s3location-version"></a>
The Amazon S3 location from which to retrieve data for an S3 retrieve node or to which to store data for an S3 storage node.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
