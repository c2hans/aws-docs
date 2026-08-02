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
