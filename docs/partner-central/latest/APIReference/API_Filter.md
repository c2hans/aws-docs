---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_Filter.html
---

# Filter

A filter node. Specify exactly one member. `AndAllFilters`, `OrAllFilters`, and `NotFilter` combine child filters. The other members compare a single field to a value. Each combinator list can contain up to 10 filters.

## Contents
<a name="API_Filter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AndAllFilters **   <a name="AWSPartnerCentral-Type-Filter-AndAllFilters"></a>
A list of child filters joined with a logical AND. The node matches only when every child filter matches.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ContainsAll **   <a name="AWSPartnerCentral-Type-Filter-ContainsAll"></a>
A condition that matches when the field contains every value in the supplied `StringListValue`. Supported on fields that hold more than one value.
Type: [FilterCondition](API_FilterCondition.md) object
Required: No

 ** ContainsAny **   <a name="AWSPartnerCentral-Type-Filter-ContainsAny"></a>
A condition that matches when the field matches any of the values in the supplied `StringListValue`.
Type: [FilterCondition](API_FilterCondition.md) object
Required: No

 ** EqualsTo **   <a name="AWSPartnerCentral-Type-Filter-EqualsTo"></a>
A condition that matches when the field equals the supplied `StringValue`.
Type: [FilterCondition](API_FilterCondition.md) object
Required: No

 ** GreaterThan **   <a name="AWSPartnerCentral-Type-Filter-GreaterThan"></a>
A condition that matches when the date field is later than the supplied `DateValue`.
Type: [FilterCondition](API_FilterCondition.md) object
Required: No

 ** GreaterThanOrEquals **   <a name="AWSPartnerCentral-Type-Filter-GreaterThanOrEquals"></a>
A condition that matches when the date field is the same as or later than the supplied `DateValue`.
Type: [FilterCondition](API_FilterCondition.md) object
Required: No

 ** LessThan **   <a name="AWSPartnerCentral-Type-Filter-LessThan"></a>
A condition that matches when the date field is earlier than the supplied `DateValue`.
Type: [FilterCondition](API_FilterCondition.md) object
Required: No

 ** LessThanOrEquals **   <a name="AWSPartnerCentral-Type-Filter-LessThanOrEquals"></a>
A condition that matches when the date field is the same as or earlier than the supplied `DateValue`.
Type: [FilterCondition](API_FilterCondition.md) object
Required: No

 ** NotFilter **   <a name="AWSPartnerCentral-Type-Filter-NotFilter"></a>
A single child filter that is negated. The node matches when the child filter doesn't match.
Type: [Filter](API_Filter.md) object
Required: No

 ** OrAllFilters **   <a name="AWSPartnerCentral-Type-Filter-OrAllFilters"></a>
A list of child filters joined with a logical OR. The node matches when at least one child filter matches.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/Filter)
