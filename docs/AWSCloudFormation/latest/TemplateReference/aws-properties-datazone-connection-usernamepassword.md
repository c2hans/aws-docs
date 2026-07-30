---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-usernamepassword.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection UsernamePassword
<a name="aws-properties-datazone-connection-usernamepassword"></a>

The username and password of a connection.

## Syntax
<a name="aws-properties-datazone-connection-usernamepassword-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-usernamepassword-syntax.json"></a>

```
{
  "[Password](#cfn-datazone-connection-usernamepassword-password)" : {{String}},
  "[Username](#cfn-datazone-connection-usernamepassword-username)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-usernamepassword-syntax.yaml"></a>

```
  [Password](#cfn-datazone-connection-usernamepassword-password): {{String}}
  [Username](#cfn-datazone-connection-usernamepassword-username): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-usernamepassword-properties"></a>

`Password`  <a name="cfn-datazone-connection-usernamepassword-password"></a>
The password of a connection.
*Required*: Yes
*Type*: String
*Pattern*: `^[\S]*$`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-datazone-connection-usernamepassword-username"></a>
The username of a connection.
*Required*: Yes
*Type*: String
*Pattern*: `^[\S]*$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
