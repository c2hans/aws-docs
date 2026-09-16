---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-connectorauthenticationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType ConnectorAuthenticationConfiguration
<a name="aws-properties-glue-connectiontype-connectorauthenticationconfiguration"></a>

<a name="aws-properties-glue-connectiontype-connectorauthenticationconfiguration-description"></a>The `ConnectorAuthenticationConfiguration` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-connectorauthenticationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-connectorauthenticationconfiguration-syntax.json"></a>

```
{
  "[AuthenticationTypes](#cfn-glue-connectiontype-connectorauthenticationconfiguration-authenticationtypes)" : {{[ String, ... ]}},
  "[BasicAuthenticationProperties](#cfn-glue-connectiontype-connectorauthenticationconfiguration-basicauthenticationproperties)" : {{BasicAuthenticationProperties}},
  "[CustomAuthenticationProperties](#cfn-glue-connectiontype-connectorauthenticationconfiguration-customauthenticationproperties)" : {{CustomAuthenticationProperties}},
  "[OAuth2Properties](#cfn-glue-connectiontype-connectorauthenticationconfiguration-oauth2properties)" : {{ConnectorOAuth2Properties}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-connectorauthenticationconfiguration-syntax.yaml"></a>

```
  [AuthenticationTypes](#cfn-glue-connectiontype-connectorauthenticationconfiguration-authenticationtypes): {{
    - String}}
  [BasicAuthenticationProperties](#cfn-glue-connectiontype-connectorauthenticationconfiguration-basicauthenticationproperties): {{
    BasicAuthenticationProperties}}
  [CustomAuthenticationProperties](#cfn-glue-connectiontype-connectorauthenticationconfiguration-customauthenticationproperties): {{
    CustomAuthenticationProperties}}
  [OAuth2Properties](#cfn-glue-connectiontype-connectorauthenticationconfiguration-oauth2properties): {{
    ConnectorOAuth2Properties}}
```

## Properties
<a name="aws-properties-glue-connectiontype-connectorauthenticationconfiguration-properties"></a>

`AuthenticationTypes`  <a name="cfn-glue-connectiontype-connectorauthenticationconfiguration-authenticationtypes"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `BASIC | OAUTH2 | CUSTOM | IAM`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BasicAuthenticationProperties`  <a name="cfn-glue-connectiontype-connectorauthenticationconfiguration-basicauthenticationproperties"></a>
Property description not available.
*Required*: No
*Type*: [BasicAuthenticationProperties](aws-properties-glue-connectiontype-basicauthenticationproperties.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomAuthenticationProperties`  <a name="cfn-glue-connectiontype-connectorauthenticationconfiguration-customauthenticationproperties"></a>
Property description not available.
*Required*: No
*Type*: [CustomAuthenticationProperties](aws-properties-glue-connectiontype-customauthenticationproperties.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OAuth2Properties`  <a name="cfn-glue-connectiontype-connectorauthenticationconfiguration-oauth2properties"></a>
Property description not available.
*Required*: No
*Type*: [ConnectorOAuth2Properties](aws-properties-glue-connectiontype-connectoroauth2properties.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
