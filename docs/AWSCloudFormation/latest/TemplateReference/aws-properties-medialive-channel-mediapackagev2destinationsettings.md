---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-mediapackagev2destinationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MediaPackageV2DestinationSettings
<a name="aws-properties-medialive-channel-mediapackagev2destinationsettings"></a>

Optional settings for MediaPackage V2 destinations.

The parent of this entity is MediaPackageOutputSettings.

## Syntax
<a name="aws-properties-medialive-channel-mediapackagev2destinationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-mediapackagev2destinationsettings-syntax.json"></a>

```
{
  "[AudioGroupId](#cfn-medialive-channel-mediapackagev2destinationsettings-audiogroupid)" : {{String}},
  "[AudioRenditionSets](#cfn-medialive-channel-mediapackagev2destinationsettings-audiorenditionsets)" : {{String}},
  "[HlsAutoSelect](#cfn-medialive-channel-mediapackagev2destinationsettings-hlsautoselect)" : {{String}},
  "[HlsDefault](#cfn-medialive-channel-mediapackagev2destinationsettings-hlsdefault)" : {{String}},
  "[OutputUsage](#cfn-medialive-channel-mediapackagev2destinationsettings-outputusage)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-medialive-channel-mediapackagev2destinationsettings-syntax.yaml"></a>

```
  [AudioGroupId](#cfn-medialive-channel-mediapackagev2destinationsettings-audiogroupid): {{String}}
  [AudioRenditionSets](#cfn-medialive-channel-mediapackagev2destinationsettings-audiorenditionsets): {{String}}
  [HlsAutoSelect](#cfn-medialive-channel-mediapackagev2destinationsettings-hlsautoselect): {{String}}
  [HlsDefault](#cfn-medialive-channel-mediapackagev2destinationsettings-hlsdefault): {{String}}
  [OutputUsage](#cfn-medialive-channel-mediapackagev2destinationsettings-outputusage): {{
    - String}}
```

## Properties
<a name="aws-properties-medialive-channel-mediapackagev2destinationsettings-properties"></a>

`AudioGroupId`  <a name="cfn-medialive-channel-mediapackagev2destinationsettings-audiogroupid"></a>
Applies only to an output that contains audio. If you want to put several audio encodes into one audio rendition group, decide on a name (ID) for the group. Then in every audio output that you want to belong to that group, enter that ID in this field. Note that this information is part of the HLS specification (not the CMAF specification), but if you include it then MediaPackage will include it in the manifest it creates for the video player.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AudioRenditionSets`  <a name="cfn-medialive-channel-mediapackagev2destinationsettings-audiorenditionsets"></a>
Applies only to an output that contains video, and only if you want to associate one or more audio groups to this video. In this field you assign the groups that you create (in the Group ID fields in the various audio outputs). Enter one group ID, or enter a comma-separated list of group IDs. Note that this information is part of the HLS specification (not the CMAF specification), but if you include it then MediaPackage will include it in the manifest it creates for the video player.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HlsAutoSelect`  <a name="cfn-medialive-channel-mediapackagev2destinationsettings-hlsautoselect"></a>
Specifies whether MediaPackage should set this output as the auto-select rendition in the HLS manifest. YES means this must be the auto-select. NO means this should never be the auto-select. OMIT means MediaPackage decides what to set on this rendition. When you consider all the renditions, you can set zero or one renditions to YES, zero or more renditions to NO (but not all), and zero, some, or all to OMIT.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HlsDefault`  <a name="cfn-medialive-channel-mediapackagev2destinationsettings-hlsdefault"></a>
Specifies whether MediaPackage should set this output as the default rendition in the HLS manifest. YES means this must be the default. NO means this should never be the default. OMIT means MediaPackage decides what to set on this rendition. When you consider all the renditions, you can set zero or one renditions to YES, zero or more renditions to NO (but not all), and zero, some, or all to OMIT.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputUsage`  <a name="cfn-medialive-channel-mediapackagev2destinationsettings-outputusage"></a>
A list of usage tags that declare how this MediaPackage V2 output participates in multiview. Valid values:
+ `MULTIVIEW_EQUAL_SIZE_VIEW` – The output is one of several equally sized views in the multiview layout.
+ `MULTIVIEW_PRIMARY_VIEW` – The output is the primary view in the multiview layout.
+ `MULTIVIEW_SECONDARY_VIEW` – The output is a secondary view in the multiview layout.
Leave this field empty (the default) if the output has no multiview role.
If any video-carrying MediaPackage V2 output in an output group specifies a multiview value, then every video-carrying MediaPackage V2 output in that group must also specify a multiview value. Put standalone video outputs in a separate output group.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
