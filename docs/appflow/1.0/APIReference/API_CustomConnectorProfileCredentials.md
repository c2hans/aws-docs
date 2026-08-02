---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_CustomConnectorProfileCredentials.html
---

# CustomConnectorProfileCredentials
<a name="API_CustomConnectorProfileCredentials"></a>

The connector-specific profile credentials that are required when using the custom connector.

## Contents
<a name="API_CustomConnectorProfileCredentials_Contents"></a>

 ** authenticationType **   <a name="appflow-Type-CustomConnectorProfileCredentials-authenticationType"></a>
The authentication type that the custom connector uses for authenticating while creating a connector profile.
Type: String
Valid Values: `OAUTH2 | APIKEY | BASIC | CUSTOM`
Required: Yes

 ** apiKey **   <a name="appflow-Type-CustomConnectorProfileCredentials-apiKey"></a>
The API keys required for the authentication of the user.
Type: [ApiKeyCredentials](API_ApiKeyCredentials.md) object
Required: No

 ** basic **   <a name="appflow-Type-CustomConnectorProfileCredentials-basic"></a>
The basic credentials that are required for the authentication of the user.
Type: [BasicAuthCredentials](API_BasicAuthCredentials.md) object
Required: No

 ** custom **   <a name="appflow-Type-CustomConnectorProfileCredentials-custom"></a>
If the connector uses the custom authentication mechanism, this holds the required credentials.
Type: [CustomAuthCredentials](API_CustomAuthCredentials.md) object
Required: No

 ** oauth2 **   <a name="appflow-Type-CustomConnectorProfileCredentials-oauth2"></a>
The OAuth 2.0 credentials required for the authentication of the user.
Type: [OAuth2Credentials](API_OAuth2Credentials.md) object
Required: No

## See Also
<a name="API_CustomConnectorProfileCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/CustomConnectorProfileCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/CustomConnectorProfileCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/CustomConnectorProfileCredentials)
