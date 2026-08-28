---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/glue-tables.html
---

# Understanding the AWS Glue data catalog tables for the Amazon Chime SDK
<a name="glue-tables"></a>

The following tables list and describe the columns, data types, and elements in an Amazon Chime SDK call analytics Glue data catalog.

**Topics**
+ [call\_analytics\_metadata](#ca-glue-metadata)
+ [call\_analytics\_recording\_metadata](#ca-glue-analytics-recording)
+ [transcribe\_call\_analytics](#ca-glue-transcribe-ca)
+ [transcribe\_call\_analytics\_category\_events](#ca-glue-transcribe-ca-events)
+ [transcribe\_call\_analytics\_post\_call](#ca-glue-transcribe)
+ [transcribe](#ca-glue-transcribe)
+ [voice\_analytics\_status](#ca-glue-va-status)
+ [speaker\_search\_status](#ca-glue-speaker-status)
+ [voice\_tone\_analysis\_status](#ca-glue-tone-status)

## call\_analytics\_metadata
<a name="ca-glue-metadata"></a>

- **time**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Event generation timestamp ISO 8601.

- **detail-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Feature type related to service-type.

- **service-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Name of the AWS service, VoiceAnalytics or CallAnalytics.

- **detail-subtype**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Used for Recording and CallAnalyticsMetadata detail-types.

- **callevent-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Event type associated with SIP, such as Update, Pause, Resume

- **mediaInsightsPipelineId**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Amazon Chime SDK media insights pipeline ID.

- **metadata**
  - **Data type:** string
  - **Elements:** voiceConnectorId / **Definition:** The Amazon Chime SDK Voice Connector ID.
  - **Elements:** callId / **Definition:** The call ID of the participant for the associated usage.
  - **Elements:** transactionId / **Definition:** The transaction ID of the call.
  - **Elements:** fromNumber / **Definition:** E.164 origination phone number.
  - **Elements:** toNumber / **Definition:** E.164 destination phone number.
  - **Elements:** direction / **Definition:** Direction of the call, Outbound or Inbound.
  - **Elements:** oneTimeMetadata.s3RecordingUrl / **Definition:** Amazon S3 bucket URL of the media object emitted by Transcribe Call Analytics.
  - **Elements:** oneTimeMetadata.s3RecordingUrlRedacted / **Definition:** Amazon S3 bucket URL of the redacted media object emitted by Transcribe Call Analytics.
  - **Elements:** oneTimeMetadata.siprecMetadata / **Definition:** SIPREC Metadata in XML format associated with the call.
  - **Elements:** oneTimeMetadata.siprecMetadataJson / **Definition:** SIPREC Metadata in JSON format associated with the call.
  - **Elements:** oneTimeMetadata.InviteHeaders / **Definition:** Invite headers.

## call\_analytics\_recording\_metadata
<a name="ca-glue-analytics-recording"></a>

- **time**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Event generation timestamp ISO 8601.

- **detail-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Feature type related to service-type.

- **service-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Name of the AWS service, VoiceAnalytics or CallAnalytics.

- **detail-subtype**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Used for Recording and CallAnalyticsMetadata detail-types.

- **callevent-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Event type associated with SIP

- **mediaInsightsPipelineId**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Amazon Chime SDK media insight pipeline ID.

- **s3MediaObjectConsoleUrl**
  - **Data type:** string
  - **Elements:**
  - **Definition:** S3 Bucket URL of the media object.

- **metadata**
  - **Data type:** string
  - **Elements:** voiceConnectorId / **Definition:** The Amazon Chime SDK Voice Connector ID.
  - **Elements:** callId / **Definition:** The call ID of the participant for the associated usage.
  - **Elements:** transactionId / **Definition:** The transaction ID of the call.
  - **Elements:** fromNumber / **Definition:** E.164 origination phone number.
  - **Elements:** toNumber / **Definition:** E.164 destination phone number.
  - **Elements:** direction / **Definition:** Direction of the call, Outbound or Inbound.
  - **Elements:** voice enhancement / **Definition:** Feature subtype related to service-type.
  - **Elements:** oneTimeMetadata.siprecMetadata / **Definition:** SIPREC Metadata in XML format associated with the call.
  - **Elements:** oneTimeMetadata.siprecMetadataJson / **Definition:** SIPREC Metadata in JSON format associated with the call.
  - **Elements:** oneTimeMetadata.InviteHeaders / **Definition:** Invite headers.

## transcribe\_call\_analytics
<a name="ca-glue-transcribe-ca"></a>

- **time**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Event generation timestamp ISO 8601.

- **detail-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Feature type related to service-type.

- **service-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Name of the AWS service, VoiceAnalytics or CallAnalytics.

- **mediaInsightsPipelineId**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Amazon Chime SDK media insight pipeline ID.

- **metadata**
  - **Data type:** string
  - **Elements:** voiceConnectorId / **Definition:** The Amazon Chime Voice Connector ID.
  - **Elements:** callId / **Definition:** The call ID of the participant for the associated usage.
  - **Elements:** transactionId / **Definition:** The transaction ID of the call.
  - **Elements:** fromNumber / **Definition:** E.164 origination phone number.
  - **Elements:** toNumber / **Definition:** E.164 destination phone number.
  - **Elements:** direction / **Definition:** Direction of the call, `Outbound` or `Inbound`.

- **UtteranceEvent**
  - **Data type:** struct
  - **Elements:** UtteranceId / **Definition:** The unique identifier associated with the specified `UtteranceEvent`.
  - **Elements:** IsPartial / **Definition:** Indicates whether the segment in the `UtteranceEvent` is complete (`FALSE`) or partial (`TRUE`).
  - **Elements:** ParticipantRole / **Definition:** Provides the role of the speaker for each audio channel, either CUSTOMER or AGENT.
  - **Elements:** BeginOffsetMillis / **Definition:** The time, in milliseconds, from the beginning of the audio stream to the start of the `UtteranceEvent`.
  - **Elements:** EndOffsetMillis / **Definition:** The time, in milliseconds, from the beginning of the audio stream to the start of the `UtteranceEvent`.
  - **Elements:** Transcript / **Definition:** Contains transcribed text.
  - **Elements:** Sentiment / **Definition:** Provides the sentiment detected in the specified segment.
  - **Elements:** Items.beginoffsetmillis / **Definition:** The start time, in milliseconds, of the transcribed item.
  - **Elements:** Items.endoffsetmillis / **Definition:** The end time, in milliseconds, of the transcribed item.
  - **Elements:** Items.itemtype / **Definition:** The type of item identified. Options: `PRONUNCIATION` (spoken words) and `PUNCTUATION`.
  - **Elements:** Items.content / **Definition:** The word or punctuation that was transcribed.
  - **Elements:** Items.confidence  / **Definition:** The confidence score associated with a word or phrase in your transcript. Scores are values between 0 and 1. A larger value indicates a higher probability that the identified item correctly matches the item spoken in your media.
  - **Elements:** Items.vocabularyfiltermatch / **Definition:**  Indicates whether the specified item matches a word in the vocabulary filter included in your request. If true, there is a vocabulary filter match.
  - **Elements:** Items.stable / **Definition:** The partial result stabilization is enabled, Stable indicates whether the specified item is stable (true) or if it may change when the segment is complete (false).
  - **Elements:** IssuesDetected.characteroffsets\_begin / **Definition:** Provides the character count of the first character where a match is identified. For example, the first character associated with an issue or a category match in a segment transcript.
  - **Elements:** IssuesDetected.characteroffsets\_end / **Definition:** Provides the character count of the last character where a match is identified. For example, the last character associated with an issue or a category match in a segment transcript.
  - **Elements:** Entities.beginoffsetmillis / **Definition:** The start time, in milliseconds, of the utterance that was identified as `PII`.
  - **Elements:** Entities.endoffsetmillis / **Definition:** The end time, in milliseconds, of the utterance that was identified as `PII`.
  - **Elements:** Entities.category / **Definition:** The category of information identified. The only category is `PII`.
  - **Elements:** Entities.type / **Definition:** The type of PII identified. For example, `NAME` or `CREDIT_DEBIT_NUMBER`.
  - **Elements:** Entities.content / **Definition:** The word or words identified as `PII`.
  - **Elements:** Entities.confidence / **Definition:** The confidence score associated with the identified `PII` entity in your audio. Confidence scores range between 0 and 1. A larger value indicates a higher probability that the identified entity correctly matches the entity spoken in your media.

## transcribe\_call\_analytics\_category\_events
<a name="ca-glue-transcribe-ca-events"></a>

- **time**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Event generation timestamp ISO 8601.

- **detail-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Feature type related to service-type.

- **service-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Name of the AWS service, VoiceAnalytics or CallAnalytics.

- **mediaInsightsPipelineId**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Amazon Chime SDK media insight pipeline ID.

- **metadata**
  - **Data type:** string
  - **Elements:** voiceConnectorId / **Definition:** The Amazon Chime Voice Connector ID.
  - **Elements:** callId / **Definition:** The call ID of the participant for the associated usage.
  - **Elements:** transactionId / **Definition:** The transaction ID of the call.
  - **Elements:** fromNumber / **Definition:** E.164 origination phone number.
  - **Elements:** toNumber / **Definition:** E.164 destination phone number.
  - **Elements:** direction / **Definition:** Direction of the call, Outbound or Inbound.

- **CategoryEvent**
  - **Data type:** array
  - **Elements:** MatchedCategories
  - **Definition:** Lists the matches in the categories defined by the user.

## transcribe\_call\_analytics\_post\_call
<a name="ca-glue-transcribe"></a>

- **JobStatus**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Event generation timestamp ISO 8601.

- **LanguageCode**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Feature type related to service-type.

- **Transcript**
  - **Data type:** struct
  - **Elements:** LoudnessScores  / **Definition:** Measures the volume at which each participant is speaking. Use this metric to see if the caller or the agent is speaking loudly or yelling, which often indicates anger. <br />This metric is represented as a normalized value (speech level per second of speech in a given segment) on a scale from 0 to 100, where a higher value indicates a louder voice.
  - **Elements:** Content / **Definition:** Contains transcribed text.
  - **Elements:** Id / **Definition:** The unique identifier associated with the specified` UtteranceEvent`.
  - **Elements:** BeginOffsetMillis  / **Definition:** The time, in milliseconds, from the beginning of the audio stream to the start of the `UtteranceEvent`.
  - **Elements:** EndOffsetMillis / **Definition:** The time, in milliseconds, from the beginning of the audio stream to the start of the `UtteranceEvent`.
  - **Elements:** Sentiment / **Definition:** Provides the sentiment detected in the specified transcript segment.
  - **Elements:** ParticipantRole  / **Definition:** Provides the role of the speaker for each audio channel, either `CUSTOMER` or `AGENT`.
  - **Elements:** IssuesDetected.CharacterOffsets.Begin / **Definition:** Provides the character offset to the first character where a match is identified. For example, the first character associated with an issue in a transcript segment.
  - **Elements:** IssuesDetected.CharacterOffsets.End  / **Definition:** Provides the character offset to the last character where a match is identified. For example, the last character associated with an issue in a transcript segment.
  - **Elements:** OutcomesDetected.CharacterOffsets.Begin / **Definition:** Provides the outcome, or resolution, identified in the call.
  - **Elements:** OutcomesDetected.CharacterOffsets.End
  - **Elements:** ActionItemsDetected.CharacterOffsets.Begin / **Definition:** Lists any action items identified in the call.
  - **Elements:** ActionItemsDetected.CharacterOffsets.End

- **AccountId**
  - **Data type:** string
  - **Elements:**
  - **Definition:** The AWS account Id

- **Categories**
  - **Data type:** struct
  - **Elements:** MatchedCategories / **Definition:** Lists the matched categories.
  - **Elements:** MatchedDetails / **Definition:** Lists the time, in milliseconds, from the beginning of the audio stream to when the Match in the category was detected.

- **Channel**
  - **Data type:** string
  - **Elements:** Channel
  - **Definition:** Indicates a Voice channel.

- **Participants **
  - **Data type:** array
  - **Elements:** ParticipantRole
  - **Definition:** Provides the role of the speaker for each audio channel, `CUSTOMER` or `AGENT`.

- **ConversationCharacteristics**
  - **Data type:** struct
  - **Elements:** NonTalkTime  / **Definition:** Measures periods of time that do not contain speech. Use this metric to find long periods of silence, such as a customer on hold for an excessive amount of time.
  - **Elements:** Interruptions / **Definition:** Measures if and when one participant cuts off the other participant mid-sentence. Frequent interruptions may be associated with rudeness or anger, and could correlate to negative sentiment for one or both participants.
  - **Elements:** TotalConversationDurationMillis / **Definition:** Total length of the conversation.
  - **Elements:** Sentiment.OverallSentiment.AGENT / **Definition:** `OverallSentiment` label for the Agent.
  - **Elements:** Sentiment.OverallSentiment.CUSTOMER / **Definition:** `OverallSentiment` label for the `Customer`.
  - **Elements:** Sentiment.SentimentByPeriod.QUARTER.AGENT / **Definition:** Sentiment labels for each quarter for the `Agent`.
  - **Elements:** Sentiment.SentimentByPeriod.QUARTER.CUSTOMER / **Definition:** Sentiment labels for each quarter for the `Customer`.
  - **Elements:** TalkSpeed / **Definition:** Measures the speed at which both participants are speaking. Comprehension can be affected if one participant speaks too quickly. This metric is measured in words per minute.
  - **Elements:** TalkTime / **Definition:** Measures the amount of time (in milliseconds) each participant spoke during the call. Use this metric to help identify if one participant is dominating the call or if the dialogue is balanced.

- **SessionId**
  - **Data type:** string
  - **Elements:**
  - **Definition:** `SessionId` for the call

- **ContentMetadata**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Field that labels raw vs. redacted content per the customer specified configuration.

## transcribe
<a name="ca-glue-transcribe"></a>

- **time**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Event generation timestamp ISO 8601.

- **detail-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Feature type related to service-type.

- **service-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Name of the AWS service, VoiceAnalytics or CallAnalytics.

- **mediaInsightsPipelineId**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Amazon Chime SDK media insight pipeline ID.

- **metadata**
  - **Data type:** string
  - **Elements:** voiceConnectorId / **Definition:** The Amazon Chime Voice Connector ID.
  - **Elements:** callId / **Definition:** The call ID of the participant for the associated usage.
  - **Elements:** transactionId / **Definition:** The transaction ID of the call.
  - **Elements:** fromNumber / **Definition:** E.164 origination phone number.
  - **Elements:** toNumber / **Definition:** E.164 destination phone number.
  - **Elements:** direction / **Definition:** Direction of the call, `Outbound` or `Inbound`.

- **TranscriptEvent**
  - **Data type:** struct
  - **Elements:** ResultId / **Definition:** The unique identifier for the `Result`.
  - **Elements:** StartTime  / **Definition:** The start time, in milliseconds, of the `Result`.
  - **Elements:** EndTime / **Definition:** The end time, in milliseconds, of the `Result`.
  - **Elements:** IsPartial  / **Definition:** Indicates whether the segment is complete. If `IsPartial` is `true`, the segment is not complete. Otherwise, the segment is complete.
  - **Elements:** ChannelId / **Definition:** The ID of the channel associated with the audio stream.
  - **Elements:** Alternatives.Entities / **Definition:** Contains entities identified as personally identifiable information (PII) in your transcription output.
  - **Elements:** Alternatives.Items.Confidence  / **Definition:** The confidence score associated with a word or phrase in your transcript. Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified item correctly matches the item spoken in your media.
  - **Elements:** Alternatives.Items.Content  / **Definition:** The transcribed word or punctuation mark.
  - **Elements:** Alternatives.Items.EndTime  / **Definition:** The end time, in milliseconds, of the transcribed item.
  - **Elements:** Alternatives.Items.Speaker / **Definition:** If speaker partitioning is enabled, `Speaker` labels the speaker of the specified item.
  - **Elements:** Alternatives.Items.Stable / **Definition:** If partial result stabilization is enabled. `Stable `indicates whether the specified item is stable (true) or if it may change when the segment is complete (false).
  - **Elements:** Alternatives.Items.StartTime / **Definition:** The start time, in milliseconds, of the transcribed item.
  - **Elements:** Alternatives.Items.Type / **Definition:** The type of item identified. Options: `PRONUNCIATION` (spoken words) and `PUNCTUATION`.
  - **Elements:** Alternatives.Items.VocabularyFilterMatch  / **Definition:** Indicates whether the specified item matches a word in the vocabulary filter included in your request. If true, there is a vocabulary filter match.
  - **Elements:** Alternatives.Transcript / **Definition:** Contains transcribed text.

## voice\_analytics\_status
<a name="ca-glue-va-status"></a>

- **time**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Event generation timestamp ISO 8601.

- **detail-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Feature type related to service-type.

- **service-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Name of the AWS service, VoiceAnalytics or CallAnalytics.

- **source**
  - **Data type:** string
  - **Elements:**
  - **Definition:** AWS service that produces the event.

- **account**
  - **Data type:** string
  - **Elements:**
  - **Definition:** AWS Account ID.

- **region**
  - **Data type:** string
  - **Elements:**
  - **Definition:** AWS Account Region.

- **version**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Version of the event schema.

- **id**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Unique ID of the event

- **detail**
  - **Data type:** struct
  - **Elements:** taskId / **Definition:** Unique ID of the task.
  - **Elements:** isCaller / **Definition:** Indicates whether the participant is caller or not.
  - **Elements:** streamStartTime / **Definition:** Start time of the stream.
  - **Elements:** transactionId / **Definition:** The transaction ID of the call.
  - **Elements:** voiceConnectorId / **Definition:** The Amazon Chime Voice Connector ID.
  - **Elements:** callId / **Definition:** The call ID of the participant for the associated usage.
  - **Elements:** detailStatus / **Definition:** Detailed feature type related to service-type.
  - **Elements:** statusMessage / **Definition:** Status of task ID success or failure.
  - **Elements:** mediaInsightsPipelineId / **Definition:** Amazon Chime SDK media insight pipeline ID. This field is populated only for speaker search tasks started through the Media Pipelines SDK, not the Voice SDK.
  - **Elements:** sourceArn / **Definition:** The resource ARN for which the task is run on
  - **Elements:** streamArn / **Definition:** The Kinesis Video Stream ARN that the task is run for. This field is populated only for speaker search tasks started through the Media Pipelines SDK, not the Voice SDK.
  - **Elements:** channelId / **Definition:** The channel of the streamArn that the task is run for. This field is populated only for speaker search tasks started through the Media Pipelines SDK, not the Voice SDK.
  - **Elements:**  speakerSearchDetails.voiceProfileId / **Definition:** ID of a voice profile enrolled whose voice embedding matches closely with the speaker in the call.
  - **Elements:**  speakerSearchDetails.confidenceScore / **Definition:** Number between [0, 1] where a larger number means the machine learning model is more confident about the voice profile match.

## speaker\_search\_status
<a name="ca-glue-speaker-status"></a>

- **time**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Event generation timestamp ISO 8601.

- **detail-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Feature type related to service-type.

- **service-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Name of the AWS service, VoiceAnalytics or CallAnalytics.

- **source**
  - **Data type:** string
  - **Elements:**
  - **Definition:** AWS service that produces the event.

- **account**
  - **Data type:** string
  - **Elements:**
  - **Definition:** AWS Account ID.

- **region**
  - **Data type:** string
  - **Elements:**
  - **Definition:** AWS Account Region.

- **version**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Version of the event schema.

- **id**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Unique ID of the event

- **detail**
  - **Data type:** struct
  - **Elements:** taskId / **Definition:** Unique ID of the task.
  - **Elements:** isCaller / **Definition:** Indicates whether the participant is caller or not.
  - **Elements:** transactionId / **Definition:** The transaction ID of the call. This field is populated if the task originates from a call made through a Voice Connector.
  - **Elements:** voiceConnectorId / **Definition:** The Amazon Chime Voice Connector ID. This field is populated if the task originates from a call made through a Voice Connector.
  - **Elements:** mediaInsightsPipelineId / **Definition:** The media insights pipeline ID. This field is populated only for speaker search tasks started through the Media Pipelines SDK, not the Voice SDK.
  - **Elements:** sourceArn / **Definition:** The resource ARN for which the task is run on.
  - **Elements:** streamArn / **Definition:** The Kinesis Video Stream ARN that the task is run for. This field is populated only for speaker search tasks started through the Media Pipelines SDK, not the Voice SDK.
  - **Elements:** channelId / **Definition:** The channel of the streamArn that the task is run for. This field is populated only for speaker search tasks started through the Media Pipelines SDK, not the Voice SDK.
  - **Elements:** participantRole / **Definition:** The participant role associated with the channelId in the streamArn. This field is populated only for speaker search tasks started through the Media Pipelines SDK, not the Voice SDK.
  - **Elements:** detailStatus / **Definition:** Detailed feature type related to service-type.
  - **Elements:** statusMessage / **Definition:** Status of task ID, success or failure.
  - **Elements:** speakerSearchDetails.voiceProfileId / **Definition:** ID of a voice profile enrolled whose voice embedding matches closely with the speaker in the call.
  - **Elements:** speakerSearchDetails.confidenceScore / **Definition:** Number between [0, 1] where a larger number means the machine learning model is more confident about the voice profile match.

## voice\_tone\_analysis\_status
<a name="ca-glue-tone-status"></a>

- **time**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Event generation timestamp ISO 8601.

- **detail-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Feature type related to service-type.

- **service-type**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Name of the AWS service, VoiceAnalytics or CallAnalytics.

- **source**
  - **Data type:** string
  - **Elements:**
  - **Definition:** AWS service that produces the event.

- **account**
  - **Data type:** string
  - **Elements:**
  - **Definition:** AWS Account ID.

- **region**
  - **Data type:** string
  - **Elements:**
  - **Definition:** AWS Account Region.

- **version**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Version of the event schema.

- **id**
  - **Data type:** string
  - **Elements:**
  - **Definition:** Unique ID of the event

- **detail**
  - **Data type:** struct
  - **Elements:** taskId / **Definition:** Unique ID of the task.
  - **Elements:** isCaller / **Definition:** Indicates whether the participant is caller or not.
  - **Elements:** transactionId / **Definition:** The transaction ID of the call. This field is populated if the task originates from a call made through a Voice Connector.
  - **Elements:** voiceConnectorId / **Definition:** The Amazon Chime Voice Connector ID. This field is populated if the task originates from a call made through a Voice Connector.
  - **Elements:** mediaInsightsPipelineId / **Definition:** The media insights pipeline ID. This field is populated only for speaker search tasks started through the Media Pipelines SDK, not the Voice SDK.
  - **Elements:** sourceArn / **Definition:** The resource ARN for which the task is run on.
  - **Elements:** streamArn / **Definition:** The Kinesis Video Stream ARN that the task is run for. This field is populated only for speaker search tasks started through the Media Pipelines SDK, not the Voice SDK.
  - **Elements:** channelId / **Definition:** The channel of the streamArn that the task is run for. This field is populated only for speaker search tasks started through the Media Pipelines SDK, not the Voice SDK.
  - **Elements:** participantRole / **Definition:** The participant role associated with the channelId in the streamArn. This field is populated only for speaker search tasks started through the Media Pipelines SDK, not the Voice SDK.
  - **Elements:** statusMessage / **Definition:** Status of task ID success or failure.
  - **Elements:** voiceToneAnalysisDetails.startFragmentNumber / **Definition:** Starting fragment number associated with the streamArn.
  - **Elements:** voiceToneAnalysisDetails.currentAverageVoiceTone.startTime  / **Definition:** Starting timestamp in ISO8601 format for the speaker's call audio that the current average sentiment is based on.
  - **Elements:** voiceToneAnalysisDetails.currentAverageVoiceTone.endTime / **Definition:** Ending timestamp in ISO8601 format for the speaker's call audio that the current average sentiment is based on.
  - **Elements:** voiceToneAnalysisDetails.currentAverageVoiceTone.beginOffsetMillis / **Definition:** Beginning offset in milliseconds from the starting fragment for the speaker's call audio that the current average sentiment is based on.
  - **Elements:** voiceToneAnalysisDetails.currentAverageVoiceTone.endOffsetMillis / **Definition:** Ending offset in milliseconds from the starting fragment for the speaker's call audio that the current average sentiment is based on.
  - **Elements:** voiceToneAnalysisDetails.currentAverageVoiceTone.voiceToneScore.positive / **Definition:** Probabilistic likelihood between [0, 1] that the speaker's sentiment is positive.
  - **Elements:** voiceToneAnalysisDetails.currentAverageVoiceTone.voiceToneScore.negative / **Definition:** Probabilistic likelihood between [0, 1] that the speaker's sentiment is negative.
  - **Elements:** voiceToneAnalysisDetails.currentAverageVoiceTone.voiceToneScore.neutral / **Definition:** Probabilistic likelihood between [0, 1] that the speaker's sentiment is neutral.
  - **Elements:** voiceToneAnalysisDetails.currentAverageVoiceTone.voiceToneLabel / **Definition:** Label with highest probability for the average voice tone score.
  - **Elements:** voiceToneAnalysisDetails.overallAverageVoiceTone.startTime  / **Definition:** Starting timestamp in ISO8601 format for the speaker's call audio that the overall average sentiment is based on.
  - **Elements:** voiceToneAnalysisDetails.overallAverageVoiceTone.endTime / **Definition:**  Ending timestamp in ISO8601 format for the speaker's call audio that the overall average sentiment is based on.
  - **Elements:** voiceToneAnalysisDetails.overallAverageVoiceTone.beginOffsetMillis / **Definition:** Beginning offset in milliseconds from the starting fragment for the speaker's call audio that the overall average sentiment is based on.
  - **Elements:** voiceToneAnalysisDetails.overallAverageVoiceTone.endOffsetMillis / **Definition:** Ending offset in milliseconds from the starting fragment for the speaker's call audio that the overall average sentiment is based on.
  - **Elements:** voiceToneAnalysisDetails.overallAverageVoiceTone.voiceToneScore.positive  / **Definition:** Probabilistic likelihood between [0, 1] that the speaker's sentiment is positive.
  - **Elements:** voiceToneAnalysisDetails.overallAverageVoiceTone.voiceToneScore.negative / **Definition:** Probabilistic likelihood between [0, 1] that the speaker's sentiment is negative.
  - **Elements:** voiceToneAnalysisDetails.overallAverageVoiceTone.voiceToneScore.neutral / **Definition:** Probabilistic likelihood between [0, 1] that the speaker's sentiment is neutral.
  - **Elements:** voiceToneAnalysisDetails.overallAverageVoiceTone.voiceToneLabel / **Definition:** Sentiment label (positive, negative, or neutral) with the highest sentiment score.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
