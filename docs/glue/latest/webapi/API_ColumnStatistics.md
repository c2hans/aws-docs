---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ColumnStatistics.html
---

# ColumnStatistics
<a name="API_ColumnStatistics"></a>

Represents the generated column-level statistics for a table or partition.

## Contents
<a name="API_ColumnStatistics_Contents"></a>

 ** AnalyzedTime **   <a name="Glue-Type-ColumnStatistics-AnalyzedTime"></a>
The timestamp of when column statistics were generated.
Type: Timestamp
Required: Yes

 ** ColumnName **   <a name="Glue-Type-ColumnStatistics-ColumnName"></a>
Name of column which statistics belong to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** ColumnType **   <a name="Glue-Type-ColumnStatistics-ColumnType"></a>
The data type of the column.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** StatisticsData **   <a name="Glue-Type-ColumnStatistics-StatisticsData"></a>
A `ColumnStatisticData` object that contains the statistics data values.
Type: [ColumnStatisticsData](API_ColumnStatisticsData.md) object
Required: Yes

## See Also
<a name="API_ColumnStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ColumnStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ColumnStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ColumnStatistics)
