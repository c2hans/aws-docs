---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_S3DataSource.html
---

# S3DataSource
<a name="API_S3DataSource"></a>

Describes the S3 data source.

Your input bucket must be in the same AWS region as your training job.

## Contents
<a name="API_S3DataSource_Contents"></a>

 ** S3DataType **   <a name="sagemaker-Type-S3DataSource-S3DataType"></a>
If you choose `S3Prefix`, `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix for model training.
If you choose `ManifestFile`, `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want SageMaker to use for model training.
If you choose `AugmentedManifestFile`, `S3Uri` identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. `AugmentedManifestFile` can only be used if the Channel's input mode is `Pipe`.
If you choose `Converse`, `S3Uri` identifies an Amazon S3 location that contains data formatted according to Converse format. This format structures conversational messages with specific roles and content types used for training and fine-tuning foundational models.
Type: String
Valid Values: `ManifestFile | S3Prefix | AugmentedManifestFile | Converse`
Required: Yes

 ** S3Uri **   <a name="sagemaker-Type-S3DataSource-S3Uri"></a>
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
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** AttributeNames **   <a name="sagemaker-Type-S3DataSource-AttributeNames"></a>
A list of one or more attribute names to use that are found in a specified augmented manifest file.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 16 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.+`
Required: No

 ** HubAccessConfig **   <a name="sagemaker-Type-S3DataSource-HubAccessConfig"></a>
The configuration for a private hub model reference that points to a SageMaker JumpStart public hub model.
Type: [HubAccessConfig](API_HubAccessConfig.md) object
Required: No

 ** InstanceGroupNames **   <a name="sagemaker-Type-S3DataSource-InstanceGroupNames"></a>
A list of names of instance groups that get data from the S3 data source.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.+`
Required: No

 ** ModelAccessConfig **   <a name="sagemaker-Type-S3DataSource-ModelAccessConfig"></a>
The access configuration file to control access to the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig`.
+ If you are a Jumpstart user, see the [End-user license agreements](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html#jumpstart-foundation-models-choose-eula) section for more details on accepting the EULA.
+ If you are an AutoML user, see the *Optional Parameters* section of *Create an AutoML job to fine-tune text generation models using the API* for details on [How to set the EULA acceptance when fine-tuning a model using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-finetune-llms.html#autopilot-llms-finetuning-api-optional-params).
Type: [ModelAccessConfig](API_ModelAccessConfig.md) object
Required: No

 ** S3DataDistributionType **   <a name="sagemaker-Type-S3DataSource-S3DataDistributionType"></a>
If you want SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify `FullyReplicated`.
If you want SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify `ShardedByS3Key`. If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data.
Don't choose more ML compute instances for training than available S3 objects. If you do, some nodes won't get any data and you will pay for nodes that aren't getting any training data. This applies in both File and Pipe modes. Keep this in mind when developing algorithms.
In distributed training, where you use multiple ML compute EC2 instances, you might choose `ShardedByS3Key`. If the algorithm requires copying training data to the ML storage volume (when `TrainingInputMode` is set to `File`), this copies 1/*n* of the number of objects.
Type: String
Valid Values: `FullyReplicated | ShardedByS3Key`
Required: No

## See Also
<a name="API_S3DataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/S3DataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/S3DataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/S3DataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
