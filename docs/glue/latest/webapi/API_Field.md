---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Field.html
---

# Field
<a name="API_Field"></a>

The `Field` object has information about the different properties associated with a field in the connector.

## Contents
<a name="API_Field_Contents"></a>

 ** CustomProperties **   <a name="Glue-Type-Field-CustomProperties"></a>
Optional map of keys which may be returned.
Type: String to string map
Required: No

 ** Description **   <a name="Glue-Type-Field-Description"></a>
A description of the field.
Type: String
Required: No

 ** FieldName **   <a name="Glue-Type-Field-FieldName"></a>
A unique identifier for the field.
Type: String
Required: No

 ** FieldType **   <a name="Glue-Type-Field-FieldType"></a>
The type of data in the field.
Type: String
Valid Values: `INT | SMALLINT | BIGINT | FLOAT | LONG | DATE | BOOLEAN | MAP | ARRAY | STRING | TIMESTAMP | DECIMAL | BYTE | SHORT | DOUBLE | STRUCT | BINARY | UNION`
Required: No

 ** IsCreateable **   <a name="Glue-Type-Field-IsCreateable"></a>
Indicates whether this field can be created as part of a destination write.
Type: Boolean
Required: No

 ** IsDefaultOnCreate **   <a name="Glue-Type-Field-IsDefaultOnCreate"></a>
Indicates whether this field is populated automatically when the object is created, such as a created at timestamp.
Type: Boolean
Required: No

 ** IsFilterable **   <a name="Glue-Type-Field-IsFilterable"></a>
 Indicates whether this field can used in a filter clause (`WHERE` clause) of a SQL statement when querying data.
Type: Boolean
Required: No

 ** IsNullable **   <a name="Glue-Type-Field-IsNullable"></a>
Indicates whether this field can be nullable or not.
Type: Boolean
Required: No

 ** IsPartitionable **   <a name="Glue-Type-Field-IsPartitionable"></a>
Indicates whether a given field can be used in partitioning the query made to SaaS.
Type: Boolean
Required: No

 ** IsPrimaryKey **   <a name="Glue-Type-Field-IsPrimaryKey"></a>
Indicates whether this field can used as a primary key for the given entity.
Type: Boolean
Required: No

 ** IsRetrievable **   <a name="Glue-Type-Field-IsRetrievable"></a>
Indicates whether this field can be added in Select clause of SQL query or whether it is retrievable or not.
Type: Boolean
Required: No

 ** IsUpdateable **   <a name="Glue-Type-Field-IsUpdateable"></a>
Indicates whether this field can be updated as part of a destination write.
Type: Boolean
Required: No

 ** IsUpsertable **   <a name="Glue-Type-Field-IsUpsertable"></a>
Indicates whether this field can be upserted as part of a destination write.
Type: Boolean
Required: No

 ** Label **   <a name="Glue-Type-Field-Label"></a>
A readable label used for the field.
Type: String
Required: No

 ** NativeDataType **   <a name="Glue-Type-Field-NativeDataType"></a>
The data type returned by the SaaS API, such as “picklist” or “textarea” from Salesforce.
Type: String
Required: No

 ** ParentField **   <a name="Glue-Type-Field-ParentField"></a>
A parent field name for a nested field.
Type: String
Required: No

 ** SupportedFilterOperators **   <a name="Glue-Type-Field-SupportedFilterOperators"></a>
Indicates the support filter operators for this field.
Type: Array of strings
Valid Values: `LESS_THAN | GREATER_THAN | BETWEEN | EQUAL_TO | NOT_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | LESS_THAN_OR_EQUAL_TO | CONTAINS | ORDER_BY`
Required: No

 ** SupportedValues **   <a name="Glue-Type-Field-SupportedValues"></a>
A list of supported values for the field.
Type: Array of strings
Required: No

## See Also
<a name="API_Field_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Field)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Field)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Field)
