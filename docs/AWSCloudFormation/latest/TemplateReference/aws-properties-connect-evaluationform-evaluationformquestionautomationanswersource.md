---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformquestionautomationanswersource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormQuestionAutomationAnswerSource
<a name="aws-properties-connect-evaluationform-evaluationformquestionautomationanswersource"></a>

A question automation answer.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformquestionautomationanswersource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformquestionautomationanswersource-syntax.json"></a>

```
{
  "[SourceType](#cfn-connect-evaluationform-evaluationformquestionautomationanswersource-sourcetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformquestionautomationanswersource-syntax.yaml"></a>

```
  [SourceType](#cfn-connect-evaluationform-evaluationformquestionautomationanswersource-sourcetype): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformquestionautomationanswersource-properties"></a>

`SourceType`  <a name="cfn-connect-evaluationform-evaluationformquestionautomationanswersource-sourcetype"></a>
The automation answer source type.
*Required*: Yes
*Type*: String
*Allowed values*: `CONTACT_LENS_DATA | GEN_AI`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
