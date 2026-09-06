---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformnumericquestionautomation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormNumericQuestionAutomation
<a name="aws-properties-connect-evaluationform-evaluationformnumericquestionautomation"></a>

Information about the automation configuration in numeric questions.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformnumericquestionautomation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformnumericquestionautomation-syntax.json"></a>

```
{
  "[AnswerSource](#cfn-connect-evaluationform-evaluationformnumericquestionautomation-answersource)" : {{EvaluationFormQuestionAutomationAnswerSource}},
  "[PropertyValue](#cfn-connect-evaluationform-evaluationformnumericquestionautomation-propertyvalue)" : {{NumericQuestionPropertyValueAutomation}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformnumericquestionautomation-syntax.yaml"></a>

```
  [AnswerSource](#cfn-connect-evaluationform-evaluationformnumericquestionautomation-answersource): {{
    EvaluationFormQuestionAutomationAnswerSource}}
  [PropertyValue](#cfn-connect-evaluationform-evaluationformnumericquestionautomation-propertyvalue): {{
    NumericQuestionPropertyValueAutomation}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformnumericquestionautomation-properties"></a>

`AnswerSource`  <a name="cfn-connect-evaluationform-evaluationformnumericquestionautomation-answersource"></a>
A source of automation answer for numeric question.
*Required*: No
*Type*: [EvaluationFormQuestionAutomationAnswerSource](aws-properties-connect-evaluationform-evaluationformquestionautomationanswersource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyValue`  <a name="cfn-connect-evaluationform-evaluationformnumericquestionautomation-propertyvalue"></a>
The property value of the automation.
*Required*: No
*Type*: [NumericQuestionPropertyValueAutomation](aws-properties-connect-evaluationform-numericquestionpropertyvalueautomation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
