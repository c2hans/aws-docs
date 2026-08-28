---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-segment-segmentdimensions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Segment SegmentDimensions
<a name="aws-properties-pinpoint-segment-segmentdimensions"></a>

Specifies the dimension settings for a segment.

## Syntax
<a name="aws-properties-pinpoint-segment-segmentdimensions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-segment-segmentdimensions-syntax.json"></a>

```
{
  "[Attributes](#cfn-pinpoint-segment-segmentdimensions-attributes)" : {{Json}},
  "[Behavior](#cfn-pinpoint-segment-segmentdimensions-behavior)" : {{Behavior}},
  "[Demographic](#cfn-pinpoint-segment-segmentdimensions-demographic)" : {{Demographic}},
  "[Location](#cfn-pinpoint-segment-segmentdimensions-location)" : {{Location}},
  "[Metrics](#cfn-pinpoint-segment-segmentdimensions-metrics)" : {{Json}},
  "[UserAttributes](#cfn-pinpoint-segment-segmentdimensions-userattributes)" : {{Json}}
}
```

### YAML
<a name="aws-properties-pinpoint-segment-segmentdimensions-syntax.yaml"></a>

```
  [Attributes](#cfn-pinpoint-segment-segmentdimensions-attributes): {{Json}}
  [Behavior](#cfn-pinpoint-segment-segmentdimensions-behavior): {{
    Behavior}}
  [Demographic](#cfn-pinpoint-segment-segmentdimensions-demographic): {{
    Demographic}}
  [Location](#cfn-pinpoint-segment-segmentdimensions-location): {{
    Location}}
  [Metrics](#cfn-pinpoint-segment-segmentdimensions-metrics): {{Json}}
  [UserAttributes](#cfn-pinpoint-segment-segmentdimensions-userattributes): {{Json}}
```

## Properties
<a name="aws-properties-pinpoint-segment-segmentdimensions-properties"></a>

`Attributes`  <a name="cfn-pinpoint-segment-segmentdimensions-attributes"></a>
One or more custom attributes to use as criteria for the segment. For more information see [AttributeDimension](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-segments.html#apps-application-id-segments-model-attributedimension)
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Behavior`  <a name="cfn-pinpoint-segment-segmentdimensions-behavior"></a>
The behavior-based criteria, such as how recently users have used your app, for the segment.
*Required*: No
*Type*: [Behavior](aws-properties-pinpoint-segment-behavior.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Demographic`  <a name="cfn-pinpoint-segment-segmentdimensions-demographic"></a>
The demographic-based criteria, such as device platform, for the segment.
*Required*: No
*Type*: [Demographic](aws-properties-pinpoint-segment-demographic.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Location`  <a name="cfn-pinpoint-segment-segmentdimensions-location"></a>
The location-based criteria, such as region or GPS coordinates, for the segment.
*Required*: No
*Type*: [Location](aws-properties-pinpoint-segment-location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metrics`  <a name="cfn-pinpoint-segment-segmentdimensions-metrics"></a>
One or more custom metrics to use as criteria for the segment.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserAttributes`  <a name="cfn-pinpoint-segment-segmentdimensions-userattributes"></a>
One or more custom user attributes to use as criteria for the segment.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
