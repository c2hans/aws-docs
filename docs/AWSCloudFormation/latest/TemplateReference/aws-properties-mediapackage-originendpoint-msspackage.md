---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackage-originendpoint-msspackage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackage::OriginEndpoint MssPackage
<a name="aws-properties-mediapackage-originendpoint-msspackage"></a>

Parameters for Microsoft Smooth Streaming packaging.

## Syntax
<a name="aws-properties-mediapackage-originendpoint-msspackage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackage-originendpoint-msspackage-syntax.json"></a>

```
{
  "[Encryption](#cfn-mediapackage-originendpoint-msspackage-encryption)" : {{MssEncryption}},
  "[ManifestWindowSeconds](#cfn-mediapackage-originendpoint-msspackage-manifestwindowseconds)" : {{Integer}},
  "[SegmentDurationSeconds](#cfn-mediapackage-originendpoint-msspackage-segmentdurationseconds)" : {{Integer}},
  "[StreamSelection](#cfn-mediapackage-originendpoint-msspackage-streamselection)" : {{StreamSelection}}
}
```

### YAML
<a name="aws-properties-mediapackage-originendpoint-msspackage-syntax.yaml"></a>

```
  [Encryption](#cfn-mediapackage-originendpoint-msspackage-encryption): {{
    MssEncryption}}
  [ManifestWindowSeconds](#cfn-mediapackage-originendpoint-msspackage-manifestwindowseconds): {{Integer}}
  [SegmentDurationSeconds](#cfn-mediapackage-originendpoint-msspackage-segmentdurationseconds): {{Integer}}
  [StreamSelection](#cfn-mediapackage-originendpoint-msspackage-streamselection): {{
    StreamSelection}}
```

## Properties
<a name="aws-properties-mediapackage-originendpoint-msspackage-properties"></a>

`Encryption`  <a name="cfn-mediapackage-originendpoint-msspackage-encryption"></a>
Parameters for encrypting content.
*Required*: No
*Type*: [MssEncryption](aws-properties-mediapackage-originendpoint-mssencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestWindowSeconds`  <a name="cfn-mediapackage-originendpoint-msspackage-manifestwindowseconds"></a>
Time window (in seconds) contained in each manifest.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentDurationSeconds`  <a name="cfn-mediapackage-originendpoint-msspackage-segmentdurationseconds"></a>
Duration (in seconds) of each fragment. Actual fragments are rounded to the nearest multiple of the source fragment duration.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamSelection`  <a name="cfn-mediapackage-originendpoint-msspackage-streamselection"></a>
Limitations for outputs from the endpoint, based on the video bitrate.
*Required*: No
*Type*: [StreamSelection](aws-properties-mediapackage-originendpoint-streamselection.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
