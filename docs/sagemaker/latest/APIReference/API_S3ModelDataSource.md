---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_S3ModelDataSource.html
---

# S3ModelDataSource
<a name="API_S3ModelDataSource"></a>

Specifies the S3 location of ML model data to deploy.

## Contents
<a name="API_S3ModelDataSource_Contents"></a>

 ** CompressionType **   <a name="sagemaker-Type-S3ModelDataSource-CompressionType"></a>
Specifies how the ML model data is prepared.
If you choose `Gzip` and choose `S3Object` as the value of `S3DataType`, `S3Uri` identifies an object that is a gzip-compressed TAR archive. SageMaker will attempt to decompress and untar the object during model deployment.
If you choose `None` and chooose `S3Object` as the value of `S3DataType`, `S3Uri` identifies an object that represents an uncompressed ML model to deploy.
If you choose None and choose `S3Prefix` as the value of `S3DataType`, `S3Uri` identifies a key name prefix, under which all objects represents the uncompressed ML model to deploy.
If you choose None, then SageMaker will follow rules below when creating model data files under /opt/ml/model directory for use by your inference code:
+ If you choose `S3Object` as the value of `S3DataType`, then SageMaker will split the key of the S3 object referenced by `S3Uri` by slash (/), and use the last part as the filename of the file holding the content of the S3 object.
+ If you choose `S3Prefix` as the value of `S3DataType`, then for each S3 object under the key name pefix referenced by `S3Uri`, SageMaker will trim its key by the prefix, and use the remainder as the path (relative to `/opt/ml/model`) of the file holding the content of the S3 object. SageMaker will split the remainder by slash (/), using intermediate parts as directory names and the last part as filename of the file holding the content of the S3 object.
+ Do not use any of the following as file names or directory names:
  + An empty or blank string
  + A string which contains null bytes
  + A string longer than 255 bytes
  + A single dot (`.`)
  + A double dot (`..`)
+ Ambiguous file names will result in model deployment failure. For example, if your uncompressed ML model consists of two S3 objects `s3://mybucket/model/weights` and `s3://mybucket/model/weights/part1` and you specify `s3://mybucket/model/` as the value of `S3Uri` and `S3Prefix` as the value of `S3DataType`, then it will result in name clash between `/opt/ml/model/weights` (a regular file) and `/opt/ml/model/weights/` (a directory).
+ Do not organize the model artifacts in [S3 console using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html). When you create a folder in S3 console, S3 creates a 0-byte object with a key set to the folder name you provide. They key of the 0-byte object ends with a slash (/) which violates SageMaker restrictions on model artifact file names, leading to model deployment failure.
Type: String
Valid Values: `None | Gzip`
Required: Yes

 ** S3DataType **   <a name="sagemaker-Type-S3ModelDataSource-S3DataType"></a>
Specifies the type of ML model data to deploy.
If you choose `S3Prefix`, `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix as part of the ML model data to deploy. A valid key name prefix identified by `S3Uri` always ends with a forward slash (/).
If you choose `S3Object`, `S3Uri` identifies an object that is the ML model data to deploy.
Type: String
Valid Values: `S3Prefix | S3Object`
Required: Yes

 ** S3Uri **   <a name="sagemaker-Type-S3ModelDataSource-S3Uri"></a>
Specifies the S3 path of ML model data to deploy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** ETag **   <a name="sagemaker-Type-S3ModelDataSource-ETag"></a>
The ETag associated with S3 URI.
Type: String
Required: No

 ** HubAccessConfig **   <a name="sagemaker-Type-S3ModelDataSource-HubAccessConfig"></a>
Configuration information for hub access.
Type: [InferenceHubAccessConfig](API_InferenceHubAccessConfig.md) object
Required: No

 ** ManifestEtag **   <a name="sagemaker-Type-S3ModelDataSource-ManifestEtag"></a>
The ETag associated with Manifest S3 URI.
Type: String
Required: No

 ** ManifestS3Uri **   <a name="sagemaker-Type-S3ModelDataSource-ManifestS3Uri"></a>
The Amazon S3 URI of the manifest file. The manifest file is a CSV file that stores the artifact locations.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** ModelAccessConfig **   <a name="sagemaker-Type-S3ModelDataSource-ModelAccessConfig"></a>
Specifies the access configuration file for the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig`. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.
Type: [ModelAccessConfig](API_ModelAccessConfig.md) object
Required: No

## See Also
<a name="API_S3ModelDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/S3ModelDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/S3ModelDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/S3ModelDataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
