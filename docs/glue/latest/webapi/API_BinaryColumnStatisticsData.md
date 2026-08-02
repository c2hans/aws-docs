---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BinaryColumnStatisticsData.html
---

# BinaryColumnStatisticsData
<a name="API_BinaryColumnStatisticsData"></a>

Defines column statistics supported for bit sequence data values.

## Contents
<a name="API_BinaryColumnStatisticsData_Contents"></a>

 ** AverageLength **   <a name="Glue-Type-BinaryColumnStatisticsData-AverageLength"></a>
The average bit sequence length in the column.
Type: Double
Valid Range: Minimum value of 0.0.
Required: Yes

 ** MaximumLength **   <a name="Glue-Type-BinaryColumnStatisticsData-MaximumLength"></a>
The size of the longest bit sequence in the column.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** NumberOfNulls **   <a name="Glue-Type-BinaryColumnStatisticsData-NumberOfNulls"></a>
The number of null values in the column.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_BinaryColumnStatisticsData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BinaryColumnStatisticsData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BinaryColumnStatisticsData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BinaryColumnStatisticsData)
