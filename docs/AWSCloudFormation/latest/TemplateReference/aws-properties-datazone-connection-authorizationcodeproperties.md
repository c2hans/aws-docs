---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-authorizationcodeproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection AuthorizationCodeProperties
<a name="aws-properties-datazone-connection-authorizationcodeproperties"></a>

The authorization code properties of a connection.

## Syntax
<a name="aws-properties-datazone-connection-authorizationcodeproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-authorizationcodeproperties-syntax.json"></a>

```
{
  "[AuthorizationCode](#cfn-datazone-connection-authorizationcodeproperties-authorizationcode)" : {{String}},
  "[RedirectUri](#cfn-datazone-connection-authorizationcodeproperties-redirecturi)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-authorizationcodeproperties-syntax.yaml"></a>

```
  [AuthorizationCode](#cfn-datazone-connection-authorizationcodeproperties-authorizationcode): {{String}}
  [RedirectUri](#cfn-datazone-connection-authorizationcodeproperties-redirecturi): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-authorizationcodeproperties-properties"></a>

`AuthorizationCode`  <a name="cfn-datazone-connection-authorizationcodeproperties-authorizationcode"></a>
The authorization code of a connection.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedirectUri`  <a name="cfn-datazone-connection-authorizationcodeproperties-redirecturi"></a>
The redirect URI of a connection.
*Required*: No
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
