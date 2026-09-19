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
  "[EnrichmentMethods](#cfn-medialive-channel-inferencesettings-enrichmentmethods)" : {{[ String, ... ]}},
  "[FeedArn](#cfn-medialive-channel-inferencesettings-feedarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-inferencesettings-syntax.yaml"></a>

```
  [AudioFeedInputs](#cfn-medialive-channel-inferencesettings-audiofeedinputs): {{
    - AudioFeedInput}}
  [EnrichmentMethods](#cfn-medialive-channel-inferencesettings-enrichmentmethods): {{
    - String}}
  [FeedArn](#cfn-medialive-channel-inferencesettings-feedarn): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-inferencesettings-properties"></a>

`AudioFeedInputs`  <a name="cfn-medialive-channel-inferencesettings-audiofeedinputs"></a>
Property description not available.
*Required*: No
*Type*: Array of [AudioFeedInput](aws-properties-medialive-channel-audiofeedinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnrichmentMethods`  <a name="cfn-medialive-channel-inferencesettings-enrichmentmethods"></a>
The Contextual Metadata Enrichment methods enabled for this channel. Each method defines how the channel augments its output with contextual metadata from the Elemental Inference feed.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FeedArn`  <a name="cfn-medialive-channel-inferencesettings-feedarn"></a>
The ARN of the feed resource that is associated with this channel. The feed is a resource in the Elemental Inference service.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
