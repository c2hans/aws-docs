---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunitySearchSummary.html
---

# OpportunitySearchSummary

A curated summary view of an opportunity returned by a search. It holds the fields needed to render a search result row, take action, and run follow-up filters.

## Contents
<a name="API_OpportunitySearchSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreatedDate **   <a name="AWSPartnerCentral-Type-OpportunitySearchSummary-CreatedDate"></a>
The date and time when the opportunity was created, in UTC.
Type: Timestamp
Required: Yes

 ** Id **   <a name="AWSPartnerCentral-Type-OpportunitySearchSummary-Id"></a>
The read-only, system-generated unique identifier of the opportunity.
Type: String
Pattern: `O[0-9]{1,19}`
Required: Yes

 ** LastModifiedDate **   <a name="AWSPartnerCentral-Type-OpportunitySearchSummary-LastModifiedDate"></a>
The date and time when the opportunity was last modified, in UTC.
Type: Timestamp
Required: Yes

 ** AwsOpportunitySummary **   <a name="AWSPartnerCentral-Type-OpportunitySearchSummary-AwsOpportunitySummary"></a>
The AWS-side view of this opportunity. Absent when no AWS opportunity summary record exists yet.
Type: [OpportunitySearchAwsSummary](API_OpportunitySearchAwsSummary.md) object
Required: No

 ** Customer **   <a name="AWSPartnerCentral-Type-OpportunitySearchSummary-Customer"></a>
A curated customer view: company name, industry, AWS account, and country.
Type: [OpportunitySearchCustomer](API_OpportunitySearchCustomer.md) object
Required: No

 ** LifeCycle **   <a name="AWSPartnerCentral-Type-OpportunitySearchSummary-LifeCycle"></a>
A curated lifecycle view: review status, stage, next steps, and target close date.
Type: [OpportunitySearchLifeCycle](API_OpportunitySearchLifeCycle.md) object
Required: No

 ** OpportunityTeam **   <a name="AWSPartnerCentral-Type-OpportunitySearchSummary-OpportunityTeam"></a>
The opportunity owner and team members. Search results include only each member's name and business title, and exclude contact email and phone.
Type: Array of [OpportunitySearchTeamMember](API_OpportunitySearchTeamMember.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** OpportunityType **   <a name="AWSPartnerCentral-Type-OpportunitySearchSummary-OpportunityType"></a>
Specifies whether the opportunity is a new business opportunity, a renewal, or an expansion.
Type: String
Valid Values: `Net New Business | Flat Renewal | Expansion`
Required: No

 ** PartnerOpportunityIdentifier **   <a name="AWSPartnerCentral-Type-OpportunitySearchSummary-PartnerOpportunityIdentifier"></a>
The unique identifier of the opportunity in your customer relationship management (CRM) system. This value lets you link the opportunity to your CRM.
Type: String
Pattern: `(?s).{0,64}`
Required: No

 ** Project **   <a name="AWSPartnerCentral-Type-OpportunitySearchSummary-Project"></a>
A curated project view: title, AWS Partner Network (APN) programs, and expected customer spend.
Type: [OpportunitySearchProject](API_OpportunitySearchProject.md) object
Required: No

 ** RelatedEntityIdentifiers **   <a name="AWSPartnerCentral-Type-OpportunitySearchSummary-RelatedEntityIdentifiers"></a>
Curated related-entity identifiers surfaced in search: AWS Marketplace offers, offer sets, and solutions.
Type: [OpportunitySearchRelatedEntityIdentifiers](API_OpportunitySearchRelatedEntityIdentifiers.md) object
Required: No

 ** Tags **   <a name="AWSPartnerCentral-Type-OpportunitySearchSummary-Tags"></a>
The tags associated with the opportunity, returned as key-value pairs.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## See Also
<a name="API_OpportunitySearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunitySearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunitySearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunitySearchSummary)
