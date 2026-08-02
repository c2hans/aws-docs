---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCorsConfiguration.html
---

# AwsCorsConfiguration
<a name="API_AwsCorsConfiguration"></a>

Contains the cross-origin resource sharing (CORS) configuration for the API. CORS is only supported for HTTP APIs.

## Contents
<a name="API_AwsCorsConfiguration_Contents"></a>

 ** AllowCredentials **   <a name="securityhub-Type-AwsCorsConfiguration-AllowCredentials"></a>
Indicates whether the CORS request includes credentials.
Type: Boolean
Required: No

 ** AllowHeaders **   <a name="securityhub-Type-AwsCorsConfiguration-AllowHeaders"></a>
The allowed headers for CORS requests.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** AllowMethods **   <a name="securityhub-Type-AwsCorsConfiguration-AllowMethods"></a>
The allowed methods for CORS requests.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** AllowOrigins **   <a name="securityhub-Type-AwsCorsConfiguration-AllowOrigins"></a>
The allowed origins for CORS requests.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** ExposeHeaders **   <a name="securityhub-Type-AwsCorsConfiguration-ExposeHeaders"></a>
The exposed headers for CORS requests.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** MaxAge **   <a name="securityhub-Type-AwsCorsConfiguration-MaxAge"></a>
The number of seconds for which the browser caches preflight request results.
Type: Integer
Required: No

## See Also
<a name="API_AwsCorsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCorsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCorsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCorsConfiguration)
