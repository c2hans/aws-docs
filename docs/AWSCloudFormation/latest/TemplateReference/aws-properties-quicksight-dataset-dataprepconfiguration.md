---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-dataprepconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataPrepConfiguration
<a name="aws-properties-quicksight-dataset-dataprepconfiguration"></a>

Configuration for data preparation operations, defining the complete pipeline from source tables through transformations to destination tables.

## Syntax
<a name="aws-properties-quicksight-dataset-dataprepconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-dataprepconfiguration-syntax.json"></a>

```
{
  "[DestinationTableMap](#cfn-quicksight-dataset-dataprepconfiguration-destinationtablemap)" : {{{{{Key}}: {{Value}}, ...}}},
  "[SourceTableMap](#cfn-quicksight-dataset-dataprepconfiguration-sourcetablemap)" : {{{{{Key}}: {{Value}}, ...}}},
  "[TransformStepMap](#cfn-quicksight-dataset-dataprepconfiguration-transformstepmap)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-dataprepconfiguration-syntax.yaml"></a>

```
  [DestinationTableMap](#cfn-quicksight-dataset-dataprepconfiguration-destinationtablemap): {{
    {{Key}}: {{Value}}}}
  [SourceTableMap](#cfn-quicksight-dataset-dataprepconfiguration-sourcetablemap): {{
    {{Key}}: {{Value}}}}
  [TransformStepMap](#cfn-quicksight-dataset-dataprepconfiguration-transformstepmap): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-quicksight-dataset-dataprepconfiguration-properties"></a>

`DestinationTableMap`  <a name="cfn-quicksight-dataset-dataprepconfiguration-destinationtablemap"></a>
A map of destination tables that receive the final prepared data.
*Required*: Yes
*Type*: Object of [DestinationTable](aws-properties-quicksight-dataset-destinationtable.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceTableMap`  <a name="cfn-quicksight-dataset-dataprepconfiguration-sourcetablemap"></a>
A map of source tables that provide information about underlying sources.
*Required*: Yes
*Type*: Object of [SourceTable](aws-properties-quicksight-dataset-sourcetable.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransformStepMap`  <a name="cfn-quicksight-dataset-dataprepconfiguration-transformstepmap"></a>
A map of transformation steps that process the data.
*Required*: Yes
*Type*: Object of [TransformStep](aws-properties-quicksight-dataset-transformstep.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
