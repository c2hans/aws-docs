---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformitemenablementconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormItemEnablementConfiguration

An item enablement configuration.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementconfiguration-syntax.json"></a>

```json
{
  "[Action](#cfn-connect-evaluationform-evaluationformitemenablementconfiguration-action)" : {{String}},
  "[Condition](#cfn-connect-evaluationform-evaluationformitemenablementconfiguration-condition)" : {{EvaluationFormItemEnablementCondition}},
  "[DefaultAction](#cfn-connect-evaluationform-evaluationformitemenablementconfiguration-defaultaction)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementconfiguration-syntax.yaml"></a>

```yaml
  [Action](#cfn-connect-evaluationform-evaluationformitemenablementconfiguration-action): {{String}}
  [Condition](#cfn-connect-evaluationform-evaluationformitemenablementconfiguration-condition): {{
    EvaluationFormItemEnablementCondition}}
  [DefaultAction](#cfn-connect-evaluationform-evaluationformitemenablementconfiguration-defaultaction): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementconfiguration-properties"></a>

`Action`  <a name="cfn-connect-evaluationform-evaluationformitemenablementconfiguration-action"></a>
The enablement action to apply if the condition is satisfied.
*Required*: Yes
*Type*: String
*Allowed values*: `DISABLE | ENABLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Condition`  <a name="cfn-connect-evaluationform-evaluationformitemenablementconfiguration-condition"></a>
A condition for item enablement configuration.
*Required*: Yes
*Type*: [EvaluationFormItemEnablementCondition](aws-properties-connect-evaluationform-evaluationformitemenablementcondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultAction`  <a name="cfn-connect-evaluationform-evaluationformitemenablementconfiguration-defaultaction"></a>
The enablement action to apply if the condition is not satisfied. This action is also applied when the condition depends on an external source that is still pending or could not be resolved.
*Required*: No
*Type*: String
*Allowed values*: `DISABLE | ENABLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
