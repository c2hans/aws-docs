---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_AuthConfig.html
---

# AuthConfig
<a name="API_AuthConfig"></a>

The authentication configuration details for a connector destination, including OAuth settings and other authentication parameters.

## Contents
<a name="API_AuthConfig_Contents"></a>

 ** GeneralAuthorization **   <a name="managedintegrations-Type-AuthConfig-GeneralAuthorization"></a>
The authorization materials for General Authorization.
Type: Array of [AuthMaterial](API_AuthMaterial.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

 ** oAuth **   <a name="managedintegrations-Type-AuthConfig-oAuth"></a>
The OAuth configuration settings used for authentication with the third-party service.
Type: [OAuthConfig](API_OAuthConfig.md) object
Required: No

## See Also
<a name="API_AuthConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/AuthConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/AuthConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/AuthConfig)
