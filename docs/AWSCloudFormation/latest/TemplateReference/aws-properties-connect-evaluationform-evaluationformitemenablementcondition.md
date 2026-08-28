---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformitemenablementcondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormItemEnablementCondition
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementcondition"></a>

A condition for item enablement.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementcondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementcondition-syntax.json"></a>

```
{
  "[Operands](#cfn-connect-evaluationform-evaluationformitemenablementcondition-operands)" : {{[ EvaluationFormItemEnablementConditionOperand, ... ]}},
  "[Operator](#cfn-connect-evaluationform-evaluationformitemenablementcondition-operator)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementcondition-syntax.yaml"></a>

```
  [Operands](#cfn-connect-evaluationform-evaluationformitemenablementcondition-operands): {{
    - EvaluationFormItemEnablementConditionOperand}}
  [Operator](#cfn-connect-evaluationform-evaluationformitemenablementcondition-operator): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementcondition-properties"></a>

`Operands`  <a name="cfn-connect-evaluationform-evaluationformitemenablementcondition-operands"></a>
Operands of the enablement condition.
*Required*: Yes
*Type*: Array of [EvaluationFormItemEnablementConditionOperand](aws-properties-connect-evaluationform-evaluationformitemenablementconditionoperand.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-connect-evaluationform-evaluationformitemenablementcondition-operator"></a>
The operator to be used to be applied to operands if more than one provided.
*Required*: No
*Type*: String
*Allowed values*: `OR | AND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
