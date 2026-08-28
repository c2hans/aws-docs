---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_RecommendationRelatedAnomaly.html
---

# RecommendationRelatedAnomaly
<a name="API_RecommendationRelatedAnomaly"></a>

 Information about an anomaly that is related to a recommendation.

## Contents
<a name="API_RecommendationRelatedAnomaly_Contents"></a>

 ** AnomalyId **   <a name="DevOpsGuru-Type-RecommendationRelatedAnomaly-AnomalyId"></a>
The ID of an anomaly that generated the insight with this recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w~.-]*$`
Required: No

 ** Resources **   <a name="DevOpsGuru-Type-RecommendationRelatedAnomaly-Resources"></a>
 An array of objects that represent resources in which DevOps Guru detected anomalous behavior. Each object contains the name and type of the resource.
Type: Array of [RecommendationRelatedAnomalyResource](API_RecommendationRelatedAnomalyResource.md) objects
Required: No

 ** SourceDetails **   <a name="DevOpsGuru-Type-RecommendationRelatedAnomaly-SourceDetails"></a>
 Information about where the anomalous behavior related the recommendation was found. For example, details in Amazon CloudWatch metrics.
Type: Array of [RecommendationRelatedAnomalySourceDetail](API_RecommendationRelatedAnomalySourceDetail.md) objects
Required: No

## See Also
<a name="API_RecommendationRelatedAnomaly_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/RecommendationRelatedAnomaly)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/RecommendationRelatedAnomaly)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/RecommendationRelatedAnomaly)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
