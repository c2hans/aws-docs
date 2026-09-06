---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_UrlEndpointConfig.html
---

# UrlEndpointConfig
<a name="API_UrlEndpointConfig"></a>

The configuration for the URL endpoint type.

## Contents
<a name="API_UrlEndpointConfig_Contents"></a>

 ** HealthUrl **   <a name="migrationhubrefactorspaces-Type-UrlEndpointConfig-HealthUrl"></a>
The health check URL of the URL endpoint type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://[-a-zA-Z0-9+\x38@#/%?=~_|!:,.;]*[-a-zA-Z0-9+\x38@#/%=~_|]`
Required: No

 ** Url **   <a name="migrationhubrefactorspaces-Type-UrlEndpointConfig-Url"></a>
The HTTP URL endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://[-a-zA-Z0-9+\x38@#/%?=~_|!:,.;]*[-a-zA-Z0-9+\x38@#/%=~_|]`
Required: No

## See Also
<a name="API_UrlEndpointConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/UrlEndpointConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/UrlEndpointConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/UrlEndpointConfig)
