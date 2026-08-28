---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_SchemaV2Field.html
---

# SchemaV2Field
<a name="API_s3Buckets_SchemaV2Field"></a>

Contains details about a schema field in the V2 format. This field format supports nested and complex data types such as `struct`, `list`, and `map`, in addition to primitive types.

## Contents
<a name="API_s3Buckets_SchemaV2Field_Contents"></a>

 ** id **   <a name="AmazonS3-Type-s3Buckets_SchemaV2Field-id"></a>
The unique identifier for the schema field. Field IDs are used by Apache Iceberg to track schema evolution and maintain compatibility across schema changes.
Type: Integer
Required: Yes

 ** name **   <a name="AmazonS3-Type-s3Buckets_SchemaV2Field-name"></a>
The name of the field.
Type: String
Required: Yes

 ** required **   <a name="AmazonS3-Type-s3Buckets_SchemaV2Field-required"></a>
A Boolean value that specifies whether values are required for each row in this field. If this is `true`, the field does not allow null values.
Type: Boolean
Required: Yes

 ** type **   <a name="AmazonS3-Type-s3Buckets_SchemaV2Field-type"></a>
The data type of the field. This can be a primitive type string such as `boolean`, `int`, `long`, `float`, `double`, `string`, `binary`, `date`, `timestamp`, or `timestamptz`, or a complex type represented as a JSON object for nested types such as `struct`, `list`, or `map`. For more information, see the [Apache Iceberg schemas and data types documentation](https://iceberg.apache.org/spec/#schemas-and-data-types).
Type: JSON value
Required: Yes

 ** doc **   <a name="AmazonS3-Type-s3Buckets_SchemaV2Field-doc"></a>
An optional description of the field.
Type: String
Required: No

## See Also
<a name="API_s3Buckets_SchemaV2Field_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/SchemaV2Field)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/SchemaV2Field)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/SchemaV2Field)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
