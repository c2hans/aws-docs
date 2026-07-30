---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-customauthcredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile CustomAuthCredentials
<a name="aws-properties-appflow-connectorprofile-customauthcredentials"></a>

The custom credentials required for custom authentication.

## Syntax
<a name="aws-properties-appflow-connectorprofile-customauthcredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-customauthcredentials-syntax.json"></a>

```
{
  "[CredentialsMap](#cfn-appflow-connectorprofile-customauthcredentials-credentialsmap)" : {{{{{Key}}: {{Value}}, ...}}},
  "[CustomAuthenticationType](#cfn-appflow-connectorprofile-customauthcredentials-customauthenticationtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-customauthcredentials-syntax.yaml"></a>

```
  [CredentialsMap](#cfn-appflow-connectorprofile-customauthcredentials-credentialsmap): {{
    {{Key}}: {{Value}}}}
  [CustomAuthenticationType](#cfn-appflow-connectorprofile-customauthcredentials-customauthenticationtype): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-customauthcredentials-properties"></a>

`CredentialsMap`  <a name="cfn-appflow-connectorprofile-customauthcredentials-credentialsmap"></a>
A map that holds custom authentication credentials.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\w]{1,128}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomAuthenticationType`  <a name="cfn-appflow-connectorprofile-customauthcredentials-customauthenticationtype"></a>
The custom authentication type that the connector uses.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
