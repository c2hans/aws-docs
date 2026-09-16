---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-jwtbearerproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType JWTBearerProperties
<a name="aws-properties-glue-connectiontype-jwtbearerproperties"></a>

<a name="aws-properties-glue-connectiontype-jwtbearerproperties-description"></a>The `JWTBearerProperties` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-jwtbearerproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-jwtbearerproperties-syntax.json"></a>

```
{
  "[ContentType](#cfn-glue-connectiontype-jwtbearerproperties-contenttype)" : {{String}},
  "[JwtToken](#cfn-glue-connectiontype-jwtbearerproperties-jwttoken)" : {{SecretConnectorProperty}},
  "[RequestMethod](#cfn-glue-connectiontype-jwtbearerproperties-requestmethod)" : {{String}},
  "[TokenUrl](#cfn-glue-connectiontype-jwtbearerproperties-tokenurl)" : {{ConnectorProperty}},
  "[TokenUrlParameters](#cfn-glue-connectiontype-jwtbearerproperties-tokenurlparameters)" : {{[ ConnectorProperty, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-jwtbearerproperties-syntax.yaml"></a>

```
  [ContentType](#cfn-glue-connectiontype-jwtbearerproperties-contenttype): {{String}}
  [JwtToken](#cfn-glue-connectiontype-jwtbearerproperties-jwttoken): {{
    SecretConnectorProperty}}
  [RequestMethod](#cfn-glue-connectiontype-jwtbearerproperties-requestmethod): {{String}}
  [TokenUrl](#cfn-glue-connectiontype-jwtbearerproperties-tokenurl): {{
    ConnectorProperty}}
  [TokenUrlParameters](#cfn-glue-connectiontype-jwtbearerproperties-tokenurlparameters): {{
    - ConnectorProperty}}
```

## Properties
<a name="aws-properties-glue-connectiontype-jwtbearerproperties-properties"></a>

`ContentType`  <a name="cfn-glue-connectiontype-jwtbearerproperties-contenttype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `APPLICATION_JSON | URL_ENCODED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JwtToken`  <a name="cfn-glue-connectiontype-jwtbearerproperties-jwttoken"></a>
Property description not available.
*Required*: No
*Type*: [SecretConnectorProperty](aws-properties-glue-connectiontype-secretconnectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RequestMethod`  <a name="cfn-glue-connectiontype-jwtbearerproperties-requestmethod"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `GET | POST`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TokenUrl`  <a name="cfn-glue-connectiontype-jwtbearerproperties-tokenurl"></a>
Property description not available.
*Required*: No
*Type*: [ConnectorProperty](aws-properties-glue-connectiontype-connectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TokenUrlParameters`  <a name="cfn-glue-connectiontype-jwtbearerproperties-tokenurlparameters"></a>
Property description not available.
*Required*: No
*Type*: Array of [ConnectorProperty](aws-properties-glue-connectiontype-connectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
