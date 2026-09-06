---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Preview.html
---

# Preview
<a name="API_Preview"></a>

Information about agent-first preview mode outbound strategy configuration.

## Contents
<a name="API_Preview_Contents"></a>

 ** AllowedUserActions **   <a name="connect-Type-Preview-AllowedUserActions"></a>
The actions the agent can perform after accepting the preview outbound contact.
Type: Array of strings
Valid Values: `CALL | DISCARD`
Required: Yes

 ** PostAcceptTimeoutConfig **   <a name="connect-Type-Preview-PostAcceptTimeoutConfig"></a>
Countdown timer configuration after the agent accepted the preview outbound contact.
Type: [PostAcceptTimeoutConfig](API_PostAcceptTimeoutConfig.md) object
Required: Yes

## See Also
<a name="API_Preview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Preview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Preview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Preview)
