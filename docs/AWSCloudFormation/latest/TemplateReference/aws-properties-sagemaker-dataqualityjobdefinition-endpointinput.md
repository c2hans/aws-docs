---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::DataQualityJobDefinition EndpointInput
<a name="aws-properties-sagemaker-dataqualityjobdefinition-endpointinput"></a>

Input object for the endpoint

## Syntax
<a name="aws-properties-sagemaker-dataqualityjobdefinition-endpointinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-dataqualityjobdefinition-endpointinput-syntax.json"></a>

```
{
  "[EndpointName](#cfn-sagemaker-dataqualityjobdefinition-endpointinput-endpointname)" : {{String}},
  "[ExcludeFeaturesAttribute](#cfn-sagemaker-dataqualityjobdefinition-endpointinput-excludefeaturesattribute)" : {{String}},
  "[LocalPath](#cfn-sagemaker-dataqualityjobdefinition-endpointinput-localpath)" : {{String}},
  "[S3DataDistributionType](#cfn-sagemaker-dataqualityjobdefinition-endpointinput-s3datadistributiontype)" : {{String}},
  "[S3InputMode](#cfn-sagemaker-dataqualityjobdefinition-endpointinput-s3inputmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-dataqualityjobdefinition-endpointinput-syntax.yaml"></a>

```
  [EndpointName](#cfn-sagemaker-dataqualityjobdefinition-endpointinput-endpointname): {{String}}
  [ExcludeFeaturesAttribute](#cfn-sagemaker-dataqualityjobdefinition-endpointinput-excludefeaturesattribute): {{String}}
  [LocalPath](#cfn-sagemaker-dataqualityjobdefinition-endpointinput-localpath): {{String}}
  [S3DataDistributionType](#cfn-sagemaker-dataqualityjobdefinition-endpointinput-s3datadistributiontype): {{String}}
  [S3InputMode](#cfn-sagemaker-dataqualityjobdefinition-endpointinput-s3inputmode): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-dataqualityjobdefinition-endpointinput-properties"></a>

`EndpointName`  <a name="cfn-sagemaker-dataqualityjobdefinition-endpointinput-endpointname"></a>
An endpoint in customer's account which has enabled `DataCaptureConfig` enabled.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExcludeFeaturesAttribute`  <a name="cfn-sagemaker-dataqualityjobdefinition-endpointinput-excludefeaturesattribute"></a>
The attributes of the input data to exclude from the analysis.
*Required*: No
*Type*: String
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LocalPath`  <a name="cfn-sagemaker-dataqualityjobdefinition-endpointinput-localpath"></a>
Path to the filesystem where the endpoint data is available to the container.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3DataDistributionType`  <a name="cfn-sagemaker-dataqualityjobdefinition-endpointinput-s3datadistributiontype"></a>
Whether input data distributed in Amazon S3 is fully replicated or sharded by an Amazon S3 key. Defaults to `FullyReplicated`
*Required*: No
*Type*: String
*Allowed values*: `FullyReplicated | ShardedByS3Key`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3InputMode`  <a name="cfn-sagemaker-dataqualityjobdefinition-endpointinput-s3inputmode"></a>
Whether the `Pipe` or `File` is used as the input mode for transferring data for the monitoring job. `Pipe` mode is recommended for large datasets. `File` mode is useful for small files that fit in memory. Defaults to `File`.
*Required*: No
*Type*: String
*Allowed values*: `Pipe | File`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
