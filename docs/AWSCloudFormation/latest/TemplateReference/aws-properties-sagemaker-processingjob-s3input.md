---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-processingjob-s3input.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ProcessingJob S3Input
<a name="aws-properties-sagemaker-processingjob-s3input"></a>

Configuration for downloading input data from Amazon S3 into the processing container.

## Syntax
<a name="aws-properties-sagemaker-processingjob-s3input-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-processingjob-s3input-syntax.json"></a>

```
{
  "[LocalPath](#cfn-sagemaker-processingjob-s3input-localpath)" : {{String}},
  "[S3CompressionType](#cfn-sagemaker-processingjob-s3input-s3compressiontype)" : {{String}},
  "[S3DataDistributionType](#cfn-sagemaker-processingjob-s3input-s3datadistributiontype)" : {{String}},
  "[S3DataType](#cfn-sagemaker-processingjob-s3input-s3datatype)" : {{String}},
  "[S3InputMode](#cfn-sagemaker-processingjob-s3input-s3inputmode)" : {{String}},
  "[S3Uri](#cfn-sagemaker-processingjob-s3input-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-processingjob-s3input-syntax.yaml"></a>

```
  [LocalPath](#cfn-sagemaker-processingjob-s3input-localpath): {{String}}
  [S3CompressionType](#cfn-sagemaker-processingjob-s3input-s3compressiontype): {{String}}
  [S3DataDistributionType](#cfn-sagemaker-processingjob-s3input-s3datadistributiontype): {{String}}
  [S3DataType](#cfn-sagemaker-processingjob-s3input-s3datatype): {{String}}
  [S3InputMode](#cfn-sagemaker-processingjob-s3input-s3inputmode): {{String}}
  [S3Uri](#cfn-sagemaker-processingjob-s3input-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-processingjob-s3input-properties"></a>

`LocalPath`  <a name="cfn-sagemaker-processingjob-s3input-localpath"></a>
The local path in your container where you want Amazon SageMaker to write input data to. `LocalPath` is an absolute path to the input data and must begin with `/opt/ml/processing/`. `LocalPath` is a required parameter when `AppManaged` is `False` (default).
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3CompressionType`  <a name="cfn-sagemaker-processingjob-s3input-s3compressiontype"></a>
Whether to GZIP-decompress the data in Amazon S3 as it is streamed into the processing container. `Gzip` can only be used when `Pipe` mode is specified as the `S3InputMode`. In `Pipe` mode, Amazon SageMaker streams input data from the source directly to your container without using the EBS volume.
*Required*: No
*Type*: String
*Allowed values*: `None | Gzip`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3DataDistributionType`  <a name="cfn-sagemaker-processingjob-s3input-s3datadistributiontype"></a>
Whether to distribute the data from Amazon S3 to all processing instances with `FullyReplicated`, or whether the data from Amazon S3 is sharded by Amazon S3 key, downloading one shard of data to each processing instance.
*Required*: No
*Type*: String
*Allowed values*: `FullyReplicated | ShardedByS3Key`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3DataType`  <a name="cfn-sagemaker-processingjob-s3input-s3datatype"></a>
Whether you use an `S3Prefix` or a `ManifestFile` for the data type. If you choose `S3Prefix`, `S3Uri` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for the processing job. If you choose `ManifestFile`, `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for the processing job.
*Required*: Yes
*Type*: String
*Allowed values*: `ManifestFile | S3Prefix`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3InputMode`  <a name="cfn-sagemaker-processingjob-s3input-s3inputmode"></a>
Whether to use `File` or `Pipe` input mode. In File mode, Amazon SageMaker copies the data from the input source onto the local ML storage volume before starting your processing container. This is the most commonly used input mode. In `Pipe` mode, Amazon SageMaker streams input data from the source directly to your processing container into named pipes without using the ML storage volume.
*Required*: No
*Type*: String
*Allowed values*: `File | Pipe`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Uri`  <a name="cfn-sagemaker-processingjob-s3input-s3uri"></a>
The URI of the Amazon S3 prefix Amazon SageMaker downloads data required to run a processing job.
*Required*: Yes
*Type*: String
*Pattern*: `(https|s3)://([^/]+)/?(.*)`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
