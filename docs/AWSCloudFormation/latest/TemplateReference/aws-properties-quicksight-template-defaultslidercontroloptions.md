---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-defaultslidercontroloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DefaultSliderControlOptions
<a name="aws-properties-quicksight-template-defaultslidercontroloptions"></a>

The default options that correspond to the `Slider` filter control type.

## Syntax
<a name="aws-properties-quicksight-template-defaultslidercontroloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-defaultslidercontroloptions-syntax.json"></a>

```
{
  "[DisplayOptions](#cfn-quicksight-template-defaultslidercontroloptions-displayoptions)" : {{SliderControlDisplayOptions}},
  "[MaximumValue](#cfn-quicksight-template-defaultslidercontroloptions-maximumvalue)" : {{Number}},
  "[MinimumValue](#cfn-quicksight-template-defaultslidercontroloptions-minimumvalue)" : {{Number}},
  "[StepSize](#cfn-quicksight-template-defaultslidercontroloptions-stepsize)" : {{Number}},
  "[Type](#cfn-quicksight-template-defaultslidercontroloptions-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-defaultslidercontroloptions-syntax.yaml"></a>

```
  [DisplayOptions](#cfn-quicksight-template-defaultslidercontroloptions-displayoptions): {{
    SliderControlDisplayOptions}}
  [MaximumValue](#cfn-quicksight-template-defaultslidercontroloptions-maximumvalue): {{Number}}
  [MinimumValue](#cfn-quicksight-template-defaultslidercontroloptions-minimumvalue): {{Number}}
  [StepSize](#cfn-quicksight-template-defaultslidercontroloptions-stepsize): {{Number}}
  [Type](#cfn-quicksight-template-defaultslidercontroloptions-type): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-defaultslidercontroloptions-properties"></a>

`DisplayOptions`  <a name="cfn-quicksight-template-defaultslidercontroloptions-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [SliderControlDisplayOptions](aws-properties-quicksight-template-slidercontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumValue`  <a name="cfn-quicksight-template-defaultslidercontroloptions-maximumvalue"></a>
The larger value that is displayed at the right of the slider.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumValue`  <a name="cfn-quicksight-template-defaultslidercontroloptions-minimumvalue"></a>
The smaller value that is displayed at the left of the slider.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StepSize`  <a name="cfn-quicksight-template-defaultslidercontroloptions-stepsize"></a>
The number of increments that the slider bar is divided into.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-template-defaultslidercontroloptions-type"></a>
The type of the `DefaultSliderControlOptions`. Choose one of the following options:
+ `SINGLE_POINT`: Filter against(equals) a single data point.
+ `RANGE`: Filter data that is in a specified range.
*Required*: No
*Type*: String
*Allowed values*: `SINGLE_POINT | RANGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
