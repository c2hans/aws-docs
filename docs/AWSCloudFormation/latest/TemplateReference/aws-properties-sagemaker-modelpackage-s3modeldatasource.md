---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-s3modeldatasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage S3ModelDataSource
<a name="aws-properties-sagemaker-modelpackage-s3modeldatasource"></a>

Specifies the S3 location of ML model data to deploy.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-s3modeldatasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-s3modeldatasource-syntax.json"></a>

```
{
  "[CompressionType](#cfn-sagemaker-modelpackage-s3modeldatasource-compressiontype)" : {{String}},
  "[ModelAccessConfig](#cfn-sagemaker-modelpackage-s3modeldatasource-modelaccessconfig)" : {{ModelAccessConfig}},
  "[S3DataType](#cfn-sagemaker-modelpackage-s3modeldatasource-s3datatype)" : {{String}},
  "[S3Uri](#cfn-sagemaker-modelpackage-s3modeldatasource-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-s3modeldatasource-syntax.yaml"></a>

```
  [CompressionType](#cfn-sagemaker-modelpackage-s3modeldatasource-compressiontype): {{String}}
  [ModelAccessConfig](#cfn-sagemaker-modelpackage-s3modeldatasource-modelaccessconfig): {{
    ModelAccessConfig}}
  [S3DataType](#cfn-sagemaker-modelpackage-s3modeldatasource-s3datatype): {{String}}
  [S3Uri](#cfn-sagemaker-modelpackage-s3modeldatasource-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-s3modeldatasource-properties"></a>

`CompressionType`  <a name="cfn-sagemaker-modelpackage-s3modeldatasource-compressiontype"></a>
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
+ Do not organize the model artifacts in [S3 console using folders](https://docs.aws.amazon.com//AmazonS3/latest/userguide/using-folders.html). When you create a folder in S3 console, S3 creates a 0-byte object with a key set to the folder name you provide. They key of the 0-byte object ends with a slash (/) which violates SageMaker restrictions on model artifact file names, leading to model deployment failure.
*Required*: Yes
*Type*: String
*Allowed values*: `None | Gzip`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelAccessConfig`  <a name="cfn-sagemaker-modelpackage-s3modeldatasource-modelaccessconfig"></a>
Specifies the access configuration file for the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig`. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.
*Required*: No
*Type*: [ModelAccessConfig](aws-properties-sagemaker-modelpackage-modelaccessconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3DataType`  <a name="cfn-sagemaker-modelpackage-s3modeldatasource-s3datatype"></a>
Specifies the type of ML model data to deploy.
If you choose `S3Prefix`, `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix as part of the ML model data to deploy. A valid key name prefix identified by `S3Uri` always ends with a forward slash (/).
If you choose `S3Object`, `S3Uri` identifies an object that is the ML model data to deploy.
*Required*: Yes
*Type*: String
*Allowed values*: `S3Prefix | S3Object`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Uri`  <a name="cfn-sagemaker-modelpackage-s3modeldatasource-s3uri"></a>
Specifies the S3 path of ML model data to deploy.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
