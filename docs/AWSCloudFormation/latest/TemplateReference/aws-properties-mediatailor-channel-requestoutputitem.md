---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-channel-requestoutputitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Channel RequestOutputItem
<a name="aws-properties-mediatailor-channel-requestoutputitem"></a>

The output configuration for this channel.

## Syntax
<a name="aws-properties-mediatailor-channel-requestoutputitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-channel-requestoutputitem-syntax.json"></a>

```
{
  "[DashPlaylistSettings](#cfn-mediatailor-channel-requestoutputitem-dashplaylistsettings)" : {{DashPlaylistSettings}},
  "[HlsPlaylistSettings](#cfn-mediatailor-channel-requestoutputitem-hlsplaylistsettings)" : {{HlsPlaylistSettings}},
  "[ManifestName](#cfn-mediatailor-channel-requestoutputitem-manifestname)" : {{String}},
  "[SourceGroup](#cfn-mediatailor-channel-requestoutputitem-sourcegroup)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-channel-requestoutputitem-syntax.yaml"></a>

```
  [DashPlaylistSettings](#cfn-mediatailor-channel-requestoutputitem-dashplaylistsettings): {{
    DashPlaylistSettings}}
  [HlsPlaylistSettings](#cfn-mediatailor-channel-requestoutputitem-hlsplaylistsettings): {{
    HlsPlaylistSettings}}
  [ManifestName](#cfn-mediatailor-channel-requestoutputitem-manifestname): {{String}}
  [SourceGroup](#cfn-mediatailor-channel-requestoutputitem-sourcegroup): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-channel-requestoutputitem-properties"></a>

`DashPlaylistSettings`  <a name="cfn-mediatailor-channel-requestoutputitem-dashplaylistsettings"></a>
DASH manifest configuration parameters.
*Required*: No
*Type*: [DashPlaylistSettings](aws-properties-mediatailor-channel-dashplaylistsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HlsPlaylistSettings`  <a name="cfn-mediatailor-channel-requestoutputitem-hlsplaylistsettings"></a>
HLS playlist configuration parameters.
*Required*: No
*Type*: [HlsPlaylistSettings](aws-properties-mediatailor-channel-hlsplaylistsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestName`  <a name="cfn-mediatailor-channel-requestoutputitem-manifestname"></a>
The name of the manifest for the channel. The name appears in the `PlaybackUrl`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceGroup`  <a name="cfn-mediatailor-channel-requestoutputitem-sourcegroup"></a>
A string used to match which `HttpPackageConfiguration` is used for each `VodSource`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
