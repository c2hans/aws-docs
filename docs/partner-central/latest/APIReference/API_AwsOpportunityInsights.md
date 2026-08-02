---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AwsOpportunityInsights.html
---

# AwsOpportunityInsights
<a name="API_AwsOpportunityInsights"></a>

Contains insights provided by AWS for the opportunity, offering recommendations and analysis that can help the partner optimize their engagement and strategy.

## Contents
<a name="API_AwsOpportunityInsights_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AwsProductsSpendInsightsBySource **   <a name="AWSPartnerCentral-Type-AwsOpportunityInsights-AwsProductsSpendInsightsBySource"></a>
Source-separated spend insights that provide independent analysis for AWS recommendations and partner estimates.
Type: [AwsProductsSpendInsightsBySource](API_AwsProductsSpendInsightsBySource.md) object
Required: No

 ** EngagementScore **   <a name="AWSPartnerCentral-Type-AwsOpportunityInsights-EngagementScore"></a>
Represents a score assigned by AWS to indicate the level of engagement and potential success for the opportunity. This score helps partners prioritize their efforts.
Type: String
Valid Values: `High | Medium | Low`
Required: No

 ** NextBestActions **   <a name="AWSPartnerCentral-Type-AwsOpportunityInsights-NextBestActions"></a>
Provides recommendations from AWS on the next best actions to take in order to move the opportunity forward and increase the likelihood of success.
Type: String
Required: No

 ** OpportunityQuality **   <a name="AWSPartnerCentral-Type-AwsOpportunityInsights-OpportunityQuality"></a>
Opportunity quality assessment. Null if not yet scored.
Type: [OpportunityQuality](API_OpportunityQuality.md) object
Required: No

 ** Recommendations **   <a name="AWSPartnerCentral-Type-AwsOpportunityInsights-Recommendations"></a>
List of recommendations from various agent-driven sources.
Type: Array of [Recommendation](API_Recommendation.md) objects
Required: No

## See Also
<a name="API_AwsOpportunityInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AwsOpportunityInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AwsOpportunityInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AwsOpportunityInsights)
