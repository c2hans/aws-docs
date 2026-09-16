---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-customauthenticationproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType CustomAuthenticationProperties
<a name="aws-properties-glue-connectiontype-customauthenticationproperties"></a>

<a name="aws-properties-glue-connectiontype-customauthenticationproperties-description"></a>The `CustomAuthenticationProperties` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-customauthenticationproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-customauthenticationproperties-syntax.json"></a>

```
{
  "[AuthenticationParameters](#cfn-glue-connectiontype-customauthenticationproperties-authenticationparameters)" : {{[ SecretConnectorProperty, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-customauthenticationproperties-syntax.yaml"></a>

```
  [AuthenticationParameters](#cfn-glue-connectiontype-customauthenticationproperties-authenticationparameters): {{
    - SecretConnectorProperty}}
```

## Properties
<a name="aws-properties-glue-connectiontype-customauthenticationproperties-properties"></a>

`AuthenticationParameters`  <a name="cfn-glue-connectiontype-customauthenticationproperties-authenticationparameters"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [SecretConnectorProperty](aws-properties-glue-connectiontype-secretconnectorproperty.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
