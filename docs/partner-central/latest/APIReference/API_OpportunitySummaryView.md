---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunitySummaryView.html
---

# OpportunitySummaryView
<a name="API_OpportunitySummaryView"></a>

 Provides a comprehensive view of an opportunity summary, including lifecycle information, team details, opportunity type, primary needs from AWS, and associated project information.

## Contents
<a name="API_OpportunitySummaryView_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Customer **   <a name="AWSPartnerCentral-Type-OpportunitySummaryView-Customer"></a>
An object that contains the customer's `Account` and `Contact`.
Type: [Customer](API_Customer.md) object
Required: No

 ** Lifecycle **   <a name="AWSPartnerCentral-Type-OpportunitySummaryView-Lifecycle"></a>
 Contains information about the opportunity's lifecycle, including its current stage, status, and important dates such as creation and last modification times.
Type: [LifeCycleForView](API_LifeCycleForView.md) object
Required: No

 ** OpportunityTeam **   <a name="AWSPartnerCentral-Type-OpportunitySummaryView-OpportunityTeam"></a>
 Represents the internal team handling the opportunity. Specify the members involved in collaborating on an opportunity within the partner's organization.
Type: Array of [Contact](API_Contact.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** OpportunityType **   <a name="AWSPartnerCentral-Type-OpportunitySummaryView-OpportunityType"></a>
 Specifies the opportunity type.
Type: String
Valid Values: `Net New Business | Flat Renewal | Expansion`
Required: No

 ** PrimaryNeedsFromAws **   <a name="AWSPartnerCentral-Type-OpportunitySummaryView-PrimaryNeedsFromAws"></a>
 Identifies the type of support the partner needs from AWS.
Type: Array of strings
Valid Values: `Co-Sell - Architectural Validation | Co-Sell - Business Presentation | Co-Sell - Competitive Information | Co-Sell - Pricing Assistance | Co-Sell - Technical Consultation | Co-Sell - Total Cost of Ownership Evaluation | Co-Sell - Deal Support | Co-Sell - Support for Public Tender / RFx`
Required: No

 ** Project **   <a name="AWSPartnerCentral-Type-OpportunitySummaryView-Project"></a>
 Contains summary information about the project associated with the opportunity, including project name, description, timeline, and other relevant details.
Type: [ProjectView](API_ProjectView.md) object
Required: No

 ** RelatedEntityIdentifiers **   <a name="AWSPartnerCentral-Type-OpportunitySummaryView-RelatedEntityIdentifiers"></a>
This field provides the associations' information for other entities with the opportunity. These entities include identifiers for `AWSProducts`, `Partner Solutions`, and `AWSMarketplaceOffers`.
Type: [RelatedEntityIdentifiers](API_RelatedEntityIdentifiers.md) object
Required: No

## See Also
<a name="API_OpportunitySummaryView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunitySummaryView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunitySummaryView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunitySummaryView)
