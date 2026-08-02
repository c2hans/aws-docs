---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-dashdvbsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint DashDvbSettings
<a name="aws-properties-mediapackagev2-originendpoint-dashdvbsettings"></a>

For endpoints that use the DVB-DASH profile only. The font download and error reporting information that you want MediaPackage to pass through to the manifest.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-dashdvbsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-dashdvbsettings-syntax.json"></a>

```
{
  "[ErrorMetrics](#cfn-mediapackagev2-originendpoint-dashdvbsettings-errormetrics)" : {{[ DashDvbMetricsReporting, ... ]}},
  "[FontDownload](#cfn-mediapackagev2-originendpoint-dashdvbsettings-fontdownload)" : {{DashDvbFontDownload}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-dashdvbsettings-syntax.yaml"></a>

```
  [ErrorMetrics](#cfn-mediapackagev2-originendpoint-dashdvbsettings-errormetrics): {{
    - DashDvbMetricsReporting}}
  [FontDownload](#cfn-mediapackagev2-originendpoint-dashdvbsettings-fontdownload): {{
    DashDvbFontDownload}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-dashdvbsettings-properties"></a>

`ErrorMetrics`  <a name="cfn-mediapackagev2-originendpoint-dashdvbsettings-errormetrics"></a>
Playback device error reporting settings.
*Required*: No
*Type*: Array of [DashDvbMetricsReporting](aws-properties-mediapackagev2-originendpoint-dashdvbmetricsreporting.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FontDownload`  <a name="cfn-mediapackagev2-originendpoint-dashdvbsettings-fontdownload"></a>
Subtitle font settings.
*Required*: No
*Type*: [DashDvbFontDownload](aws-properties-mediapackagev2-originendpoint-dashdvbfontdownload.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
