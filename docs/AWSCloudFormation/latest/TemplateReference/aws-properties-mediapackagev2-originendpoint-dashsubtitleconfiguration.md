---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-dashsubtitleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint DashSubtitleConfiguration
<a name="aws-properties-mediapackagev2-originendpoint-dashsubtitleconfiguration"></a>

The configuration for DASH subtitles.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-dashsubtitleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-dashsubtitleconfiguration-syntax.json"></a>

```
{
  "[TtmlConfiguration](#cfn-mediapackagev2-originendpoint-dashsubtitleconfiguration-ttmlconfiguration)" : {{DashTtmlConfiguration}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-dashsubtitleconfiguration-syntax.yaml"></a>

```
  [TtmlConfiguration](#cfn-mediapackagev2-originendpoint-dashsubtitleconfiguration-ttmlconfiguration): {{
    DashTtmlConfiguration}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-dashsubtitleconfiguration-properties"></a>

`TtmlConfiguration`  <a name="cfn-mediapackagev2-originendpoint-dashsubtitleconfiguration-ttmlconfiguration"></a>
Settings for TTML subtitles.
*Required*: No
*Type*: [DashTtmlConfiguration](aws-properties-mediapackagev2-originendpoint-dashttmlconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
