---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-dashttmlconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint DashTtmlConfiguration
<a name="aws-properties-mediapackagev2-originendpoint-dashttmlconfiguration"></a>

The settings for TTML subtitles.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-dashttmlconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-dashttmlconfiguration-syntax.json"></a>

```
{
  "[TtmlProfile](#cfn-mediapackagev2-originendpoint-dashttmlconfiguration-ttmlprofile)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-dashttmlconfiguration-syntax.yaml"></a>

```
  [TtmlProfile](#cfn-mediapackagev2-originendpoint-dashttmlconfiguration-ttmlprofile): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-dashttmlconfiguration-properties"></a>

`TtmlProfile`  <a name="cfn-mediapackagev2-originendpoint-dashttmlconfiguration-ttmlprofile"></a>
The profile that MediaPackage uses when signaling subtitles in the manifest. `IMSC` is the default profile. `EBU-TT-D` produces subtitles that are compliant with the EBU-TT-D TTML profile. MediaPackage passes through subtitle styles to the manifest. For more information about EBU-TT-D subtitles, see [EBU-TT-D Subtitling Distribution Format](https://tech.ebu.ch/publications/tech3380).
*Required*: Yes
*Type*: String
*Allowed values*: `IMSC_1 | EBU_TT_D_101`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
