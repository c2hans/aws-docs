---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DataTable.html
---

# DataTable
<a name="API_DataTable"></a>

Represents a data table in Amazon Connect. A data table is a JSON-like data structure where attributes and values are dynamically set by customers. Customers can reference table values within call flows, applications, views, and workspaces to pinpoint dynamic configuration that changes their contact center's behavior in a predetermined and safe way.

## Contents
<a name="API_DataTable_Contents"></a>

 ** Arn **   <a name="connect-Type-DataTable-Arn"></a>
The Amazon Resource Name (ARN) for the data table. Does not include version aliases.
Type: String
Required: Yes

 ** Id **   <a name="connect-Type-DataTable-Id"></a>
The unique identifier for the data table. Does not include version aliases.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** LastModifiedTime **   <a name="connect-Type-DataTable-LastModifiedTime"></a>
The timestamp when the data table or any of its properties were last modified.
Type: Timestamp
Required: Yes

 ** Name **   <a name="connect-Type-DataTable-Name"></a>
The human-readable name of the data table. Must be unique within the instance and conform to Connect naming standards.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** TimeZone **   <a name="connect-Type-DataTable-TimeZone"></a>
The IANA timezone identifier used when resolving time based dynamic values. Required even if no time slices are specified.
Type: String
Required: Yes

 ** CreatedTime **   <a name="connect-Type-DataTable-CreatedTime"></a>
The timestamp when the data table was created.
Type: Timestamp
Required: No

 ** Description **   <a name="connect-Type-DataTable-Description"></a>
An optional description of the data table's purpose and contents.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.
Pattern: `^[\\P{C}\r\n\t]+$`
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-DataTable-LastModifiedRegion"></a>
The AWS Region where the data table was last modified, used for region replication.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LockVersion **   <a name="connect-Type-DataTable-LockVersion"></a>
The lock version information used for optimistic locking and table versioning. Changes with each update to prevent concurrent modification conflicts.
Type: [DataTableLockVersion](API_DataTableLockVersion.md) object
Required: No

 ** Status **   <a name="connect-Type-DataTable-Status"></a>
The current status of the data table. One of PUBLISHED or SAVED.
Type: String
Valid Values: `PUBLISHED`
Required: No

 ** Tags **   <a name="connect-Type-DataTable-Tags"></a>
Key-value pairs for attribute based access control (TBAC or ABAC) and organization.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** ValueLockLevel **   <a name="connect-Type-DataTable-ValueLockLevel"></a>
The data level that concurrent value edits are locked on. One of DATA\_TABLE, PRIMARY\_VALUE, ATTRIBUTE, VALUE, and NONE. Determines how concurrent edits are handled when multiple users attempt to modify values simultaneously.
Type: String
Valid Values: `NONE | DATA_TABLE | PRIMARY_VALUE | ATTRIBUTE | VALUE`
Required: No

 ** Version **   <a name="connect-Type-DataTable-Version"></a>
A unique identifier and alias for customer managed versions (not $LATEST or $SAVED).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** VersionDescription **   <a name="connect-Type-DataTable-VersionDescription"></a>
A description of the customer managed version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.
Pattern: `^[\\P{C}\r\n\t]+$`
Required: No

## See Also
<a name="API_DataTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DataTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DataTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DataTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
