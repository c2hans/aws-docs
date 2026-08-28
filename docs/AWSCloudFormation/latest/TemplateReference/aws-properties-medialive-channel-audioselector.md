---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-audioselector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AudioSelector
<a name="aws-properties-medialive-channel-audioselector"></a>

Information about one audio to extract from the input.

The parent of this entity is InputSettings.

## Syntax
<a name="aws-properties-medialive-channel-audioselector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-audioselector-syntax.json"></a>

```
{
  "[Name](#cfn-medialive-channel-audioselector-name)" : {{String}},
  "[SelectorSettings](#cfn-medialive-channel-audioselector-selectorsettings)" : {{AudioSelectorSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-audioselector-syntax.yaml"></a>

```
  [Name](#cfn-medialive-channel-audioselector-name): {{String}}
  [SelectorSettings](#cfn-medialive-channel-audioselector-selectorsettings): {{
    AudioSelectorSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-audioselector-properties"></a>

`Name`  <a name="cfn-medialive-channel-audioselector-name"></a>
A name for this AudioSelector.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectorSettings`  <a name="cfn-medialive-channel-audioselector-selectorsettings"></a>
Information about the specific audio to extract from the input.
*Required*: No
*Type*: [AudioSelectorSettings](aws-properties-medialive-channel-audioselectorsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
