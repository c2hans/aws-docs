---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-channel-dashplaylistsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Channel DashPlaylistSettings
<a name="aws-properties-mediatailor-channel-dashplaylistsettings"></a>

Dash manifest configuration parameters.

## Syntax
<a name="aws-properties-mediatailor-channel-dashplaylistsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-channel-dashplaylistsettings-syntax.json"></a>

```
{
  "[ManifestWindowSeconds](#cfn-mediatailor-channel-dashplaylistsettings-manifestwindowseconds)" : {{Number}},
  "[MinBufferTimeSeconds](#cfn-mediatailor-channel-dashplaylistsettings-minbuffertimeseconds)" : {{Number}},
  "[MinUpdatePeriodSeconds](#cfn-mediatailor-channel-dashplaylistsettings-minupdateperiodseconds)" : {{Number}},
  "[SuggestedPresentationDelaySeconds](#cfn-mediatailor-channel-dashplaylistsettings-suggestedpresentationdelayseconds)" : {{Number}}
}
```

### YAML
<a name="aws-properties-mediatailor-channel-dashplaylistsettings-syntax.yaml"></a>

```
  [ManifestWindowSeconds](#cfn-mediatailor-channel-dashplaylistsettings-manifestwindowseconds): {{Number}}
  [MinBufferTimeSeconds](#cfn-mediatailor-channel-dashplaylistsettings-minbuffertimeseconds): {{Number}}
  [MinUpdatePeriodSeconds](#cfn-mediatailor-channel-dashplaylistsettings-minupdateperiodseconds): {{Number}}
  [SuggestedPresentationDelaySeconds](#cfn-mediatailor-channel-dashplaylistsettings-suggestedpresentationdelayseconds): {{Number}}
```

## Properties
<a name="aws-properties-mediatailor-channel-dashplaylistsettings-properties"></a>

`ManifestWindowSeconds`  <a name="cfn-mediatailor-channel-dashplaylistsettings-manifestwindowseconds"></a>
The total duration (in seconds) of each manifest. Minimum value: `30` seconds. Maximum value: `3600` seconds.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinBufferTimeSeconds`  <a name="cfn-mediatailor-channel-dashplaylistsettings-minbuffertimeseconds"></a>
Minimum amount of content (measured in seconds) that a player must keep available in the buffer. Minimum value: `2` seconds. Maximum value: `60` seconds.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinUpdatePeriodSeconds`  <a name="cfn-mediatailor-channel-dashplaylistsettings-minupdateperiodseconds"></a>
Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest. Minimum value: `2` seconds. Maximum value: `60` seconds.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuggestedPresentationDelaySeconds`  <a name="cfn-mediatailor-channel-dashplaylistsettings-suggestedpresentationdelayseconds"></a>
Amount of time (in seconds) that the player should be from the live point at the end of the manifest. Minimum value: `2` seconds. Maximum value: `60` seconds.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
