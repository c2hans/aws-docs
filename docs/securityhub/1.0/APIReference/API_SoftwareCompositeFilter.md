---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SoftwareCompositeFilter.html
---

# SoftwareCompositeFilter
<a name="API_SoftwareCompositeFilter"></a>

Enables the creation of criteria for software packages in Security Hub.

## Contents
<a name="API_SoftwareCompositeFilter_Contents"></a>

 ** NestedCompositeFilters **   <a name="securityhub-Type-SoftwareCompositeFilter-NestedCompositeFilters"></a>
Provides an additional level of filtering, creating a three-layer nested structure. The first layer is a `CompositeFilters` array with a `CompositeOperator` (`AND`/`OR`). The second layer is a `CompositeFilter` object that contains direct filters and `NestedCompositeFilters`. The third layer is `NestedCompositeFilters`, which contains additional filter conditions.
Type: Array of [SoftwareCompositeFilter](#API_SoftwareCompositeFilter) objects
Required: No

 ** Operator **   <a name="securityhub-Type-SoftwareCompositeFilter-Operator"></a>
The logical operator used to combine multiple filter conditions.
Type: String
Valid Values: `AND | OR`
Required: No

 ** StringFilters **   <a name="securityhub-Type-SoftwareCompositeFilter-StringFilters"></a>
Enables filtering based on string field values.
Type: Array of [SoftwareStringFilter](API_SoftwareStringFilter.md) objects
Required: No

## See Also
<a name="API_SoftwareCompositeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/SoftwareCompositeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/SoftwareCompositeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/SoftwareCompositeFilter)
