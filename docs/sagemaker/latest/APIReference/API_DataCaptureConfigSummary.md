---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DataCaptureConfigSummary.html
---

# DataCaptureConfigSummary
<a name="API_DataCaptureConfigSummary"></a>

The currently active data capture configuration used by your Endpoint.

## Contents
<a name="API_DataCaptureConfigSummary_Contents"></a>

 ** CaptureStatus **   <a name="sagemaker-Type-DataCaptureConfigSummary-CaptureStatus"></a>
Whether data capture is currently functional.
Type: String
Valid Values: `Started | Stopped`
Required: Yes

 ** CurrentSamplingPercentage **   <a name="sagemaker-Type-DataCaptureConfigSummary-CurrentSamplingPercentage"></a>
The percentage of requests being captured by your Endpoint.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

 ** DestinationS3Uri **   <a name="sagemaker-Type-DataCaptureConfigSummary-DestinationS3Uri"></a>
The Amazon S3 location being used to capture the data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(https|s3)://([^/])/?(.*)`
Required: Yes

 ** EnableCapture **   <a name="sagemaker-Type-DataCaptureConfigSummary-EnableCapture"></a>
Whether data capture is enabled or disabled.
Type: Boolean
Required: Yes

 ** KmsKeyId **   <a name="sagemaker-Type-DataCaptureConfigSummary-KmsKeyId"></a>
The KMS key being used to encrypt the data in Amazon S3.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: Yes

## See Also
<a name="API_DataCaptureConfigSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DataCaptureConfigSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DataCaptureConfigSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DataCaptureConfigSummary)
