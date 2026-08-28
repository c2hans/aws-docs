---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-segment-location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Segment Location
<a name="aws-properties-pinpoint-segment-location"></a>

Specifies location-based criteria, such as region or GPS coordinates, for the segment.

## Syntax
<a name="aws-properties-pinpoint-segment-location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-segment-location-syntax.json"></a>

```
{
  "[Country](#cfn-pinpoint-segment-location-country)" : {{SetDimension}},
  "[GPSPoint](#cfn-pinpoint-segment-location-gpspoint)" : {{GPSPoint}}
}
```

### YAML
<a name="aws-properties-pinpoint-segment-location-syntax.yaml"></a>

```
  [Country](#cfn-pinpoint-segment-location-country): {{
    SetDimension}}
  [GPSPoint](#cfn-pinpoint-segment-location-gpspoint): {{
    GPSPoint}}
```

## Properties
<a name="aws-properties-pinpoint-segment-location-properties"></a>

`Country`  <a name="cfn-pinpoint-segment-location-country"></a>
The country or region code, in ISO 3166-1 alpha-2 format, for the segment.
*Required*: No
*Type*: [SetDimension](aws-properties-pinpoint-segment-setdimension.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GPSPoint`  <a name="cfn-pinpoint-segment-location-gpspoint"></a>
The GPS point dimension for the segment.
*Required*: No
*Type*: [GPSPoint](aws-properties-pinpoint-segment-gpspoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
