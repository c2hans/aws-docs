---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-outputcolumnnameoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet OutputColumnNameOverride
<a name="aws-properties-quicksight-dataset-outputcolumnnameoverride"></a>

Specifies a mapping to override the name of an output column from a transform operation.

## Syntax
<a name="aws-properties-quicksight-dataset-outputcolumnnameoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-outputcolumnnameoverride-syntax.json"></a>

```
{
  "[OutputColumnName](#cfn-quicksight-dataset-outputcolumnnameoverride-outputcolumnname)" : {{String}},
  "[SourceColumnName](#cfn-quicksight-dataset-outputcolumnnameoverride-sourcecolumnname)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-outputcolumnnameoverride-syntax.yaml"></a>

```
  [OutputColumnName](#cfn-quicksight-dataset-outputcolumnnameoverride-outputcolumnname): {{String}}
  [SourceColumnName](#cfn-quicksight-dataset-outputcolumnnameoverride-sourcecolumnname): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-outputcolumnnameoverride-properties"></a>

`OutputColumnName`  <a name="cfn-quicksight-dataset-outputcolumnnameoverride-outputcolumnname"></a>
The new name to assign to the column in the output.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceColumnName`  <a name="cfn-quicksight-dataset-outputcolumnnameoverride-sourcecolumnname"></a>
The original name of the column from the source transform operation.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
