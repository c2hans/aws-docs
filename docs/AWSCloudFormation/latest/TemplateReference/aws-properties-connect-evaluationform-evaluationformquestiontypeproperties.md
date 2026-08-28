---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformquestiontypeproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormQuestionTypeProperties
<a name="aws-properties-connect-evaluationform-evaluationformquestiontypeproperties"></a>

Information about properties for a question in an evaluation form. The question type properties must be either for a numeric question or a single select question.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformquestiontypeproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformquestiontypeproperties-syntax.json"></a>

```
{
  "[MultiSelect](#cfn-connect-evaluationform-evaluationformquestiontypeproperties-multiselect)" : {{EvaluationFormMultiSelectQuestionProperties}},
  "[Numeric](#cfn-connect-evaluationform-evaluationformquestiontypeproperties-numeric)" : {{EvaluationFormNumericQuestionProperties}},
  "[SingleSelect](#cfn-connect-evaluationform-evaluationformquestiontypeproperties-singleselect)" : {{EvaluationFormSingleSelectQuestionProperties}},
  "[Text](#cfn-connect-evaluationform-evaluationformquestiontypeproperties-text)" : {{EvaluationFormTextQuestionProperties}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformquestiontypeproperties-syntax.yaml"></a>

```
  [MultiSelect](#cfn-connect-evaluationform-evaluationformquestiontypeproperties-multiselect): {{
    EvaluationFormMultiSelectQuestionProperties}}
  [Numeric](#cfn-connect-evaluationform-evaluationformquestiontypeproperties-numeric): {{
    EvaluationFormNumericQuestionProperties}}
  [SingleSelect](#cfn-connect-evaluationform-evaluationformquestiontypeproperties-singleselect): {{
    EvaluationFormSingleSelectQuestionProperties}}
  [Text](#cfn-connect-evaluationform-evaluationformquestiontypeproperties-text): {{
    EvaluationFormTextQuestionProperties}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformquestiontypeproperties-properties"></a>

`MultiSelect`  <a name="cfn-connect-evaluationform-evaluationformquestiontypeproperties-multiselect"></a>
Properties for multi-select question types.
*Required*: No
*Type*: [EvaluationFormMultiSelectQuestionProperties](aws-properties-connect-evaluationform-evaluationformmultiselectquestionproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Numeric`  <a name="cfn-connect-evaluationform-evaluationformquestiontypeproperties-numeric"></a>
The properties of the numeric question.
*Required*: No
*Type*: [EvaluationFormNumericQuestionProperties](aws-properties-connect-evaluationform-evaluationformnumericquestionproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SingleSelect`  <a name="cfn-connect-evaluationform-evaluationformquestiontypeproperties-singleselect"></a>
The properties of the numeric question.
*Required*: No
*Type*: [EvaluationFormSingleSelectQuestionProperties](aws-properties-connect-evaluationform-evaluationformsingleselectquestionproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-connect-evaluationform-evaluationformquestiontypeproperties-text"></a>
The properties of the text question.
*Required*: No
*Type*: [EvaluationFormTextQuestionProperties](aws-properties-connect-evaluationform-evaluationformtextquestionproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
