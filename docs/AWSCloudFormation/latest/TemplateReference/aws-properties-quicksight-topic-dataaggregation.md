---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-dataaggregation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic DataAggregation
<a name="aws-properties-quicksight-topic-dataaggregation"></a>

The definition of a data aggregation.

## Syntax
<a name="aws-properties-quicksight-topic-dataaggregation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-dataaggregation-syntax.json"></a>

```
{
  "[DatasetRowDateGranularity](#cfn-quicksight-topic-dataaggregation-datasetrowdategranularity)" : {{String}},
  "[DefaultDateColumnName](#cfn-quicksight-topic-dataaggregation-defaultdatecolumnname)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-dataaggregation-syntax.yaml"></a>

```
  [DatasetRowDateGranularity](#cfn-quicksight-topic-dataaggregation-datasetrowdategranularity): {{String}}
  [DefaultDateColumnName](#cfn-quicksight-topic-dataaggregation-defaultdatecolumnname): {{String}}
```

## Properties
<a name="aws-properties-quicksight-topic-dataaggregation-properties"></a>

`DatasetRowDateGranularity`  <a name="cfn-quicksight-topic-dataaggregation-datasetrowdategranularity"></a>
The level of time precision that is used to aggregate `DateTime` values.
*Required*: No
*Type*: String
*Allowed values*: `SECOND | MINUTE | HOUR | DAY | WEEK | MONTH | QUARTER | YEAR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultDateColumnName`  <a name="cfn-quicksight-topic-dataaggregation-defaultdatecolumnname"></a>
The column name for the default date.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
