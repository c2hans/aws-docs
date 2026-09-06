---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_MultiMeasureAttributeMapping.html
---

# MultiMeasureAttributeMapping
<a name="API_query_MultiMeasureAttributeMapping"></a>

Attribute mapping for MULTI value measures.

## Contents
<a name="API_query_MultiMeasureAttributeMapping_Contents"></a>

 ** MeasureValueType **   <a name="timestream-Type-query_MultiMeasureAttributeMapping-MeasureValueType"></a>
Type of the attribute to be read from the source column.
Type: String
Valid Values: `BIGINT | BOOLEAN | DOUBLE | VARCHAR | TIMESTAMP`
Required: Yes

 ** SourceColumn **   <a name="timestream-Type-query_MultiMeasureAttributeMapping-SourceColumn"></a>
Source column from where the attribute value is to be read.
Type: String
Required: Yes

 ** TargetMultiMeasureAttributeName **   <a name="timestream-Type-query_MultiMeasureAttributeMapping-TargetMultiMeasureAttributeName"></a>
Custom name to be used for attribute name in derived table. If not provided, source column name would be used.
Type: String
Required: No

## See Also
<a name="API_query_MultiMeasureAttributeMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/MultiMeasureAttributeMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/MultiMeasureAttributeMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/MultiMeasureAttributeMapping)
