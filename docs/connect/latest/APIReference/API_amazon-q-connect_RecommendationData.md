---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_RecommendationData.html
---

# RecommendationData
<a name="API_amazon-q-connect_RecommendationData"></a>

Information about the recommendation.

## Contents
<a name="API_amazon-q-connect_RecommendationData_Contents"></a>

 ** recommendationId **   <a name="connect-Type-amazon-q-connect_RecommendationData-recommendationId"></a>
The identifier of the recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** data **   <a name="connect-Type-amazon-q-connect_RecommendationData-data"></a>
 Summary of the recommended content.
Type: [DataSummary](API_amazon-q-connect_DataSummary.md) object
Required: No

 ** document **   <a name="connect-Type-amazon-q-connect_RecommendationData-document"></a>
The recommended document.
Type: [Document](API_amazon-q-connect_Document.md) object
Required: No

 ** relevanceLevel **   <a name="connect-Type-amazon-q-connect_RecommendationData-relevanceLevel"></a>
The relevance level of the recommendation.
Type: String
Valid Values: `HIGH | MEDIUM | LOW`
Required: No

 ** relevanceScore **   <a name="connect-Type-amazon-q-connect_RecommendationData-relevanceScore"></a>
The relevance score of the recommendation.
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

 ** type **   <a name="connect-Type-amazon-q-connect_RecommendationData-type"></a>
The type of recommendation.
Type: String
Valid Values: `KNOWLEDGE_CONTENT | GENERATIVE_RESPONSE | GENERATIVE_ANSWER | DETECTED_INTENT | GENERATIVE_ANSWER_CHUNK | BLOCKED_GENERATIVE_ANSWER_CHUNK | INTENT_ANSWER_CHUNK | BLOCKED_INTENT_ANSWER_CHUNK | EMAIL_RESPONSE_CHUNK | EMAIL_OVERVIEW_CHUNK | EMAIL_GENERATIVE_ANSWER_CHUNK | CASE_SUMMARIZATION_CHUNK | BLOCKED_CASE_SUMMARIZATION_CHUNK | SUGGESTED_MESSAGE | NOTES_CHUNK | BLOCKED_NOTES_CHUNK`
Required: No

## See Also
<a name="API_amazon-q-connect_RecommendationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/RecommendationData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/RecommendationData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/RecommendationData)
