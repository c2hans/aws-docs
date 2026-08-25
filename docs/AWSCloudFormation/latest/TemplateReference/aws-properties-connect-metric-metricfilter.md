---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-metric-metricfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Metric MetricFilter
<a name="aws-properties-connect-metric-metricfilter"></a>

A filter condition applied to a metric component in a calculation. Filters restrict the data included in the metric computation.

## Syntax
<a name="aws-properties-connect-metric-metricfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-metric-metricfilter-syntax.json"></a>

```
{
  "[BooleanCondition](#cfn-connect-metric-metricfilter-booleancondition)" : {{MetricFilterBooleanCondition}},
  "[MetricFilterKey](#cfn-connect-metric-metricfilter-metricfilterkey)" : {{String}},
  "[Negate](#cfn-connect-metric-metricfilter-negate)" : {{Boolean}},
  "[NumberCondition](#cfn-connect-metric-metricfilter-numbercondition)" : {{MetricFilterNumberCondition}},
  "[StringCondition](#cfn-connect-metric-metricfilter-stringcondition)" : {{MetricFilterStringCondition}}
}
```

### YAML
<a name="aws-properties-connect-metric-metricfilter-syntax.yaml"></a>

```
  [BooleanCondition](#cfn-connect-metric-metricfilter-booleancondition): {{
    MetricFilterBooleanCondition}}
  [MetricFilterKey](#cfn-connect-metric-metricfilter-metricfilterkey): {{String}}
  [Negate](#cfn-connect-metric-metricfilter-negate): {{Boolean}}
  [NumberCondition](#cfn-connect-metric-metricfilter-numbercondition): {{
    MetricFilterNumberCondition}}
  [StringCondition](#cfn-connect-metric-metricfilter-stringcondition): {{
    MetricFilterStringCondition}}
```

## Properties
<a name="aws-properties-connect-metric-metricfilter-properties"></a>

`BooleanCondition`  <a name="cfn-connect-metric-metricfilter-booleancondition"></a>
A boolean comparison condition.
*Required*: No
*Type*: [MetricFilterBooleanCondition](aws-properties-connect-metric-metricfilterbooleancondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricFilterKey`  <a name="cfn-connect-metric-metricfilter-metricfilterkey"></a>
The key identifying the field to filter on.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Negate`  <a name="cfn-connect-metric-metricfilter-negate"></a>
Specifies whether the filter condition is negated. When set to `true`, the filter excludes matching data instead of including it.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberCondition`  <a name="cfn-connect-metric-metricfilter-numbercondition"></a>
A numeric comparison condition.
*Required*: No
*Type*: [MetricFilterNumberCondition](aws-properties-connect-metric-metricfilternumbercondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringCondition`  <a name="cfn-connect-metric-metricfilter-stringcondition"></a>
A string comparison condition.
*Required*: No
*Type*: [MetricFilterStringCondition](aws-properties-connect-metric-metricfilterstringcondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
