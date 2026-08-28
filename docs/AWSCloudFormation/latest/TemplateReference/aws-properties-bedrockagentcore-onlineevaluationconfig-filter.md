---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-onlineevaluationconfig-filter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OnlineEvaluationConfig Filter
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-filter"></a>

 A filter that applies conditions to agent traces during online evaluation to determine which traces should be evaluated.

## Syntax
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-filter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-filter-syntax.json"></a>

```
{
  "[Key](#cfn-bedrockagentcore-onlineevaluationconfig-filter-key)" : {{String}},
  "[Operator](#cfn-bedrockagentcore-onlineevaluationconfig-filter-operator)" : {{String}},
  "[Value](#cfn-bedrockagentcore-onlineevaluationconfig-filter-value)" : {{FilterValue}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-filter-syntax.yaml"></a>

```
  [Key](#cfn-bedrockagentcore-onlineevaluationconfig-filter-key): {{String}}
  [Operator](#cfn-bedrockagentcore-onlineevaluationconfig-filter-operator): {{String}}
  [Value](#cfn-bedrockagentcore-onlineevaluationconfig-filter-value): {{
    FilterValue}}
```

## Properties
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-filter-properties"></a>

`Key`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-filter-key"></a>
 The key or field name to filter on within the agent trace data.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-filter-operator"></a>
 The comparison operator to use for filtering. Valid values include `Equals`, `NotEquals`, `GreaterThan`, `LessThan`, `GreaterThanOrEqual`, `LessThanOrEqual`, `Contains`, and `NotContains`.
*Required*: Yes
*Type*: String
*Allowed values*: `Equals | NotEquals | GreaterThan | LessThan | GreaterThanOrEqual | LessThanOrEqual | Contains | NotContains`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-filter-value"></a>
 The value to compare against using the specified operator.
*Required*: Yes
*Type*: [FilterValue](aws-properties-bedrockagentcore-onlineevaluationconfig-filtervalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
