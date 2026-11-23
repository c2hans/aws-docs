---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EngagementSearchSort.html
---

# EngagementSearchSort

Configures sorting of the search results.

## Contents
<a name="API_EngagementSearchSort_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SortBy **   <a name="AWSPartnerCentral-Type-EngagementSearchSort-SortBy"></a>
The field to sort the results by.
Type: String
Valid Values: `EngagementId | Title | PartnerId | CreatedAt | LastModifiedAt | MemberCount | ProspectingCustomerGeo | ProspectingCustomerRegion | ProspectingCustomerIndustry | ProspectingCustomerSegment | ProspectingCustomerCountry | ProspectingCustomerCompanySize | ProspectingInsightsMarketplaceEngagementScore | ProspectingInsightsSolutionCategory | ProspectingInsightsSolutionSubCategory | LeadQualificationStatus | LeadReadinessScore | LeadCustomerIndustry | LeadCustomerCountryCode | LeadCustomerAwsMaturity | LeadCustomerMarketSegment | LeadCustomerCompanyName | LeadInteractionsContactFirstName | LeadInteractionsContactLastName | LeadInteractionsUsecase | LeadInteractionsContactBusinessTitle`
Required: Yes

 ** SortOrder **   <a name="AWSPartnerCentral-Type-EngagementSearchSort-SortOrder"></a>
The direction of the sort, either ascending or descending.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: Yes

## See Also
<a name="API_EngagementSearchSort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EngagementSearchSort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EngagementSearchSort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EngagementSearchSort)
