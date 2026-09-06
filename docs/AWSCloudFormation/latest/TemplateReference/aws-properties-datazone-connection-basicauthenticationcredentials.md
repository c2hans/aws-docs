---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-basicauthenticationcredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection BasicAuthenticationCredentials
<a name="aws-properties-datazone-connection-basicauthenticationcredentials"></a>

The basic authentication credentials of a connection.

## Syntax
<a name="aws-properties-datazone-connection-basicauthenticationcredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-basicauthenticationcredentials-syntax.json"></a>

```
{
  "[Password](#cfn-datazone-connection-basicauthenticationcredentials-password)" : {{String}},
  "[UserName](#cfn-datazone-connection-basicauthenticationcredentials-username)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-basicauthenticationcredentials-syntax.yaml"></a>

```
  [Password](#cfn-datazone-connection-basicauthenticationcredentials-password): {{String}}
  [UserName](#cfn-datazone-connection-basicauthenticationcredentials-username): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-basicauthenticationcredentials-properties"></a>

`Password`  <a name="cfn-datazone-connection-basicauthenticationcredentials-password"></a>
The password for a connection.
*Required*: No
*Type*: String
*Pattern*: `^.*$`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserName`  <a name="cfn-datazone-connection-basicauthenticationcredentials-username"></a>
The user name for the connecion.
*Required*: No
*Type*: String
*Pattern*: `^\S+$`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
