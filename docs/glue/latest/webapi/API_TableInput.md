---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TableInput.html
---

# TableInput
<a name="API_TableInput"></a>

A structure used to define a table.

## Contents
<a name="API_TableInput_Contents"></a>

 ** Name **   <a name="Glue-Type-TableInput-Name"></a>
The table name. For Hive compatibility, this is folded to lowercase when it is stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** Description **   <a name="Glue-Type-TableInput-Description"></a>
A description of the table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LastAccessTime **   <a name="Glue-Type-TableInput-LastAccessTime"></a>
The last time that the table was accessed.
Type: Timestamp
Required: No

 ** LastAnalyzedTime **   <a name="Glue-Type-TableInput-LastAnalyzedTime"></a>
The last time that column statistics were computed for this table.
Type: Timestamp
Required: No

 ** Owner **   <a name="Glue-Type-TableInput-Owner"></a>
The table owner. Included for Apache Hive compatibility. Not used in the normal course of AWS Glue operations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Parameters **   <a name="Glue-Type-TableInput-Parameters"></a>
These key-value pairs define properties associated with the table.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** PartitionKeys **   <a name="Glue-Type-TableInput-PartitionKeys"></a>
A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
When you create a table used by Amazon Athena, and you do not specify any `partitionKeys`, you must at least set the value of `partitionKeys` to an empty list. For example:
 `"PartitionKeys": []`
Type: Array of [Column](API_Column.md) objects
Required: No

 ** Retention **   <a name="Glue-Type-TableInput-Retention"></a>
The retention time for this table.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** StorageDescriptor **   <a name="Glue-Type-TableInput-StorageDescriptor"></a>
A storage descriptor containing information about the physical storage of this table.
Type: [StorageDescriptor](API_StorageDescriptor.md) object
Required: No

 ** TableType **   <a name="Glue-Type-TableInput-TableType"></a>
The type of this table. AWS Glue will create tables with the `EXTERNAL_TABLE` type. Other services, such as Athena, may create tables with additional table types.
 AWS Glue related table types:
EXTERNAL\_TABLE
Hive compatible attribute - indicates a non-Hive managed table.
GOVERNED
Used by AWS Lake Formation. The AWS Glue Data Catalog understands `GOVERNED`.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** TargetTable **   <a name="Glue-Type-TableInput-TargetTable"></a>
A `TableIdentifier` structure that describes a target table for resource linking.
Type: [TableIdentifier](API_TableIdentifier.md) object
Required: No

 ** ViewDefinition **   <a name="Glue-Type-TableInput-ViewDefinition"></a>
A structure that contains all the information that defines the view, including the dialect or dialects for the view, and the query.
Type: [ViewDefinitionInput](API_ViewDefinitionInput.md) object
Required: No

 ** ViewExpandedText **   <a name="Glue-Type-TableInput-ViewExpandedText"></a>
Included for Apache Hive compatibility. Not used in the normal course of AWS Glue operations.
Type: String
Length Constraints: Maximum length of 409600.
Required: No

 ** ViewOriginalText **   <a name="Glue-Type-TableInput-ViewOriginalText"></a>
Included for Apache Hive compatibility. Not used in the normal course of AWS Glue operations. If the table is a `VIRTUAL_VIEW`, certain Athena configuration encoded in base64.
Type: String
Length Constraints: Maximum length of 409600.
Required: No

## See Also
<a name="API_TableInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TableInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TableInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TableInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
