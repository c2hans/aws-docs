---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-namedentitydefinitionmetric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic NamedEntityDefinitionMetric
<a name="aws-properties-quicksight-topic-namedentitydefinitionmetric"></a>

A structure that represents a metric.

## Syntax
<a name="aws-properties-quicksight-topic-namedentitydefinitionmetric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-namedentitydefinitionmetric-syntax.json"></a>

```
{
  "[Aggregation](#cfn-quicksight-topic-namedentitydefinitionmetric-aggregation)" : {{String}},
  "[AggregationFunctionParameters](#cfn-quicksight-topic-namedentitydefinitionmetric-aggregationfunctionparameters)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-namedentitydefinitionmetric-syntax.yaml"></a>

```
  [Aggregation](#cfn-quicksight-topic-namedentitydefinitionmetric-aggregation): {{String}}
  [AggregationFunctionParameters](#cfn-quicksight-topic-namedentitydefinitionmetric-aggregationfunctionparameters): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-quicksight-topic-namedentitydefinitionmetric-properties"></a>

`Aggregation`  <a name="cfn-quicksight-topic-namedentitydefinitionmetric-aggregation"></a>
The aggregation of a named entity. Valid values for this structure are `SUM`, `MIN`, `MAX`, `COUNT`, `AVERAGE`, `DISTINCT_COUNT`, `STDEV`, `STDEVP`, `VAR`, `VARP`, `PERCENTILE`, `MEDIAN`, and `CUSTOM`.
*Required*: No
*Type*: String
*Allowed values*: `SUM | MIN | MAX | COUNT | AVERAGE | DISTINCT_COUNT | STDEV | STDEVP | VAR | VARP | PERCENTILE | MEDIAN | CUSTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AggregationFunctionParameters`  <a name="cfn-quicksight-topic-namedentitydefinitionmetric-aggregationfunctionparameters"></a>
The additional parameters for an aggregation function.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
