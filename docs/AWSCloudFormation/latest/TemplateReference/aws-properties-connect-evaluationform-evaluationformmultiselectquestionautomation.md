---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformmultiselectquestionautomation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormMultiSelectQuestionAutomation
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionautomation"></a>

Automation configuration for multi-select questions.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionautomation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionautomation-syntax.json"></a>

```
{
  "[AnswerSource](#cfn-connect-evaluationform-evaluationformmultiselectquestionautomation-answersource)" : {{EvaluationFormQuestionAutomationAnswerSource}},
  "[DefaultOptionRefIds](#cfn-connect-evaluationform-evaluationformmultiselectquestionautomation-defaultoptionrefids)" : {{[ String, ... ]}},
  "[Options](#cfn-connect-evaluationform-evaluationformmultiselectquestionautomation-options)" : {{[ EvaluationFormMultiSelectQuestionAutomationOption, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionautomation-syntax.yaml"></a>

```
  [AnswerSource](#cfn-connect-evaluationform-evaluationformmultiselectquestionautomation-answersource): {{
    EvaluationFormQuestionAutomationAnswerSource}}
  [DefaultOptionRefIds](#cfn-connect-evaluationform-evaluationformmultiselectquestionautomation-defaultoptionrefids): {{
    - String}}
  [Options](#cfn-connect-evaluationform-evaluationformmultiselectquestionautomation-options): {{
    - EvaluationFormMultiSelectQuestionAutomationOption}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionautomation-properties"></a>

`AnswerSource`  <a name="cfn-connect-evaluationform-evaluationformmultiselectquestionautomation-answersource"></a>
Property description not available.
*Required*: No
*Type*: [EvaluationFormQuestionAutomationAnswerSource](aws-properties-connect-evaluationform-evaluationformquestionautomationanswersource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultOptionRefIds`  <a name="cfn-connect-evaluationform-evaluationformmultiselectquestionautomation-defaultoptionrefids"></a>
Reference IDs of default options.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Options`  <a name="cfn-connect-evaluationform-evaluationformmultiselectquestionautomation-options"></a>
Automation options for the multi-select question.
*Required*: No
*Type*: Array of [EvaluationFormMultiSelectQuestionAutomationOption](aws-properties-connect-evaluationform-evaluationformmultiselectquestionautomationoption.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
