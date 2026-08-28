---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_RecommendationResourcesAggregates.html
---

# RecommendationResourcesAggregates
<a name="API_RecommendationResourcesAggregates"></a>

Aggregation of Recommendation Resources

## Contents
<a name="API_RecommendationResourcesAggregates_Contents"></a>

 ** errorCount **   <a name="ta-Type-RecommendationResourcesAggregates-errorCount"></a>
The number of AWS resources that were flagged to have errors according to the Trusted Advisor check
Type: Long
Required: Yes

 ** okCount **   <a name="ta-Type-RecommendationResourcesAggregates-okCount"></a>
The number of AWS resources that were flagged to be OK according to the Trusted Advisor check
Type: Long
Required: Yes

 ** warningCount **   <a name="ta-Type-RecommendationResourcesAggregates-warningCount"></a>
The number of AWS resources that were flagged to have warning according to the Trusted Advisor check
Type: Long
Required: Yes

 ** excludedCount **   <a name="ta-Type-RecommendationResourcesAggregates-excludedCount"></a>
The number of AWS resources belonging to this Trusted Advisor check that were excluded by the customer
Type: Long
Required: No

## See Also
<a name="API_RecommendationResourcesAggregates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/RecommendationResourcesAggregates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/RecommendationResourcesAggregates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/RecommendationResourcesAggregates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Trusted Advisor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query trustedadvisor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
