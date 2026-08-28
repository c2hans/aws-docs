---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-webapp-webappunits.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::WebApp WebAppUnits
<a name="aws-properties-transfer-webapp-webappunits"></a>

Contains an integer value that represents the value for number of concurrent connections or the user sessions on your web app.

## Syntax
<a name="aws-properties-transfer-webapp-webappunits-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-webapp-webappunits-syntax.json"></a>

```
{
  "[Provisioned](#cfn-transfer-webapp-webappunits-provisioned)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-transfer-webapp-webappunits-syntax.yaml"></a>

```
  [Provisioned](#cfn-transfer-webapp-webappunits-provisioned): {{Integer}}
```

## Properties
<a name="aws-properties-transfer-webapp-webappunits-properties"></a>

`Provisioned`  <a name="cfn-transfer-webapp-webappunits-provisioned"></a>
An integer that represents the number of units for your desired number of concurrent connections, or the number of user sessions on your web app at the same time.
Each increment allows an additional 250 concurrent sessions: a value of `1` sets the number of concurrent sessions to 250; `2` sets a value of 500, and so on.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
