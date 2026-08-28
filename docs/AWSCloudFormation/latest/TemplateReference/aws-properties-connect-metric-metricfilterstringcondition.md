---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-metric-metricfilterstringcondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Metric MetricFilterStringCondition
<a name="aws-properties-connect-metric-metricfilterstringcondition"></a>

A string comparison condition for metric filters.

## Syntax
<a name="aws-properties-connect-metric-metricfilterstringcondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-metric-metricfilterstringcondition-syntax.json"></a>

```
{
  "[Comparison](#cfn-connect-metric-metricfilterstringcondition-comparison)" : {{String}},
  "[Values](#cfn-connect-metric-metricfilterstringcondition-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-metric-metricfilterstringcondition-syntax.yaml"></a>

```
  [Comparison](#cfn-connect-metric-metricfilterstringcondition-comparison): {{String}}
  [Values](#cfn-connect-metric-metricfilterstringcondition-values): {{
    - String}}
```

## Properties
<a name="aws-properties-connect-metric-metricfilterstringcondition-properties"></a>

`Comparison`  <a name="cfn-connect-metric-metricfilterstringcondition-comparison"></a>
The comparison operator. Valid values: `MATCHES_ANY` (matches any of the specified values) \| `MATCHES_NONE` (matches none of the specified values).
*Required*: Yes
*Type*: String
*Allowed values*: `MATCHES_ANY | MATCHES_NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-connect-metric-metricfilterstringcondition-values"></a>
The string values to compare against.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
