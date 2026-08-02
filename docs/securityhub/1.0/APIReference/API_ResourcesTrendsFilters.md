---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ResourcesTrendsFilters.html
---

# ResourcesTrendsFilters
<a name="API_ResourcesTrendsFilters"></a>

The structure that defines filters to apply to resources trend data queries.

## Contents
<a name="API_ResourcesTrendsFilters_Contents"></a>

 ** CompositeFilters **   <a name="securityhub-Type-ResourcesTrendsFilters-CompositeFilters"></a>
A list of composite filters to apply to the resources trend data.
Type: Array of [ResourcesTrendsCompositeFilter](API_ResourcesTrendsCompositeFilter.md) objects
Required: No

 ** CompositeOperator **   <a name="securityhub-Type-ResourcesTrendsFilters-CompositeOperator"></a>
The logical operator (AND, OR) to apply between multiple composite filters.
Type: String
Valid Values: `AND | OR`
Required: No

## See Also
<a name="API_ResourcesTrendsFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ResourcesTrendsFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ResourcesTrendsFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ResourcesTrendsFilters)
