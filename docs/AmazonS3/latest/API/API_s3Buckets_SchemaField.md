---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_SchemaField.html
---

# SchemaField
<a name="API_s3Buckets_SchemaField"></a>

Contains details about a schema field.

## Contents
<a name="API_s3Buckets_SchemaField_Contents"></a>

 ** name **   <a name="AmazonS3-Type-s3Buckets_SchemaField-name"></a>
The name of the field.
Type: String
Required: Yes

 ** type **   <a name="AmazonS3-Type-s3Buckets_SchemaField-type"></a>
The field type. S3 Tables supports all Apache Iceberg primitive types. For more information, see the [Apache Iceberg documentation](https://iceberg.apache.org/spec/#primitive-types).
Type: String
Required: Yes

 ** id **   <a name="AmazonS3-Type-s3Buckets_SchemaField-id"></a>
An optional unique identifier for the schema field. Field IDs are used by Apache Iceberg to track schema evolution and maintain compatibility across schema changes. If not specified, S3 Tables automatically assigns field IDs.
Type: Integer
Required: No

 ** required **   <a name="AmazonS3-Type-s3Buckets_SchemaField-required"></a>
A Boolean value that specifies whether values are required for each row in this field. By default, this is `false` and null values are allowed in the field. If this is `true` the field does not allow null values.
Type: Boolean
Required: No

## See Also
<a name="API_s3Buckets_SchemaField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/SchemaField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/SchemaField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/SchemaField)
