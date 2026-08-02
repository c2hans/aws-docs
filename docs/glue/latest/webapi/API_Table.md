---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Table.html
---

# Table
<a name="API_Table"></a>

Represents a collection of related data organized in columns and rows.

## Contents
<a name="API_Table_Contents"></a>

 ** Name **   <a name="Glue-Type-Table-Name"></a>
The table name. For Hive compatibility, this must be entirely lowercase.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** CatalogId **   <a name="Glue-Type-Table-CatalogId"></a>
The ID of the Data Catalog in which the table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** CreatedBy **   <a name="Glue-Type-Table-CreatedBy"></a>
The person or entity who created the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** CreateTime **   <a name="Glue-Type-Table-CreateTime"></a>
The time when the table definition was created in the Data Catalog.
Type: Timestamp
Required: No

 ** DatabaseName **   <a name="Glue-Type-Table-DatabaseName"></a>
The name of the database where the table metadata resides. For Hive compatibility, this must be all lowercase.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Description **   <a name="Glue-Type-Table-Description"></a>
A description of the table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** FederatedTable **   <a name="Glue-Type-Table-FederatedTable"></a>
A `FederatedTable` structure that references an entity outside the AWS Glue Data Catalog.
Type: [FederatedTable](API_FederatedTable.md) object
Required: No

 ** IsMaterializedView **   <a name="Glue-Type-Table-IsMaterializedView"></a>
Indicates a table is a `MaterializedView`.
Type: Boolean
Required: No

 ** IsMultiDialectView **   <a name="Glue-Type-Table-IsMultiDialectView"></a>
Specifies whether the view supports the SQL dialects of one or more different query engines and can therefore be read by those engines.
Type: Boolean
Required: No

 ** IsRegisteredWithLakeFormation **   <a name="Glue-Type-Table-IsRegisteredWithLakeFormation"></a>
Indicates whether the table has been registered with AWS Lake Formation.
Type: Boolean
Required: No

 ** LastAccessTime **   <a name="Glue-Type-Table-LastAccessTime"></a>
The last time that the table was accessed. This is usually taken from HDFS, and might not be reliable.
Type: Timestamp
Required: No

 ** LastAnalyzedTime **   <a name="Glue-Type-Table-LastAnalyzedTime"></a>
The last time that column statistics were computed for this table.
Type: Timestamp
Required: No

 ** Owner **   <a name="Glue-Type-Table-Owner"></a>
The owner of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Parameters **   <a name="Glue-Type-Table-Parameters"></a>
These key-value pairs define properties associated with the table.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** PartitionKeys **   <a name="Glue-Type-Table-PartitionKeys"></a>
A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
When you create a table used by Amazon Athena, and you do not specify any `partitionKeys`, you must at least set the value of `partitionKeys` to an empty list. For example:
 `"PartitionKeys": []`
Type: Array of [Column](API_Column.md) objects
Required: No

 ** Retention **   <a name="Glue-Type-Table-Retention"></a>
The retention time for this table.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Status **   <a name="Glue-Type-Table-Status"></a>
Indicates the the state of an asynchronous change to a table.
Type: [TableStatus](API_TableStatus.md) object
Required: No

 ** StorageDescriptor **   <a name="Glue-Type-Table-StorageDescriptor"></a>
A storage descriptor containing information about the physical storage of this table.
Type: [StorageDescriptor](API_StorageDescriptor.md) object
Required: No

 ** TableType **   <a name="Glue-Type-Table-TableType"></a>
The type of this table. AWS Glue will create tables with the `EXTERNAL_TABLE` type. Other services, such as Athena, may create tables with additional table types.
 AWS Glue related table types:
EXTERNAL\_TABLE
Hive compatible attribute - indicates a non-Hive managed table.
GOVERNED
Used by AWS Lake Formation. The AWS Glue Data Catalog understands `GOVERNED`.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** TargetTable **   <a name="Glue-Type-Table-TargetTable"></a>
A `TableIdentifier` structure that describes a target table for resource linking.
Type: [TableIdentifier](API_TableIdentifier.md) object
Required: No

 ** UpdateTime **   <a name="Glue-Type-Table-UpdateTime"></a>
The last time that the table was updated.
Type: Timestamp
Required: No

 ** VersionId **   <a name="Glue-Type-Table-VersionId"></a>
The ID of the table version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ViewDefinition **   <a name="Glue-Type-Table-ViewDefinition"></a>
A structure that contains all the information that defines the view, including the dialect or dialects for the view, and the query.
Type: [ViewDefinition](API_ViewDefinition.md) object
Required: No

 ** ViewExpandedText **   <a name="Glue-Type-Table-ViewExpandedText"></a>
Included for Apache Hive compatibility. Not used in the normal course of AWS Glue operations.
Type: String
Length Constraints: Maximum length of 409600.
Required: No

 ** ViewOriginalText **   <a name="Glue-Type-Table-ViewOriginalText"></a>
Included for Apache Hive compatibility. Not used in the normal course of AWS Glue operations. If the table is a `VIRTUAL_VIEW`, certain Athena configuration encoded in base64.
Type: String
Length Constraints: Maximum length of 409600.
Required: No

## See Also
<a name="API_Table_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Table)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Table)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Table)
