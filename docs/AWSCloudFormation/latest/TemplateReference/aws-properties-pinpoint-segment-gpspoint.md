---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-segment-gpspoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Segment GPSPoint
<a name="aws-properties-pinpoint-segment-gpspoint"></a>

Specifies the GPS coordinates of the endpoint location.

## Syntax
<a name="aws-properties-pinpoint-segment-gpspoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-segment-gpspoint-syntax.json"></a>

```
{
  "[Coordinates](#cfn-pinpoint-segment-gpspoint-coordinates)" : {{Coordinates}},
  "[RangeInKilometers](#cfn-pinpoint-segment-gpspoint-rangeinkilometers)" : {{Number}}
}
```

### YAML
<a name="aws-properties-pinpoint-segment-gpspoint-syntax.yaml"></a>

```
  [Coordinates](#cfn-pinpoint-segment-gpspoint-coordinates): {{
    Coordinates}}
  [RangeInKilometers](#cfn-pinpoint-segment-gpspoint-rangeinkilometers): {{Number}}
```

## Properties
<a name="aws-properties-pinpoint-segment-gpspoint-properties"></a>

`Coordinates`  <a name="cfn-pinpoint-segment-gpspoint-coordinates"></a>
The GPS coordinates to measure distance from.
*Required*: Yes
*Type*: [Coordinates](aws-properties-pinpoint-segment-coordinates.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RangeInKilometers`  <a name="cfn-pinpoint-segment-gpspoint-rangeinkilometers"></a>
The range, in kilometers, from the GPS coordinates.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
