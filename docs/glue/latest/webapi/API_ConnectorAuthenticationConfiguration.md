---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ConnectorAuthenticationConfiguration.html
---

# ConnectorAuthenticationConfiguration
<a name="API_ConnectorAuthenticationConfiguration"></a>

Configuration that defines the supported authentication types and required properties for the connection type.

## Contents
<a name="API_ConnectorAuthenticationConfiguration_Contents"></a>

 ** AuthenticationTypes **   <a name="Glue-Type-ConnectorAuthenticationConfiguration-AuthenticationTypes"></a>
A list of authentication types supported by this connection type, such as Basic, OAuth2, or Custom authentication methods.
Type: Array of strings
Valid Values: `BASIC | OAUTH2 | CUSTOM | IAM`
Required: Yes

 ** BasicAuthenticationProperties **   <a name="Glue-Type-ConnectorAuthenticationConfiguration-BasicAuthenticationProperties"></a>
Basic authentication configuration that defines the username and password properties for HTTP Basic authentication.
Type: [BasicAuthenticationProperties](API_BasicAuthenticationProperties.md) object
Required: No

 ** CustomAuthenticationProperties **   <a name="Glue-Type-ConnectorAuthenticationConfiguration-CustomAuthenticationProperties"></a>
Custom authentication configuration that allows for flexible authentication mechanisms beyond standard Basic and OAuth2 flows.
Type: [CustomAuthenticationProperties](API_CustomAuthenticationProperties.md) object
Required: No

 ** OAuth2Properties **   <a name="Glue-Type-ConnectorAuthenticationConfiguration-OAuth2Properties"></a>
OAuth2 configuration container that defines the authentication properties and flow-specific configurations for OAuth2-based connections.
Type: [ConnectorOAuth2Properties](API_ConnectorOAuth2Properties.md) object
Required: No

## See Also
<a name="API_ConnectorAuthenticationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ConnectorAuthenticationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ConnectorAuthenticationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ConnectorAuthenticationConfiguration)
