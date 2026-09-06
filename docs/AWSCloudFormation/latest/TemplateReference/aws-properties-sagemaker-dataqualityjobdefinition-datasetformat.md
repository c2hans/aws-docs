---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-dataqualityjobdefinition-datasetformat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::DataQualityJobDefinition DatasetFormat
<a name="aws-properties-sagemaker-dataqualityjobdefinition-datasetformat"></a>

The format of the dataset used for the data quality monitoring job.

## Syntax
<a name="aws-properties-sagemaker-dataqualityjobdefinition-datasetformat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-dataqualityjobdefinition-datasetformat-syntax.json"></a>

```
{
  "[Csv](#cfn-sagemaker-dataqualityjobdefinition-datasetformat-csv)" : {{Csv}},
  "[Json](#cfn-sagemaker-dataqualityjobdefinition-datasetformat-json)" : {{Json}},
  "[Parquet](#cfn-sagemaker-dataqualityjobdefinition-datasetformat-parquet)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-sagemaker-dataqualityjobdefinition-datasetformat-syntax.yaml"></a>

```
  [Csv](#cfn-sagemaker-dataqualityjobdefinition-datasetformat-csv): {{
    Csv}}
  [Json](#cfn-sagemaker-dataqualityjobdefinition-datasetformat-json): {{
    Json}}
  [Parquet](#cfn-sagemaker-dataqualityjobdefinition-datasetformat-parquet): {{Boolean}}
```

## Properties
<a name="aws-properties-sagemaker-dataqualityjobdefinition-datasetformat-properties"></a>

`Csv`  <a name="cfn-sagemaker-dataqualityjobdefinition-datasetformat-csv"></a>
The CSV format configuration for the dataset.
*Required*: No
*Type*: [Csv](aws-properties-sagemaker-dataqualityjobdefinition-csv.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Json`  <a name="cfn-sagemaker-dataqualityjobdefinition-datasetformat-json"></a>
The JSON format configuration for the dataset.
*Required*: No
*Type*: [Json](aws-properties-sagemaker-dataqualityjobdefinition-json.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Parquet`  <a name="cfn-sagemaker-dataqualityjobdefinition-datasetformat-parquet"></a>
Indicates that the dataset is in Parquet format.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
