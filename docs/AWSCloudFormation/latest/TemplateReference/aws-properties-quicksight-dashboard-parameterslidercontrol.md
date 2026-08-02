---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-parameterslidercontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ParameterSliderControl
<a name="aws-properties-quicksight-dashboard-parameterslidercontrol"></a>

A control to display a horizontal toggle bar. This is used to change a value by sliding the toggle.

## Syntax
<a name="aws-properties-quicksight-dashboard-parameterslidercontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-parameterslidercontrol-syntax.json"></a>

```
{
  "[DisplayOptions](#cfn-quicksight-dashboard-parameterslidercontrol-displayoptions)" : {{SliderControlDisplayOptions}},
  "[MaximumValue](#cfn-quicksight-dashboard-parameterslidercontrol-maximumvalue)" : {{Number}},
  "[MinimumValue](#cfn-quicksight-dashboard-parameterslidercontrol-minimumvalue)" : {{Number}},
  "[ParameterControlId](#cfn-quicksight-dashboard-parameterslidercontrol-parametercontrolid)" : {{String}},
  "[SourceParameterName](#cfn-quicksight-dashboard-parameterslidercontrol-sourceparametername)" : {{String}},
  "[StepSize](#cfn-quicksight-dashboard-parameterslidercontrol-stepsize)" : {{Number}},
  "[Title](#cfn-quicksight-dashboard-parameterslidercontrol-title)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-parameterslidercontrol-syntax.yaml"></a>

```
  [DisplayOptions](#cfn-quicksight-dashboard-parameterslidercontrol-displayoptions): {{
    SliderControlDisplayOptions}}
  [MaximumValue](#cfn-quicksight-dashboard-parameterslidercontrol-maximumvalue): {{Number}}
  [MinimumValue](#cfn-quicksight-dashboard-parameterslidercontrol-minimumvalue): {{Number}}
  [ParameterControlId](#cfn-quicksight-dashboard-parameterslidercontrol-parametercontrolid): {{String}}
  [SourceParameterName](#cfn-quicksight-dashboard-parameterslidercontrol-sourceparametername): {{String}}
  [StepSize](#cfn-quicksight-dashboard-parameterslidercontrol-stepsize): {{Number}}
  [Title](#cfn-quicksight-dashboard-parameterslidercontrol-title): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-parameterslidercontrol-properties"></a>

`DisplayOptions`  <a name="cfn-quicksight-dashboard-parameterslidercontrol-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [SliderControlDisplayOptions](aws-properties-quicksight-dashboard-slidercontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumValue`  <a name="cfn-quicksight-dashboard-parameterslidercontrol-maximumvalue"></a>
The larger value that is displayed at the right of the slider.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumValue`  <a name="cfn-quicksight-dashboard-parameterslidercontrol-minimumvalue"></a>
The smaller value that is displayed at the left of the slider.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterControlId`  <a name="cfn-quicksight-dashboard-parameterslidercontrol-parametercontrolid"></a>
The ID of the `ParameterSliderControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceParameterName`  <a name="cfn-quicksight-dashboard-parameterslidercontrol-sourceparametername"></a>
The source parameter name of the `ParameterSliderControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StepSize`  <a name="cfn-quicksight-dashboard-parameterslidercontrol-stepsize"></a>
The number of increments that the slider bar is divided into.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-dashboard-parameterslidercontrol-title"></a>
The title of the `ParameterSliderControl`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
