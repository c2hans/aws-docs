---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AggregatedUtterancesSummary.html
---

# AggregatedUtterancesSummary
<a name="API_AggregatedUtterancesSummary"></a>

Provides summary information for aggregated utterances. The `ListAggregatedUtterances` operations combines all instances of the same utterance into a single aggregated summary.

## Contents
<a name="API_AggregatedUtterancesSummary_Contents"></a>

 ** containsDataFromDeletedResources **   <a name="lexv2-Type-AggregatedUtterancesSummary-containsDataFromDeletedResources"></a>
Aggregated utterance data may contain utterances from versions of your bot that have since been deleted. When the aggregated contains this kind of data, this field is set to true.
Type: Boolean
Required: No

 ** hitCount **   <a name="lexv2-Type-AggregatedUtterancesSummary-hitCount"></a>
The number of times that the utterance was detected by Amazon Lex during the time period. When an utterance is detected, it activates an intent or a slot.
Type: Integer
Required: No

 ** missedCount **   <a name="lexv2-Type-AggregatedUtterancesSummary-missedCount"></a>
The number of times that the utterance was missed by Amazon Lex An utterance is missed when it doesn't activate an intent or slot.
Type: Integer
Required: No

 ** utterance **   <a name="lexv2-Type-AggregatedUtterancesSummary-utterance"></a>
The text of the utterance. If the utterance was used with the `RecognizeUtterance` operation, the text is the transcription of the audio utterance.
Type: String
Required: No

 ** utteranceFirstRecordedInAggregationDuration **   <a name="lexv2-Type-AggregatedUtterancesSummary-utteranceFirstRecordedInAggregationDuration"></a>
The date and time that the utterance was first recorded in the time window for aggregation. An utterance may have been sent to Amazon Lex before that time, but only utterances within the time window are counted.
Type: Timestamp
Required: No

 ** utteranceLastRecordedInAggregationDuration **   <a name="lexv2-Type-AggregatedUtterancesSummary-utteranceLastRecordedInAggregationDuration"></a>
The last date and time that an utterance was recorded in the time window for aggregation. An utterance may be sent to Amazon Lex after that time, but only utterances within the time window are counted.
Type: Timestamp
Required: No

## See Also
<a name="API_AggregatedUtterancesSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AggregatedUtterancesSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AggregatedUtterancesSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AggregatedUtterancesSummary)
