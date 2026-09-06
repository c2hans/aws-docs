---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-trainingdataset-columnschema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::TrainingDataset ColumnSchema
<a name="aws-properties-cleanroomsml-trainingdataset-columnschema"></a>

Metadata for a column.

## Syntax
<a name="aws-properties-cleanroomsml-trainingdataset-columnschema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-trainingdataset-columnschema-syntax.json"></a>

```
{
  "[ColumnName](#cfn-cleanroomsml-trainingdataset-columnschema-columnname)" : {{String}},
  "[ColumnTypes](#cfn-cleanroomsml-trainingdataset-columnschema-columntypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-trainingdataset-columnschema-syntax.yaml"></a>

```
  [ColumnName](#cfn-cleanroomsml-trainingdataset-columnschema-columnname): {{String}}
  [ColumnTypes](#cfn-cleanroomsml-trainingdataset-columnschema-columntypes): {{
    - String}}
```

## Properties
<a name="aws-properties-cleanroomsml-trainingdataset-columnschema-properties"></a>

`ColumnName`  <a name="cfn-cleanroomsml-trainingdataset-columnschema-columnname"></a>
The name of a column.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ColumnTypes`  <a name="cfn-cleanroomsml-trainingdataset-columnschema-columntypes"></a>
The data type of column.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
