---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_GroupingRecommendation.html
---

# GroupingRecommendation
<a name="API_GroupingRecommendation"></a>

Creates a new grouping recommendation.

## Contents
<a name="API_GroupingRecommendation_Contents"></a>

 ** confidenceLevel **   <a name="resiliencehub-Type-GroupingRecommendation-confidenceLevel"></a>
Indicates the confidence level of AWS Resilience Hub on the grouping recommendation.
Type: String
Valid Values: `High | Medium`
Required: Yes

 ** creationTime **   <a name="resiliencehub-Type-GroupingRecommendation-creationTime"></a>
Indicates the creation time of the grouping recommendation.
Type: Timestamp
Required: Yes

 ** groupingAppComponent **   <a name="resiliencehub-Type-GroupingRecommendation-groupingAppComponent"></a>
Indicates the name of the recommended Application Component (AppComponent).
Type: [GroupingAppComponent](API_GroupingAppComponent.md) object
Required: Yes

 ** groupingRecommendationId **   <a name="resiliencehub-Type-GroupingRecommendation-groupingRecommendationId"></a>
Indicates all the reasons available for rejecting a grouping recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** recommendationReasons **   <a name="resiliencehub-Type-GroupingRecommendation-recommendationReasons"></a>
Indicates all the reasons available for rejecting a grouping recommendation.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** resources **   <a name="resiliencehub-Type-GroupingRecommendation-resources"></a>
Indicates the resources that are grouped in a recommended AppComponent.
Type: Array of [GroupingResource](API_GroupingResource.md) objects
Required: Yes

 ** score **   <a name="resiliencehub-Type-GroupingRecommendation-score"></a>
Indicates the confidence level of the grouping recommendation.
Type: Double
Required: Yes

 ** status **   <a name="resiliencehub-Type-GroupingRecommendation-status"></a>
Indicates the status of grouping resources into AppComponents.
Type: String
Valid Values: `Accepted | Rejected | PendingDecision`
Required: Yes

 ** rejectionReason **   <a name="resiliencehub-Type-GroupingRecommendation-rejectionReason"></a>
Indicates the reason you had selected while rejecting a grouping recommendation.
Type: String
Valid Values: `DistinctBusinessPurpose | SeparateDataConcern | DistinctUserGroupHandling | Other`
Required: No

## See Also
<a name="API_GroupingRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/GroupingRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/GroupingRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/GroupingRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
