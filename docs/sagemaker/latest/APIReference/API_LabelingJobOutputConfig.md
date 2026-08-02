---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LabelingJobOutputConfig.html
---

# LabelingJobOutputConfig
<a name="API_LabelingJobOutputConfig"></a>

Output configuration information for a labeling job.

## Contents
<a name="API_LabelingJobOutputConfig_Contents"></a>

 ** S3OutputPath **   <a name="sagemaker-Type-LabelingJobOutputConfig-S3OutputPath"></a>
The Amazon S3 location to write output data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** KmsKeyId **   <a name="sagemaker-Type-LabelingJobOutputConfig-KmsKeyId"></a>
The AWS Key Management Service ID of the key used to encrypt the output data, if any.
If you provide your own KMS key ID, you must add the required permissions to your KMS key described in [Encrypt Output Data and Storage Volume with AWS KMS](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-permission.html#sms-security-kms-permissions).
If you don't provide a KMS key ID, Amazon SageMaker uses the default AWS KMS key for Amazon S3 for your role's account to encrypt your output data.
If you use a bucket policy with an `s3:PutObject` permission that only allows objects with server-side encryption, set the condition key of `s3:x-amz-server-side-encryption` to `"aws:kms"`. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide.*
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** SnsTopicArn **   <a name="sagemaker-Type-LabelingJobOutputConfig-SnsTopicArn"></a>
An Amazon Simple Notification Service (Amazon SNS) output topic ARN. Provide a `SnsTopicArn` if you want to do real time chaining to another streaming job and receive an Amazon SNS notifications each time a data object is submitted by a worker.
If you provide an `SnsTopicArn` in `OutputConfig`, when workers complete labeling tasks, Ground Truth will send labeling task output data to the SNS output topic you specify here.
To learn more, see [Receive Output Data from a Streaming Labeling Job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-labeling-job.html#sms-streaming-how-it-works-output-data).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sns:[a-z0-9\-]*:[0-9]{12}:[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_LabelingJobOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LabelingJobOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LabelingJobOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LabelingJobOutputConfig)
