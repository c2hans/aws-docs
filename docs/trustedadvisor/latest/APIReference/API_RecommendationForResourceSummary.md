---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_RecommendationForResourceSummary.html
---

# RecommendationForResourceSummary
<a name="API_RecommendationForResourceSummary"></a>

Summary of a Recommendation for a specific AWS Resource

## Contents
<a name="API_RecommendationForResourceSummary_Contents"></a>

 ** awsResourceArn **   <a name="ta-Type-RecommendationForResourceSummary-awsResourceArn"></a>
The AWS Resource ARN
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*`
Required: Yes

 ** checkArn **   <a name="ta-Type-RecommendationForResourceSummary-checkArn"></a>
The Check ARN
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w-]+:trustedadvisor:::check\/[\w-]+`
Required: Yes

 ** exclusionStatus **   <a name="ta-Type-RecommendationForResourceSummary-exclusionStatus"></a>
The exclusion status of the recommendation
Type: String
Valid Values: `excluded | included`
Required: Yes

 ** lastUpdatedAt **   <a name="ta-Type-RecommendationForResourceSummary-lastUpdatedAt"></a>
When the recommendation was last updated
Type: Timestamp
Required: Yes

 ** metadata **   <a name="ta-Type-RecommendationForResourceSummary-metadata"></a>
Metadata associated with the recommendation
Type: String to string map
Required: Yes

 ** pillars **   <a name="ta-Type-RecommendationForResourceSummary-pillars"></a>
The Pillars that the Recommendation is optimizing
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Valid Values: `cost_optimizing | performance | security | service_limits | fault_tolerance | operational_excellence`
Required: Yes

 ** recommendationArn **   <a name="ta-Type-RecommendationForResourceSummary-recommendationArn"></a>
The Recommendation ARN
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w-]+:trustedadvisor::\d{12}:recommendation\/[\w-]+`
Required: Yes

 ** status **   <a name="ta-Type-RecommendationForResourceSummary-status"></a>
The current status of the recommendation
Type: String
Valid Values: `ok | warning | error`
Required: Yes

## See Also
<a name="API_RecommendationForResourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/RecommendationForResourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/RecommendationForResourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/RecommendationForResourceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Trusted Advisor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query trustedadvisor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
