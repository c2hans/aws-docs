---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DataTableLockVersion.html
---

# DataTableLockVersion
<a name="API_DataTableLockVersion"></a>

Contains lock version information for different levels of a data table hierarchy. Used for optimistic locking to prevent concurrent modification conflicts. Each component has its own lock version that changes when that component is modified.

## Contents
<a name="API_DataTableLockVersion_Contents"></a>

 ** Attribute **   <a name="connect-Type-DataTableLockVersion-Attribute"></a>
The lock version for a specific attribute. When the ValueLockLevel is ATTRIBUTE, this version changes when any value for the attribute changes. For other lock levels, it only changes when the attribute's properties are directly updated.
Type: String
Required: No

 ** DataTable **   <a name="connect-Type-DataTableLockVersion-DataTable"></a>
The lock version for the data table itself. Used for optimistic locking and table versioning. Changes with each update to the table's metadata or structure.
Type: String
Required: No

 ** PrimaryValues **   <a name="connect-Type-DataTableLockVersion-PrimaryValues"></a>
The lock version for a specific set of primary values (record). This includes the default record even if the table does not have any primary attributes. Used for record-level locking.
Type: String
Required: No

 ** Value **   <a name="connect-Type-DataTableLockVersion-Value"></a>
The lock version for a specific value. Changes each time the individual value is modified. Used for the finest-grained locking control.
Type: String
Required: No

## See Also
<a name="API_DataTableLockVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DataTableLockVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DataTableLockVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DataTableLockVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
