---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AwsJobPresignedUrlConfig.html
---

# AwsJobPresignedUrlConfig
<a name="API_AwsJobPresignedUrlConfig"></a>

Configuration information for pre-signed URLs. Valid when `protocols` contains HTTP.

## Contents
<a name="API_AwsJobPresignedUrlConfig_Contents"></a>

 ** expiresInSec **   <a name="iot-Type-AwsJobPresignedUrlConfig-expiresInSec"></a>
How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 1800 seconds. Pre-signed URLs are generated when a request for the job document is received.
Type: Long
Required: No

## See Also
<a name="API_AwsJobPresignedUrlConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AwsJobPresignedUrlConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AwsJobPresignedUrlConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AwsJobPresignedUrlConfig)
