---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-validationendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType ValidationEndpointConfiguration
<a name="aws-properties-glue-connectiontype-validationendpointconfiguration"></a>

<a name="aws-properties-glue-connectiontype-validationendpointconfiguration-description"></a>The `ValidationEndpointConfiguration` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-validationendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-validationendpointconfiguration-syntax.json"></a>

```
{
  "[RequestMethod](#cfn-glue-connectiontype-validationendpointconfiguration-requestmethod)" : {{String}},
  "[RequestPath](#cfn-glue-connectiontype-validationendpointconfiguration-requestpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-validationendpointconfiguration-syntax.yaml"></a>

```
  [RequestMethod](#cfn-glue-connectiontype-validationendpointconfiguration-requestmethod): {{String}}
  [RequestPath](#cfn-glue-connectiontype-validationendpointconfiguration-requestpath): {{String}}
```

## Properties
<a name="aws-properties-glue-connectiontype-validationendpointconfiguration-properties"></a>

`RequestMethod`  <a name="cfn-glue-connectiontype-validationendpointconfiguration-requestmethod"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `GET | POST`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RequestPath`  <a name="cfn-glue-connectiontype-validationendpointconfiguration-requestpath"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^/[a-zA-Z0-9._~:/?#\[\]@!$&'()*+,;={}-]*$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
