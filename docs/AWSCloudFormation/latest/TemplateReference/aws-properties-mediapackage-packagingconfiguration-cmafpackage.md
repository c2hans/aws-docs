---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackage::PackagingConfiguration CmafPackage
<a name="aws-properties-mediapackage-packagingconfiguration-cmafpackage"></a>

Parameters for a packaging configuration that uses Common Media Application Format (CMAF) packaging.

## Syntax
<a name="aws-properties-mediapackage-packagingconfiguration-cmafpackage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackage-packagingconfiguration-cmafpackage-syntax.json"></a>

```
{
  "[Encryption](#cfn-mediapackage-packagingconfiguration-cmafpackage-encryption)" : {{CmafEncryption}},
  "[HlsManifests](#cfn-mediapackage-packagingconfiguration-cmafpackage-hlsmanifests)" : {{[ HlsManifest, ... ]}},
  "[IncludeEncoderConfigurationInSegments](#cfn-mediapackage-packagingconfiguration-cmafpackage-includeencoderconfigurationinsegments)" : {{Boolean}},
  "[SegmentDurationSeconds](#cfn-mediapackage-packagingconfiguration-cmafpackage-segmentdurationseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediapackage-packagingconfiguration-cmafpackage-syntax.yaml"></a>

```
  [Encryption](#cfn-mediapackage-packagingconfiguration-cmafpackage-encryption): {{
    CmafEncryption}}
  [HlsManifests](#cfn-mediapackage-packagingconfiguration-cmafpackage-hlsmanifests): {{
    - HlsManifest}}
  [IncludeEncoderConfigurationInSegments](#cfn-mediapackage-packagingconfiguration-cmafpackage-includeencoderconfigurationinsegments): {{Boolean}}
  [SegmentDurationSeconds](#cfn-mediapackage-packagingconfiguration-cmafpackage-segmentdurationseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediapackage-packagingconfiguration-cmafpackage-properties"></a>

`Encryption`  <a name="cfn-mediapackage-packagingconfiguration-cmafpackage-encryption"></a>
Parameters for encrypting content.
*Required*: No
*Type*: [CmafEncryption](aws-properties-mediapackage-packagingconfiguration-cmafencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HlsManifests`  <a name="cfn-mediapackage-packagingconfiguration-cmafpackage-hlsmanifests"></a>
A list of HLS manifest configurations that are available from this endpoint.
*Required*: Yes
*Type*: Array of [HlsManifest](aws-properties-mediapackage-packagingconfiguration-hlsmanifest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeEncoderConfigurationInSegments`  <a name="cfn-mediapackage-packagingconfiguration-cmafpackage-includeencoderconfigurationinsegments"></a>
When includeEncoderConfigurationInSegments is set to true, AWS Elemental MediaPackage places your encoder's Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) metadata in every video segment instead of in the init fragment. This lets you use different SPS/PPS/VPS settings for your assets during content playback.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentDurationSeconds`  <a name="cfn-mediapackage-packagingconfiguration-cmafpackage-segmentdurationseconds"></a>
Duration (in seconds) of each segment. Actual segments are rounded to the nearest multiple of the source fragment duration.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
