---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FindingsTrendsFilters.html
---

# FindingsTrendsFilters
<a name="API_FindingsTrendsFilters"></a>

The structure that defines filters to apply to findings trend data queries.

## Contents
<a name="API_FindingsTrendsFilters_Contents"></a>

 ** CompositeFilters **   <a name="securityhub-Type-FindingsTrendsFilters-CompositeFilters"></a>
A list of composite filters to apply to the findings trend data.
Type: Array of [FindingsTrendsCompositeFilter](API_FindingsTrendsCompositeFilter.md) objects
Required: No

 ** CompositeOperator **   <a name="securityhub-Type-FindingsTrendsFilters-CompositeOperator"></a>
The logical operator (AND, OR) to apply between multiple composite filters.
Type: String
Valid Values: `AND | OR`
Required: No

## See Also
<a name="API_FindingsTrendsFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/FindingsTrendsFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/FindingsTrendsFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/FindingsTrendsFilters)
