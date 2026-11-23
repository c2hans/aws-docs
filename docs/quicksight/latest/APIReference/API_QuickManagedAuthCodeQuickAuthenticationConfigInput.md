---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_QuickManagedAuthCodeQuickAuthenticationConfigInput.html
---

# QuickManagedAuthCodeQuickAuthenticationConfigInput

The configuration for a Quick Sight-managed client. You provide the redirect URIs, and Quick Sight generates the client ID.

## Contents
<a name="API_QuickManagedAuthCodeQuickAuthenticationConfigInput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RedirectUris **   <a name="QS-Type-QuickManagedAuthCodeQuickAuthenticationConfigInput-RedirectUris"></a>
The OAuth 2.0 redirect URIs of the client.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://[-a-zA-Z0-9+&@/%=~_|!:,.;]*[-a-zA-Z0-9+&@/%=~_|]`
Required: Yes

## See Also
<a name="API_QuickManagedAuthCodeQuickAuthenticationConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/QuickManagedAuthCodeQuickAuthenticationConfigInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/QuickManagedAuthCodeQuickAuthenticationConfigInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/QuickManagedAuthCodeQuickAuthenticationConfigInput)
