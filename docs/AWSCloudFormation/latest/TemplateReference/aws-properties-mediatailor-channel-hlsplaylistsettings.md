---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-channel-hlsplaylistsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Channel HlsPlaylistSettings
<a name="aws-properties-mediatailor-channel-hlsplaylistsettings"></a>

HLS playlist configuration parameters.

## Syntax
<a name="aws-properties-mediatailor-channel-hlsplaylistsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-channel-hlsplaylistsettings-syntax.json"></a>

```
{
  "[AdMarkupType](#cfn-mediatailor-channel-hlsplaylistsettings-admarkuptype)" : {{[ String, ... ]}},
  "[ManifestWindowSeconds](#cfn-mediatailor-channel-hlsplaylistsettings-manifestwindowseconds)" : {{Number}}
}
```

### YAML
<a name="aws-properties-mediatailor-channel-hlsplaylistsettings-syntax.yaml"></a>

```
  [AdMarkupType](#cfn-mediatailor-channel-hlsplaylistsettings-admarkuptype): {{
    - String}}
  [ManifestWindowSeconds](#cfn-mediatailor-channel-hlsplaylistsettings-manifestwindowseconds): {{Number}}
```

## Properties
<a name="aws-properties-mediatailor-channel-hlsplaylistsettings-properties"></a>

`AdMarkupType`  <a name="cfn-mediatailor-channel-hlsplaylistsettings-admarkuptype"></a>
Determines the type of SCTE 35 tags to use in ad markup. Specify `DATERANGE` to use `DATERANGE` tags (for live or VOD content). Specify `SCTE35_ENHANCED` to use `EXT-X-CUE-OUT` and `EXT-X-CUE-IN` tags (for VOD content only).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestWindowSeconds`  <a name="cfn-mediatailor-channel-hlsplaylistsettings-manifestwindowseconds"></a>
The total duration (in seconds) of each manifest. Minimum value: `30` seconds. Maximum value: `3600` seconds.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
