---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-topicnumericrangefilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic TopicNumericRangeFilter
<a name="aws-properties-quicksight-topic-topicnumericrangefilter"></a>

A filter that filters topics based on the value of a numeric field. The filter includes only topics whose numeric field value falls within the specified range.

## Syntax
<a name="aws-properties-quicksight-topic-topicnumericrangefilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-topicnumericrangefilter-syntax.json"></a>

```
{
  "[Aggregation](#cfn-quicksight-topic-topicnumericrangefilter-aggregation)" : {{String}},
  "[Constant](#cfn-quicksight-topic-topicnumericrangefilter-constant)" : {{TopicRangeFilterConstant}},
  "[Inclusive](#cfn-quicksight-topic-topicnumericrangefilter-inclusive)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-topicnumericrangefilter-syntax.yaml"></a>

```
  [Aggregation](#cfn-quicksight-topic-topicnumericrangefilter-aggregation): {{String}}
  [Constant](#cfn-quicksight-topic-topicnumericrangefilter-constant): {{
    TopicRangeFilterConstant}}
  [Inclusive](#cfn-quicksight-topic-topicnumericrangefilter-inclusive): {{Boolean}}
```

## Properties
<a name="aws-properties-quicksight-topic-topicnumericrangefilter-properties"></a>

`Aggregation`  <a name="cfn-quicksight-topic-topicnumericrangefilter-aggregation"></a>
An aggregation function that specifies how to calculate the value of a numeric field for a topic, Valid values for this structure are `NO_AGGREGATION`, `SUM`, `AVERAGE`, `COUNT`, `DISTINCT_COUNT`, `MAX`, `MEDIAN`, `MIN`, `STDEV`, `STDEVP`, `VAR`, and `VARP`.
*Required*: No
*Type*: String
*Allowed values*: `NO_AGGREGATION | SUM | AVERAGE | COUNT | DISTINCT_COUNT | MAX | MEDIAN | MIN | STDEV | STDEVP | VAR | VARP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Constant`  <a name="cfn-quicksight-topic-topicnumericrangefilter-constant"></a>
The constant used in a numeric range filter.
*Required*: No
*Type*: [TopicRangeFilterConstant](aws-properties-quicksight-topic-topicrangefilterconstant.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Inclusive`  <a name="cfn-quicksight-topic-topicnumericrangefilter-inclusive"></a>
A Boolean value that indicates whether the endpoints of the numeric range are included in the filter. If set to true, topics whose numeric field value is equal to the endpoint values will be included in the filter. If set to false, topics whose numeric field value is equal to the endpoint values will be excluded from the filter.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
