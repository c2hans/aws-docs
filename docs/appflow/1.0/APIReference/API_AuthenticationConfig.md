---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_AuthenticationConfig.html
---

# AuthenticationConfig
<a name="API_AuthenticationConfig"></a>

Contains information about the authentication config that the connector supports.

## Contents
<a name="API_AuthenticationConfig_Contents"></a>

 ** customAuthConfigs **   <a name="appflow-Type-AuthenticationConfig-customAuthConfigs"></a>
Contains information required for custom authentication.
Type: Array of [CustomAuthConfig](API_CustomAuthConfig.md) objects
Required: No

 ** isApiKeyAuthSupported **   <a name="appflow-Type-AuthenticationConfig-isApiKeyAuthSupported"></a>
Indicates whether API key authentication is supported by the connector
Type: Boolean
Required: No

 ** isBasicAuthSupported **   <a name="appflow-Type-AuthenticationConfig-isBasicAuthSupported"></a>
Indicates whether basic authentication is supported by the connector.
Type: Boolean
Required: No

 ** isCustomAuthSupported **   <a name="appflow-Type-AuthenticationConfig-isCustomAuthSupported"></a>
Indicates whether custom authentication is supported by the connector
Type: Boolean
Required: No

 ** isOAuth2Supported **   <a name="appflow-Type-AuthenticationConfig-isOAuth2Supported"></a>
Indicates whether OAuth 2.0 authentication is supported by the connector.
Type: Boolean
Required: No

 ** oAuth2Defaults **   <a name="appflow-Type-AuthenticationConfig-oAuth2Defaults"></a>
Contains the default values required for OAuth 2.0 authentication.
Type: [OAuth2Defaults](API_OAuth2Defaults.md) object
Required: No

## See Also
<a name="API_AuthenticationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/AuthenticationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/AuthenticationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/AuthenticationConfig)
