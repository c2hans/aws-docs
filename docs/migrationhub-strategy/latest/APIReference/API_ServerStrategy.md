---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ServerStrategy.html
---

# ServerStrategy
<a name="API_ServerStrategy"></a>

 Contains information about a strategy recommendation for a server.

## Contents
<a name="API_ServerStrategy_Contents"></a>

 ** isPreferred **   <a name="migrationhubstrategy-Type-ServerStrategy-isPreferred"></a>
 Set to true if the recommendation is set as preferred.
Type: Boolean
Required: No

 ** numberOfApplicationComponents **   <a name="migrationhubstrategy-Type-ServerStrategy-numberOfApplicationComponents"></a>
 The number of application components with this strategy recommendation running on the server.
Type: Integer
Required: No

 ** recommendation **   <a name="migrationhubstrategy-Type-ServerStrategy-recommendation"></a>
 Strategy recommendation for the server.
Type: [RecommendationSet](API_RecommendationSet.md) object
Required: No

 ** status **   <a name="migrationhubstrategy-Type-ServerStrategy-status"></a>
 The recommendation status of the strategy for the server.
Type: String
Valid Values: `recommended | viableOption | notRecommended | potential`
Required: No

## See Also
<a name="API_ServerStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/ServerStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/ServerStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/ServerStrategy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
