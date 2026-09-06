---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_OAuth2Properties.html
---

# OAuth2Properties
<a name="API_OAuth2Properties"></a>

The OAuth2 properties.

## Contents
<a name="API_OAuth2Properties_Contents"></a>

 ** authorizationCodeProperties **   <a name="datazone-Type-OAuth2Properties-authorizationCodeProperties"></a>
The authorization code properties of the OAuth2 properties.
Type: [AuthorizationCodeProperties](API_AuthorizationCodeProperties.md) object
Required: No

 ** oAuth2ClientApplication **   <a name="datazone-Type-OAuth2Properties-oAuth2ClientApplication"></a>
The OAuth2 client application of the OAuth2 properties.
Type: [OAuth2ClientApplication](API_OAuth2ClientApplication.md) object
Required: No

 ** oAuth2Credentials **   <a name="datazone-Type-OAuth2Properties-oAuth2Credentials"></a>
The OAuth2 credentials of the OAuth2 properties.
Type: [GlueOAuth2Credentials](API_GlueOAuth2Credentials.md) object
Required: No

 ** oAuth2GrantType **   <a name="datazone-Type-OAuth2Properties-oAuth2GrantType"></a>
The OAuth2 grant type of the OAuth2 properties.
Type: String
Valid Values: `AUTHORIZATION_CODE | CLIENT_CREDENTIALS | JWT_BEARER`
Required: No

 ** tokenUrl **   <a name="datazone-Type-OAuth2Properties-tokenUrl"></a>
The OAuth2 token URL of the OAuth2 properties.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
Required: No

 ** tokenUrlParametersMap **   <a name="datazone-Type-OAuth2Properties-tokenUrlParametersMap"></a>
The OAuth2 token URL parameter map of the OAuth2 properties.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_OAuth2Properties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/OAuth2Properties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/OAuth2Properties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/OAuth2Properties)
