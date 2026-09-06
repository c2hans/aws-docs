---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_MultiMeasureMappings.html
---

# MultiMeasureMappings
<a name="API_query_MultiMeasureMappings"></a>

Only one of MixedMeasureMappings or MultiMeasureMappings is to be provided. MultiMeasureMappings can be used to ingest data as multi measures in the derived table.

## Contents
<a name="API_query_MultiMeasureMappings_Contents"></a>

 ** MultiMeasureAttributeMappings **   <a name="timestream-Type-query_MultiMeasureMappings-MultiMeasureAttributeMappings"></a>
Required. Attribute mappings to be used for mapping query results to ingest data for multi-measure attributes.
Type: Array of [MultiMeasureAttributeMapping](API_query_MultiMeasureAttributeMapping.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** TargetMultiMeasureName **   <a name="timestream-Type-query_MultiMeasureMappings-TargetMultiMeasureName"></a>
The name of the target multi-measure name in the derived table. This input is required when measureNameColumn is not provided. If MeasureNameColumn is provided, then value from that column will be used as multi-measure name.
Type: String
Required: No

## See Also
<a name="API_query_MultiMeasureMappings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/MultiMeasureMappings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/MultiMeasureMappings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/MultiMeasureMappings)
