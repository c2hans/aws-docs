---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-trainingdataset-dataset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::TrainingDataset Dataset
<a name="aws-properties-cleanroomsml-trainingdataset-dataset"></a>

Defines where the training dataset is located, what type of data it contains, and how to access the data.

## Syntax
<a name="aws-properties-cleanroomsml-trainingdataset-dataset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-trainingdataset-dataset-syntax.json"></a>

```
{
  "[InputConfig](#cfn-cleanroomsml-trainingdataset-dataset-inputconfig)" : {{DatasetInputConfig}},
  "[Type](#cfn-cleanroomsml-trainingdataset-dataset-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-trainingdataset-dataset-syntax.yaml"></a>

```
  [InputConfig](#cfn-cleanroomsml-trainingdataset-dataset-inputconfig): {{
    DatasetInputConfig}}
  [Type](#cfn-cleanroomsml-trainingdataset-dataset-type): {{String}}
```

## Properties
<a name="aws-properties-cleanroomsml-trainingdataset-dataset-properties"></a>

`InputConfig`  <a name="cfn-cleanroomsml-trainingdataset-dataset-inputconfig"></a>
A DatasetInputConfig object that defines the data source and schema mapping.
*Required*: Yes
*Type*: [DatasetInputConfig](aws-properties-cleanroomsml-trainingdataset-datasetinputconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-cleanroomsml-trainingdataset-dataset-type"></a>
What type of information is found in the dataset.
*Required*: Yes
*Type*: String
*Allowed values*: `INTERACTIONS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
