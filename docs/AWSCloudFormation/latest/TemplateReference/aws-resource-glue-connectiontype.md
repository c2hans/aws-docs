---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-connectiontype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType
<a name="aws-resource-glue-connectiontype"></a>

<a name="aws-resource-glue-connectiontype-description"></a>The `AWS::Glue::ConnectionType` resource Property description not available. for Glue.

## Syntax
<a name="aws-resource-glue-connectiontype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-glue-connectiontype-syntax.json"></a>

```
{
  "Type" : "AWS::Glue::ConnectionType",
  "Properties" : {
      "[ConnectionProperties](#cfn-glue-connectiontype-connectionproperties)" : {{ConnectionPropertiesConfiguration}},
      "[ConnectionType](#cfn-glue-connectiontype-connectiontype)" : {{String}},
      "[ConnectorAuthenticationConfiguration](#cfn-glue-connectiontype-connectorauthenticationconfiguration)" : {{ConnectorAuthenticationConfiguration}},
      "[Description](#cfn-glue-connectiontype-description)" : {{String}},
      "[IntegrationType](#cfn-glue-connectiontype-integrationtype)" : {{String}},
      "[RestConfiguration](#cfn-glue-connectiontype-restconfiguration)" : {{RestConfiguration}},
      "[Tags](#cfn-glue-connectiontype-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-glue-connectiontype-syntax.yaml"></a>

```
Type: AWS::Glue::ConnectionType
Properties:
  [ConnectionProperties](#cfn-glue-connectiontype-connectionproperties): {{
    ConnectionPropertiesConfiguration}}
  [ConnectionType](#cfn-glue-connectiontype-connectiontype): {{String}}
  [ConnectorAuthenticationConfiguration](#cfn-glue-connectiontype-connectorauthenticationconfiguration): {{
    ConnectorAuthenticationConfiguration}}
  [Description](#cfn-glue-connectiontype-description): {{String}}
  [IntegrationType](#cfn-glue-connectiontype-integrationtype): {{String}}
  [RestConfiguration](#cfn-glue-connectiontype-restconfiguration): {{
    RestConfiguration}}
  [Tags](#cfn-glue-connectiontype-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-glue-connectiontype-properties"></a>

`ConnectionProperties`  <a name="cfn-glue-connectiontype-connectionproperties"></a>
Property description not available.
*Required*: No
*Type*: [ConnectionPropertiesConfiguration](aws-properties-glue-connectiontype-connectionpropertiesconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConnectionType`  <a name="cfn-glue-connectiontype-connectiontype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConnectorAuthenticationConfiguration`  <a name="cfn-glue-connectiontype-connectorauthenticationconfiguration"></a>
A structure containing the authentication configuration.
*Required*: No
*Type*: [ConnectorAuthenticationConfiguration](aws-properties-glue-connectiontype-connectorauthenticationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-glue-connectiontype-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IntegrationType`  <a name="cfn-glue-connectiontype-integrationtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `REST`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RestConfiguration`  <a name="cfn-glue-connectiontype-restconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [RestConfiguration](aws-properties-glue-connectiontype-restconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-glue-connectiontype-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-glue-connectiontype-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-glue-connectiontype-return-values"></a>

### Ref
<a name="aws-resource-glue-connectiontype-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-glue-connectiontype-return-values-fn--getatt"></a>

####
<a name="aws-resource-glue-connectiontype-return-values-fn--getatt-fn--getatt"></a>

`ConnectionTypeArn`  <a name="ConnectionTypeArn-fn::getatt"></a>
Property description not available.
