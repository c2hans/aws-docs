---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ApplicationComponentStrategy.html
---

# ApplicationComponentStrategy
<a name="API_ApplicationComponentStrategy"></a>

 Contains information about a strategy recommendation for an application component.

## Contents
<a name="API_ApplicationComponentStrategy_Contents"></a>

 ** isPreferred **   <a name="migrationhubstrategy-Type-ApplicationComponentStrategy-isPreferred"></a>
 Set to true if the recommendation is set as preferred.
Type: Boolean
Required: No

 ** recommendation **   <a name="migrationhubstrategy-Type-ApplicationComponentStrategy-recommendation"></a>
 Strategy recommendation for the application component.
Type: [RecommendationSet](API_RecommendationSet.md) object
Required: No

 ** status **   <a name="migrationhubstrategy-Type-ApplicationComponentStrategy-status"></a>
 The recommendation status of a strategy for an application component.
Type: String
Valid Values: `recommended | viableOption | notRecommended | potential`
Required: No

## See Also
<a name="API_ApplicationComponentStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/ApplicationComponentStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/ApplicationComponentStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/ApplicationComponentStrategy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
