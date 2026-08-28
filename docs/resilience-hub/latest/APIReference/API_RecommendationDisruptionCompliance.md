---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_RecommendationDisruptionCompliance.html
---

# RecommendationDisruptionCompliance
<a name="API_RecommendationDisruptionCompliance"></a>

Defines a disruption compliance recommendation.

## Contents
<a name="API_RecommendationDisruptionCompliance_Contents"></a>

 ** expectedComplianceStatus **   <a name="resiliencehub-Type-RecommendationDisruptionCompliance-expectedComplianceStatus"></a>
The expected compliance status after applying the recommended configuration change.
Type: String
Valid Values: `PolicyBreached | PolicyMet | NotApplicable | MissingPolicy`
Required: Yes

 ** expectedRpoDescription **   <a name="resiliencehub-Type-RecommendationDisruptionCompliance-expectedRpoDescription"></a>
The expected Recovery Point Objective (RPO) description after applying the recommended configuration change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** expectedRpoInSecs **   <a name="resiliencehub-Type-RecommendationDisruptionCompliance-expectedRpoInSecs"></a>
The expected RPO after applying the recommended configuration change.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** expectedRtoDescription **   <a name="resiliencehub-Type-RecommendationDisruptionCompliance-expectedRtoDescription"></a>
The expected Recovery Time Objective (RTO) description after applying the recommended configuration change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** expectedRtoInSecs **   <a name="resiliencehub-Type-RecommendationDisruptionCompliance-expectedRtoInSecs"></a>
The expected RTO after applying the recommended configuration change.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_RecommendationDisruptionCompliance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/RecommendationDisruptionCompliance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/RecommendationDisruptionCompliance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/RecommendationDisruptionCompliance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
