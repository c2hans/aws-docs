---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datapreppercentileaggregationfunction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataPrepPercentileAggregationFunction
<a name="aws-properties-quicksight-dataset-datapreppercentileaggregationfunction"></a>

<a name="aws-properties-quicksight-dataset-datapreppercentileaggregationfunction-description"></a>The `DataPrepPercentileAggregationFunction` property type specifies Property description not available. for an [AWS::QuickSight::DataSet](aws-resource-quicksight-dataset.md).

## Syntax
<a name="aws-properties-quicksight-dataset-datapreppercentileaggregationfunction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datapreppercentileaggregationfunction-syntax.json"></a>

```
{
  "[InputColumnName](#cfn-quicksight-dataset-datapreppercentileaggregationfunction-inputcolumnname)" : {{String}},
  "[PercentileValue](#cfn-quicksight-dataset-datapreppercentileaggregationfunction-percentilevalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datapreppercentileaggregationfunction-syntax.yaml"></a>

```
  [InputColumnName](#cfn-quicksight-dataset-datapreppercentileaggregationfunction-inputcolumnname): {{String}}
  [PercentileValue](#cfn-quicksight-dataset-datapreppercentileaggregationfunction-percentilevalue): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datapreppercentileaggregationfunction-properties"></a>

`InputColumnName`  <a name="cfn-quicksight-dataset-datapreppercentileaggregationfunction-inputcolumnname"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PercentileValue`  <a name="cfn-quicksight-dataset-datapreppercentileaggregationfunction-percentilevalue"></a>
Property description not available.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
