---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-parameterdatetimepickercontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ParameterDateTimePickerControl
<a name="aws-properties-quicksight-analysis-parameterdatetimepickercontrol"></a>

A control from a date parameter that specifies date and time.

## Syntax
<a name="aws-properties-quicksight-analysis-parameterdatetimepickercontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-parameterdatetimepickercontrol-syntax.json"></a>

```
{
  "[DisplayOptions](#cfn-quicksight-analysis-parameterdatetimepickercontrol-displayoptions)" : {{DateTimePickerControlDisplayOptions}},
  "[ParameterControlId](#cfn-quicksight-analysis-parameterdatetimepickercontrol-parametercontrolid)" : {{String}},
  "[SourceParameterName](#cfn-quicksight-analysis-parameterdatetimepickercontrol-sourceparametername)" : {{String}},
  "[Title](#cfn-quicksight-analysis-parameterdatetimepickercontrol-title)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-parameterdatetimepickercontrol-syntax.yaml"></a>

```
  [DisplayOptions](#cfn-quicksight-analysis-parameterdatetimepickercontrol-displayoptions): {{
    DateTimePickerControlDisplayOptions}}
  [ParameterControlId](#cfn-quicksight-analysis-parameterdatetimepickercontrol-parametercontrolid): {{String}}
  [SourceParameterName](#cfn-quicksight-analysis-parameterdatetimepickercontrol-sourceparametername): {{String}}
  [Title](#cfn-quicksight-analysis-parameterdatetimepickercontrol-title): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-parameterdatetimepickercontrol-properties"></a>

`DisplayOptions`  <a name="cfn-quicksight-analysis-parameterdatetimepickercontrol-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [DateTimePickerControlDisplayOptions](aws-properties-quicksight-analysis-datetimepickercontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterControlId`  <a name="cfn-quicksight-analysis-parameterdatetimepickercontrol-parametercontrolid"></a>
The ID of the `ParameterDateTimePickerControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceParameterName`  <a name="cfn-quicksight-analysis-parameterdatetimepickercontrol-sourceparametername"></a>
The name of the `ParameterDateTimePickerControl`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-quicksight-analysis-parameterdatetimepickercontrol-title"></a>
The title of the `ParameterDateTimePickerControl`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
