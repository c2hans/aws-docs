---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-parameterdatetimepickercontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ParameterDateTimePickerControl
<a name="aws-properties-quicksight-template-parameterdatetimepickercontrol"></a>

A control from a date parameter that specifies date and time.

## Syntax
<a name="aws-properties-quicksight-template-parameterdatetimepickercontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-parameterdatetimepickercontrol-syntax.json"></a>

```
{
  "[DisplayOptions](#cfn-quicksight-template-parameterdatetimepickercontrol-displayoptions)" : {{DateTimePickerControlDisplayOptions}},
  "[ParameterControlId](#cfn-quicksight-template-parameterdatetimepickercontrol-parametercontrolid)" : {{String}},
  "[SourceParameterName](#cfn-quicksight-template-parameterdatetimepickercontrol-sourceparametername)" : {{String}},
  "[Title](#cfn-quicksight-template-parameterdatetimepickercontrol-title)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-parameterdatetimepickercontrol-syntax.yaml"></a>

```
  [DisplayOptions](#cfn-quicksight-template-parameterdatetimepickercontrol-displayoptions): {{
    DateTimePickerControlDisplayOptions}}
  [ParameterControlId](#cfn-quicksight-template-parameterdatetimepickercontrol-parametercontrolid): {{String}}
  [SourceParameterName](#cfn-quicksight-template-parameterdatetimepickercontrol-sourceparametername): {{String}}
  [Title](#cfn-quicksight-template-parameterdatetimepickercontrol-title): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-parameterdatetimepickercontrol-properties"></a>

`DisplayOptions`  <a name="cfn-quicksight-template-parameterdatetimepickercontrol-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [DateTimePickerControlDisplayOptions](aws-properties-quicksight-template-datetimepickercontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterControlId`  <a name="cfn-quicksight-template-parameterdatetimepickercontrol-parametercontrolid"></a>
The ID of the `ParameterDateTimePickerControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceParameterName`  <a name="cfn-quicksight-template-parameterdatetimepickercontrol-sourceparametername"></a>
The name of the `ParameterDateTimePickerControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-template-parameterdatetimepickercontrol-title"></a>
The title of the `ParameterDateTimePickerControl`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
