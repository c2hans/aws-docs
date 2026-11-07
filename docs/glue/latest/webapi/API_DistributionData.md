---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DistributionData.html
---

# DistributionData
<a name="API_DistributionData"></a>

The distribution data for a statistic.

## Contents
<a name="API_DistributionData_Contents"></a>

 ** BinEdges **   <a name="Glue-Type-DistributionData-BinEdges"></a>
The bin edge values for the distribution.
Type: Array of strings
Required: No

 ** Count **   <a name="Glue-Type-DistributionData-Count"></a>
The frequency count for each bin in the distribution.
Type: Array of integers
Required: No

 ** DataType **   <a name="Glue-Type-DistributionData-DataType"></a>
The data type of the column for the distribution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_DistributionData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DistributionData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DistributionData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DistributionData)
