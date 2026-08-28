---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Partition.html
---

# Partition
<a name="API_Partition"></a>

Represents a slice of table data.

## Contents
<a name="API_Partition_Contents"></a>

 ** CatalogId **   <a name="Glue-Type-Partition-CatalogId"></a>
The ID of the Data Catalog in which the partition resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** CreationTime **   <a name="Glue-Type-Partition-CreationTime"></a>
The time at which the partition was created.
Type: Timestamp
Required: No

 ** DatabaseName **   <a name="Glue-Type-Partition-DatabaseName"></a>
The name of the catalog database in which to create the partition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** LastAccessTime **   <a name="Glue-Type-Partition-LastAccessTime"></a>
The last time at which the partition was accessed.
Type: Timestamp
Required: No

 ** LastAnalyzedTime **   <a name="Glue-Type-Partition-LastAnalyzedTime"></a>
The last time at which column statistics were computed for this partition.
Type: Timestamp
Required: No

 ** Parameters **   <a name="Glue-Type-Partition-Parameters"></a>
These key-value pairs define partition parameters.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** StorageDescriptor **   <a name="Glue-Type-Partition-StorageDescriptor"></a>
Provides information about the physical location where the partition is stored.
Type: [StorageDescriptor](API_StorageDescriptor.md) object
Required: No

 ** TableName **   <a name="Glue-Type-Partition-TableName"></a>
The name of the database table in which to create the partition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Values **   <a name="Glue-Type-Partition-Values"></a>
The values of the partition.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_Partition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Partition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Partition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Partition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
