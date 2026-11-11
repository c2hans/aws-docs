---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_OAuth2PropertiesPatch.html
---

# OAuth2PropertiesPatch
<a name="API_OAuth2PropertiesPatch"></a>

Contains the OAuth2 properties, such as the client application, grant type, and token URL, that you want to update for a connection.

## Contents
<a name="API_OAuth2PropertiesPatch_Contents"></a>

 ** oAuth2ClientApplication **   <a name="datazone-Type-OAuth2PropertiesPatch-oAuth2ClientApplication"></a>
The OAuth2 client application of the OAuth2 properties to update.
Type: [OAuth2ClientApplication](API_OAuth2ClientApplication.md) object
Required: No

 ** oAuth2GrantType **   <a name="datazone-Type-OAuth2PropertiesPatch-oAuth2GrantType"></a>
The OAuth2 grant type of the OAuth2 properties to update.
Type: String
Valid Values: `AUTHORIZATION_CODE | CLIENT_CREDENTIALS | JWT_BEARER`
Required: No

 ** tokenUrl **   <a name="datazone-Type-OAuth2PropertiesPatch-tokenUrl"></a>
The OAuth2 token URL of the OAuth2 properties to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
Required: No

 ** tokenUrlParametersMap **   <a name="datazone-Type-OAuth2PropertiesPatch-tokenUrlParametersMap"></a>
The OAuth2 token URL parameter map of the OAuth2 properties to update, for example the scope. If you specify an empty map, the existing parameters are kept.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_OAuth2PropertiesPatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/OAuth2PropertiesPatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/OAuth2PropertiesPatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/OAuth2PropertiesPatch)
