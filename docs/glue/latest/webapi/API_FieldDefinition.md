---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_FieldDefinition.html
---

# FieldDefinition
<a name="API_FieldDefinition"></a>

Defines a field in an entity schema for REST connector data sources, specifying the field name and data type.

## Contents
<a name="API_FieldDefinition_Contents"></a>

 ** FieldDataType **   <a name="Glue-Type-FieldDefinition-FieldDataType"></a>
The data type of the field.
Type: String
Valid Values: `INT | SMALLINT | BIGINT | FLOAT | LONG | DATE | BOOLEAN | MAP | ARRAY | STRING | TIMESTAMP | DECIMAL | BYTE | SHORT | DOUBLE | STRUCT | BINARY | UNION`
Required: Yes

 ** Name **   <a name="Glue-Type-FieldDefinition-Name"></a>
The name of the field in the entity schema.
Type: String
Required: Yes

 ** FilterOverrides **   <a name="Glue-Type-FieldDefinition-FilterOverrides"></a>
Per-field overrides for filter behavior, allowing customization of how filters are applied to this specific field.
Type: [FilterOverrides](API_FilterOverrides.md) object
Required: No

 ** IsNullable **   <a name="Glue-Type-FieldDefinition-IsNullable"></a>
Indicates whether this field can contain null values.
Type: Boolean
Required: No

 ** IsOrderable **   <a name="Glue-Type-FieldDefinition-IsOrderable"></a>
Indicates whether this field can be used for ordering results.
Type: Boolean
Required: No

 ** IsPartitionable **   <a name="Glue-Type-FieldDefinition-IsPartitionable"></a>
Indicates whether this field can be used for partitioning queries to the data source.
Type: Boolean
Required: No

 ** IsQueryable **   <a name="Glue-Type-FieldDefinition-IsQueryable"></a>
Indicates whether this field can be used in filter predicates when querying data.
Type: Boolean
Required: No

 ** ResponseDateFormat **   <a name="Glue-Type-FieldDefinition-ResponseDateFormat"></a>
The format pattern for parsing date values from API responses. Required when the API uses a non-ISO-8601 format. Accepts Java `DateTimeFormatter` patterns (for example, `EEE, d MMM yyyy HH:mm:ss Z`), `EPOCH_SECONDS` for Unix epoch seconds, or `EPOCH_MILLIS` for Unix epoch milliseconds.
Type: String
Required: No

## See Also
<a name="API_FieldDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/FieldDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/FieldDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/FieldDefinition)
