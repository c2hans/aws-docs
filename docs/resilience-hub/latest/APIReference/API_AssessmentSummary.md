---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_AssessmentSummary.html
---

# AssessmentSummary
<a name="API_AssessmentSummary"></a>

Indicates the AI-generated summary for the AWS Resilience Hub assessment, providing a concise overview that highlights the top risks and recommendations.

**Note**
This property is available only in the US East (N. Virginia) Region.

## Contents
<a name="API_AssessmentSummary_Contents"></a>

 ** riskRecommendations **   <a name="resiliencehub-Type-AssessmentSummary-riskRecommendations"></a>
Indicates the top risks and recommendations identified by the AWS Resilience Hub assessment, each representing a specific risk and the corresponding recommendation to address it.
This property is available only in the US East (N. Virginia) Region.
Type: Array of [AssessmentRiskRecommendation](API_AssessmentRiskRecommendation.md) objects
Required: No

 ** summary **   <a name="resiliencehub-Type-AssessmentSummary-summary"></a>
Indicates a concise summary that provides an overview of the AWS Resilience Hub assessment.
This property is available only in the US East (N. Virginia) Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## See Also
<a name="API_AssessmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/AssessmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/AssessmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/AssessmentSummary)
