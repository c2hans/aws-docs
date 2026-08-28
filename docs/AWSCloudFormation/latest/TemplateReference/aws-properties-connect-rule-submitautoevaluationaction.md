---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-rule-submitautoevaluationaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Rule SubmitAutoEvaluationAction
<a name="aws-properties-connect-rule-submitautoevaluationaction"></a>

<a name="aws-properties-connect-rule-submitautoevaluationaction-description"></a>The `SubmitAutoEvaluationAction` property type specifies Property description not available. for an [AWS::Connect::Rule](aws-resource-connect-rule.md).

## Syntax
<a name="aws-properties-connect-rule-submitautoevaluationaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-rule-submitautoevaluationaction-syntax.json"></a>

```
{
  "[EvaluationFormArn](#cfn-connect-rule-submitautoevaluationaction-evaluationformarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-rule-submitautoevaluationaction-syntax.yaml"></a>

```
  [EvaluationFormArn](#cfn-connect-rule-submitautoevaluationaction-evaluationformarn): {{String}}
```

## Properties
<a name="aws-properties-connect-rule-submitautoevaluationaction-properties"></a>

`EvaluationFormArn`  <a name="cfn-connect-rule-submitautoevaluationaction-evaluationformarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^$|arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/evaluation-form/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
