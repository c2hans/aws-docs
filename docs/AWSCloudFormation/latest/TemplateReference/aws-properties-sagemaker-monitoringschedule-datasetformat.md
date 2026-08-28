---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-monitoringschedule-datasetformat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MonitoringSchedule DatasetFormat
<a name="aws-properties-sagemaker-monitoringschedule-datasetformat"></a>

The format of the dataset used for the monitoring schedule.

## Syntax
<a name="aws-properties-sagemaker-monitoringschedule-datasetformat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-monitoringschedule-datasetformat-syntax.json"></a>

```
{
  "[Csv](#cfn-sagemaker-monitoringschedule-datasetformat-csv)" : {{Csv}},
  "[Json](#cfn-sagemaker-monitoringschedule-datasetformat-json)" : {{Json}},
  "[Parquet](#cfn-sagemaker-monitoringschedule-datasetformat-parquet)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-sagemaker-monitoringschedule-datasetformat-syntax.yaml"></a>

```
  [Csv](#cfn-sagemaker-monitoringschedule-datasetformat-csv): {{
    Csv}}
  [Json](#cfn-sagemaker-monitoringschedule-datasetformat-json): {{
    Json}}
  [Parquet](#cfn-sagemaker-monitoringschedule-datasetformat-parquet): {{Boolean}}
```

## Properties
<a name="aws-properties-sagemaker-monitoringschedule-datasetformat-properties"></a>

`Csv`  <a name="cfn-sagemaker-monitoringschedule-datasetformat-csv"></a>
The CSV format configuration for the dataset.
*Required*: No
*Type*: [Csv](aws-properties-sagemaker-monitoringschedule-csv.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Json`  <a name="cfn-sagemaker-monitoringschedule-datasetformat-json"></a>
The JSON format configuration for the dataset.
*Required*: No
*Type*: [Json](aws-properties-sagemaker-monitoringschedule-json.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parquet`  <a name="cfn-sagemaker-monitoringschedule-datasetformat-parquet"></a>
Indicates that the dataset is in Parquet format.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
