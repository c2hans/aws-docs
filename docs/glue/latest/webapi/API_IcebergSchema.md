---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergSchema.html
---

# IcebergSchema
<a name="API_IcebergSchema"></a>

Defines the schema structure for an Iceberg table, including field definitions, data types, and schema metadata.

## Contents
<a name="API_IcebergSchema_Contents"></a>

 ** Fields **   <a name="Glue-Type-IcebergSchema-Fields"></a>
The list of field definitions that make up the table schema, including field names, types, and metadata.
Type: Array of [IcebergStructField](API_IcebergStructField.md) objects
Required: Yes

 ** IdentifierFieldIds **   <a name="Glue-Type-IcebergSchema-IdentifierFieldIds"></a>
The list of field identifiers that uniquely identify records in the table, used for row-level operations and deduplication.
Type: Array of integers
Required: No

 ** SchemaId **   <a name="Glue-Type-IcebergSchema-SchemaId"></a>
The unique identifier for this schema version within the Iceberg table's schema evolution history.
Type: Integer
Required: No

 ** Type **   <a name="Glue-Type-IcebergSchema-Type"></a>
The root type of the schema structure, typically "struct" for Iceberg table schemas.
Type: String
Valid Values: `struct`
Required: No

## See Also
<a name="API_IcebergSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergSchema)
