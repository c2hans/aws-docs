---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelbiasjobdefinition-datasetformat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelBiasJobDefinition DatasetFormat
<a name="aws-properties-sagemaker-modelbiasjobdefinition-datasetformat"></a>

The format of the dataset used for the model bias monitoring job.

## Syntax
<a name="aws-properties-sagemaker-modelbiasjobdefinition-datasetformat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelbiasjobdefinition-datasetformat-syntax.json"></a>

```
{
  "[Csv](#cfn-sagemaker-modelbiasjobdefinition-datasetformat-csv)" : {{Csv}},
  "[Json](#cfn-sagemaker-modelbiasjobdefinition-datasetformat-json)" : {{Json}},
  "[Parquet](#cfn-sagemaker-modelbiasjobdefinition-datasetformat-parquet)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelbiasjobdefinition-datasetformat-syntax.yaml"></a>

```
  [Csv](#cfn-sagemaker-modelbiasjobdefinition-datasetformat-csv): {{
    Csv}}
  [Json](#cfn-sagemaker-modelbiasjobdefinition-datasetformat-json): {{
    Json}}
  [Parquet](#cfn-sagemaker-modelbiasjobdefinition-datasetformat-parquet): {{Boolean}}
```

## Properties
<a name="aws-properties-sagemaker-modelbiasjobdefinition-datasetformat-properties"></a>

`Csv`  <a name="cfn-sagemaker-modelbiasjobdefinition-datasetformat-csv"></a>
The CSV format configuration for the dataset.
*Required*: No
*Type*: [Csv](aws-properties-sagemaker-modelbiasjobdefinition-csv.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Json`  <a name="cfn-sagemaker-modelbiasjobdefinition-datasetformat-json"></a>
The JSON format configuration for the dataset.
*Required*: No
*Type*: [Json](aws-properties-sagemaker-modelbiasjobdefinition-json.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Parquet`  <a name="cfn-sagemaker-modelbiasjobdefinition-datasetformat-parquet"></a>
Indicates that the dataset is in Parquet format.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
