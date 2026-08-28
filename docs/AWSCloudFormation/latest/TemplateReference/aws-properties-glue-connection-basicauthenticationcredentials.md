---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connection-basicauthenticationcredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Connection BasicAuthenticationCredentials
<a name="aws-properties-glue-connection-basicauthenticationcredentials"></a>

For supplying basic auth credentials when not providing a `SecretArn` value.

## Syntax
<a name="aws-properties-glue-connection-basicauthenticationcredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connection-basicauthenticationcredentials-syntax.json"></a>

```
{
  "[Password](#cfn-glue-connection-basicauthenticationcredentials-password)" : {{String}},
  "[Username](#cfn-glue-connection-basicauthenticationcredentials-username)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-connection-basicauthenticationcredentials-syntax.yaml"></a>

```
  [Password](#cfn-glue-connection-basicauthenticationcredentials-password): {{String}}
  [Username](#cfn-glue-connection-basicauthenticationcredentials-username): {{String}}
```

## Properties
<a name="aws-properties-glue-connection-basicauthenticationcredentials-properties"></a>

`Password`  <a name="cfn-glue-connection-basicauthenticationcredentials-password"></a>
The password to connect to the data source.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-glue-connection-basicauthenticationcredentials-username"></a>
The username to connect to the data source.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
