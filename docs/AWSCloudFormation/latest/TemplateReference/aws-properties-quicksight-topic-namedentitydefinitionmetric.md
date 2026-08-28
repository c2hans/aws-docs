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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
