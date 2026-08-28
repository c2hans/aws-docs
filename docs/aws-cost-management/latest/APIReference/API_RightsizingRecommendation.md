---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RightsizingRecommendation.html
---

# RightsizingRecommendation
<a name="API_RightsizingRecommendation"></a>

Recommendations to rightsize resources.

## Contents
<a name="API_RightsizingRecommendation_Contents"></a>

 ** AccountId **   <a name="awscostmanagement-Type-RightsizingRecommendation-AccountId"></a>
The account that this recommendation is for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrentInstance **   <a name="awscostmanagement-Type-RightsizingRecommendation-CurrentInstance"></a>
Context regarding the current instance.
Type: [CurrentInstance](API_CurrentInstance.md) object
Required: No

 ** FindingReasonCodes **   <a name="awscostmanagement-Type-RightsizingRecommendation-FindingReasonCodes"></a>
The list of possible reasons why the recommendation is generated, such as under- or over-utilization of specific metrics (for example, CPU, Memory, Network).
Type: Array of strings
Valid Values: `CPU_OVER_PROVISIONED | CPU_UNDER_PROVISIONED | MEMORY_OVER_PROVISIONED | MEMORY_UNDER_PROVISIONED | EBS_THROUGHPUT_OVER_PROVISIONED | EBS_THROUGHPUT_UNDER_PROVISIONED | EBS_IOPS_OVER_PROVISIONED | EBS_IOPS_UNDER_PROVISIONED | NETWORK_BANDWIDTH_OVER_PROVISIONED | NETWORK_BANDWIDTH_UNDER_PROVISIONED | NETWORK_PPS_OVER_PROVISIONED | NETWORK_PPS_UNDER_PROVISIONED | DISK_IOPS_OVER_PROVISIONED | DISK_IOPS_UNDER_PROVISIONED | DISK_THROUGHPUT_OVER_PROVISIONED | DISK_THROUGHPUT_UNDER_PROVISIONED`
Required: No

 ** ModifyRecommendationDetail **   <a name="awscostmanagement-Type-RightsizingRecommendation-ModifyRecommendationDetail"></a>
The details for the modification recommendations.
Type: [ModifyRecommendationDetail](API_ModifyRecommendationDetail.md) object
Required: No

 ** RightsizingType **   <a name="awscostmanagement-Type-RightsizingRecommendation-RightsizingType"></a>
A recommendation to either terminate or modify the resource.
Type: String
Valid Values: `TERMINATE | MODIFY`
Required: No

 ** TerminateRecommendationDetail **   <a name="awscostmanagement-Type-RightsizingRecommendation-TerminateRecommendationDetail"></a>
The details for termination recommendations.
Type: [TerminateRecommendationDetail](API_TerminateRecommendationDetail.md) object
Required: No

## See Also
<a name="API_RightsizingRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/RightsizingRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/RightsizingRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/RightsizingRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
