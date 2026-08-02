---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_OAuth2Credentials.html
---

# OAuth2Credentials
<a name="API_OAuth2Credentials"></a>

The credentials used when the authentication type is OAuth2 authentication.

## Contents
<a name="API_OAuth2Credentials_Contents"></a>

 ** AccessToken **   <a name="Glue-Type-OAuth2Credentials-AccessToken"></a>
The access token used when the authentication type is OAuth2.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `^[\x20-\x7E]*$`
Required: No

 ** JwtToken **   <a name="Glue-Type-OAuth2Credentials-JwtToken"></a>
The JSON Web Token (JWT) used when the authentication type is OAuth2.
Type: String
Length Constraints: Maximum length of 8000.
Pattern: `^([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_\-\+\/=]*)`
Required: No

 ** RefreshToken **   <a name="Glue-Type-OAuth2Credentials-RefreshToken"></a>
The refresh token used when the authentication type is OAuth2.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `^[\x20-\x7E]*$`
Required: No

 ** UserManagedClientApplicationClientSecret **   <a name="Glue-Type-OAuth2Credentials-UserManagedClientApplicationClientSecret"></a>
The client application client secret if the client application is user managed.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `^[\x20-\x7E]*$`
Required: No

## See Also
<a name="API_OAuth2Credentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/OAuth2Credentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/OAuth2Credentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/OAuth2Credentials)
