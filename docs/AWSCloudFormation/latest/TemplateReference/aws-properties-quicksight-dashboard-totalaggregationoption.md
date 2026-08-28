---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-totalaggregationoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TotalAggregationOption
<a name="aws-properties-quicksight-dashboard-totalaggregationoption"></a>

The total aggregation settings map of a field id.

## Syntax
<a name="aws-properties-quicksight-dashboard-totalaggregationoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-totalaggregationoption-syntax.json"></a>

```
{
  "[FieldId](#cfn-quicksight-dashboard-totalaggregationoption-fieldid)" : {{String}},
  "[TotalAggregationFunction](#cfn-quicksight-dashboard-totalaggregationoption-totalaggregationfunction)" : {{TotalAggregationFunction}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-totalaggregationoption-syntax.yaml"></a>

```
  [FieldId](#cfn-quicksight-dashboard-totalaggregationoption-fieldid): {{String}}
  [TotalAggregationFunction](#cfn-quicksight-dashboard-totalaggregationoption-totalaggregationfunction): {{
    TotalAggregationFunction}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-totalaggregationoption-properties"></a>

`FieldId`  <a name="cfn-quicksight-dashboard-totalaggregationoption-fieldid"></a>
The field id that's associated with the total aggregation option.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalAggregationFunction`  <a name="cfn-quicksight-dashboard-totalaggregationoption-totalaggregationfunction"></a>
The total aggregation function that you want to set for a specified field id.
*Required*: Yes
*Type*: [TotalAggregationFunction](aws-properties-quicksight-dashboard-totalaggregationfunction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
