---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformitemenablementexpression.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormItemEnablementExpression
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementexpression"></a>

An expression that defines a basic building block of conditional enablement.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementexpression-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementexpression-syntax.json"></a>

```
{
  "[Comparator](#cfn-connect-evaluationform-evaluationformitemenablementexpression-comparator)" : {{String}},
  "[Source](#cfn-connect-evaluationform-evaluationformitemenablementexpression-source)" : {{EvaluationFormItemEnablementSource}},
  "[Values](#cfn-connect-evaluationform-evaluationformitemenablementexpression-values)" : {{[ EvaluationFormItemEnablementSourceValue, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementexpression-syntax.yaml"></a>

```
  [Comparator](#cfn-connect-evaluationform-evaluationformitemenablementexpression-comparator): {{String}}
  [Source](#cfn-connect-evaluationform-evaluationformitemenablementexpression-source): {{
    EvaluationFormItemEnablementSource}}
  [Values](#cfn-connect-evaluationform-evaluationformitemenablementexpression-values): {{
    - EvaluationFormItemEnablementSourceValue}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformitemenablementexpression-properties"></a>

`Comparator`  <a name="cfn-connect-evaluationform-evaluationformitemenablementexpression-comparator"></a>
A comparator to be used against list of values.
*Required*: Yes
*Type*: String
*Allowed values*: `IN | NOT_IN | ALL_IN | EXACT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-connect-evaluationform-evaluationformitemenablementexpression-source"></a>
A source item of enablement expression.
*Required*: Yes
*Type*: [EvaluationFormItemEnablementSource](aws-properties-connect-evaluationform-evaluationformitemenablementsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-connect-evaluationform-evaluationformitemenablementexpression-values"></a>
A list of values from source item.
*Required*: Yes
*Type*: Array of [EvaluationFormItemEnablementSourceValue](aws-properties-connect-evaluationform-evaluationformitemenablementsourcevalue.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
