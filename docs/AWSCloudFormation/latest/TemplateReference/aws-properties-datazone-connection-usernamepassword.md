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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
