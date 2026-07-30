---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-intermediatestorage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource IntermediateStorage
<a name="aws-properties-bedrock-datasource-intermediatestorage"></a>

A location for storing content from data sources temporarily as it is processed by custom components in the ingestion pipeline.

## Syntax
<a name="aws-properties-bedrock-datasource-intermediatestorage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-intermediatestorage-syntax.json"></a>

```
{
  "[S3Location](#cfn-bedrock-datasource-intermediatestorage-s3location)" : {{S3Location}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-intermediatestorage-syntax.yaml"></a>

```
  [S3Location](#cfn-bedrock-datasource-intermediatestorage-s3location): {{
    S3Location}}
```

## Properties
<a name="aws-properties-bedrock-datasource-intermediatestorage-properties"></a>

`S3Location`  <a name="cfn-bedrock-datasource-intermediatestorage-s3location"></a>
An S3 bucket path.
*Required*: Yes
*Type*: [S3Location](aws-properties-bedrock-datasource-s3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
