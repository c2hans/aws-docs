---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Campaign DefaultButtonConfiguration
<a name="aws-properties-pinpoint-campaign-defaultbuttonconfiguration"></a>

Specifies the default behavior for a button that appears in an in-app message. You can optionally add button configurations that specifically apply to iOS, Android, or web browser users.

## Syntax
<a name="aws-properties-pinpoint-campaign-defaultbuttonconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-campaign-defaultbuttonconfiguration-syntax.json"></a>

```
{
  "[BackgroundColor](#cfn-pinpoint-campaign-defaultbuttonconfiguration-backgroundcolor)" : {{String}},
  "[BorderRadius](#cfn-pinpoint-campaign-defaultbuttonconfiguration-borderradius)" : {{Integer}},
  "[ButtonAction](#cfn-pinpoint-campaign-defaultbuttonconfiguration-buttonaction)" : {{String}},
  "[Link](#cfn-pinpoint-campaign-defaultbuttonconfiguration-link)" : {{String}},
  "[Text](#cfn-pinpoint-campaign-defaultbuttonconfiguration-text)" : {{String}},
  "[TextColor](#cfn-pinpoint-campaign-defaultbuttonconfiguration-textcolor)" : {{String}}
}
```

### YAML
<a name="aws-properties-pinpoint-campaign-defaultbuttonconfiguration-syntax.yaml"></a>

```
  [BackgroundColor](#cfn-pinpoint-campaign-defaultbuttonconfiguration-backgroundcolor): {{String}}
  [BorderRadius](#cfn-pinpoint-campaign-defaultbuttonconfiguration-borderradius): {{Integer}}
  [ButtonAction](#cfn-pinpoint-campaign-defaultbuttonconfiguration-buttonaction): {{String}}
  [Link](#cfn-pinpoint-campaign-defaultbuttonconfiguration-link): {{String}}
  [Text](#cfn-pinpoint-campaign-defaultbuttonconfiguration-text): {{String}}
  [TextColor](#cfn-pinpoint-campaign-defaultbuttonconfiguration-textcolor): {{String}}
```

## Properties
<a name="aws-properties-pinpoint-campaign-defaultbuttonconfiguration-properties"></a>

`BackgroundColor`  <a name="cfn-pinpoint-campaign-defaultbuttonconfiguration-backgroundcolor"></a>
The background color of a button, expressed as a hex color code (such as \#000000 for black).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BorderRadius`  <a name="cfn-pinpoint-campaign-defaultbuttonconfiguration-borderradius"></a>
The border radius of a button.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ButtonAction`  <a name="cfn-pinpoint-campaign-defaultbuttonconfiguration-buttonaction"></a>
The action that occurs when a recipient chooses a button in an in-app message. You can specify one of the following:
+ `LINK` – A link to a web destination.
+ `DEEP_LINK` – A link to a specific page in an application.
+ `CLOSE` – Dismisses the message.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Link`  <a name="cfn-pinpoint-campaign-defaultbuttonconfiguration-link"></a>
The destination (such as a URL) for a button.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-pinpoint-campaign-defaultbuttonconfiguration-text"></a>
The text that appears on a button in an in-app message.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextColor`  <a name="cfn-pinpoint-campaign-defaultbuttonconfiguration-textcolor"></a>
The color of the body text in a button, expressed as a hex color code (such as \#000000 for black).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
