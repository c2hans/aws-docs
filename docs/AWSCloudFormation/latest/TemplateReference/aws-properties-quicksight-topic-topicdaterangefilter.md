---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-topicdaterangefilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic TopicDateRangeFilter
<a name="aws-properties-quicksight-topic-topicdaterangefilter"></a>

A filter used to restrict data based on a range of dates or times.

## Syntax
<a name="aws-properties-quicksight-topic-topicdaterangefilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-topicdaterangefilter-syntax.json"></a>

```
{
  "[Constant](#cfn-quicksight-topic-topicdaterangefilter-constant)" : {{TopicRangeFilterConstant}},
  "[Inclusive](#cfn-quicksight-topic-topicdaterangefilter-inclusive)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-topicdaterangefilter-syntax.yaml"></a>

```
  [Constant](#cfn-quicksight-topic-topicdaterangefilter-constant): {{
    TopicRangeFilterConstant}}
  [Inclusive](#cfn-quicksight-topic-topicdaterangefilter-inclusive): {{Boolean}}
```

## Properties
<a name="aws-properties-quicksight-topic-topicdaterangefilter-properties"></a>

`Constant`  <a name="cfn-quicksight-topic-topicdaterangefilter-constant"></a>
The constant used in a date range filter.
*Required*: No
*Type*: [TopicRangeFilterConstant](aws-properties-quicksight-topic-topicrangefilterconstant.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Inclusive`  <a name="cfn-quicksight-topic-topicdaterangefilter-inclusive"></a>
A Boolean value that indicates whether the date range filter should include the boundary values. If set to true, the filter includes the start and end dates. If set to false, the filter excludes them.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
