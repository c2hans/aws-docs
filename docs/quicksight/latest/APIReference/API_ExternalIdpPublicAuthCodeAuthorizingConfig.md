---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ExternalIdpPublicAuthCodeAuthorizingConfig.html
---

# ExternalIdpPublicAuthCodeAuthorizingConfig

The configuration for an external OpenID Connect IdP that uses the authorization code flow with PKCE and a public client.

## Contents
<a name="API_ExternalIdpPublicAuthCodeAuthorizingConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClientId **   <a name="QS-Type-ExternalIdpPublicAuthCodeAuthorizingConfig-ClientId"></a>
The OAuth 2.0 client ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** IssuerUrl **   <a name="QS-Type-ExternalIdpPublicAuthCodeAuthorizingConfig-IssuerUrl"></a>
The issuer URL of the external OpenID Connect IdP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://[-a-zA-Z0-9+&@/%=~_|!:,.;]*[-a-zA-Z0-9+&@/%=~_|]`
Required: Yes

## See Also
<a name="API_ExternalIdpPublicAuthCodeAuthorizingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ExternalIdpPublicAuthCodeAuthorizingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ExternalIdpPublicAuthCodeAuthorizingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ExternalIdpPublicAuthCodeAuthorizingConfig)
