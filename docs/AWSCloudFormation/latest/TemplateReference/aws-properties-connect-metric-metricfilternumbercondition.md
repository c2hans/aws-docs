---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-metric-metricfilternumbercondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Metric MetricFilterNumberCondition
<a name="aws-properties-connect-metric-metricfilternumbercondition"></a>

A numeric comparison condition for metric filters.

## Syntax
<a name="aws-properties-connect-metric-metricfilternumbercondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-metric-metricfilternumbercondition-syntax.json"></a>

```
{
  "[Comparison](#cfn-connect-metric-metricfilternumbercondition-comparison)" : {{String}},
  "[Values](#cfn-connect-metric-metricfilternumbercondition-values)" : {{[ Number, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-metric-metricfilternumbercondition-syntax.yaml"></a>

```
  [Comparison](#cfn-connect-metric-metricfilternumbercondition-comparison): {{String}}
  [Values](#cfn-connect-metric-metricfilternumbercondition-values): {{
    - Number}}
```

## Properties
<a name="aws-properties-connect-metric-metricfilternumbercondition-properties"></a>

`Comparison`  <a name="cfn-connect-metric-metricfilternumbercondition-comparison"></a>
The comparison operator. Valid values: `LESSER` (less than) \| `LESSER_OR_EQUAL` (less than or equal to) \| `GREATER` (greater than) \| `GREATER_OR_EQUAL` (greater than or equal to).
*Required*: Yes
*Type*: String
*Allowed values*: `LESSER | LESSER_OR_EQUAL | GREATER | GREATER_OR_EQUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-connect-metric-metricfilternumbercondition-values"></a>
The numeric values to compare against.
*Required*: Yes
*Type*: Array of Number
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
