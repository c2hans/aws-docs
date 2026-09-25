---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_OAuthClientCredential.html
---

# OAuthClientCredential
<a name="API_OAuthClientCredential"></a>

Credentials for an OAuth 2.0 client-credentials grant used to authenticate an integration with its external system.

## Contents
<a name="API_OAuthClientCredential_Contents"></a>

 ** clientId **   <a name="cloudwatchomni-Type-OAuthClientCredential-clientId"></a>
The OAuth 2.0 client identifier registered with the external system.
Type: String
Required: Yes

 ** clientSecret **   <a name="cloudwatchomni-Type-OAuthClientCredential-clientSecret"></a>
The OAuth 2.0 client secret that pairs with the client identifier.
Type: String
Required: Yes

 ** providerId **   <a name="cloudwatchomni-Type-OAuthClientCredential-providerId"></a>
The identifier of the OAuth provider that issued the client credentials.
Type: String
Required: No

## See Also
<a name="API_OAuthClientCredential_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/OAuthClientCredential)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/OAuthClientCredential)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/OAuthClientCredential)
