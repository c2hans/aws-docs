---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SessionSpecification.html
---

# SessionSpecification
<a name="API_SessionSpecification"></a>

An object containing information about a specific session.

## Contents
<a name="API_SessionSpecification_Contents"></a>

 ** botAliasId **   <a name="lexv2-Type-SessionSpecification-botAliasId"></a>
The identifier of the alias of the bot that the session was held with.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^(\bTSTALIASID\b|[0-9a-zA-Z]+)$`
Required: No

 ** botVersion **   <a name="lexv2-Type-SessionSpecification-botVersion"></a>
The version of the bot that the session was held with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^[0-9]+$`
Required: No

 ** channel **   <a name="lexv2-Type-SessionSpecification-channel"></a>
The channel that is integrated with the bot that the session was held with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** conversationDurationSeconds **   <a name="lexv2-Type-SessionSpecification-conversationDurationSeconds"></a>
The duration of the conversation in seconds. A conversation is defined as a unique combination of a `sessionId` and an `originatingRequestId`.
Type: Long
Required: No

 ** conversationEndState **   <a name="lexv2-Type-SessionSpecification-conversationEndState"></a>
The final state of the conversation. A conversation is defined as a unique combination of a `sessionId` and an `originatingRequestId`.
Type: String
Valid Values: `Success | Failure | Dropped`
Required: No

 ** conversationEndTime **   <a name="lexv2-Type-SessionSpecification-conversationEndTime"></a>
The date and time when the conversation ended. A conversation is defined as a unique combination of a `sessionId` and an `originatingRequestId`.
Type: Timestamp
Required: No

 ** conversationStartTime **   <a name="lexv2-Type-SessionSpecification-conversationStartTime"></a>
The date and time when the conversation began. A conversation is defined as a unique combination of a `sessionId` and an `originatingRequestId`.
Type: Timestamp
Required: No

 ** invokedIntentSamples **   <a name="lexv2-Type-SessionSpecification-invokedIntentSamples"></a>
A list of objects containing the name of an intent that was invoked.
Type: Array of [InvokedIntentSample](API_InvokedIntentSample.md) objects
Required: No

 ** localeId **   <a name="lexv2-Type-SessionSpecification-localeId"></a>
The locale of the bot that the session was held with.
Type: String
Required: No

 ** mode **   <a name="lexv2-Type-SessionSpecification-mode"></a>
The mode of the session. The possible values are as follows:
+  `Speech` – The session was spoken.
+  `Text` – The session was written.
+  `DTMF` – The session used a touch-tone keypad (Dual Tone Multi-Frequency).
+  `MultiMode` – The session used multiple modes.
Type: String
Valid Values: `Speech | Text | DTMF | MultiMode`
Required: No

 ** numberOfTurns **   <a name="lexv2-Type-SessionSpecification-numberOfTurns"></a>
The number of turns that the session took.
Type: Long
Required: No

 ** originatingRequestId **   <a name="lexv2-Type-SessionSpecification-originatingRequestId"></a>
The identifier of the first request in a session.
Type: String
Required: No

 ** sessionId **   <a name="lexv2-Type-SessionSpecification-sessionId"></a>
The identifier of the session.
Type: String
Pattern: `[0-9a-zA-Z._:-]`
Required: No

## See Also
<a name="API_SessionSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SessionSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SessionSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SessionSpecification)
