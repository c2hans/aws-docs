---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-filterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint FilterConfiguration
<a name="aws-properties-mediapackagev2-originendpoint-filterconfiguration"></a>

Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-filterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-filterconfiguration-syntax.json"></a>

```
{
  "[ClipStartTime](#cfn-mediapackagev2-originendpoint-filterconfiguration-clipstarttime)" : {{String}},
  "[DrmSettings](#cfn-mediapackagev2-originendpoint-filterconfiguration-drmsettings)" : {{String}},
  "[End](#cfn-mediapackagev2-originendpoint-filterconfiguration-end)" : {{String}},
  "[ManifestFilter](#cfn-mediapackagev2-originendpoint-filterconfiguration-manifestfilter)" : {{String}},
  "[Start](#cfn-mediapackagev2-originendpoint-filterconfiguration-start)" : {{String}},
  "[TimeDelaySeconds](#cfn-mediapackagev2-originendpoint-filterconfiguration-timedelayseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-filterconfiguration-syntax.yaml"></a>

```
  [ClipStartTime](#cfn-mediapackagev2-originendpoint-filterconfiguration-clipstarttime): {{String}}
  [DrmSettings](#cfn-mediapackagev2-originendpoint-filterconfiguration-drmsettings): {{String}}
  [End](#cfn-mediapackagev2-originendpoint-filterconfiguration-end): {{String}}
  [ManifestFilter](#cfn-mediapackagev2-originendpoint-filterconfiguration-manifestfilter): {{String}}
  [Start](#cfn-mediapackagev2-originendpoint-filterconfiguration-start): {{String}}
  [TimeDelaySeconds](#cfn-mediapackagev2-originendpoint-filterconfiguration-timedelayseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-filterconfiguration-properties"></a>

`ClipStartTime`  <a name="cfn-mediapackagev2-originendpoint-filterconfiguration-clipstarttime"></a>
Optionally specify the clip start time for all of your manifest egress requests. When you include clip start time, note that you cannot use clip start time query parameters for this manifest's endpoint URL.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DrmSettings`  <a name="cfn-mediapackagev2-originendpoint-filterconfiguration-drmsettings"></a>
Optionally specify one or more DRM settings for all of your manifest egress requests. When you include a DRM setting, note that you cannot use an identical DRM setting query parameter for this manifest's endpoint URL.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`End`  <a name="cfn-mediapackagev2-originendpoint-filterconfiguration-end"></a>
Optionally specify the end time for all of your manifest egress requests. When you include end time, note that you cannot use end time query parameters for this manifest's endpoint URL.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestFilter`  <a name="cfn-mediapackagev2-originendpoint-filterconfiguration-manifestfilter"></a>
Optionally specify one or more manifest filters for all of your manifest egress requests. When you include a manifest filter, note that you cannot use an identical manifest filter query parameter for this manifest's endpoint URL.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Start`  <a name="cfn-mediapackagev2-originendpoint-filterconfiguration-start"></a>
Optionally specify the start time for all of your manifest egress requests. When you include start time, note that you cannot use start time query parameters for this manifest's endpoint URL.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeDelaySeconds`  <a name="cfn-mediapackagev2-originendpoint-filterconfiguration-timedelayseconds"></a>
Optionally specify the time delay for all of your manifest egress requests. Enter a value that is smaller than your endpoint's startover window. When you include time delay, note that you cannot use time delay query parameters for this manifest's endpoint URL.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `1209600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
