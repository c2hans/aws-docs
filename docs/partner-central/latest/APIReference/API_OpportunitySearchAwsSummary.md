---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunitySearchAwsSummary.html
---

# OpportunitySearchAwsSummary

Contains the AWS-sourced fields (co-sell motion and a trimmed set of insights) returned for an opportunity in search results.

## Contents
<a name="API_OpportunitySearchAwsSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CosellMotion **   <a name="AWSPartnerCentral-Type-OpportunitySearchAwsSummary-CosellMotion"></a>
The engagement classification for this opportunity. Read-only.
Type: String
Required: No

 ** Insights **   <a name="AWSPartnerCentral-Type-OpportunitySearchAwsSummary-Insights"></a>
Curated insights returned in search results: the engagement score and quality score.
Type: [OpportunitySearchInsights](API_OpportunitySearchInsights.md) object
Required: No

 ** Origin **   <a name="AWSPartnerCentral-Type-OpportunitySearchAwsSummary-Origin"></a>
Specifies whether the opportunity originated from AWS or from the partner.
Type: String
Valid Values: `AWS Referral | Partner Referral`
Required: No

## See Also
<a name="API_OpportunitySearchAwsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunitySearchAwsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunitySearchAwsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunitySearchAwsSummary)
