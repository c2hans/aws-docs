---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-connectorauthorizationcodeproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType ConnectorAuthorizationCodeProperties
<a name="aws-properties-glue-connectiontype-connectorauthorizationcodeproperties"></a>

<a name="aws-properties-glue-connectiontype-connectorauthorizationcodeproperties-description"></a>The `ConnectorAuthorizationCodeProperties` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-connectorauthorizationcodeproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-connectorauthorizationcodeproperties-syntax.json"></a>

```
{
  "[AuthorizationCode](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-authorizationcode)" : {{ConnectorProperty}},
  "[AuthorizationCodeUrl](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-authorizationcodeurl)" : {{ConnectorProperty}},
  "[ClientId](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-clientid)" : {{SecretConnectorProperty}},
  "[ClientSecret](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-clientsecret)" : {{SecretConnectorProperty}},
  "[ContentType](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-contenttype)" : {{String}},
  "[Prompt](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-prompt)" : {{ConnectorProperty}},
  "[RedirectUri](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-redirecturi)" : {{ConnectorProperty}},
  "[RequestMethod](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-requestmethod)" : {{String}},
  "[Scope](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-scope)" : {{ConnectorProperty}},
  "[TokenUrl](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-tokenurl)" : {{ConnectorProperty}},
  "[TokenUrlParameters](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-tokenurlparameters)" : {{[ ConnectorProperty, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-connectorauthorizationcodeproperties-syntax.yaml"></a>

```
  [AuthorizationCode](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-authorizationcode): {{
    ConnectorProperty}}
  [AuthorizationCodeUrl](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-authorizationcodeurl): {{
    ConnectorProperty}}
  [ClientId](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-clientid): {{
    SecretConnectorProperty}}
  [ClientSecret](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-clientsecret): {{
    SecretConnectorProperty}}
  [ContentType](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-contenttype): {{String}}
  [Prompt](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-prompt): {{
    ConnectorProperty}}
  [RedirectUri](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-redirecturi): {{
    ConnectorProperty}}
  [RequestMethod](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-requestmethod): {{String}}
  [Scope](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-scope): {{
    ConnectorProperty}}
  [TokenUrl](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-tokenurl): {{
    ConnectorProperty}}
  [TokenUrlParameters](#cfn-glue-connectiontype-connectorauthorizationcodeproperties-tokenurlparameters): {{
    - ConnectorProperty}}
```

## Properties
<a name="aws-properties-glue-connectiontype-connectorauthorizationcodeproperties-properties"></a>

`AuthorizationCode`  <a name="cfn-glue-connectiontype-connectorauthorizationcodeproperties-authorizationcode"></a>
Property description not available.
*Required*: No
*Type*: [ConnectorProperty](aws-properties-glue-connectiontype-connectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AuthorizationCodeUrl`  <a name="cfn-glue-connectiontype-connectorauthorizationcodeproperties-authorizationcodeurl"></a>
Property description not available.
*Required*: No
*Type*: [ConnectorProperty](aws-properties-glue-connectiontype-connectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClientId`  <a name="cfn-glue-connectiontype-connectorauthorizationcodeproperties-clientid"></a>
Property description not available.
*Required*: No
*Type*: [SecretConnectorProperty](aws-properties-glue-connectiontype-secretconnectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClientSecret`  <a name="cfn-glue-connectiontype-connectorauthorizationcodeproperties-clientsecret"></a>
Property description not available.
*Required*: No
*Type*: [SecretConnectorProperty](aws-properties-glue-connectiontype-secretconnectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContentType`  <a name="cfn-glue-connectiontype-connectorauthorizationcodeproperties-contenttype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `APPLICATION_JSON | URL_ENCODED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Prompt`  <a name="cfn-glue-connectiontype-connectorauthorizationcodeproperties-prompt"></a>
Property description not available.
*Required*: No
*Type*: [ConnectorProperty](aws-properties-glue-connectiontype-connectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RedirectUri`  <a name="cfn-glue-connectiontype-connectorauthorizationcodeproperties-redirecturi"></a>
Property description not available.
*Required*: No
*Type*: [ConnectorProperty](aws-properties-glue-connectiontype-connectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RequestMethod`  <a name="cfn-glue-connectiontype-connectorauthorizationcodeproperties-requestmethod"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `GET | POST`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Scope`  <a name="cfn-glue-connectiontype-connectorauthorizationcodeproperties-scope"></a>
Property description not available.
*Required*: No
*Type*: [ConnectorProperty](aws-properties-glue-connectiontype-connectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TokenUrl`  <a name="cfn-glue-connectiontype-connectorauthorizationcodeproperties-tokenurl"></a>
Property description not available.
*Required*: No
*Type*: [ConnectorProperty](aws-properties-glue-connectiontype-connectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TokenUrlParameters`  <a name="cfn-glue-connectiontype-connectorauthorizationcodeproperties-tokenurlparameters"></a>
Property description not available.
*Required*: No
*Type*: Array of [ConnectorProperty](aws-properties-glue-connectiontype-connectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
