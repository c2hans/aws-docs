---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RecommendationDetailHourlyMetrics.html
---

# RecommendationDetailHourlyMetrics
<a name="API_RecommendationDetailHourlyMetrics"></a>

Contains the hourly metrics for the given recommendation over the lookback period.

## Contents
<a name="API_RecommendationDetailHourlyMetrics_Contents"></a>

 ** CurrentCoverage **   <a name="awscostmanagement-Type-RecommendationDetailHourlyMetrics-CurrentCoverage"></a>
The current amount of Savings Plans eligible usage that the Savings Plan covered.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedCoverage **   <a name="awscostmanagement-Type-RecommendationDetailHourlyMetrics-EstimatedCoverage"></a>
The estimated coverage amount based on the recommended Savings Plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedNewCommitmentUtilization **   <a name="awscostmanagement-Type-RecommendationDetailHourlyMetrics-EstimatedNewCommitmentUtilization"></a>
The estimated utilization for the recommended Savings Plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedOnDemandCost **   <a name="awscostmanagement-Type-RecommendationDetailHourlyMetrics-EstimatedOnDemandCost"></a>
The remaining On-Demand cost estimated to not be covered by the recommended Savings Plan, over the length of the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** StartTime **   <a name="awscostmanagement-Type-RecommendationDetailHourlyMetrics-StartTime"></a>
The period of time that you want the usage and costs for.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

## See Also
<a name="API_RecommendationDetailHourlyMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/RecommendationDetailHourlyMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/RecommendationDetailHourlyMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/RecommendationDetailHourlyMetrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
