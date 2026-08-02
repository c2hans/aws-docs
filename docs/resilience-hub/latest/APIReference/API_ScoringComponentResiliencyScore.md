---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ScoringComponentResiliencyScore.html
---

# ScoringComponentResiliencyScore
<a name="API_ScoringComponentResiliencyScore"></a>

Resiliency score of each scoring component. For more information about scoring component, see [Calculating resiliency score](https://docs.aws.amazon.com/resilience-hub/latest/userguide/calculate-score.html).

## Contents
<a name="API_ScoringComponentResiliencyScore_Contents"></a>

 ** excludedCount **   <a name="resiliencehub-Type-ScoringComponentResiliencyScore-excludedCount"></a>
Number of recommendations that were excluded from the assessment.
For example, if the `excludedCount` for Alarms coverage scoring component is 7, it indicates that 7 Amazon CloudWatch alarms are excluded from the assessment.
Type: Long
Required: No

 ** outstandingCount **   <a name="resiliencehub-Type-ScoringComponentResiliencyScore-outstandingCount"></a>
Number of recommendations that must be implemented to obtain the maximum possible score for the scoring component. For SOPs, alarms, and tests, these are the number of recommendations that must be implemented. For compliance, these are the number of Application Components that have breached the resiliency policy.
For example, if the `outstandingCount` for Alarms coverage scoring component is 5, it indicates that 5 Amazon CloudWatch alarms need to be implemented to achieve the maximum possible score.
Type: Long
Required: No

 ** possibleScore **   <a name="resiliencehub-Type-ScoringComponentResiliencyScore-possibleScore"></a>
Maximum possible score that can be obtained for the scoring component.
For example, if the `possibleScore` is 20 points, it indicates the maximum possible score you can achieve for the scoring component when you run a new assessment after implementing all the AWS Resilience Hub recommendations.
Type: Double
Required: No

 ** score **   <a name="resiliencehub-Type-ScoringComponentResiliencyScore-score"></a>
Resiliency score points given for the scoring component. The score is always less than or equal to the `possibleScore`.
Type: Double
Required: No

## See Also
<a name="API_ScoringComponentResiliencyScore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ScoringComponentResiliencyScore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ScoringComponentResiliencyScore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ScoringComponentResiliencyScore)
