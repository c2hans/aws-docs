---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-campaign-overridebuttonconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Campaign OverrideButtonConfiguration
<a name="aws-properties-pinpoint-campaign-overridebuttonconfiguration"></a>

Specifies the configuration of a button with settings that are specific to a certain device type.

## Syntax
<a name="aws-properties-pinpoint-campaign-overridebuttonconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-campaign-overridebuttonconfiguration-syntax.json"></a>

```
{
  "[ButtonAction](#cfn-pinpoint-campaign-overridebuttonconfiguration-buttonaction)" : {{String}},
  "[Link](#cfn-pinpoint-campaign-overridebuttonconfiguration-link)" : {{String}}
}
```

### YAML
<a name="aws-properties-pinpoint-campaign-overridebuttonconfiguration-syntax.yaml"></a>

```
  [ButtonAction](#cfn-pinpoint-campaign-overridebuttonconfiguration-buttonaction): {{String}}
  [Link](#cfn-pinpoint-campaign-overridebuttonconfiguration-link): {{String}}
```

## Properties
<a name="aws-properties-pinpoint-campaign-overridebuttonconfiguration-properties"></a>

`ButtonAction`  <a name="cfn-pinpoint-campaign-overridebuttonconfiguration-buttonaction"></a>
The action that occurs when a recipient chooses a button in an in-app message. You can specify one of the following:
+ `LINK` – A link to a web destination.
+ `DEEP_LINK` – A link to a specific page in an application.
+ `CLOSE` – Dismisses the message.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Link`  <a name="cfn-pinpoint-campaign-overridebuttonconfiguration-link"></a>
The destination (such as a URL) for a button.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
