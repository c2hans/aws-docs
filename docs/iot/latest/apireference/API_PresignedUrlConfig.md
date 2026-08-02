---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_PresignedUrlConfig.html
---

# PresignedUrlConfig
<a name="API_PresignedUrlConfig"></a>

Configuration for pre-signed S3 URLs.

## Contents
<a name="API_PresignedUrlConfig_Contents"></a>

 ** expiresInSec **   <a name="iot-Type-PresignedUrlConfig-expiresInSec"></a>
How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.
Type: Long
Valid Range: Minimum value of 60. Maximum value of 3600.
Required: No

 ** roleArn **   <a name="iot-Type-PresignedUrlConfig-roleArn"></a>
The ARN of an IAM role that grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files.
For information about addressing the confused deputy problem, see [cross-service confused deputy prevention](https://docs.aws.amazon.com/iot/latest/developerguide/cross-service-confused-deputy-prevention.html) in the * AWS IoT Core developer guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## See Also
<a name="API_PresignedUrlConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/PresignedUrlConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/PresignedUrlConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/PresignedUrlConfig)
