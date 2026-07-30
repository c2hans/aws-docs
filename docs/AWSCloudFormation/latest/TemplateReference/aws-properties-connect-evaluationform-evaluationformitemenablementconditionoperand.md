---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformitemenablementconditionoperand.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormItemEnablementConditionOperand
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementconditionoperand"></a>

An operand of the enablement condition.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementconditionoperand-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementconditionoperand-syntax.json"></a>

```
{
  "[Expression](#cfn-connect-evaluationform-evaluationformitemenablementconditionoperand-expression)" : {{EvaluationFormItemEnablementExpression}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementconditionoperand-syntax.yaml"></a>

```
  [Expression](#cfn-connect-evaluationform-evaluationformitemenablementconditionoperand-expression): {{
    EvaluationFormItemEnablementExpression}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementconditionoperand-properties"></a>

`Expression`  <a name="cfn-connect-evaluationform-evaluationformitemenablementconditionoperand-expression"></a>
An expression of the enablement condition.
*Required*: No
*Type*: [EvaluationFormItemEnablementExpression](aws-properties-connect-evaluationform-evaluationformitemenablementexpression.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
