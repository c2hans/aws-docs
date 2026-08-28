---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_DisconnectionEvent.html
---

# DisconnectionEvent
<a name="API_runtime_DisconnectionEvent"></a>

A notification from the client that it is disconnecting from Amazon Lex. Sending a `DisconnectionEvent` event is optional, but can help identify a conversation in logs.

## Contents
<a name="API_runtime_DisconnectionEvent_Contents"></a>

 ** clientTimestampMillis **   <a name="lexv2-Type-runtime_DisconnectionEvent-clientTimestampMillis"></a>
A timestamp set by the client of the date and time that the event was sent to Amazon Lex.
Type: Long
Required: No

 ** eventId **   <a name="lexv2-Type-runtime_DisconnectionEvent-eventId"></a>
A unique identifier that your application assigns to the event. You can use this to identify events in logs.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[0-9a-zA-Z._:-]+`
Required: No

## See Also
<a name="API_runtime_DisconnectionEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/runtime.lex.v2-2020-08-07/DisconnectionEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/runtime.lex.v2-2020-08-07/DisconnectionEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/runtime.lex.v2-2020-08-07/DisconnectionEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
