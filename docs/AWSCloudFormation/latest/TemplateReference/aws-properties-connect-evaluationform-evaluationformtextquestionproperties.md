---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformtextquestionproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormTextQuestionProperties
<a name="aws-properties-connect-evaluationform-evaluationformtextquestionproperties"></a>

Information about properties for a text question in an evaluation form.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformtextquestionproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformtextquestionproperties-syntax.json"></a>

```
{
  "[Automation](#cfn-connect-evaluationform-evaluationformtextquestionproperties-automation)" : {{EvaluationFormTextQuestionAutomation}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformtextquestionproperties-syntax.yaml"></a>

```
  [Automation](#cfn-connect-evaluationform-evaluationformtextquestionproperties-automation): {{
    EvaluationFormTextQuestionAutomation}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformtextquestionproperties-properties"></a>

`Automation`  <a name="cfn-connect-evaluationform-evaluationformtextquestionproperties-automation"></a>
The automation properties of the text question.
*Required*: No
*Type*: [EvaluationFormTextQuestionAutomation](aws-properties-connect-evaluationform-evaluationformtextquestionautomation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
