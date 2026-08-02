---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-customplugin-custompluginlocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::CustomPlugin CustomPluginLocation
<a name="aws-properties-kafkaconnect-customplugin-custompluginlocation"></a>

Information about the location of a custom plugin.

## Syntax
<a name="aws-properties-kafkaconnect-customplugin-custompluginlocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-customplugin-custompluginlocation-syntax.json"></a>

```
{
  "[S3Location](#cfn-kafkaconnect-customplugin-custompluginlocation-s3location)" : {{S3Location}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-customplugin-custompluginlocation-syntax.yaml"></a>

```
  [S3Location](#cfn-kafkaconnect-customplugin-custompluginlocation-s3location): {{
    S3Location}}
```

## Properties
<a name="aws-properties-kafkaconnect-customplugin-custompluginlocation-properties"></a>

`S3Location`  <a name="cfn-kafkaconnect-customplugin-custompluginlocation-s3location"></a>
The S3 bucket Amazon Resource Name (ARN), file key, and object version of the plugin file stored in Amazon S3.
*Required*: Yes
*Type*: [S3Location](aws-properties-kafkaconnect-customplugin-s3location.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
