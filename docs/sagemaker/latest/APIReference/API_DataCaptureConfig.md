---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DataCaptureConfig.html
---

# DataCaptureConfig
<a name="API_DataCaptureConfig"></a>

Configuration to control how SageMaker AI captures inference data.

## Contents
<a name="API_DataCaptureConfig_Contents"></a>

 ** CaptureOptions **   <a name="sagemaker-Type-DataCaptureConfig-CaptureOptions"></a>
Specifies data Model Monitor will capture. You can configure whether to collect only input, only output, or both
Type: Array of [CaptureOption](API_CaptureOption.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: Yes

 ** DestinationS3Uri **   <a name="sagemaker-Type-DataCaptureConfig-DestinationS3Uri"></a>
The Amazon S3 location used to capture the data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(https|s3)://([^/])/?(.*)`
Required: Yes

 ** InitialSamplingPercentage **   <a name="sagemaker-Type-DataCaptureConfig-InitialSamplingPercentage"></a>
The percentage of requests SageMaker AI will capture. A lower value is recommended for Endpoints with high traffic.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

 ** CaptureContentTypeHeader **   <a name="sagemaker-Type-DataCaptureConfig-CaptureContentTypeHeader"></a>
Configuration specifying how to treat different headers. If no headers are specified SageMaker AI will by default base64 encode when capturing the data.
Type: [CaptureContentTypeHeader](API_CaptureContentTypeHeader.md) object
Required: No

 ** EnableCapture **   <a name="sagemaker-Type-DataCaptureConfig-EnableCapture"></a>
Whether data capture should be enabled or disabled (defaults to enabled).
Type: Boolean
Required: No

 ** KmsKeyId **   <a name="sagemaker-Type-DataCaptureConfig-KmsKeyId"></a>
The Amazon Resource Name (ARN) of an AWS Key Management Service key that SageMaker AI uses to encrypt the captured data at rest using Amazon S3 server-side encryption.
The KmsKeyId can be any of the following formats:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
+ Alias name: `alias/ExampleAlias`
+ Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

## See Also
<a name="API_DataCaptureConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DataCaptureConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DataCaptureConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DataCaptureConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
