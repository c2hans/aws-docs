---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ColumnStatisticsData.html
---

# ColumnStatisticsData
<a name="API_ColumnStatisticsData"></a>

Contains the individual types of column statistics data. Only one data object should be set and indicated by the `Type` attribute.

## Contents
<a name="API_ColumnStatisticsData_Contents"></a>

 ** Type **   <a name="Glue-Type-ColumnStatisticsData-Type"></a>
The type of column statistics data.
Type: String
Valid Values: `BOOLEAN | DATE | DECIMAL | DOUBLE | LONG | STRING | BINARY`
Required: Yes

 ** BinaryColumnStatisticsData **   <a name="Glue-Type-ColumnStatisticsData-BinaryColumnStatisticsData"></a>
Binary column statistics data.
Type: [BinaryColumnStatisticsData](API_BinaryColumnStatisticsData.md) object
Required: No

 ** BooleanColumnStatisticsData **   <a name="Glue-Type-ColumnStatisticsData-BooleanColumnStatisticsData"></a>
Boolean column statistics data.
Type: [BooleanColumnStatisticsData](API_BooleanColumnStatisticsData.md) object
Required: No

 ** DateColumnStatisticsData **   <a name="Glue-Type-ColumnStatisticsData-DateColumnStatisticsData"></a>
Date column statistics data.
Type: [DateColumnStatisticsData](API_DateColumnStatisticsData.md) object
Required: No

 ** DecimalColumnStatisticsData **   <a name="Glue-Type-ColumnStatisticsData-DecimalColumnStatisticsData"></a>
 Decimal column statistics data. UnscaledValues within are Base64-encoded binary objects storing big-endian, two's complement representations of the decimal's unscaled value.
Type: [DecimalColumnStatisticsData](API_DecimalColumnStatisticsData.md) object
Required: No

 ** DoubleColumnStatisticsData **   <a name="Glue-Type-ColumnStatisticsData-DoubleColumnStatisticsData"></a>
Double column statistics data.
Type: [DoubleColumnStatisticsData](API_DoubleColumnStatisticsData.md) object
Required: No

 ** LongColumnStatisticsData **   <a name="Glue-Type-ColumnStatisticsData-LongColumnStatisticsData"></a>
Long column statistics data.
Type: [LongColumnStatisticsData](API_LongColumnStatisticsData.md) object
Required: No

 ** StringColumnStatisticsData **   <a name="Glue-Type-ColumnStatisticsData-StringColumnStatisticsData"></a>
String column statistics data.
Type: [StringColumnStatisticsData](API_StringColumnStatisticsData.md) object
Required: No

## See Also
<a name="API_ColumnStatisticsData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ColumnStatisticsData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ColumnStatisticsData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ColumnStatisticsData)
