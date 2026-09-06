---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_OAuth2PropertiesInput.html
---

# OAuth2PropertiesInput
<a name="API_OAuth2PropertiesInput"></a>

A structure containing properties for OAuth2 in the CreateConnection request.

## Contents
<a name="API_OAuth2PropertiesInput_Contents"></a>

 ** AuthorizationCodeProperties **   <a name="Glue-Type-OAuth2PropertiesInput-AuthorizationCodeProperties"></a>
The set of properties required for the the OAuth2 `AUTHORIZATION_CODE` grant type.
Type: [AuthorizationCodeProperties](API_AuthorizationCodeProperties.md) object
Required: No

 ** OAuth2ClientApplication **   <a name="Glue-Type-OAuth2PropertiesInput-OAuth2ClientApplication"></a>
The client application type in the CreateConnection request. For example, `AWS_MANAGED` or `USER_MANAGED`.
Type: [OAuth2ClientApplication](API_OAuth2ClientApplication.md) object
Required: No

 ** OAuth2Credentials **   <a name="Glue-Type-OAuth2PropertiesInput-OAuth2Credentials"></a>
The credentials used when the authentication type is OAuth2 authentication.
Type: [OAuth2Credentials](API_OAuth2Credentials.md) object
Required: No

 ** OAuth2GrantType **   <a name="Glue-Type-OAuth2PropertiesInput-OAuth2GrantType"></a>
The OAuth2 grant type in the CreateConnection request. For example, `AUTHORIZATION_CODE`, `JWT_BEARER`, or `CLIENT_CREDENTIALS`.
Type: String
Valid Values: `AUTHORIZATION_CODE | CLIENT_CREDENTIALS | JWT_BEARER`
Required: No

 ** TokenUrl **   <a name="Glue-Type-OAuth2PropertiesInput-TokenUrl"></a>
The URL of the provider's authentication server, to exchange an authorization code for an access token.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
Required: No

 ** TokenUrlParametersMap **   <a name="Glue-Type-OAuth2PropertiesInput-TokenUrlParametersMap"></a>
A map of parameters that are added to the token `GET` request.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_OAuth2PropertiesInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/OAuth2PropertiesInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/OAuth2PropertiesInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/OAuth2PropertiesInput)
