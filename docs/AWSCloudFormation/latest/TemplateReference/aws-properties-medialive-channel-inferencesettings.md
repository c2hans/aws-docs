---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-inferencesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel InferenceSettings
<a name="aws-properties-medialive-channel-inferencesettings"></a>

Include this setting to include Elemental Inference features in this channel.

## Syntax
<a name="aws-properties-medialive-channel-inferencesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-inferencesettings-syntax.json"></a>

```
{
  "[AudioFeedInputs](#cfn-medialive-channel-inferencesettings-audiofeedinputs)" : {{[ AudioFeedInput, ... ]}},
  "[FeedArn](#cfn-medialive-channel-inferencesettings-feedarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-inferencesettings-syntax.yaml"></a>

```
  [AudioFeedInputs](#cfn-medialive-channel-inferencesettings-audiofeedinputs): {{
    - AudioFeedInput}}
  [FeedArn](#cfn-medialive-channel-inferencesettings-feedarn): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-inferencesettings-properties"></a>

`AudioFeedInputs`  <a name="cfn-medialive-channel-inferencesettings-audiofeedinputs"></a>
Property description not available.
*Required*: No
*Type*: Array of [AudioFeedInput](aws-properties-medialive-channel-audiofeedinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FeedArn`  <a name="cfn-medialive-channel-inferencesettings-feedarn"></a>
The ARN of the feed resource that is associated with this channel. The feed is a resource in the Elemental Inference service.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
