---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CompositeFilter.html
---

# CompositeFilter
<a name="API_CompositeFilter"></a>

Enables the creation of filtering criteria for security findings.

## Contents
<a name="API_CompositeFilter_Contents"></a>

 ** BooleanFilters **   <a name="securityhub-Type-CompositeFilter-BooleanFilters"></a>
Enables filtering based on boolean field values.
Type: Array of [OcsfBooleanFilter](API_OcsfBooleanFilter.md) objects
Required: No

 ** DateFilters **   <a name="securityhub-Type-CompositeFilter-DateFilters"></a>
Enables filtering based on date and timestamp fields.
Type: Array of [OcsfDateFilter](API_OcsfDateFilter.md) objects
Required: No

 ** IpFilters **   <a name="securityhub-Type-CompositeFilter-IpFilters"></a>
A list of IP address filters that allowing you to filter findings based on IP address properties.
Type: Array of [OcsfIpFilter](API_OcsfIpFilter.md) objects
Required: No

 ** MapFilters **   <a name="securityhub-Type-CompositeFilter-MapFilters"></a>
Enables filtering based on map field values.
Type: Array of [OcsfMapFilter](API_OcsfMapFilter.md) objects
Required: No

 ** NestedCompositeFilters **   <a name="securityhub-Type-CompositeFilter-NestedCompositeFilters"></a>
 Provides an additional level of filtering, creating a three-layer nested structure. The first layer is a `CompositeFilters` array with a `CompositeOperator` (`AND`/`OR`). The second layer is a `CompositeFilter` object that contains direct filters and `NestedCompositeFilters`. The third layer is `NestedCompositeFilters`, which contains additional filter conditions.
Type: Array of [CompositeFilter](#API_CompositeFilter) objects
Required: No

 ** NumberFilters **   <a name="securityhub-Type-CompositeFilter-NumberFilters"></a>
Enables filtering based on numerical field values.
Type: Array of [OcsfNumberFilter](API_OcsfNumberFilter.md) objects
Required: No

 ** Operator **   <a name="securityhub-Type-CompositeFilter-Operator"></a>
The logical operator used to combine multiple filter conditions.
Type: String
Valid Values: `AND | OR`
Required: No

 ** StringFilters **   <a name="securityhub-Type-CompositeFilter-StringFilters"></a>
Enables filtering based on string field values.
Type: Array of [OcsfStringFilter](API_OcsfStringFilter.md) objects
Required: No

## See Also
<a name="API_CompositeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CompositeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CompositeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CompositeFilter)
