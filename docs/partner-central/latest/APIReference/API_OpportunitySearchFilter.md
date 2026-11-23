---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunitySearchFilter.html
---

# OpportunitySearchFilter

A recursive filter node. Exactly one member must be set. The boolean combinators nest sub-filters: `AndAllFilters` joins its children with AND, `OrAllFilters` matches when at least one child matches, and `NotFilter` negates its single child. The remaining members are leaf conditions over a single field. Nesting is bounded (depth up to 3, each combinator list up to 10 entries, and up to 20 leaf conditions per tree). If a request exceeds these limits, the service returns a `ValidationException`.

## Contents
<a name="API_OpportunitySearchFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AndAllFilters **   <a name="AWSPartnerCentral-Type-OpportunitySearchFilter-AndAllFilters"></a>
A list of sub-filters that are joined with a logical AND. The node matches only when every sub-filter matches.
Type: Array of [OpportunitySearchFilter](API_OpportunitySearchFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ContainsAll **   <a name="AWSPartnerCentral-Type-OpportunitySearchFilter-ContainsAll"></a>
A leaf condition that matches when the field holds every supplied value. On a multi-valued field, every listed value must be present.
Type: [OpportunitySearchPredicate](API_OpportunitySearchPredicate.md) object
Required: No

 ** ContainsAny **   <a name="AWSPartnerCentral-Type-OpportunitySearchFilter-ContainsAny"></a>
A leaf condition that matches when the field contains any of the supplied values as a case-insensitive substring. On a multi-valued field, the condition matches when any element contains the substring.
Type: [OpportunitySearchPredicate](API_OpportunitySearchPredicate.md) object
Required: No

 ** EqualsTo **   <a name="AWSPartnerCentral-Type-OpportunitySearchFilter-EqualsTo"></a>
A leaf condition that matches when the field equals the supplied value.
Type: [OpportunitySearchPredicate](API_OpportunitySearchPredicate.md) object
Required: No

 ** GreaterThan **   <a name="AWSPartnerCentral-Type-OpportunitySearchFilter-GreaterThan"></a>
A leaf condition that matches when the field is greater than the supplied value. Supported on ordered fields only (date or numeric).
Type: [OpportunitySearchPredicate](API_OpportunitySearchPredicate.md) object
Required: No

 ** GreaterThanOrEquals **   <a name="AWSPartnerCentral-Type-OpportunitySearchFilter-GreaterThanOrEquals"></a>
A leaf condition that matches when the field is greater than or equal to the supplied value. Supported on ordered fields only (date or numeric).
Type: [OpportunitySearchPredicate](API_OpportunitySearchPredicate.md) object
Required: No

 ** LessThan **   <a name="AWSPartnerCentral-Type-OpportunitySearchFilter-LessThan"></a>
A leaf condition that matches when the field is less than the supplied value. Supported on ordered fields only (date or numeric).
Type: [OpportunitySearchPredicate](API_OpportunitySearchPredicate.md) object
Required: No

 ** LessThanOrEquals **   <a name="AWSPartnerCentral-Type-OpportunitySearchFilter-LessThanOrEquals"></a>
A leaf condition that matches when the field is less than or equal to the supplied value. Supported on ordered fields only (date or numeric).
Type: [OpportunitySearchPredicate](API_OpportunitySearchPredicate.md) object
Required: No

 ** NotFilter **   <a name="AWSPartnerCentral-Type-OpportunitySearchFilter-NotFilter"></a>
A single sub-filter that is negated. The node matches when the sub-filter does not match.
Type: [OpportunitySearchFilter](API_OpportunitySearchFilter.md) object
Required: No

 ** OrAllFilters **   <a name="AWSPartnerCentral-Type-OpportunitySearchFilter-OrAllFilters"></a>
A list of sub-filters that are joined with a logical OR. The node matches when at least one sub-filter matches.
Type: Array of [OpportunitySearchFilter](API_OpportunitySearchFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_OpportunitySearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunitySearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunitySearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunitySearchFilter)
