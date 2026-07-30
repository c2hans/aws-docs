---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformmultiselectquestionproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormMultiSelectQuestionProperties
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionproperties"></a>

Properties for a multi-select question in an evaluation form.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionproperties-syntax.json"></a>

```
{
  "[Automation](#cfn-connect-evaluationform-evaluationformmultiselectquestionproperties-automation)" : {{EvaluationFormMultiSelectQuestionAutomation}},
  "[DisplayAs](#cfn-connect-evaluationform-evaluationformmultiselectquestionproperties-displayas)" : {{String}},
  "[Options](#cfn-connect-evaluationform-evaluationformmultiselectquestionproperties-options)" : {{[ EvaluationFormMultiSelectQuestionOption, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionproperties-syntax.yaml"></a>

```
  [Automation](#cfn-connect-evaluationform-evaluationformmultiselectquestionproperties-automation): {{
    EvaluationFormMultiSelectQuestionAutomation}}
  [DisplayAs](#cfn-connect-evaluationform-evaluationformmultiselectquestionproperties-displayas): {{String}}
  [Options](#cfn-connect-evaluationform-evaluationformmultiselectquestionproperties-options): {{
    - EvaluationFormMultiSelectQuestionOption}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionproperties-properties"></a>

`Automation`  <a name="cfn-connect-evaluationform-evaluationformmultiselectquestionproperties-automation"></a>
Automation configuration for this multi-select question.
*Required*: No
*Type*: [EvaluationFormMultiSelectQuestionAutomation](aws-properties-connect-evaluationform-evaluationformmultiselectquestionautomation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayAs`  <a name="cfn-connect-evaluationform-evaluationformmultiselectquestionproperties-displayas"></a>
Display format for the multi-select question.
*Required*: No
*Type*: String
*Allowed values*: `DROPDOWN | CHECKBOX`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Options`  <a name="cfn-connect-evaluationform-evaluationformmultiselectquestionproperties-options"></a>
Options available for this multi-select question.
*Required*: Yes
*Type*: Array of [EvaluationFormMultiSelectQuestionOption](aws-properties-connect-evaluationform-evaluationformmultiselectquestionoption.md)
*Minimum*: `2`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
