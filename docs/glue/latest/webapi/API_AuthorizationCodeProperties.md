---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_AuthorizationCodeProperties.html
---

# AuthorizationCodeProperties
<a name="API_AuthorizationCodeProperties"></a>

The set of properties required for the the OAuth2 `AUTHORIZATION_CODE` grant type workflow.

## Contents
<a name="API_AuthorizationCodeProperties_Contents"></a>

 ** AuthorizationCode **   <a name="Glue-Type-AuthorizationCodeProperties-AuthorizationCode"></a>
An authorization code to be used in the third leg of the `AUTHORIZATION_CODE` grant workflow. This is a single-use code which becomes invalid once exchanged for an access token, thus it is acceptable to have this value as a request parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `\S+`
Required: No

 ** RedirectUri **   <a name="Glue-Type-AuthorizationCodeProperties-RedirectUri"></a>
The redirect URI where the user gets redirected to by authorization server when issuing an authorization code. The URI is subsequently used when the authorization code is exchanged for an access token.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `^(https?):\/\/[^\s/$.?#].[^\s]*$`
Required: No

## See Also
<a name="API_AuthorizationCodeProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/AuthorizationCodeProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/AuthorizationCodeProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/AuthorizationCodeProperties)
