---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_MixedMeasureMapping.html
---

# MixedMeasureMapping
<a name="API_query_MixedMeasureMapping"></a>

MixedMeasureMappings are mappings that can be used to ingest data into a mixture of narrow and multi measures in the derived table.

## Contents
<a name="API_query_MixedMeasureMapping_Contents"></a>

 ** MeasureValueType **   <a name="timestream-Type-query_MixedMeasureMapping-MeasureValueType"></a>
Type of the value that is to be read from sourceColumn. If the mapping is for MULTI, use MeasureValueType.MULTI.
Type: String
Valid Values: `BIGINT | BOOLEAN | DOUBLE | VARCHAR | MULTI`
Required: Yes

 ** MeasureName **   <a name="timestream-Type-query_MixedMeasureMapping-MeasureName"></a>
Refers to the value of measure\_name in a result row. This field is required if MeasureNameColumn is provided.
Type: String
Required: No

 ** MultiMeasureAttributeMappings **   <a name="timestream-Type-query_MixedMeasureMapping-MultiMeasureAttributeMappings"></a>
Required when measureValueType is MULTI. Attribute mappings for MULTI value measures.
Type: Array of [MultiMeasureAttributeMapping](API_query_MultiMeasureAttributeMapping.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** SourceColumn **   <a name="timestream-Type-query_MixedMeasureMapping-SourceColumn"></a>
This field refers to the source column from which measure-value is to be read for result materialization.
Type: String
Required: No

 ** TargetMeasureName **   <a name="timestream-Type-query_MixedMeasureMapping-TargetMeasureName"></a>
Target measure name to be used. If not provided, the target measure name by default would be measure-name if provided, or sourceColumn otherwise.
Type: String
Required: No

## See Also
<a name="API_query_MixedMeasureMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/MixedMeasureMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/MixedMeasureMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/MixedMeasureMapping)
