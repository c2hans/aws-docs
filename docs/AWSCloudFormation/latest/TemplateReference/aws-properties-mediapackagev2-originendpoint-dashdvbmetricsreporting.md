---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-dashdvbmetricsreporting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint DashDvbMetricsReporting
<a name="aws-properties-mediapackagev2-originendpoint-dashdvbmetricsreporting"></a>

For use with DVB-DASH profiles only. The settings for error reporting from the playback device that you want AWS Elemental MediaPackage to pass through to the manifest.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-dashdvbmetricsreporting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-dashdvbmetricsreporting-syntax.json"></a>

```
{
  "[Probability](#cfn-mediapackagev2-originendpoint-dashdvbmetricsreporting-probability)" : {{Integer}},
  "[ReportingUrl](#cfn-mediapackagev2-originendpoint-dashdvbmetricsreporting-reportingurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-dashdvbmetricsreporting-syntax.yaml"></a>

```
  [Probability](#cfn-mediapackagev2-originendpoint-dashdvbmetricsreporting-probability): {{Integer}}
  [ReportingUrl](#cfn-mediapackagev2-originendpoint-dashdvbmetricsreporting-reportingurl): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-dashdvbmetricsreporting-properties"></a>

`Probability`  <a name="cfn-mediapackagev2-originendpoint-dashdvbmetricsreporting-probability"></a>
The number of playback devices per 1000 that will send error reports to the reporting URL. This represents the probability that a playback device will be a reporting player for this session.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReportingUrl`  <a name="cfn-mediapackagev2-originendpoint-dashdvbmetricsreporting-reportingurl"></a>
The URL where playback devices send error reports.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
