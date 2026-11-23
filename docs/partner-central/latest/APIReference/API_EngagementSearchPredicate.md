---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EngagementSearchPredicate.html
---

# EngagementSearchPredicate

A leaf condition in an `EngagementSearchFilter` tree. It specifies the field (`Key`) and the typed value (`Value`) to compare. The `EngagementSearchFilter` member that contains the condition specifies the comparison operator.

## Contents
<a name="API_EngagementSearchPredicate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **   <a name="AWSPartnerCentral-Type-EngagementSearchPredicate-Key"></a>
The engagement field that the condition applies to.
Type: String
Valid Values: `EngagementId | Title | PartnerId | CreatedAt | LastModifiedAt | MemberCount | ProspectingCustomerGeo | ProspectingCustomerRegion | ProspectingCustomerIndustry | ProspectingCustomerSegment | ProspectingCustomerCountry | ProspectingCustomerCompanySize | ProspectingInsightsMarketplaceEngagementScore | ProspectingInsightsSolutionCategory | ProspectingInsightsSolutionSubCategory | LeadQualificationStatus | LeadReadinessScore | LeadCustomerIndustry | LeadCustomerCountryCode | LeadCustomerAwsMaturity | LeadCustomerMarketSegment | LeadInteractionsSourceType | LeadCustomerCompanyName | LeadInteractionsContactFirstName | LeadInteractionsContactLastName | LeadInteractionsUsecase | LeadInteractionsSourceName | LeadInteractionsContactBusinessTitle | ContextType`
Required: Yes

 ** Value **   <a name="AWSPartnerCentral-Type-EngagementSearchPredicate-Value"></a>
The typed value the condition compares against.
Type: [EngagementSearchFilterValue](API_EngagementSearchFilterValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_EngagementSearchPredicate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EngagementSearchPredicate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EngagementSearchPredicate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EngagementSearchPredicate)
