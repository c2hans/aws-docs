---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunitySearchInsights.html
---

# OpportunitySearchInsights

Contains the insight scores (engagement score and opportunity quality score) returned for an opportunity in search results.

## Contents
<a name="API_OpportunitySearchInsights_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EngagementScore **   <a name="AWSPartnerCentral-Type-OpportunitySearchInsights-EngagementScore"></a>
The level of engagement with the opportunity. The value is `High`, `Medium`, or `Low`.
Type: String
Valid Values: `High | Medium | Low`
Required: No

 ** OpportunityQuality **   <a name="AWSPartnerCentral-Type-OpportunitySearchInsights-OpportunityQuality"></a>
The opportunity quality score. Null when the opportunity has not yet been scored.
Type: [OpportunitySearchOpportunityQuality](API_OpportunitySearchOpportunityQuality.md) object
Required: No

## See Also
<a name="API_OpportunitySearchInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunitySearchInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunitySearchInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunitySearchInsights)
