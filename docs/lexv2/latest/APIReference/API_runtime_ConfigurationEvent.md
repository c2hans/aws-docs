---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_ConfigurationEvent.html
---

# ConfigurationEvent
<a name="API_runtime_ConfigurationEvent"></a>

The initial event sent from the application to Amazon Lex to configure the conversation, including session and request attributes and the response content type.

## Contents
<a name="API_runtime_ConfigurationEvent_Contents"></a>

 ** responseContentType **   <a name="lexv2-Type-runtime_ConfigurationEvent-responseContentType"></a>
The message that Amazon Lex returns in the response can be either text or speech based on the `responseContentType` value.
+ If the value is `text/plain;charset=utf-8`, Amazon Lex returns text in the response.
+ If the value begins with `audio/`, Amazon Lex returns speech in the response. Amazon Lex uses Amazon Polly to generate the speech using the configuration that you specified in the `requestContentType` parameter. For example, if you specify `audio/mpeg` as the value, Amazon Lex returns speech in the MPEG format.
+ If the value is `audio/pcm`, the speech returned is audio/pcm in 16-bit, little-endian format.
+ The following are the accepted values:
  + audio/mpeg
  + audio/ogg
  + audio/pcm
  + audio/\* (defaults to mpeg)
  + text/plain; charset=utf-8
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** clientTimestampMillis **   <a name="lexv2-Type-runtime_ConfigurationEvent-clientTimestampMillis"></a>
A timestamp set by the client of the date and time that the event was sent to Amazon Lex.
Type: Long
Required: No

 ** disablePlayback **   <a name="lexv2-Type-runtime_ConfigurationEvent-disablePlayback"></a>
Determines whether Amazon Lex should send audio responses to the client application.
Set this field to false when the client is operating in a playback mode where audio responses are played to the user. If the client isn't operating in playback mode, such as a text chat application, set this to true so that Amazon Lex doesn't wait for the prompt to finish playing on the client.
Type: Boolean
Required: No

 ** eventId **   <a name="lexv2-Type-runtime_ConfigurationEvent-eventId"></a>
A unique identifier that your application assigns to the event. You can use this to identify events in logs.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[0-9a-zA-Z._:-]+`
Required: No

 ** requestAttributes **   <a name="lexv2-Type-runtime_ConfigurationEvent-requestAttributes"></a>
Request-specific information passed between the client application and Amazon Lex.
The namespace `x-amz-lex:` is reserved for special attributes. Don't create any request attributes for prefix `x-amz-lex:`.
Type: String to string map
Key Length Constraints: Minimum length of 1.
Required: No

 ** sessionState **   <a name="lexv2-Type-runtime_ConfigurationEvent-sessionState"></a>
The state of the user's session with Amazon Lex.
Type: [SessionState](API_runtime_SessionState.md) object
Required: No

 ** welcomeMessages **   <a name="lexv2-Type-runtime_ConfigurationEvent-welcomeMessages"></a>
A list of messages to send to the user.
If you set the `welcomeMessage` field, you must also set the [`DialogAction`](https://docs.aws.amazon.com/lexv2/latest/dg/API_runtime_DialogAction.html) structure's [`type`](https://docs.aws.amazon.com/lexv2/latest/dg/API_runtime_DialogAction.html#lexv2-Type-runtime_DialogAction-type) field.
Type: Array of [Message](API_runtime_Message.md) objects
Array Members: Maximum number of 10 items.
Required: No

## See Also
<a name="API_runtime_ConfigurationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/runtime.lex.v2-2020-08-07/ConfigurationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/runtime.lex.v2-2020-08-07/ConfigurationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/runtime.lex.v2-2020-08-07/ConfigurationEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
