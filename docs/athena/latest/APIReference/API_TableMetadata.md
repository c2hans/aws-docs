---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_TableMetadata.html
---

# TableMetadata
<a name="API_TableMetadata"></a>

Contains metadata for a table.

## Contents
<a name="API_TableMetadata_Contents"></a>

 ** Name **   <a name="athena-Type-TableMetadata-Name"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Columns **   <a name="athena-Type-TableMetadata-Columns"></a>
A list of the columns in the table.
Type: Array of [Column](API_Column.md) objects
Required: No

 ** CreateTime **   <a name="athena-Type-TableMetadata-CreateTime"></a>
The time that the table was created.
Type: Timestamp
Required: No

 ** LastAccessTime **   <a name="athena-Type-TableMetadata-LastAccessTime"></a>
The last time the table was accessed.
Type: Timestamp
Required: No

 ** Parameters **   <a name="athena-Type-TableMetadata-Parameters"></a>
A set of custom key/value pairs for table properties.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 51200.
Required: No

 ** PartitionKeys **   <a name="athena-Type-TableMetadata-PartitionKeys"></a>
A list of the partition keys in the table.
Type: Array of [Column](API_Column.md) objects
Required: No

 ** TableType **   <a name="athena-Type-TableMetadata-TableType"></a>
The type of table. In Athena, only `EXTERNAL_TABLE` is supported.
Type: String
Length Constraints: Maximum length of 255.
Required: No

## See Also
<a name="API_TableMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/TableMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/TableMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/TableMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
