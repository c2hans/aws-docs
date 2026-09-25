---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instanceeventwindow-timerange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::InstanceEventWindow TimeRange
<a name="aws-properties-ec2-instanceeventwindow-timerange"></a>

<a name="aws-properties-ec2-instanceeventwindow-timerange-description"></a>The `TimeRange` property type specifies Property description not available. for an [AWS::EC2::InstanceEventWindow](aws-resource-ec2-instanceeventwindow.md).

## Syntax
<a name="aws-properties-ec2-instanceeventwindow-timerange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instanceeventwindow-timerange-syntax.json"></a>

```
{
  "[EndHour](#cfn-ec2-instanceeventwindow-timerange-endhour)" : {{Integer}},
  "[EndWeekDay](#cfn-ec2-instanceeventwindow-timerange-endweekday)" : {{String}},
  "[StartHour](#cfn-ec2-instanceeventwindow-timerange-starthour)" : {{Integer}},
  "[StartWeekDay](#cfn-ec2-instanceeventwindow-timerange-startweekday)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-instanceeventwindow-timerange-syntax.yaml"></a>

```
  [EndHour](#cfn-ec2-instanceeventwindow-timerange-endhour): {{Integer}}
  [EndWeekDay](#cfn-ec2-instanceeventwindow-timerange-endweekday): {{String}}
  [StartHour](#cfn-ec2-instanceeventwindow-timerange-starthour): {{Integer}}
  [StartWeekDay](#cfn-ec2-instanceeventwindow-timerange-startweekday): {{String}}
```

## Properties
<a name="aws-properties-ec2-instanceeventwindow-timerange-properties"></a>

`EndHour`  <a name="cfn-ec2-instanceeventwindow-timerange-endhour"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `23`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndWeekDay`  <a name="cfn-ec2-instanceeventwindow-timerange-endweekday"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `sunday | monday | tuesday | wednesday | thursday | friday | saturday`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartHour`  <a name="cfn-ec2-instanceeventwindow-timerange-starthour"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `23`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartWeekDay`  <a name="cfn-ec2-instanceeventwindow-timerange-startweekday"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `sunday | monday | tuesday | wednesday | thursday | friday | saturday`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
