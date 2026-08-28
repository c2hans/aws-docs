---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-monitoringschedule-batchtransforminput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MonitoringSchedule BatchTransformInput
<a name="aws-properties-sagemaker-monitoringschedule-batchtransforminput"></a>

Input object for the batch transform job.

## Syntax
<a name="aws-properties-sagemaker-monitoringschedule-batchtransforminput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-monitoringschedule-batchtransforminput-syntax.json"></a>

```
{
  "[DataCapturedDestinationS3Uri](#cfn-sagemaker-monitoringschedule-batchtransforminput-datacaptureddestinations3uri)" : {{String}},
  "[DatasetFormat](#cfn-sagemaker-monitoringschedule-batchtransforminput-datasetformat)" : {{DatasetFormat}},
  "[ExcludeFeaturesAttribute](#cfn-sagemaker-monitoringschedule-batchtransforminput-excludefeaturesattribute)" : {{String}},
  "[LocalPath](#cfn-sagemaker-monitoringschedule-batchtransforminput-localpath)" : {{String}},
  "[S3DataDistributionType](#cfn-sagemaker-monitoringschedule-batchtransforminput-s3datadistributiontype)" : {{String}},
  "[S3InputMode](#cfn-sagemaker-monitoringschedule-batchtransforminput-s3inputmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-monitoringschedule-batchtransforminput-syntax.yaml"></a>

```
  [DataCapturedDestinationS3Uri](#cfn-sagemaker-monitoringschedule-batchtransforminput-datacaptureddestinations3uri): {{String}}
  [DatasetFormat](#cfn-sagemaker-monitoringschedule-batchtransforminput-datasetformat): {{
    DatasetFormat}}
  [ExcludeFeaturesAttribute](#cfn-sagemaker-monitoringschedule-batchtransforminput-excludefeaturesattribute): {{String}}
  [LocalPath](#cfn-sagemaker-monitoringschedule-batchtransforminput-localpath): {{String}}
  [S3DataDistributionType](#cfn-sagemaker-monitoringschedule-batchtransforminput-s3datadistributiontype): {{String}}
  [S3InputMode](#cfn-sagemaker-monitoringschedule-batchtransforminput-s3inputmode): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-monitoringschedule-batchtransforminput-properties"></a>

`DataCapturedDestinationS3Uri`  <a name="cfn-sagemaker-monitoringschedule-batchtransforminput-datacaptureddestinations3uri"></a>
The Amazon S3 location being used to capture the data.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatasetFormat`  <a name="cfn-sagemaker-monitoringschedule-batchtransforminput-datasetformat"></a>
The dataset format for your batch transform job.
*Required*: Yes
*Type*: [DatasetFormat](aws-properties-sagemaker-monitoringschedule-datasetformat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludeFeaturesAttribute`  <a name="cfn-sagemaker-monitoringschedule-batchtransforminput-excludefeaturesattribute"></a>
The attributes of the input data to exclude from the analysis.
*Required*: No
*Type*: String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalPath`  <a name="cfn-sagemaker-monitoringschedule-batchtransforminput-localpath"></a>
Path to the filesystem where the batch transform data is available to the container.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3DataDistributionType`  <a name="cfn-sagemaker-monitoringschedule-batchtransforminput-s3datadistributiontype"></a>
Whether input data distributed in Amazon S3 is fully replicated or sharded by an S3 key. Defaults to `FullyReplicated`
*Required*: No
*Type*: String
*Allowed values*: `FullyReplicated | ShardedByS3Key`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3InputMode`  <a name="cfn-sagemaker-monitoringschedule-batchtransforminput-s3inputmode"></a>
Whether the `Pipe` or `File` is used as the input mode for transferring data for the monitoring job. `Pipe` mode is recommended for large datasets. `File` mode is useful for small files that fit in memory. Defaults to `File`.
*Required*: No
*Type*: String
*Allowed values*: `Pipe | File`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
