---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-multiselectquestionrulecategoryautomation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm MultiSelectQuestionRuleCategoryAutomation
<a name="aws-properties-connect-evaluationform-multiselectquestionrulecategoryautomation"></a>

Automation rule for multi-select questions based on rule categories.

## Syntax
<a name="aws-properties-connect-evaluationform-multiselectquestionrulecategoryautomation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-multiselectquestionrulecategoryautomation-syntax.json"></a>

```
{
  "[Category](#cfn-connect-evaluationform-multiselectquestionrulecategoryautomation-category)" : {{String}},
  "[Condition](#cfn-connect-evaluationform-multiselectquestionrulecategoryautomation-condition)" : {{String}},
  "[OptionRefIds](#cfn-connect-evaluationform-multiselectquestionrulecategoryautomation-optionrefids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-multiselectquestionrulecategoryautomation-syntax.yaml"></a>

```
  [Category](#cfn-connect-evaluationform-multiselectquestionrulecategoryautomation-category): {{String}}
  [Condition](#cfn-connect-evaluationform-multiselectquestionrulecategoryautomation-condition): {{String}}
  [OptionRefIds](#cfn-connect-evaluationform-multiselectquestionrulecategoryautomation-optionrefids): {{
    - String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-multiselectquestionrulecategoryautomation-properties"></a>

`Category`  <a name="cfn-connect-evaluationform-multiselectquestionrulecategoryautomation-category"></a>
The category name for this automation rule.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Condition`  <a name="cfn-connect-evaluationform-multiselectquestionrulecategoryautomation-condition"></a>
The condition for this automation rule.
*Required*: Yes
*Type*: String
*Allowed values*: `PRESENT | NOT_PRESENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OptionRefIds`  <a name="cfn-connect-evaluationform-multiselectquestionrulecategoryautomation-optionrefids"></a>
Reference IDs of options for this automation rule.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
