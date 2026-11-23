---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunitySearchPredicate.html
---

# OpportunitySearchPredicate

A leaf filter condition. It carries the field (`Key`) and the typed value (`Value`) to compare against. The enclosing `OpportunitySearchFilter` member determines the comparison operator.

## Contents
<a name="API_OpportunitySearchPredicate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **   <a name="AWSPartnerCentral-Type-OpportunitySearchPredicate-Key"></a>
The opportunity field that the condition applies to.
Type: String
Valid Values: `OpportunityId | Stage | ReviewStatus | CustomerCompanyName | LastModifiedDate | TargetCloseDate | CreatedDate | CountryCode | PartnerProjectTitle | OpportunityType | PartnerOpportunityIdentifier | Industry | AwsAccountId | ApnPrograms | Origin | Tags | NextStep | OfferId | OfferSetId | AwsMarketplaceSolution | CosellMotion | OpportunityOwner | EstimatedMrr | EngagementScore`
Required: Yes

 ** Value **   <a name="AWSPartnerCentral-Type-OpportunitySearchPredicate-Value"></a>
The typed value the condition compares against. Specify one of the following:
+ A single string value – used by `EqualsTo`, and by `ContainsAny` or `ContainsAll` for a single-value match.
+ A list of string values – used by `ContainsAny` or `ContainsAll` to match against multiple values.
+ An integral numeric value – used by the range comparisons on integral numeric fields.
+ A fractional numeric value – used by the range comparisons on numeric amount fields such as `EstimatedMrr`.
+ A date-time value in RFC 3339 format – used by the range comparisons on date fields.
Type: [OpportunitySearchFilterValue](API_OpportunitySearchFilterValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_OpportunitySearchPredicate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunitySearchPredicate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunitySearchPredicate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunitySearchPredicate)
