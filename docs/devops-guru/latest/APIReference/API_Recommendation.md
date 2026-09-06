---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_Recommendation.html
---

# Recommendation
<a name="API_Recommendation"></a>

 Recommendation information to help you remediate detected anomalous behavior that generated an insight.

## Contents
<a name="API_Recommendation_Contents"></a>

 ** Category **   <a name="DevOpsGuru-Type-Recommendation-Category"></a>
The category type of the recommendation.
Type: String
Required: No

 ** Description **   <a name="DevOpsGuru-Type-Recommendation-Description"></a>
 A description of the problem.
Type: String
Required: No

 ** Link **   <a name="DevOpsGuru-Type-Recommendation-Link"></a>
 A hyperlink to information to help you address the problem.
Type: String
Required: No

 ** Name **   <a name="DevOpsGuru-Type-Recommendation-Name"></a>
 The name of the recommendation.
Type: String
Required: No

 ** Reason **   <a name="DevOpsGuru-Type-Recommendation-Reason"></a>
 The reason DevOps Guru flagged the anomalous behavior as a problem.
Type: String
Required: No

 ** RelatedAnomalies **   <a name="DevOpsGuru-Type-Recommendation-RelatedAnomalies"></a>
 Anomalies that are related to the problem. Use these Anomalies to learn more about what's happening and to help address the issue.
Type: Array of [RecommendationRelatedAnomaly](API_RecommendationRelatedAnomaly.md) objects
Required: No

 ** RelatedEvents **   <a name="DevOpsGuru-Type-Recommendation-RelatedEvents"></a>
 Events that are related to the problem. Use these events to learn more about what's happening and to help address the issue.
Type: Array of [RecommendationRelatedEvent](API_RecommendationRelatedEvent.md) objects
Required: No

## See Also
<a name="API_Recommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/Recommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/Recommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/Recommendation)
