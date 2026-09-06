---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergStructField.html
---

# IcebergStructField
<a name="API_IcebergStructField"></a>

Defines a single field within an Iceberg table schema, including its identifier, name, data type, nullability, and documentation.

## Contents
<a name="API_IcebergStructField_Contents"></a>

 ** Id **   <a name="Glue-Type-IcebergStructField-Id"></a>
The unique identifier assigned to this field within the Iceberg table schema, used for schema evolution and field tracking.
Type: Integer
Required: Yes

 ** Name **   <a name="Glue-Type-IcebergStructField-Name"></a>
The name of the field as it appears in the table schema and query operations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** Required **   <a name="Glue-Type-IcebergStructField-Required"></a>
Indicates whether this field is required (non-nullable) or optional (nullable) in the table schema.
Type: Boolean
Required: Yes

 ** Type **   <a name="Glue-Type-IcebergStructField-Type"></a>
The data type definition for this field, specifying the structure and format of the data it contains.
Type: JSON value
Required: Yes

 ** Doc **   <a name="Glue-Type-IcebergStructField-Doc"></a>
Optional documentation or description text that provides additional context about the purpose and usage of this field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** InitialDefault **   <a name="Glue-Type-IcebergStructField-InitialDefault"></a>
Default value used to populate the field's value for all records that were written before the field was added to the schema. This enables backward compatibility when adding new fields to existing Iceberg tables.
Type: JSON value
Required: No

 ** WriteDefault **   <a name="Glue-Type-IcebergStructField-WriteDefault"></a>
Default value used to populate the field's value for any records written after the field was added to the schema, if the writer does not supply the field's value. This can be changed through schema evolution.
Type: JSON value
Required: No

## See Also
<a name="API_IcebergStructField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergStructField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergStructField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergStructField)
