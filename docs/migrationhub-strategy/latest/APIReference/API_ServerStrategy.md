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
