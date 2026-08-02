---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-connector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::Connector
<a name="aws-resource-config-connector"></a>

The details of the connector, including the connector configuration and connector ARN.

## Syntax
<a name="aws-resource-config-connector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-config-connector-syntax.json"></a>

```
{
  "Type" : "AWS::Config::Connector",
  "Properties" : {
      "[ConnectorConfiguration](#cfn-config-connector-connectorconfiguration)" : {{ConnectorConfiguration}},
      "[Tags](#cfn-config-connector-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-config-connector-syntax.yaml"></a>

```
Type: AWS::Config::Connector
Properties:
  [ConnectorConfiguration](#cfn-config-connector-connectorconfiguration): {{
    ConnectorConfiguration}}
  [Tags](#cfn-config-connector-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-config-connector-properties"></a>

`ConnectorConfiguration`  <a name="cfn-config-connector-connectorconfiguration"></a>
The provider-specific configuration for connecting to the third-party cloud service provider.
*Required*: Yes
*Type*: [ConnectorConfiguration](aws-properties-config-connector-connectorconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-config-connector-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-config-connector-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-config-connector-return-values"></a>

### Ref
<a name="aws-resource-config-connector-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-config-connector-return-values-fn--getatt"></a>

####
<a name="aws-resource-config-connector-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the connector.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The date and time that the connector was created.

`Name`  <a name="Name-fn::getatt"></a>
The name of the connector.
