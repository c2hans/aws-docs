---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-outputdataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob OutputDataConfig
<a name="aws-properties-sagemaker-trainingjob-outputdataconfig"></a>

Provides information about how to store model training results (model artifacts).

## Syntax
<a name="aws-properties-sagemaker-trainingjob-outputdataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-outputdataconfig-syntax.json"></a>

```
{
  "[CompressionType](#cfn-sagemaker-trainingjob-outputdataconfig-compressiontype)" : {{String}},
  "[KmsKeyId](#cfn-sagemaker-trainingjob-outputdataconfig-kmskeyid)" : {{String}},
  "[S3OutputPath](#cfn-sagemaker-trainingjob-outputdataconfig-s3outputpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-outputdataconfig-syntax.yaml"></a>

```
  [CompressionType](#cfn-sagemaker-trainingjob-outputdataconfig-compressiontype): {{String}}
  [KmsKeyId](#cfn-sagemaker-trainingjob-outputdataconfig-kmskeyid): {{String}}
  [S3OutputPath](#cfn-sagemaker-trainingjob-outputdataconfig-s3outputpath): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-outputdataconfig-properties"></a>

`CompressionType`  <a name="cfn-sagemaker-trainingjob-outputdataconfig-compressiontype"></a>
The model output compression type. Select `None` to output an uncompressed model, recommended for large model outputs. Defaults to gzip.
*Required*: No
*Type*: String
*Allowed values*: `GZIP | NONE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-sagemaker-trainingjob-outputdataconfig-kmskeyid"></a>
The AWS Key Management Service (AWS KMS) key that SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The `KmsKeyId` can be any of the following formats:
+ // KMS Key ID

   `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ // Amazon Resource Name (ARN) of a KMS Key

   `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
+ // KMS Key Alias

   `"alias/ExampleAlias"`
+ // Amazon Resource Name (ARN) of a KMS Key Alias

   `"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"`
If you use a KMS key ID or an alias of your KMS key, the SageMaker execution role must include permissions to call `kms:Encrypt`. If you don't provide a KMS key ID, SageMaker uses the default KMS key for Amazon S3 for your role's account. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide*. If the output data is stored in Amazon S3 Express One Zone, it is encrypted with server-side encryption with Amazon S3 managed keys (SSE-S3). KMS key is not supported for Amazon S3 Express One Zone
The KMS key policy must grant permission to the IAM role that you specify in your `CreateTrainingJob`, `CreateTransformJob`, or `CreateHyperParameterTuningJob` requests. For more information, see [Using Key Policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *AWS Key Management Service Developer Guide*.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3OutputPath`  <a name="cfn-sagemaker-trainingjob-outputdataconfig-s3outputpath"></a>
Identifies the S3 path where you want SageMaker to store the model artifacts. For example, `s3://bucket-name/key-name-prefix`.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
