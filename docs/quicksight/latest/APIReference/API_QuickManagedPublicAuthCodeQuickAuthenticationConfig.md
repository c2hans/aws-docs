---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_QuickManagedPublicAuthCodeQuickAuthenticationConfig.html
---

# QuickManagedPublicAuthCodeQuickAuthenticationConfig

The configuration of a Quick Sight-managed public client that uses PKCE.

## Contents
<a name="API_QuickManagedPublicAuthCodeQuickAuthenticationConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClientId **   <a name="QS-Type-QuickManagedPublicAuthCodeQuickAuthenticationConfig-ClientId"></a>
The OAuth 2.0 client ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** RedirectUris **   <a name="QS-Type-QuickManagedPublicAuthCodeQuickAuthenticationConfig-RedirectUris"></a>
The OAuth 2.0 redirect URIs of the client.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://[-a-zA-Z0-9+&@/%=~_|!:,.;]*[-a-zA-Z0-9+&@/%=~_|]`
Required: Yes

## See Also
<a name="API_QuickManagedPublicAuthCodeQuickAuthenticationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/QuickManagedPublicAuthCodeQuickAuthenticationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/QuickManagedPublicAuthCodeQuickAuthenticationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/QuickManagedPublicAuthCodeQuickAuthenticationConfig)
