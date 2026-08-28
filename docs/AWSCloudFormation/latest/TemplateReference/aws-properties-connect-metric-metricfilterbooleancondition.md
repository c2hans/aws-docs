---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-metric-metricfilterbooleancondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Metric MetricFilterBooleanCondition
<a name="aws-properties-connect-metric-metricfilterbooleancondition"></a>

A boolean comparison condition for metric filters.

## Syntax
<a name="aws-properties-connect-metric-metricfilterbooleancondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-metric-metricfilterbooleancondition-syntax.json"></a>

```
{
  "[Comparison](#cfn-connect-metric-metricfilterbooleancondition-comparison)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-metric-metricfilterbooleancondition-syntax.yaml"></a>

```
  [Comparison](#cfn-connect-metric-metricfilterbooleancondition-comparison): {{String}}
```

## Properties
<a name="aws-properties-connect-metric-metricfilterbooleancondition-properties"></a>

`Comparison`  <a name="cfn-connect-metric-metricfilterbooleancondition-comparison"></a>
The comparison operator. Valid values: `IS_TRUE` (matches when the field is true) \| `IS_FALSE` (matches when the field is false).
*Required*: Yes
*Type*: String
*Allowed values*: `IS_TRUE | IS_FALSE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
