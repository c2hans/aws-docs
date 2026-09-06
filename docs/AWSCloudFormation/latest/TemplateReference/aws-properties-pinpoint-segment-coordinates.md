---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-segment-coordinates.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Segment Coordinates
<a name="aws-properties-pinpoint-segment-coordinates"></a>

Specifies the GPS coordinates of a location.

## Syntax
<a name="aws-properties-pinpoint-segment-coordinates-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-segment-coordinates-syntax.json"></a>

```
{
  "[Latitude](#cfn-pinpoint-segment-coordinates-latitude)" : {{Number}},
  "[Longitude](#cfn-pinpoint-segment-coordinates-longitude)" : {{Number}}
}
```

### YAML
<a name="aws-properties-pinpoint-segment-coordinates-syntax.yaml"></a>

```
  [Latitude](#cfn-pinpoint-segment-coordinates-latitude): {{Number}}
  [Longitude](#cfn-pinpoint-segment-coordinates-longitude): {{Number}}
```

## Properties
<a name="aws-properties-pinpoint-segment-coordinates-properties"></a>

`Latitude`  <a name="cfn-pinpoint-segment-coordinates-latitude"></a>
The latitude coordinate of the location.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Longitude`  <a name="cfn-pinpoint-segment-coordinates-longitude"></a>
The longitude coordinate of the location.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
