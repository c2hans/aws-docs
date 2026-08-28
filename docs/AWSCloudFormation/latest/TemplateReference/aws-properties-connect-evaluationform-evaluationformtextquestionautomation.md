---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformtextquestionautomation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormTextQuestionAutomation
<a name="aws-properties-connect-evaluationform-evaluationformtextquestionautomation"></a>

Information about the automation configuration in text questions.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformtextquestionautomation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformtextquestionautomation-syntax.json"></a>

```
{
  "[AnswerSource](#cfn-connect-evaluationform-evaluationformtextquestionautomation-answersource)" : {{EvaluationFormQuestionAutomationAnswerSource}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformtextquestionautomation-syntax.yaml"></a>

```
  [AnswerSource](#cfn-connect-evaluationform-evaluationformtextquestionautomation-answersource): {{
    EvaluationFormQuestionAutomationAnswerSource}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformtextquestionautomation-properties"></a>

`AnswerSource`  <a name="cfn-connect-evaluationform-evaluationformtextquestionautomation-answersource"></a>
Automation answer source.
*Required*: No
*Type*: [EvaluationFormQuestionAutomationAnswerSource](aws-properties-connect-evaluationform-evaluationformquestionautomationanswersource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
