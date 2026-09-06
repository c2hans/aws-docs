---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-trainingdataset-datasetinputconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::TrainingDataset DatasetInputConfig
<a name="aws-properties-cleanroomsml-trainingdataset-datasetinputconfig"></a>

Defines the Glue data source and schema mapping information.

## Syntax
<a name="aws-properties-cleanroomsml-trainingdataset-datasetinputconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-trainingdataset-datasetinputconfig-syntax.json"></a>

```
{
  "[DataSource](#cfn-cleanroomsml-trainingdataset-datasetinputconfig-datasource)" : {{DataSource}},
  "[Schema](#cfn-cleanroomsml-trainingdataset-datasetinputconfig-schema)" : {{[ ColumnSchema, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-trainingdataset-datasetinputconfig-syntax.yaml"></a>

```
  [DataSource](#cfn-cleanroomsml-trainingdataset-datasetinputconfig-datasource): {{
    DataSource}}
  [Schema](#cfn-cleanroomsml-trainingdataset-datasetinputconfig-schema): {{
    - ColumnSchema}}
```

## Properties
<a name="aws-properties-cleanroomsml-trainingdataset-datasetinputconfig-properties"></a>

`DataSource`  <a name="cfn-cleanroomsml-trainingdataset-datasetinputconfig-datasource"></a>
A DataSource object that specifies the Glue data source for the training data.
*Required*: Yes
*Type*: [DataSource](aws-properties-cleanroomsml-trainingdataset-datasource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Schema`  <a name="cfn-cleanroomsml-trainingdataset-datasetinputconfig-schema"></a>
The schema information for the training data.
*Required*: Yes
*Type*: Array of [ColumnSchema](aws-properties-cleanroomsml-trainingdataset-columnschema.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
