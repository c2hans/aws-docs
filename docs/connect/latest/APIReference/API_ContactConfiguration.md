---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactConfiguration.html
---

# ContactConfiguration
<a name="API_ContactConfiguration"></a>

The contact configuration for push notification registration.

## Contents
<a name="API_ContactConfiguration_Contents"></a>

 ** ContactId **   <a name="connect-Type-ContactConfiguration-ContactId"></a>
The identifier of the contact within the Amazon Connect instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** IncludeRawMessage **   <a name="connect-Type-ContactConfiguration-IncludeRawMessage"></a>
Whether to include raw connect message in the push notification payload. Default is `False`.
Type: Boolean
Required: No

 ** ParticipantRole **   <a name="connect-Type-ContactConfiguration-ParticipantRole"></a>
The role of the participant in the chat conversation.
Only `CUSTOMER` is currently supported. Any other values other than `CUSTOMER` will result in an exception (4xx error).
Type: String
Valid Values: `AGENT | CUSTOMER | SYSTEM | CUSTOM_BOT | SUPERVISOR`
Required: No

## See Also
<a name="API_ContactConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactConfiguration)
