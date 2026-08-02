---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_ThrottleSettings.html
---

# ThrottleSettings
<a name="API_ThrottleSettings"></a>

 The API request rate limits.

## Contents
<a name="API_ThrottleSettings_Contents"></a>

 ** burstLimit **   <a name="apigw-Type-ThrottleSettings-burstLimit"></a>
The API target request burst rate limit. This allows more requests through for a period of time than the target rate limit.
Type: Integer
Required: No

 ** rateLimit **   <a name="apigw-Type-ThrottleSettings-rateLimit"></a>
The API target request rate limit.
Type: Double
Required: No

## See Also
<a name="API_ThrottleSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/ThrottleSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/ThrottleSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/ThrottleSettings)
