---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-topiccategoryfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic TopicCategoryFilter
<a name="aws-properties-quicksight-topic-topiccategoryfilter"></a>

A structure that represents a category filter.

## Syntax
<a name="aws-properties-quicksight-topic-topiccategoryfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-topiccategoryfilter-syntax.json"></a>

```
{
  "[CategoryFilterFunction](#cfn-quicksight-topic-topiccategoryfilter-categoryfilterfunction)" : {{String}},
  "[CategoryFilterType](#cfn-quicksight-topic-topiccategoryfilter-categoryfiltertype)" : {{String}},
  "[Constant](#cfn-quicksight-topic-topiccategoryfilter-constant)" : {{TopicCategoryFilterConstant}},
  "[Inverse](#cfn-quicksight-topic-topiccategoryfilter-inverse)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-topiccategoryfilter-syntax.yaml"></a>

```
  [CategoryFilterFunction](#cfn-quicksight-topic-topiccategoryfilter-categoryfilterfunction): {{String}}
  [CategoryFilterType](#cfn-quicksight-topic-topiccategoryfilter-categoryfiltertype): {{String}}
  [Constant](#cfn-quicksight-topic-topiccategoryfilter-constant): {{
    TopicCategoryFilterConstant}}
  [Inverse](#cfn-quicksight-topic-topiccategoryfilter-inverse): {{Boolean}}
```

## Properties
<a name="aws-properties-quicksight-topic-topiccategoryfilter-properties"></a>

`CategoryFilterFunction`  <a name="cfn-quicksight-topic-topiccategoryfilter-categoryfilterfunction"></a>
The category filter function. Valid values for this structure are `EXACT` and `CONTAINS`.
*Required*: No
*Type*: String
*Allowed values*: `EXACT | CONTAINS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CategoryFilterType`  <a name="cfn-quicksight-topic-topiccategoryfilter-categoryfiltertype"></a>
The category filter type. This element is used to specify whether a filter is a simple category filter or an inverse category filter.
*Required*: No
*Type*: String
*Allowed values*: `CUSTOM_FILTER | CUSTOM_FILTER_LIST | FILTER_LIST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Constant`  <a name="cfn-quicksight-topic-topiccategoryfilter-constant"></a>
The constant used in a category filter.
*Required*: No
*Type*: [TopicCategoryFilterConstant](aws-properties-quicksight-topic-topiccategoryfilterconstant.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Inverse`  <a name="cfn-quicksight-topic-topiccategoryfilter-inverse"></a>
A Boolean value that indicates if the filter is inverse.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
