---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_OAuthProperties.html
---

# OAuthProperties
<a name="API_OAuthProperties"></a>

 The OAuth properties required for OAuth type authentication.

## Contents
<a name="API_OAuthProperties_Contents"></a>

 ** authCodeUrl **   <a name="appflow-Type-OAuthProperties-authCodeUrl"></a>
 The authorization code url required to redirect to SAP Login Page to fetch authorization code for OAuth type authentication.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
Required: Yes

 ** oAuthScopes **   <a name="appflow-Type-OAuthProperties-oAuthScopes"></a>
 The OAuth scopes required for OAuth type authentication.
Type: Array of strings
Length Constraints: Maximum length of 128.
Pattern: `\S+`
Required: Yes

 ** tokenUrl **   <a name="appflow-Type-OAuthProperties-tokenUrl"></a>
 The token url required to fetch access/refresh tokens using authorization code and also to refresh expired access token using refresh token.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
Required: Yes

## See Also
<a name="API_OAuthProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/OAuthProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/OAuthProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/OAuthProperties)
