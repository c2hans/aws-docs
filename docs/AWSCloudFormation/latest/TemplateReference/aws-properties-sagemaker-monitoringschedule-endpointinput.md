---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-monitoringschedule-endpointinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MonitoringSchedule EndpointInput
<a name="aws-properties-sagemaker-monitoringschedule-endpointinput"></a>

Input object for the endpoint

## Syntax
<a name="aws-properties-sagemaker-monitoringschedule-endpointinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-monitoringschedule-endpointinput-syntax.json"></a>

```
{
  "[EndpointName](#cfn-sagemaker-monitoringschedule-endpointinput-endpointname)" : {{String}},
  "[ExcludeFeaturesAttribute](#cfn-sagemaker-monitoringschedule-endpointinput-excludefeaturesattribute)" : {{String}},
  "[LocalPath](#cfn-sagemaker-monitoringschedule-endpointinput-localpath)" : {{String}},
  "[S3DataDistributionType](#cfn-sagemaker-monitoringschedule-endpointinput-s3datadistributiontype)" : {{String}},
  "[S3InputMode](#cfn-sagemaker-monitoringschedule-endpointinput-s3inputmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-monitoringschedule-endpointinput-syntax.yaml"></a>

```
  [EndpointName](#cfn-sagemaker-monitoringschedule-endpointinput-endpointname): {{String}}
  [ExcludeFeaturesAttribute](#cfn-sagemaker-monitoringschedule-endpointinput-excludefeaturesattribute): {{String}}
  [LocalPath](#cfn-sagemaker-monitoringschedule-endpointinput-localpath): {{String}}
  [S3DataDistributionType](#cfn-sagemaker-monitoringschedule-endpointinput-s3datadistributiontype): {{String}}
  [S3InputMode](#cfn-sagemaker-monitoringschedule-endpointinput-s3inputmode): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-monitoringschedule-endpointinput-properties"></a>

`EndpointName`  <a name="cfn-sagemaker-monitoringschedule-endpointinput-endpointname"></a>
An endpoint in customer's account which has enabled `DataCaptureConfig` enabled.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludeFeaturesAttribute`  <a name="cfn-sagemaker-monitoringschedule-endpointinput-excludefeaturesattribute"></a>
The attributes of the input data to exclude from the analysis.
*Required*: No
*Type*: String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalPath`  <a name="cfn-sagemaker-monitoringschedule-endpointinput-localpath"></a>
Path to the filesystem where the endpoint data is available to the container.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3DataDistributionType`  <a name="cfn-sagemaker-monitoringschedule-endpointinput-s3datadistributiontype"></a>
Whether input data distributed in Amazon S3 is fully replicated or sharded by an Amazon S3 key. Defaults to `FullyReplicated`
*Required*: No
*Type*: String
*Allowed values*: `FullyReplicated | ShardedByS3Key`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3InputMode`  <a name="cfn-sagemaker-monitoringschedule-endpointinput-s3inputmode"></a>
Whether the `Pipe` or `File` is used as the input mode for transferring data for the monitoring job. `Pipe` mode is recommended for large datasets. `File` mode is useful for small files that fit in memory. Defaults to `File`.
*Required*: No
*Type*: String
*Allowed values*: `Pipe | File`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
