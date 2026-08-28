---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-segment-demographic.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Segment Demographic
<a name="aws-properties-pinpoint-segment-demographic"></a>

Specifies demographic-based criteria, such as device platform, for the segment.

## Syntax
<a name="aws-properties-pinpoint-segment-demographic-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-segment-demographic-syntax.json"></a>

```
{
  "[AppVersion](#cfn-pinpoint-segment-demographic-appversion)" : {{SetDimension}},
  "[Channel](#cfn-pinpoint-segment-demographic-channel)" : {{SetDimension}},
  "[DeviceType](#cfn-pinpoint-segment-demographic-devicetype)" : {{SetDimension}},
  "[Make](#cfn-pinpoint-segment-demographic-make)" : {{SetDimension}},
  "[Model](#cfn-pinpoint-segment-demographic-model)" : {{SetDimension}},
  "[Platform](#cfn-pinpoint-segment-demographic-platform)" : {{SetDimension}}
}
```

### YAML
<a name="aws-properties-pinpoint-segment-demographic-syntax.yaml"></a>

```
  [AppVersion](#cfn-pinpoint-segment-demographic-appversion): {{
    SetDimension}}
  [Channel](#cfn-pinpoint-segment-demographic-channel): {{
    SetDimension}}
  [DeviceType](#cfn-pinpoint-segment-demographic-devicetype): {{
    SetDimension}}
  [Make](#cfn-pinpoint-segment-demographic-make): {{
    SetDimension}}
  [Model](#cfn-pinpoint-segment-demographic-model): {{
    SetDimension}}
  [Platform](#cfn-pinpoint-segment-demographic-platform): {{
    SetDimension}}
```

## Properties
<a name="aws-properties-pinpoint-segment-demographic-properties"></a>

`AppVersion`  <a name="cfn-pinpoint-segment-demographic-appversion"></a>
The app version criteria for the segment.
*Required*: No
*Type*: [SetDimension](aws-properties-pinpoint-segment-setdimension.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Channel`  <a name="cfn-pinpoint-segment-demographic-channel"></a>
The channel criteria for the segment.
*Required*: No
*Type*: [SetDimension](aws-properties-pinpoint-segment-setdimension.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceType`  <a name="cfn-pinpoint-segment-demographic-devicetype"></a>
The device type criteria for the segment.
*Required*: No
*Type*: [SetDimension](aws-properties-pinpoint-segment-setdimension.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Make`  <a name="cfn-pinpoint-segment-demographic-make"></a>
The device make criteria for the segment.
*Required*: No
*Type*: [SetDimension](aws-properties-pinpoint-segment-setdimension.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Model`  <a name="cfn-pinpoint-segment-demographic-model"></a>
The device model criteria for the segment.
*Required*: No
*Type*: [SetDimension](aws-properties-pinpoint-segment-setdimension.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Platform`  <a name="cfn-pinpoint-segment-demographic-platform"></a>
The device platform criteria for the segment.
*Required*: No
*Type*: [SetDimension](aws-properties-pinpoint-segment-setdimension.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
