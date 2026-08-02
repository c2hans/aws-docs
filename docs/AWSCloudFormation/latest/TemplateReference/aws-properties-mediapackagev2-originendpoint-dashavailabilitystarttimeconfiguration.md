---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-dashavailabilitystarttimeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint DashAvailabilityStartTimeConfiguration
<a name="aws-properties-mediapackagev2-originendpoint-dashavailabilitystarttimeconfiguration"></a>

The configuration for the DASH `availabilityStartTime` attribute of the Media Presentation Description (MPD). Use this configuration to set a custom availability start time for your DASH manifest.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-dashavailabilitystarttimeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-dashavailabilitystarttimeconfiguration-syntax.json"></a>

```
{
  "[FixedAvailabilityStartTime](#cfn-mediapackagev2-originendpoint-dashavailabilitystarttimeconfiguration-fixedavailabilitystarttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-dashavailabilitystarttimeconfiguration-syntax.yaml"></a>

```
  [FixedAvailabilityStartTime](#cfn-mediapackagev2-originendpoint-dashavailabilitystarttimeconfiguration-fixedavailabilitystarttime): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-dashavailabilitystarttimeconfiguration-properties"></a>

`FixedAvailabilityStartTime`  <a name="cfn-mediapackagev2-originendpoint-dashavailabilitystarttimeconfiguration-fixedavailabilitystarttime"></a>
The fixed availability start time for the DASH manifest, in ISO 8601 date-time format. The value must have hourly granularity, meaning that the minutes, seconds, and fractional seconds must be zero. The value must be on or after `2024-01-01T00:00:00Z` and must be at least 14 days before the current time.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
