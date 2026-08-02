---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datapreplistaggregationfunction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataPrepListAggregationFunction
<a name="aws-properties-quicksight-dataset-datapreplistaggregationfunction"></a>

An aggregation function that concatenates values from multiple rows into a single string with a specified separator.

## Syntax
<a name="aws-properties-quicksight-dataset-datapreplistaggregationfunction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datapreplistaggregationfunction-syntax.json"></a>

```
{
  "[Distinct](#cfn-quicksight-dataset-datapreplistaggregationfunction-distinct)" : {{Boolean}},
  "[InputColumnName](#cfn-quicksight-dataset-datapreplistaggregationfunction-inputcolumnname)" : {{String}},
  "[Separator](#cfn-quicksight-dataset-datapreplistaggregationfunction-separator)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datapreplistaggregationfunction-syntax.yaml"></a>

```
  [Distinct](#cfn-quicksight-dataset-datapreplistaggregationfunction-distinct): {{Boolean}}
  [InputColumnName](#cfn-quicksight-dataset-datapreplistaggregationfunction-inputcolumnname): {{String}}
  [Separator](#cfn-quicksight-dataset-datapreplistaggregationfunction-separator): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datapreplistaggregationfunction-properties"></a>

`Distinct`  <a name="cfn-quicksight-dataset-datapreplistaggregationfunction-distinct"></a>
Whether to include only distinct values in the concatenated result, removing duplicates.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputColumnName`  <a name="cfn-quicksight-dataset-datapreplistaggregationfunction-inputcolumnname"></a>
The name of the column containing values to be concatenated.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Separator`  <a name="cfn-quicksight-dataset-datapreplistaggregationfunction-separator"></a>
The string used to separate values in the concatenated result.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
