---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-numericquestionpropertyvalueautomation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm NumericQuestionPropertyValueAutomation
<a name="aws-properties-connect-evaluationform-numericquestionpropertyvalueautomation"></a>

Information about the property value used in automation of a numeric questions.

## Syntax
<a name="aws-properties-connect-evaluationform-numericquestionpropertyvalueautomation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-numericquestionpropertyvalueautomation-syntax.json"></a>

```
{
  "[Label](#cfn-connect-evaluationform-numericquestionpropertyvalueautomation-label)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-numericquestionpropertyvalueautomation-syntax.yaml"></a>

```
  [Label](#cfn-connect-evaluationform-numericquestionpropertyvalueautomation-label): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-numericquestionpropertyvalueautomation-properties"></a>

`Label`  <a name="cfn-connect-evaluationform-numericquestionpropertyvalueautomation-label"></a>
The property label of the automation.
*Required*: Yes
*Type*: String
*Allowed values*: `OVERALL_CUSTOMER_SENTIMENT_SCORE | OVERALL_AGENT_SENTIMENT_SCORE | NON_TALK_TIME | NON_TALK_TIME_PERCENTAGE | NUMBER_OF_INTERRUPTIONS | CONTACT_DURATION | AGENT_INTERACTION_DURATION | CUSTOMER_HOLD_TIME | LONGEST_HOLD_DURATION | NUMBER_OF_HOLDS | AGENT_INTERACTION_AND_HOLD_DURATION | CUSTOMER_SENTIMENT_SCORE_WITHOUT_AGENT | CUSTOMER_SENTIMENT_SCORE_WITH_AGENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
