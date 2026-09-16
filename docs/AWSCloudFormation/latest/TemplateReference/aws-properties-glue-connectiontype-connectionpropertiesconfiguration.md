---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-connectionpropertiesconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType ConnectionPropertiesConfiguration
<a name="aws-properties-glue-connectiontype-connectionpropertiesconfiguration"></a>

<a name="aws-properties-glue-connectiontype-connectionpropertiesconfiguration-description"></a>The `ConnectionPropertiesConfiguration` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-connectionpropertiesconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-connectionpropertiesconfiguration-syntax.json"></a>

```
{
  "[AdditionalRequestParameters](#cfn-glue-connectiontype-connectionpropertiesconfiguration-additionalrequestparameters)" : {{[ ConnectorProperty, ... ]}},
  "[Url](#cfn-glue-connectiontype-connectionpropertiesconfiguration-url)" : {{ConnectorProperty}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-connectionpropertiesconfiguration-syntax.yaml"></a>

```
  [AdditionalRequestParameters](#cfn-glue-connectiontype-connectionpropertiesconfiguration-additionalrequestparameters): {{
    - ConnectorProperty}}
  [Url](#cfn-glue-connectiontype-connectionpropertiesconfiguration-url): {{
    ConnectorProperty}}
```

## Properties
<a name="aws-properties-glue-connectiontype-connectionpropertiesconfiguration-properties"></a>

`AdditionalRequestParameters`  <a name="cfn-glue-connectiontype-connectionpropertiesconfiguration-additionalrequestparameters"></a>
Property description not available.
*Required*: No
*Type*: Array of [ConnectorProperty](aws-properties-glue-connectiontype-connectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Url`  <a name="cfn-glue-connectiontype-connectionpropertiesconfiguration-url"></a>
Property description not available.
*Required*: No
*Type*: [ConnectorProperty](aws-properties-glue-connectiontype-connectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
