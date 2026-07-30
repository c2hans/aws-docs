---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormItem
<a name="aws-properties-connect-evaluationform-evaluationformitem"></a>

Items that are part of the evaluation form. The total number of sections and questions must not exceed 100 each. Questions must be contained in a section.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformitem-syntax.json"></a>

```
{
  "[Question](#cfn-connect-evaluationform-evaluationformitem-question)" : {{EvaluationFormQuestion}},
  "[Section](#cfn-connect-evaluationform-evaluationformitem-section)" : {{EvaluationFormSection}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformitem-syntax.yaml"></a>

```
  [Question](#cfn-connect-evaluationform-evaluationformitem-question): {{
    EvaluationFormQuestion}}
  [Section](#cfn-connect-evaluationform-evaluationformitem-section): {{
    EvaluationFormSection}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformitem-properties"></a>

`Question`  <a name="cfn-connect-evaluationform-evaluationformitem-question"></a>
The information of the question.
*Required*: No
*Type*: [EvaluationFormQuestion](aws-properties-connect-evaluationform-evaluationformquestion.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Section`  <a name="cfn-connect-evaluationform-evaluationformitem-section"></a>
The information of the section.
*Required*: No
*Type*: [EvaluationFormSection](aws-properties-connect-evaluationform-evaluationformsection.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
