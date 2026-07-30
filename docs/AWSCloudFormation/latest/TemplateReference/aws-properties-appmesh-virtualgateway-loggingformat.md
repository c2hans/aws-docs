---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-loggingformat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway LoggingFormat
<a name="aws-properties-appmesh-virtualgateway-loggingformat"></a>

An object that represents the format for the logs.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-loggingformat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-loggingformat-syntax.json"></a>

```
{
  "[Json](#cfn-appmesh-virtualgateway-loggingformat-json)" : {{[ JsonFormatRef, ... ]}},
  "[Text](#cfn-appmesh-virtualgateway-loggingformat-text)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-loggingformat-syntax.yaml"></a>

```
  [Json](#cfn-appmesh-virtualgateway-loggingformat-json): {{
    - JsonFormatRef}}
  [Text](#cfn-appmesh-virtualgateway-loggingformat-text): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-loggingformat-properties"></a>

`Json`  <a name="cfn-appmesh-virtualgateway-loggingformat-json"></a>
The logging format for JSON.
*Required*: No
*Type*: Array of [JsonFormatRef](aws-properties-appmesh-virtualgateway-jsonformatref.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-appmesh-virtualgateway-loggingformat-text"></a>
The logging format for text.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
