---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-clientcredentialsproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType ClientCredentialsProperties
<a name="aws-properties-glue-connectiontype-clientcredentialsproperties"></a>

<a name="aws-properties-glue-connectiontype-clientcredentialsproperties-description"></a>The `ClientCredentialsProperties` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-clientcredentialsproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-clientcredentialsproperties-syntax.json"></a>

```
{
  "[ClientId](#cfn-glue-connectiontype-clientcredentialsproperties-clientid)" : {{SecretConnectorProperty}},
  "[ClientSecret](#cfn-glue-connectiontype-clientcredentialsproperties-clientsecret)" : {{SecretConnectorProperty}},
  "[ContentType](#cfn-glue-connectiontype-clientcredentialsproperties-contenttype)" : {{String}},
  "[RequestMethod](#cfn-glue-connectiontype-clientcredentialsproperties-requestmethod)" : {{String}},
  "[Scope](#cfn-glue-connectiontype-clientcredentialsproperties-scope)" : {{ConnectorProperty}},
  "[TokenUrl](#cfn-glue-connectiontype-clientcredentialsproperties-tokenurl)" : {{ConnectorProperty}},
  "[TokenUrlParameters](#cfn-glue-connectiontype-clientcredentialsproperties-tokenurlparameters)" : {{[ ConnectorProperty, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-clientcredentialsproperties-syntax.yaml"></a>

```
  [ClientId](#cfn-glue-connectiontype-clientcredentialsproperties-clientid): {{
    SecretConnectorProperty}}
  [ClientSecret](#cfn-glue-connectiontype-clientcredentialsproperties-clientsecret): {{
    SecretConnectorProperty}}
  [ContentType](#cfn-glue-connectiontype-clientcredentialsproperties-contenttype): {{String}}
  [RequestMethod](#cfn-glue-connectiontype-clientcredentialsproperties-requestmethod): {{String}}
  [Scope](#cfn-glue-connectiontype-clientcredentialsproperties-scope): {{
    ConnectorProperty}}
  [TokenUrl](#cfn-glue-connectiontype-clientcredentialsproperties-tokenurl): {{
    ConnectorProperty}}
  [TokenUrlParameters](#cfn-glue-connectiontype-clientcredentialsproperties-tokenurlparameters): {{
    - ConnectorProperty}}
```

## Properties
<a name="aws-properties-glue-connectiontype-clientcredentialsproperties-properties"></a>

`ClientId`  <a name="cfn-glue-connectiontype-clientcredentialsproperties-clientid"></a>
Property description not available.
*Required*: No
*Type*: [SecretConnectorProperty](aws-properties-glue-connectiontype-secretconnectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClientSecret`  <a name="cfn-glue-connectiontype-clientcredentialsproperties-clientsecret"></a>
Property description not available.
*Required*: No
*Type*: [SecretConnectorProperty](aws-properties-glue-connectiontype-secretconnectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContentType`  <a name="cfn-glue-connectiontype-clientcredentialsproperties-contenttype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `APPLICATION_JSON | URL_ENCODED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RequestMethod`  <a name="cfn-glue-connectiontype-clientcredentialsproperties-requestmethod"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `GET | POST`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Scope`  <a name="cfn-glue-connectiontype-clientcredentialsproperties-scope"></a>
Property description not available.
*Required*: No
*Type*: [ConnectorProperty](aws-properties-glue-connectiontype-connectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TokenUrl`  <a name="cfn-glue-connectiontype-clientcredentialsproperties-tokenurl"></a>
Property description not available.
*Required*: No
*Type*: [ConnectorProperty](aws-properties-glue-connectiontype-connectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TokenUrlParameters`  <a name="cfn-glue-connectiontype-clientcredentialsproperties-tokenurlparameters"></a>
Property description not available.
*Required*: No
*Type*: Array of [ConnectorProperty](aws-properties-glue-connectiontype-connectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
