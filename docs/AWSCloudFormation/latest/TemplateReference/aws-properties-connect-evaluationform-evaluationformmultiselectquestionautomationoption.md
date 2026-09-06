---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformmultiselectquestionautomationoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormMultiSelectQuestionAutomationOption
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionautomationoption"></a>

An automation option for a multi-select question.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionautomationoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionautomationoption-syntax.json"></a>

```
{
  "[RuleCategory](#cfn-connect-evaluationform-evaluationformmultiselectquestionautomationoption-rulecategory)" : {{MultiSelectQuestionRuleCategoryAutomation}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionautomationoption-syntax.yaml"></a>

```
  [RuleCategory](#cfn-connect-evaluationform-evaluationformmultiselectquestionautomationoption-rulecategory): {{
    MultiSelectQuestionRuleCategoryAutomation}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionautomationoption-properties"></a>

`RuleCategory`  <a name="cfn-connect-evaluationform-evaluationformmultiselectquestionautomationoption-rulecategory"></a>
Rule category configuration for this automation option.
*Required*: Yes
*Type*: [MultiSelectQuestionRuleCategoryAutomation](aws-properties-connect-evaluationform-multiselectquestionrulecategoryautomation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
