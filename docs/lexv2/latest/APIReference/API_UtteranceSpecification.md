---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UtteranceSpecification.html
---

# UtteranceSpecification
<a name="API_UtteranceSpecification"></a>

An object containing information about a specific utterance.

## Contents
<a name="API_UtteranceSpecification_Contents"></a>

 ** associatedIntentName **   <a name="lexv2-Type-UtteranceSpecification-associatedIntentName"></a>
The name of the intent that the utterance is associated to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

 ** associatedSlotName **   <a name="lexv2-Type-UtteranceSpecification-associatedSlotName"></a>
The name of the slot that the utterance is associated to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

 ** audioVoiceDurationMillis **   <a name="lexv2-Type-UtteranceSpecification-audioVoiceDurationMillis"></a>
The duration in milliseconds of the audio associated with the utterance.
Type: Long
Required: No

 ** botAliasId **   <a name="lexv2-Type-UtteranceSpecification-botAliasId"></a>
The identifier of the alias of the bot that the utterance was made to.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^(\bTSTALIASID\b|[0-9a-zA-Z]+)$`
Required: No

 ** botResponseAudioVoiceId **   <a name="lexv2-Type-UtteranceSpecification-botResponseAudioVoiceId"></a>
The identifier for the audio of the bot response.
Type: String
Required: No

 ** botResponses **   <a name="lexv2-Type-UtteranceSpecification-botResponses"></a>
A list of objects containing information about the bot response to the utterance.
Type: Array of [UtteranceBotResponse](API_UtteranceBotResponse.md) objects
Required: No

 ** botVersion **   <a name="lexv2-Type-UtteranceSpecification-botVersion"></a>
The version of the bot that the utterance was made to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^[0-9]+$`
Required: No

 ** channel **   <a name="lexv2-Type-UtteranceSpecification-channel"></a>
The channel that is integrated with the bot that the utterance was made to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** conversationEndTime **   <a name="lexv2-Type-UtteranceSpecification-conversationEndTime"></a>
The date and time when the conversation in which the utterance took place ended. A conversation is defined as a unique combination of a `sessionId` and an `originatingRequestId`.
Type: Timestamp
Required: No

 ** conversationStartTime **   <a name="lexv2-Type-UtteranceSpecification-conversationStartTime"></a>
The date and time when the conversation in which the utterance took place began. A conversation is defined as a unique combination of a `sessionId` and an `originatingRequestId`.
Type: Timestamp
Required: No

 ** dialogActionType **   <a name="lexv2-Type-UtteranceSpecification-dialogActionType"></a>
The type of dialog action that the utterance is associated to. See the `type` field in [DialogAction](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_DialogAction.html) for more information.
Type: String
Required: No

 ** inputType **   <a name="lexv2-Type-UtteranceSpecification-inputType"></a>
The input type of the utterance. The possible values are as follows:
+ PCM format: audio data must be in little-endian byte order.
  +  `audio/l16; rate=16000; channels=1`
  +  `audio/x-l16; sample-rate=16000; channel-count=1`
  +  `audio/lpcm; sample-rate=8000; sample-size-bits=16; channel-count=1; is-big-endian=false`
+ Opus format
  +  `audio/x-cbr-opus-with-preamble;preamble-size=0;bit-rate=256000;frame-size-milliseconds=4`
+ Text format
  +  `text/plain; charset=utf-8`
Type: String
Required: No

 ** intentState **   <a name="lexv2-Type-UtteranceSpecification-intentState"></a>
The state of the intent that the utterance is associated to.
Type: String
Valid Values: `Failed | Fulfilled | InProgress | ReadyForFulfillment | Waiting | FulfillmentInProgress`
Required: No

 ** localeId **   <a name="lexv2-Type-UtteranceSpecification-localeId"></a>
The locale of the bot that the utterance was made to.
Type: String
Required: No

 ** mode **   <a name="lexv2-Type-UtteranceSpecification-mode"></a>
The mode of the session. The possible values are as follows:
+  `Speech` – The session consisted of spoken dialogue.
+  `Text` – The session consisted of written dialogue.
+  `DTMF` – The session consisted of touch-tone keypad (Dual Tone Multi-Frequency) key presses.
+  `MultiMode` – The session consisted of multiple modes.
Type: String
Valid Values: `Speech | Text | DTMF | MultiMode`
Required: No

 ** outputType **   <a name="lexv2-Type-UtteranceSpecification-outputType"></a>
The output type of the utterance. The possible values are as follows:
+  `audio/mpeg`
+  `audio/ogg`
+  `audio/pcm (16 KHz)`
+  `audio/` (defaults to `mpeg`)
+  `text/plain; charset=utf-8`
Type: String
Required: No

 ** sessionId **   <a name="lexv2-Type-UtteranceSpecification-sessionId"></a>
The identifier of the session that the utterance was made in.
Type: String
Pattern: `[0-9a-zA-Z._:-]`
Required: No

 ** slotsFilledInSession **   <a name="lexv2-Type-UtteranceSpecification-slotsFilledInSession"></a>
The slots that have been filled in the session by the time of the utterance.
Type: String
Required: No

 ** utterance **   <a name="lexv2-Type-UtteranceSpecification-utterance"></a>
The text of the utterance.
Type: String
Required: No

 ** utteranceRequestId **   <a name="lexv2-Type-UtteranceSpecification-utteranceRequestId"></a>
The identifier of the request associated with the utterance.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: No

 ** utteranceTimestamp **   <a name="lexv2-Type-UtteranceSpecification-utteranceTimestamp"></a>
The date and time when the utterance took place.
Type: Timestamp
Required: No

 ** utteranceUnderstood **   <a name="lexv2-Type-UtteranceSpecification-utteranceUnderstood"></a>
Specifies whether the bot understood the utterance or not.
Type: Boolean
Required: No

## See Also
<a name="API_UtteranceSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UtteranceSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UtteranceSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UtteranceSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
