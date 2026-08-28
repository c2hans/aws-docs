---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackage::PackagingConfiguration DashManifest
<a name="aws-properties-mediapackage-packagingconfiguration-dashmanifest"></a>

Parameters for a DASH manifest.

## Syntax
<a name="aws-properties-mediapackage-packagingconfiguration-dashmanifest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackage-packagingconfiguration-dashmanifest-syntax.json"></a>

```
{
  "[ManifestLayout](#cfn-mediapackage-packagingconfiguration-dashmanifest-manifestlayout)" : {{String}},
  "[ManifestName](#cfn-mediapackage-packagingconfiguration-dashmanifest-manifestname)" : {{String}},
  "[MinBufferTimeSeconds](#cfn-mediapackage-packagingconfiguration-dashmanifest-minbuffertimeseconds)" : {{Integer}},
  "[Profile](#cfn-mediapackage-packagingconfiguration-dashmanifest-profile)" : {{String}},
  "[ScteMarkersSource](#cfn-mediapackage-packagingconfiguration-dashmanifest-sctemarkerssource)" : {{String}},
  "[StreamSelection](#cfn-mediapackage-packagingconfiguration-dashmanifest-streamselection)" : {{StreamSelection}}
}
```

### YAML
<a name="aws-properties-mediapackage-packagingconfiguration-dashmanifest-syntax.yaml"></a>

```
  [ManifestLayout](#cfn-mediapackage-packagingconfiguration-dashmanifest-manifestlayout): {{String}}
  [ManifestName](#cfn-mediapackage-packagingconfiguration-dashmanifest-manifestname): {{String}}
  [MinBufferTimeSeconds](#cfn-mediapackage-packagingconfiguration-dashmanifest-minbuffertimeseconds): {{Integer}}
  [Profile](#cfn-mediapackage-packagingconfiguration-dashmanifest-profile): {{String}}
  [ScteMarkersSource](#cfn-mediapackage-packagingconfiguration-dashmanifest-sctemarkerssource): {{String}}
  [StreamSelection](#cfn-mediapackage-packagingconfiguration-dashmanifest-streamselection): {{
    StreamSelection}}
```

## Properties
<a name="aws-properties-mediapackage-packagingconfiguration-dashmanifest-properties"></a>

`ManifestLayout`  <a name="cfn-mediapackage-packagingconfiguration-dashmanifest-manifestlayout"></a>
Determines the position of some tags in the Media Presentation Description (MPD). When set to `FULL`, elements like `SegmentTemplate` and `ContentProtection` are included in each `Representation`. When set to `COMPACT`, duplicate elements are combined and presented at the AdaptationSet level.
*Required*: No
*Type*: String
*Allowed values*: `FULL | COMPACT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestName`  <a name="cfn-mediapackage-packagingconfiguration-dashmanifest-manifestname"></a>
A short string that's appended to the end of the endpoint URL to create a unique path to this packaging configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinBufferTimeSeconds`  <a name="cfn-mediapackage-packagingconfiguration-dashmanifest-minbuffertimeseconds"></a>
Minimum amount of content (measured in seconds) that a player must keep available in the buffer.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Profile`  <a name="cfn-mediapackage-packagingconfiguration-dashmanifest-profile"></a>
The DASH profile type. When set to `HBBTV_1_5`, the content is compliant with HbbTV 1.5.
*Required*: No
*Type*: String
*Allowed values*: `NONE | HBBTV_1_5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScteMarkersSource`  <a name="cfn-mediapackage-packagingconfiguration-dashmanifest-sctemarkerssource"></a>
The source of scte markers used.
Value description:
+ `SEGMENTS` - The scte markers are sourced from the segments of the ingested content.
+ `MANIFEST` - the scte markers are sourced from the manifest of the ingested content. The MANIFEST value is compatible with source HLS playlists using the SCTE-35 Enhanced syntax (`EXT-OATCLS-SCTE35` tags). SCTE-35 Elemental and SCTE-35 Daterange syntaxes are not supported with this option.
*Required*: No
*Type*: String
*Allowed values*: `SEGMENTS | MANIFEST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamSelection`  <a name="cfn-mediapackage-packagingconfiguration-dashmanifest-streamselection"></a>
Limitations for outputs from the endpoint, based on the video bitrate.
*Required*: No
*Type*: [StreamSelection](aws-properties-mediapackage-packagingconfiguration-streamselection.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
