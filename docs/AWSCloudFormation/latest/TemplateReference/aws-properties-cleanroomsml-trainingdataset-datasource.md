---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-trainingdataset-datasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::TrainingDataset DataSource
<a name="aws-properties-cleanroomsml-trainingdataset-datasource"></a>

Defines information about the Glue data source that contains the training data.

## Syntax
<a name="aws-properties-cleanroomsml-trainingdataset-datasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-trainingdataset-datasource-syntax.json"></a>

```
{
  "[GlueDataSource](#cfn-cleanroomsml-trainingdataset-datasource-gluedatasource)" : {{GlueDataSource}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-trainingdataset-datasource-syntax.yaml"></a>

```
  [GlueDataSource](#cfn-cleanroomsml-trainingdataset-datasource-gluedatasource): {{
    GlueDataSource}}
```

## Properties
<a name="aws-properties-cleanroomsml-trainingdataset-datasource-properties"></a>

`GlueDataSource`  <a name="cfn-cleanroomsml-trainingdataset-datasource-gluedatasource"></a>
A GlueDataSource object that defines the catalog ID, database name, and table name for the training data.
*Required*: Yes
*Type*: [GlueDataSource](aws-properties-cleanroomsml-trainingdataset-gluedatasource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
