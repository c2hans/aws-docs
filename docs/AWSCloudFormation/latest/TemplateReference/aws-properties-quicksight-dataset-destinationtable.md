---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-destinationtable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DestinationTable
<a name="aws-properties-quicksight-dataset-destinationtable"></a>

Defines a destination table in data preparation that receives the final transformed data.

## Syntax
<a name="aws-properties-quicksight-dataset-destinationtable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-destinationtable-syntax.json"></a>

```
{
  "[Alias](#cfn-quicksight-dataset-destinationtable-alias)" : {{String}},
  "[Source](#cfn-quicksight-dataset-destinationtable-source)" : {{DestinationTableSource}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-destinationtable-syntax.yaml"></a>

```
  [Alias](#cfn-quicksight-dataset-destinationtable-alias): {{String}}
  [Source](#cfn-quicksight-dataset-destinationtable-source): {{
    DestinationTableSource}}
```

## Properties
<a name="aws-properties-quicksight-dataset-destinationtable-properties"></a>

`Alias`  <a name="cfn-quicksight-dataset-destinationtable-alias"></a>
Alias for the destination table.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-dataset-destinationtable-source"></a>
The source configuration that specifies which transform operation provides data to this destination table.
*Required*: Yes
*Type*: [DestinationTableSource](aws-properties-quicksight-dataset-destinationtablesource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
