---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_UpdateLeadContext.html
---

# UpdateLeadContext
<a name="API_UpdateLeadContext"></a>

Updates the context information for a lead with qualification status, customer details, and interaction data.

## Contents
<a name="API_UpdateLeadContext_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Customer **   <a name="AWSPartnerCentral-Type-UpdateLeadContext-Customer"></a>
Updated customer information associated with the lead.
Type: [LeadCustomer](API_LeadCustomer.md) object
Required: Yes

 ** Insights **   <a name="AWSPartnerCentral-Type-UpdateLeadContext-Insights"></a>
Insights that AI generates and associates with the lead. These insights provide automated analysis to help partners assess the lead quality and readiness.
Type: [LeadInsights](API_LeadInsights.md) object
Required: No

 ** Interaction **   <a name="AWSPartnerCentral-Type-UpdateLeadContext-Interaction"></a>
Updated interaction details for the lead context.
Type: [LeadInteraction](API_LeadInteraction.md) object
Required: No

 ** QualificationStatus **   <a name="AWSPartnerCentral-Type-UpdateLeadContext-QualificationStatus"></a>
The updated qualification status of the lead.
Type: String
Pattern: `(?s).{1,255}`
Required: No

## See Also
<a name="API_UpdateLeadContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/UpdateLeadContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/UpdateLeadContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/UpdateLeadContext)
