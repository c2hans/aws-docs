---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EnrichmentContext.html
---

# EnrichmentContext
<a name="API_EnrichmentContext"></a>

Contains enrichment data for engagement invitations. You can view propensity scores, program eligibility, and lead readiness insights directly in the invitation, before you take action on the invitation.

## Contents
<a name="API_EnrichmentContext_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LeadInsights **   <a name="AWSPartnerCentral-Type-EnrichmentContext-LeadInsights"></a>
The AI-generated lead readiness score for this lead. Use this score to assess lead quality and prioritize engagement efforts.
Type: [LeadInsights](API_LeadInsights.md) object
Required: No

 ** ProspectingResultAws **   <a name="AWSPartnerCentral-Type-EnrichmentContext-ProspectingResultAws"></a>
The customer account data and propensity insights for the prospected account. It includes geographic, industry, and segment classifications, along with engagement and solution scoring.
Type: [InvitationProspectingResultAws](API_InvitationProspectingResultAws.md) object
Required: No

## See Also
<a name="API_EnrichmentContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EnrichmentContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EnrichmentContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EnrichmentContext)
