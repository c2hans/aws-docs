---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_EngagementSearchFilter.html
---

# EngagementSearchFilter

A recursive filter node. Exactly one member must be set. The boolean combinators nest sub-filters: `AndAllFilters` joins its children with AND, `OrAllFilters` matches when at least one child matches, and `NotFilter` negates its single child. The remaining members are leaf conditions over a single field. Nesting is limited to a depth of 3, and each combinator list can contain up to 10 entries.

## Contents
<a name="API_EngagementSearchFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AndAllFilters **   <a name="AWSPartnerCentral-Type-EngagementSearchFilter-AndAllFilters"></a>
A list of sub-filters that are joined with a logical AND. The node matches only when every sub-filter matches.
Type: Array of [EngagementSearchFilter](API_EngagementSearchFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ContainsAll **   <a name="AWSPartnerCentral-Type-EngagementSearchFilter-ContainsAll"></a>
A leaf condition that matches when the field holds every supplied value exactly. Specify a single `StringValue` or a `StringListValue`. For a field that holds one value for each lead interaction, each supplied value must be present on at least one interaction. For a single-valued field, a list of more than one value returns no results. Supported on string fields only.
Type: [EngagementSearchPredicate](API_EngagementSearchPredicate.md) object
Required: No

 ** ContainsAny **   <a name="AWSPartnerCentral-Type-EngagementSearchFilter-ContainsAny"></a>
A leaf condition that matches when the field contains any of the supplied values as a case-insensitive substring. Specify a single `StringValue` or a `StringListValue`. For a field that holds one value for each lead interaction, the condition matches when any of those values contains a supplied value. Supported on string fields only.
Type: [EngagementSearchPredicate](API_EngagementSearchPredicate.md) object
Required: No

 ** EqualsTo **   <a name="AWSPartnerCentral-Type-EngagementSearchFilter-EqualsTo"></a>
A leaf condition that matches when the field equals the supplied `StringValue`.
Type: [EngagementSearchPredicate](API_EngagementSearchPredicate.md) object
Required: No

 ** GreaterThan **   <a name="AWSPartnerCentral-Type-EngagementSearchFilter-GreaterThan"></a>
A leaf condition that matches when the field is greater than the supplied value. This condition is supported only on ordered fields, such as date and numeric fields.
Type: [EngagementSearchPredicate](API_EngagementSearchPredicate.md) object
Required: No

 ** GreaterThanOrEquals **   <a name="AWSPartnerCentral-Type-EngagementSearchFilter-GreaterThanOrEquals"></a>
A leaf condition that matches when the field is greater than or equal to the supplied value. This condition is supported only on ordered fields, such as date and numeric fields.
Type: [EngagementSearchPredicate](API_EngagementSearchPredicate.md) object
Required: No

 ** LessThan **   <a name="AWSPartnerCentral-Type-EngagementSearchFilter-LessThan"></a>
A leaf condition that matches when the field is less than the supplied value. This condition is supported only on ordered fields, such as date and numeric fields.
Type: [EngagementSearchPredicate](API_EngagementSearchPredicate.md) object
Required: No

 ** LessThanOrEquals **   <a name="AWSPartnerCentral-Type-EngagementSearchFilter-LessThanOrEquals"></a>
A leaf condition that matches when the field is less than or equal to the supplied value. This condition is supported only on ordered fields, such as date and numeric fields.
Type: [EngagementSearchPredicate](API_EngagementSearchPredicate.md) object
Required: No

 ** NotFilter **   <a name="AWSPartnerCentral-Type-EngagementSearchFilter-NotFilter"></a>
A single sub-filter that is negated. The node matches when the sub-filter does not match.
Type: [EngagementSearchFilter](API_EngagementSearchFilter.md) object
Required: No

 ** OrAllFilters **   <a name="AWSPartnerCentral-Type-EngagementSearchFilter-OrAllFilters"></a>
A list of sub-filters that are joined with a logical OR. The node matches when at least one sub-filter matches.
Type: Array of [EngagementSearchFilter](API_EngagementSearchFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_EngagementSearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/EngagementSearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/EngagementSearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/EngagementSearchFilter)
