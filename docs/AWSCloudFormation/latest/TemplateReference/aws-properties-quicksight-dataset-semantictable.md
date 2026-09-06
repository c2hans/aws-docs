---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-semantictable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet SemanticTable
<a name="aws-properties-quicksight-dataset-semantictable"></a>

A semantic table that represents the final analytical structure of the data.

## Syntax
<a name="aws-properties-quicksight-dataset-semantictable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-semantictable-syntax.json"></a>

```
{
  "[Alias](#cfn-quicksight-dataset-semantictable-alias)" : {{String}},
  "[DestinationTableId](#cfn-quicksight-dataset-semantictable-destinationtableid)" : {{String}},
  "[RowLevelPermissionConfiguration](#cfn-quicksight-dataset-semantictable-rowlevelpermissionconfiguration)" : {{RowLevelPermissionConfiguration}},
  "[SemanticMetadata](#cfn-quicksight-dataset-semantictable-semanticmetadata)" : {{TableSemanticMetadata}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-semantictable-syntax.yaml"></a>

```
  [Alias](#cfn-quicksight-dataset-semantictable-alias): {{String}}
  [DestinationTableId](#cfn-quicksight-dataset-semantictable-destinationtableid): {{String}}
  [RowLevelPermissionConfiguration](#cfn-quicksight-dataset-semantictable-rowlevelpermissionconfiguration): {{
    RowLevelPermissionConfiguration}}
  [SemanticMetadata](#cfn-quicksight-dataset-semantictable-semanticmetadata): {{
    TableSemanticMetadata}}
```

## Properties
<a name="aws-properties-quicksight-dataset-semantictable-properties"></a>

`Alias`  <a name="cfn-quicksight-dataset-semantictable-alias"></a>
Alias for the semantic table.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationTableId`  <a name="cfn-quicksight-dataset-semantictable-destinationtableid"></a>
The identifier of the destination table from data preparation that provides data to this semantic table.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z-]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RowLevelPermissionConfiguration`  <a name="cfn-quicksight-dataset-semantictable-rowlevelpermissionconfiguration"></a>
Configuration for row level security that control data access for this semantic table.
*Required*: No
*Type*: [RowLevelPermissionConfiguration](aws-properties-quicksight-dataset-rowlevelpermissionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SemanticMetadata`  <a name="cfn-quicksight-dataset-semantictable-semanticmetadata"></a>
The column-level semantic metadata for this semantic table.
*Required*: No
*Type*: [TableSemanticMetadata](aws-properties-quicksight-dataset-tablesemanticmetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
