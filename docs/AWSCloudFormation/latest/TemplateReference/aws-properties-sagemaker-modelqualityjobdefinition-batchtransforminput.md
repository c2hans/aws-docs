---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelQualityJobDefinition BatchTransformInput
<a name="aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput"></a>

Input object for the batch transform job.

## Syntax
<a name="aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput-syntax.json"></a>

```
{
  "[DataCapturedDestinationS3Uri](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-datacaptureddestinations3uri)" : {{String}},
  "[DatasetFormat](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-datasetformat)" : {{DatasetFormat}},
  "[EndTimeOffset](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-endtimeoffset)" : {{String}},
  "[InferenceAttribute](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-inferenceattribute)" : {{String}},
  "[LocalPath](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-localpath)" : {{String}},
  "[ProbabilityAttribute](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-probabilityattribute)" : {{String}},
  "[ProbabilityThresholdAttribute](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-probabilitythresholdattribute)" : {{Number}},
  "[S3DataDistributionType](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-s3datadistributiontype)" : {{String}},
  "[S3InputMode](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-s3inputmode)" : {{String}},
  "[StartTimeOffset](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-starttimeoffset)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput-syntax.yaml"></a>

```
  [DataCapturedDestinationS3Uri](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-datacaptureddestinations3uri): {{String}}
  [DatasetFormat](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-datasetformat): {{
    DatasetFormat}}
  [EndTimeOffset](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-endtimeoffset): {{String}}
  [InferenceAttribute](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-inferenceattribute): {{String}}
  [LocalPath](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-localpath): {{String}}
  [ProbabilityAttribute](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-probabilityattribute): {{String}}
  [ProbabilityThresholdAttribute](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-probabilitythresholdattribute): {{Number}}
  [S3DataDistributionType](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-s3datadistributiontype): {{String}}
  [S3InputMode](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-s3inputmode): {{String}}
  [StartTimeOffset](#cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-starttimeoffset): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput-properties"></a>

`DataCapturedDestinationS3Uri`  <a name="cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-datacaptureddestinations3uri"></a>
The Amazon S3 location being used to capture the data.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatasetFormat`  <a name="cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-datasetformat"></a>
The dataset format for your batch transform job.
*Required*: Yes
*Type*: [DatasetFormat](aws-properties-sagemaker-modelqualityjobdefinition-datasetformat.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndTimeOffset`  <a name="cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-endtimeoffset"></a>
If specified, monitoring jobs subtract this time from the end time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html).
*Required*: No
*Type*: String
*Pattern*: `^.?P.*`
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InferenceAttribute`  <a name="cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-inferenceattribute"></a>
The attribute of the input data that represents the ground truth label.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LocalPath`  <a name="cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-localpath"></a>
Path to the filesystem where the batch transform data is available to the container.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProbabilityAttribute`  <a name="cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-probabilityattribute"></a>
In a classification problem, the attribute that represents the class probability.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProbabilityThresholdAttribute`  <a name="cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-probabilitythresholdattribute"></a>
The threshold for the class probability to be evaluated as a positive result.
*Required*: No
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3DataDistributionType`  <a name="cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-s3datadistributiontype"></a>
Whether input data distributed in Amazon S3 is fully replicated or sharded by an S3 key. Defaults to `FullyReplicated`
*Required*: No
*Type*: String
*Allowed values*: `FullyReplicated | ShardedByS3Key`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3InputMode`  <a name="cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-s3inputmode"></a>
Whether the `Pipe` or `File` is used as the input mode for transferring data for the monitoring job. `Pipe` mode is recommended for large datasets. `File` mode is useful for small files that fit in memory. Defaults to `File`.
*Required*: No
*Type*: String
*Allowed values*: `Pipe | File`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StartTimeOffset`  <a name="cfn-sagemaker-modelqualityjobdefinition-batchtransforminput-starttimeoffset"></a>
If specified, monitoring jobs substract this time from the start time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html).
*Required*: No
*Type*: String
*Pattern*: `^.?P.*`
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
