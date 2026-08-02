---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ConnectorOAuth2Properties.html
---

# ConnectorOAuth2Properties
<a name="API_ConnectorOAuth2Properties"></a>

OAuth2 configuration container that defines the authentication properties and flow-specific configurations for OAuth2-based connections.

## Contents
<a name="API_ConnectorOAuth2Properties_Contents"></a>

 ** OAuth2GrantType **   <a name="Glue-Type-ConnectorOAuth2Properties-OAuth2GrantType"></a>
The OAuth2 grant type to use for authentication, such as CLIENT\_CREDENTIALS, JWT\_BEARER, or AUTHORIZATION\_CODE.
Type: String
Valid Values: `CLIENT_CREDENTIALS | JWT_BEARER | AUTHORIZATION_CODE`
Required: Yes

 ** AuthorizationCodeProperties **   <a name="Glue-Type-ConnectorOAuth2Properties-AuthorizationCodeProperties"></a>
Configuration properties specific to the OAuth2 Authorization Code grant type flow.
Type: [ConnectorAuthorizationCodeProperties](API_ConnectorAuthorizationCodeProperties.md) object
Required: No

 ** ClientCredentialsProperties **   <a name="Glue-Type-ConnectorOAuth2Properties-ClientCredentialsProperties"></a>
Configuration properties specific to the OAuth2 Client Credentials grant type flow.
Type: [ClientCredentialsProperties](API_ClientCredentialsProperties.md) object
Required: No

 ** JWTBearerProperties **   <a name="Glue-Type-ConnectorOAuth2Properties-JWTBearerProperties"></a>
Configuration properties specific to the OAuth2 JWT Bearer grant type flow.
Type: [JWTBearerProperties](API_JWTBearerProperties.md) object
Required: No

## See Also
<a name="API_ConnectorOAuth2Properties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ConnectorOAuth2Properties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ConnectorOAuth2Properties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ConnectorOAuth2Properties)
