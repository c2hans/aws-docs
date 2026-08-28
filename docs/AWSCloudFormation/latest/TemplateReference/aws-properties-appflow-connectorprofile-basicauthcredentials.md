---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-basicauthcredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile BasicAuthCredentials
<a name="aws-properties-appflow-connectorprofile-basicauthcredentials"></a>

 The basic auth credentials required for basic authentication.

## Syntax
<a name="aws-properties-appflow-connectorprofile-basicauthcredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-basicauthcredentials-syntax.json"></a>

```
{
  "[Password](#cfn-appflow-connectorprofile-basicauthcredentials-password)" : {{String}},
  "[Username](#cfn-appflow-connectorprofile-basicauthcredentials-username)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-basicauthcredentials-syntax.yaml"></a>

```
  [Password](#cfn-appflow-connectorprofile-basicauthcredentials-password): {{String}}
  [Username](#cfn-appflow-connectorprofile-basicauthcredentials-username): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-basicauthcredentials-properties"></a>

`Password`  <a name="cfn-appflow-connectorprofile-basicauthcredentials-password"></a>
 The password to use to connect to a resource.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-appflow-connectorprofile-basicauthcredentials-username"></a>
 The username to use to connect to a resource.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
