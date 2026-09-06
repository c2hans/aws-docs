---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_TextOutputEvent.html
---

# TextOutputEvent
<a name="API_TextOutputEvent"></a>

An output event for an AI-generated response in an Amazon Q Business web experience.

## Contents
<a name="API_TextOutputEvent_Contents"></a>

 ** conversationId **   <a name="qbusiness-Type-TextOutputEvent-conversationId"></a>
The identifier of the conversation with which the text output event is associated.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** systemMessage **   <a name="qbusiness-Type-TextOutputEvent-systemMessage"></a>
An AI-generated message in a `TextOutputEvent`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** systemMessageId **   <a name="qbusiness-Type-TextOutputEvent-systemMessageId"></a>
The identifier of an AI-generated message in a `TextOutputEvent`.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** systemMessageType **   <a name="qbusiness-Type-TextOutputEvent-systemMessageType"></a>
The type of AI-generated message in a `TextOutputEvent`. Amazon Q Business currently supports two types of messages:
+  `RESPONSE` - The Amazon Q Business system response.
+  `GROUNDED_RESPONSE` - The corrected, hallucination-reduced, response returned by Amazon Q Business. Available only if hallucination reduction is supported and configured for the application and detected in the end user chat query by Amazon Q Business.
Type: String
Valid Values: `RESPONSE | GROUNDED_RESPONSE`
Required: No

 ** userMessageId **   <a name="qbusiness-Type-TextOutputEvent-userMessageId"></a>
The identifier of an end user message in a `TextOutputEvent`.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

## See Also
<a name="API_TextOutputEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/TextOutputEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/TextOutputEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/TextOutputEvent)
