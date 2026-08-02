---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_OAuthUpdate.html
---

# OAuthUpdate
<a name="API_OAuthUpdate"></a>

Structure containing updated OAuth configuration settings.

## Contents
<a name="API_OAuthUpdate_Contents"></a>

 ** oAuthCompleteRedirectUrl **   <a name="managedintegrations-Type-OAuthUpdate-oAuthCompleteRedirectUrl"></a>
The updated URL where users are redirected after completing the OAuth authorization process.
Type: String
Required: No

 ** proactiveRefreshTokenRenewal **   <a name="managedintegrations-Type-OAuthUpdate-proactiveRefreshTokenRenewal"></a>
Updated configuration for proactively refreshing OAuth tokens before they expire.
Type: [ProactiveRefreshTokenRenewal](API_ProactiveRefreshTokenRenewal.md) object
Required: No

## See Also
<a name="API_OAuthUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/OAuthUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/OAuthUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/OAuthUpdate)
