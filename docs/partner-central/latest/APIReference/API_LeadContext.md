---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_LeadContext.html
---

# LeadContext
<a name="API_LeadContext"></a>

Provides comprehensive details about a lead associated with an engagement. This structure contains information about lead qualification status, customer details, and interaction history to facilitate lead management and tracking within the engagement.

## Contents
<a name="API_LeadContext_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Customer **   <a name="AWSPartnerCentral-Type-LeadContext-Customer"></a>
Contains detailed information about the customer associated with the lead, including company information, contact details, and other relevant customer data.
Type: [LeadCustomer](API_LeadCustomer.md) object
Required: Yes

 ** Interactions **   <a name="AWSPartnerCentral-Type-LeadContext-Interactions"></a>
An array of interactions that have occurred with the lead, providing a history of communications, meetings, and other engagement activities related to the lead.
Type: Array of [LeadInteraction](API_LeadInteraction.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** Insights **   <a name="AWSPartnerCentral-Type-LeadContext-Insights"></a>
Insights that AI generates and associates with the lead. These insights provide automated analysis such as lead readiness scoring to help partners assess the lead quality.
Type: [LeadInsights](API_LeadInsights.md) object
Required: No

 ** QualificationStatus **   <a name="AWSPartnerCentral-Type-LeadContext-QualificationStatus"></a>
Indicates the current qualification status of the lead, such as whether it has been qualified, disqualified, or is still under evaluation. This helps track the lead's progression through the qualification process.
Type: String
Pattern: `(?s).{1,255}`
Required: No

## See Also
<a name="API_LeadContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/LeadContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/LeadContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/LeadContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
