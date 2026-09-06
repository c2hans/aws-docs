---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-model-s3datasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Model S3DataSource
<a name="aws-properties-sagemaker-model-s3datasource"></a>

Describes the S3 data source.

Your input bucket must be in the same AWS region as your training job.

## Syntax
<a name="aws-properties-sagemaker-model-s3datasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-model-s3datasource-syntax.json"></a>

```
{
  "[CompressionType](#cfn-sagemaker-model-s3datasource-compressiontype)" : {{String}},
  "[HubAccessConfig](#cfn-sagemaker-model-s3datasource-hubaccessconfig)" : {{HubAccessConfig}},
  "[ModelAccessConfig](#cfn-sagemaker-model-s3datasource-modelaccessconfig)" : {{ModelAccessConfig}},
  "[S3DataType](#cfn-sagemaker-model-s3datasource-s3datatype)" : {{String}},
  "[S3Uri](#cfn-sagemaker-model-s3datasource-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-model-s3datasource-syntax.yaml"></a>

```
  [CompressionType](#cfn-sagemaker-model-s3datasource-compressiontype): {{String}}
  [HubAccessConfig](#cfn-sagemaker-model-s3datasource-hubaccessconfig): {{
    HubAccessConfig}}
  [ModelAccessConfig](#cfn-sagemaker-model-s3datasource-modelaccessconfig): {{
    ModelAccessConfig}}
  [S3DataType](#cfn-sagemaker-model-s3datasource-s3datatype): {{String}}
  [S3Uri](#cfn-sagemaker-model-s3datasource-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-model-s3datasource-properties"></a>

`CompressionType`  <a name="cfn-sagemaker-model-s3datasource-compressiontype"></a>
The compression type of the model data in Amazon S3.
*Required*: Yes
*Type*: String
*Allowed values*: `None | Gzip`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HubAccessConfig`  <a name="cfn-sagemaker-model-s3datasource-hubaccessconfig"></a>
The configuration for a private hub model reference that points to a SageMaker JumpStart public hub model.
*Required*: No
*Type*: [HubAccessConfig](aws-properties-sagemaker-model-hubaccessconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelAccessConfig`  <a name="cfn-sagemaker-model-s3datasource-modelaccessconfig"></a>
Configuration for accessing the model data in Amazon S3.
*Required*: No
*Type*: [ModelAccessConfig](aws-properties-sagemaker-model-modelaccessconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3DataType`  <a name="cfn-sagemaker-model-s3datasource-s3datatype"></a>
If you choose `S3Prefix`, `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix for model training.
If you choose `ManifestFile`, `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want SageMaker to use for model training.
If you choose `AugmentedManifestFile`, `S3Uri` identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. `AugmentedManifestFile` can only be used if the Channel's input mode is `Pipe`.
If you choose `Converse`, `S3Uri` identifies an Amazon S3 location that contains data formatted according to Converse format. This format structures conversational messages with specific roles and content types used for training and fine-tuning foundational models.
*Required*: Yes
*Type*: String
*Allowed values*: `S3Prefix | S3Object`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Uri`  <a name="cfn-sagemaker-model-s3datasource-s3uri"></a>
Depending on the value specified for the `S3DataType`, identifies either a key name prefix or a manifest. For example:
+  A key name prefix might look like this: `s3://bucketname/exampleprefix/`
+  A manifest might look like this: `s3://bucketname/example.manifest`

   A manifest is an S3 object which is a JSON file consisting of an array of elements. The first element is a prefix which is followed by one or more suffixes. SageMaker appends the suffix elements to the prefix to get a full set of `S3Uri`. Note that the prefix must be a valid non-empty `S3Uri` that precludes users from specifying a manifest whose individual `S3Uri` is sourced from different S3 buckets.

   The following code example shows a valid manifest format:

   `[ {"prefix": "s3://customer_bucket/some/prefix/"},`

   ` "relative/path/to/custdata-1",`

   ` "relative/path/custdata-2",`

   ` ...`

   ` "relative/path/custdata-N"`

   `]`

   This JSON is equivalent to the following `S3Uri` list:

   `s3://customer_bucket/some/prefix/relative/path/to/custdata-1`

   `s3://customer_bucket/some/prefix/relative/path/custdata-2`

   `...`

   `s3://customer_bucket/some/prefix/relative/path/custdata-N`

  The complete set of `S3Uri` in this manifest is the input data for the channel for this data source. The object that each `S3Uri` points to must be readable by the IAM role that SageMaker uses to perform tasks on your behalf.
Your input bucket must be located in same AWS region as your training job.
*Required*: Yes
*Type*: String
*Pattern*: `(https|s3)://([^/]+)/?(.*)`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
