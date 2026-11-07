---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateOutboundRawMessage.html
---

# UpdateOutboundRawMessage
<a name="API_UpdateOutboundRawMessage"></a>

Contains the raw body content of an outbound email draft.

## Contents
<a name="API_UpdateOutboundRawMessage_Contents"></a>

 ** Body **   <a name="connect-Type-UpdateOutboundRawMessage-Body"></a>
The email message body.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5242880.
Required: Yes

 ** ContentType **   <a name="connect-Type-UpdateOutboundRawMessage-ContentType"></a>
The content type of the email body. Valid values:
+  `text/plain` – Plain text content.
+  `text/html` – HTML-formatted content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## See Also
<a name="API_UpdateOutboundRawMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateOutboundRawMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateOutboundRawMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateOutboundRawMessage)
