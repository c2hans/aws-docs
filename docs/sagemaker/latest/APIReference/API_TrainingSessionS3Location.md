---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingSessionS3Location.html
---

# TrainingSessionS3Location
<a name="API_TrainingSessionS3Location"></a>

Specifies the Amazon S3 path and optional encryption settings for training session output data, including checkpoints, model artifacts, and invocation results.

## Contents
<a name="API_TrainingSessionS3Location_Contents"></a>

 ** Path **   <a name="sagemaker-Type-TrainingSessionS3Location-Path"></a>
The Amazon S3 path where training session outputs are stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** KmsKeyArn **   <a name="sagemaker-Type-TrainingSessionS3Location-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt output data. If not specified, the default Amazon S3 encryption is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:kms:[a-z0-9\-]+:[0-9]{12}:key/(mrk-)?[a-f0-9\-]+`
Required: No

## See Also
<a name="API_TrainingSessionS3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingSessionS3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingSessionS3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingSessionS3Location)
