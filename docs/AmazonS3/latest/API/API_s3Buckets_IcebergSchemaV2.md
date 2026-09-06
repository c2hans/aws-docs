---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergSchemaV2.html
---

# IcebergSchemaV2
<a name="API_s3Buckets_IcebergSchemaV2"></a>

Contains details about the schema for an Iceberg table using the V2 format. This schema format supports nested and complex data types such as `struct`, `list`, and `map`, in addition to primitive types.

## Contents
<a name="API_s3Buckets_IcebergSchemaV2_Contents"></a>

 ** fields **   <a name="AmazonS3-Type-s3Buckets_IcebergSchemaV2-fields"></a>
The schema fields for the table. Each field defines a column in the table, including its name, type, and whether it is required.
Type: Array of [SchemaV2Field](API_s3Buckets_SchemaV2Field.md) objects
Required: Yes

 ** type **   <a name="AmazonS3-Type-s3Buckets_IcebergSchemaV2-type"></a>
The type of the top-level schema, which is always a `struct` type as defined in the [Apache Iceberg specification](https://iceberg.apache.org/spec/#schemas-and-data-types). This value must be `struct`.
Type: String
Valid Values: `struct`
Required: Yes

 ** identifier-field-ids **   <a name="AmazonS3-Type-s3Buckets_IcebergSchemaV2-identifier-field-ids"></a>
A list of field IDs that are used as the identifier fields for the table. Identifier fields uniquely identify a row in the table.
Type: Array of integers
Required: No

 ** schema-id **   <a name="AmazonS3-Type-s3Buckets_IcebergSchemaV2-schema-id"></a>
An optional unique identifier for the schema. Schema IDs are used by Apache Iceberg to track schema evolution.
Type: Integer
Required: No

## See Also
<a name="API_s3Buckets_IcebergSchemaV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/IcebergSchemaV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/IcebergSchemaV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/IcebergSchemaV2)
