---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_Filter.html
---

# Filter
<a name="API_connect-customer-profiles_Filter"></a>

Defines how to filter the objects coming in for calculated attributes.

## Contents
<a name="API_connect-customer-profiles_Filter_Contents"></a>

 ** Groups **   <a name="connect-Type-connect-customer-profiles_Filter-Groups"></a>
Holds the list of Filter groups within the Filter definition.
Type: Array of [FilterGroup](API_connect-customer-profiles_FilterGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** Include **   <a name="connect-Type-connect-customer-profiles_Filter-Include"></a>
Define whether to include or exclude objects for Calculated Attributed calculation that fit the filter groups criteria.
Type: String
Valid Values: `ALL | ANY | NONE`
Required: Yes

## See Also
<a name="API_connect-customer-profiles_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/Filter)
