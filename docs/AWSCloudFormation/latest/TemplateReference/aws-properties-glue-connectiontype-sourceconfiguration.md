---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-sourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType SourceConfiguration
<a name="aws-properties-glue-connectiontype-sourceconfiguration"></a>

<a name="aws-properties-glue-connectiontype-sourceconfiguration-description"></a>The `SourceConfiguration` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-sourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-sourceconfiguration-syntax.json"></a>

```
{
  "[FilterConfiguration](#cfn-glue-connectiontype-sourceconfiguration-filterconfiguration)" : {{FilterConfiguration}},
  "[PaginationConfiguration](#cfn-glue-connectiontype-sourceconfiguration-paginationconfiguration)" : {{PaginationConfiguration}},
  "[RequestMethod](#cfn-glue-connectiontype-sourceconfiguration-requestmethod)" : {{String}},
  "[RequestParameters](#cfn-glue-connectiontype-sourceconfiguration-requestparameters)" : {{[ ConnectorProperty, ... ]}},
  "[RequestPath](#cfn-glue-connectiontype-sourceconfiguration-requestpath)" : {{String}},
  "[ResponseConfiguration](#cfn-glue-connectiontype-sourceconfiguration-responseconfiguration)" : {{ResponseConfiguration}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-sourceconfiguration-syntax.yaml"></a>

```
  [FilterConfiguration](#cfn-glue-connectiontype-sourceconfiguration-filterconfiguration): {{
    FilterConfiguration}}
  [PaginationConfiguration](#cfn-glue-connectiontype-sourceconfiguration-paginationconfiguration): {{
    PaginationConfiguration}}
  [RequestMethod](#cfn-glue-connectiontype-sourceconfiguration-requestmethod): {{String}}
  [RequestParameters](#cfn-glue-connectiontype-sourceconfiguration-requestparameters): {{
    - ConnectorProperty}}
  [RequestPath](#cfn-glue-connectiontype-sourceconfiguration-requestpath): {{String}}
  [ResponseConfiguration](#cfn-glue-connectiontype-sourceconfiguration-responseconfiguration): {{
    ResponseConfiguration}}
```

## Properties
<a name="aws-properties-glue-connectiontype-sourceconfiguration-properties"></a>

`FilterConfiguration`  <a name="cfn-glue-connectiontype-sourceconfiguration-filterconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [FilterConfiguration](aws-properties-glue-connectiontype-filterconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PaginationConfiguration`  <a name="cfn-glue-connectiontype-sourceconfiguration-paginationconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [PaginationConfiguration](aws-properties-glue-connectiontype-paginationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RequestMethod`  <a name="cfn-glue-connectiontype-sourceconfiguration-requestmethod"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `GET | POST`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RequestParameters`  <a name="cfn-glue-connectiontype-sourceconfiguration-requestparameters"></a>
Property description not available.
*Required*: No
*Type*: Array of [ConnectorProperty](aws-properties-glue-connectiontype-connectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RequestPath`  <a name="cfn-glue-connectiontype-sourceconfiguration-requestpath"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^/[a-zA-Z0-9._~:/?#\[\]@!$&'()*+,;={}-]*$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResponseConfiguration`  <a name="cfn-glue-connectiontype-sourceconfiguration-responseconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [ResponseConfiguration](aws-properties-glue-connectiontype-responseconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
