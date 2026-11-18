---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConformancePacksFilters.html
---

# DescribeConformancePacksFilters
<a name="API_DescribeConformancePacksFilters"></a>

Filters for filtering results from [DescribeConformancePacks](API_DescribeConformancePacks.md) and [DescribeConformancePackStatus](API_DescribeConformancePackStatus.md) by conformance pack type.

## Contents
<a name="API_DescribeConformancePacksFilters_Contents"></a>

 ** Types **   <a name="config-Type-DescribeConformancePacksFilters-Types"></a>
Filters results by conformance pack type. Valid values:
+  `CUSTOM` – A custom conformance pack.
+  `MANAGED` – A managed conformance pack.
If you specify both values, AWS Config returns conformance packs of either type.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `CUSTOM | MANAGED`
Required: No

## See Also
<a name="API_DescribeConformancePacksFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeConformancePacksFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeConformancePacksFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeConformancePacksFilters)
