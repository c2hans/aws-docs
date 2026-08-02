---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-tablesemanticmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet TableSemanticMetadata
<a name="aws-properties-quicksight-dataset-tablesemanticmetadata"></a>

Column-level semantic metadata for a semantic table.

## Syntax
<a name="aws-properties-quicksight-dataset-tablesemanticmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-tablesemanticmetadata-syntax.json"></a>

```
{
  "[ColumnMetadata](#cfn-quicksight-dataset-tablesemanticmetadata-columnmetadata)" : {{[ SharedColumnSemanticMetadata, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-tablesemanticmetadata-syntax.yaml"></a>

```
  [ColumnMetadata](#cfn-quicksight-dataset-tablesemanticmetadata-columnmetadata): {{
    - SharedColumnSemanticMetadata}}
```

## Properties
<a name="aws-properties-quicksight-dataset-tablesemanticmetadata-properties"></a>

`ColumnMetadata`  <a name="cfn-quicksight-dataset-tablesemanticmetadata-columnmetadata"></a>
A list of column semantic metadata entries.
*Required*: No
*Type*: Array of [SharedColumnSemanticMetadata](aws-properties-quicksight-dataset-sharedcolumnsemanticmetadata.md)
*Minimum*: `1`
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
