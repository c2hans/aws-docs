---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StorageDescriptor.html
---

# StorageDescriptor
<a name="API_StorageDescriptor"></a>

Describes the physical storage of table data.

## Contents
<a name="API_StorageDescriptor_Contents"></a>

 ** AdditionalLocations **   <a name="Glue-Type-StorageDescriptor-AdditionalLocations"></a>
A list of locations that point to the path where a Delta table is located.
Type: Array of strings
Length Constraints: Maximum length of 2056.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** BucketColumns **   <a name="Glue-Type-StorageDescriptor-BucketColumns"></a>
A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Columns **   <a name="Glue-Type-StorageDescriptor-Columns"></a>
A list of the `Columns` in the table.
Type: Array of [Column](API_Column.md) objects
Required: No

 ** Compressed **   <a name="Glue-Type-StorageDescriptor-Compressed"></a>
 `True` if the data in the table is compressed, or `False` if not.
Type: Boolean
Required: No

 ** InputFormat **   <a name="Glue-Type-StorageDescriptor-InputFormat"></a>
The input format: `SequenceFileInputFormat` (binary), or `TextInputFormat`, or a custom format.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Location **   <a name="Glue-Type-StorageDescriptor-Location"></a>
The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
Type: String
Length Constraints: Maximum length of 2056.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** NumberOfBuckets **   <a name="Glue-Type-StorageDescriptor-NumberOfBuckets"></a>
Must be specified if the table contains any dimension columns.
Type: Integer
Required: No

 ** OutputFormat **   <a name="Glue-Type-StorageDescriptor-OutputFormat"></a>
The output format: `SequenceFileOutputFormat` (binary), or `IgnoreKeyTextOutputFormat`, or a custom format.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Parameters **   <a name="Glue-Type-StorageDescriptor-Parameters"></a>
The user-supplied properties in key-value form.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** SchemaReference **   <a name="Glue-Type-StorageDescriptor-SchemaReference"></a>
An object that references a schema stored in the AWS Glue Schema Registry.
When creating a table, you can pass an empty list of columns for the schema, and instead use a schema reference.
Type: [SchemaReference](API_SchemaReference.md) object
Required: No

 ** SerdeInfo **   <a name="Glue-Type-StorageDescriptor-SerdeInfo"></a>
The serialization/deserialization (SerDe) information.
Type: [SerDeInfo](API_SerDeInfo.md) object
Required: No

 ** SkewedInfo **   <a name="Glue-Type-StorageDescriptor-SkewedInfo"></a>
The information about values that appear frequently in a column (skewed values).
Type: [SkewedInfo](API_SkewedInfo.md) object
Required: No

 ** SortColumns **   <a name="Glue-Type-StorageDescriptor-SortColumns"></a>
A list specifying the sort order of each bucket in the table.
Type: Array of [Order](API_Order.md) objects
Required: No

 ** StoredAsSubDirectories **   <a name="Glue-Type-StorageDescriptor-StoredAsSubDirectories"></a>
 `True` if the table data is stored in subdirectories, or `False` if not.
Type: Boolean
Required: No

## See Also
<a name="API_StorageDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StorageDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StorageDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StorageDescriptor)
