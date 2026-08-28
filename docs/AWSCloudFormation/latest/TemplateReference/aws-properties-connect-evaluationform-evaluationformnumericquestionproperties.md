---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformnumericquestionproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormNumericQuestionProperties
<a name="aws-properties-connect-evaluationform-evaluationformnumericquestionproperties"></a>

Information about properties for a numeric question in an evaluation form.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformnumericquestionproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformnumericquestionproperties-syntax.json"></a>

```
{
  "[Automation](#cfn-connect-evaluationform-evaluationformnumericquestionproperties-automation)" : {{EvaluationFormNumericQuestionAutomation}},
  "[MaxValue](#cfn-connect-evaluationform-evaluationformnumericquestionproperties-maxvalue)" : {{Integer}},
  "[MinValue](#cfn-connect-evaluationform-evaluationformnumericquestionproperties-minvalue)" : {{Integer}},
  "[Options](#cfn-connect-evaluationform-evaluationformnumericquestionproperties-options)" : {{[ EvaluationFormNumericQuestionOption, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformnumericquestionproperties-syntax.yaml"></a>

```
  [Automation](#cfn-connect-evaluationform-evaluationformnumericquestionproperties-automation): {{
    EvaluationFormNumericQuestionAutomation}}
  [MaxValue](#cfn-connect-evaluationform-evaluationformnumericquestionproperties-maxvalue): {{Integer}}
  [MinValue](#cfn-connect-evaluationform-evaluationformnumericquestionproperties-minvalue): {{Integer}}
  [Options](#cfn-connect-evaluationform-evaluationformnumericquestionproperties-options): {{
    - EvaluationFormNumericQuestionOption}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformnumericquestionproperties-properties"></a>

`Automation`  <a name="cfn-connect-evaluationform-evaluationformnumericquestionproperties-automation"></a>
The automation properties of the numeric question.
*Required*: No
*Type*: [EvaluationFormNumericQuestionAutomation](aws-properties-connect-evaluationform-evaluationformnumericquestionautomation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxValue`  <a name="cfn-connect-evaluationform-evaluationformnumericquestionproperties-maxvalue"></a>
The maximum answer value.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinValue`  <a name="cfn-connect-evaluationform-evaluationformnumericquestionproperties-minvalue"></a>
The minimum answer value.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Options`  <a name="cfn-connect-evaluationform-evaluationformnumericquestionproperties-options"></a>
The scoring options of the numeric question.
*Required*: No
*Type*: Array of [EvaluationFormNumericQuestionOption](aws-properties-connect-evaluationform-evaluationformnumericquestionoption.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
