---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormItemEnablementSource.html
---

# EvaluationFormItemEnablementSource

An enablement expression source item.

## Contents
<a name="API_EvaluationFormItemEnablementSource_Contents"></a>

 ** Type **   <a name="connect-Type-EvaluationFormItemEnablementSource-Type"></a>
A type of source item. Valid values:
+  `QUESTION_REF_ID` - The answer to another question in the evaluation form.
+  `CONTACT` - Data from the evaluated contact.
+  `EVALUATION_METADATA` - Metadata of the evaluation, such as the evaluation type.
+  `AI_METRICS` - Metrics about AI agents, AI sessions, and AI tools on the contact.
Type: String
Valid Values: `QUESTION_REF_ID | CONTACT | EVALUATION_METADATA | FORM_METADATA | AI_METRICS`
Required: Yes

 ** AiMetricsField **   <a name="connect-Type-EvaluationFormItemEnablementSource-AiMetricsField"></a>
The AI metrics field to use as the source. Use when `Type` is `AI_METRICS`.
Type: String
Valid Values: `AI_SESSION_IS_HANDED_OFF | AI_SESSION_SELF_SERVICE_DURATION | AI_SESSION_GOAL_SUCCESS_RATE | AI_SESSION_COMPLETENESS_SCORE | AI_SESSION_FAITHFULNESS_SCORE | AI_AGENT_MAX_PROMPT_LATENCY | AI_TOOL_MAX_LATENCY | AI_TOOL_SELECTION_ACCURACY | AI_TOOL_PARAMETER_ACCURACY | AI_TOOL_UTILIZATION_ACCURACY`
Required: No

 ** ContactAttributeKey **   <a name="connect-Type-EvaluationFormItemEnablementSource-ContactAttributeKey"></a>
The key of the contact attribute to use as the source. Use when `Type` is `CONTACT`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32767.
Required: No

 ** ContactField **   <a name="connect-Type-EvaluationFormItemEnablementSource-ContactField"></a>
The contact field to use as the source, such as `CHANNEL`, `QUEUE_ARN`, `OVERALL_CUSTOMER_SENTIMENT_SCORE`, or `RECORDING_MEDIA_STREAM_TYPES`. Use when `Type` is `CONTACT`.
Type: String
Valid Values: `CATEGORIES | AGENT_ARN | QUEUE_ARN | ROUTING_PROFILE_ARN | CHANNEL | INITIATION_METHOD | IS_QUEUED | OVERALL_CUSTOMER_SENTIMENT_SCORE | OVERALL_AGENT_SENTIMENT_SCORE | CUSTOMER_SENTIMENT_SCORE_WITHOUT_AGENT | CUSTOMER_SENTIMENT_SCORE_WITH_AGENT | NON_TALK_TIME | NON_TALK_TIME_PERCENTAGE | NUMBER_OF_INTERRUPTIONS | CONTACT_DURATION | AGENT_INTERACTION_DURATION | CUSTOMER_HOLD_TIME | LONGEST_HOLD_DURATION | NUMBER_OF_HOLDS | AGENT_INTERACTION_AND_HOLD_DURATION | RECORDING_MEDIA_STREAM_TYPES`
Required: No

 ** EvaluationMetadataField **   <a name="connect-Type-EvaluationFormItemEnablementSource-EvaluationMetadataField"></a>
The evaluation metadata field to use as the source. Use when `Type` is `EVALUATION_METADATA`.
Type: String
Valid Values: `EVALUATION_TYPE`
Required: No

 ** RefId **   <a name="connect-Type-EvaluationFormItemEnablementSource-RefId"></a>
A referenceId of the source item. Use when `Type` is `QUESTION_REF_ID`.
Type: String
Required: No

 ** SegmentAttributeKey **   <a name="connect-Type-EvaluationFormItemEnablementSource-SegmentAttributeKey"></a>
The key of the contact segment attribute to use as the source. Use when `Type` is `CONTACT`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_EvaluationFormItemEnablementSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormItemEnablementSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormItemEnablementSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormItemEnablementSource)
