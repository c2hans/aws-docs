---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_PointInTimeRestoreConfiguration.html
---

# PointInTimeRestoreConfiguration
<a name="API_PointInTimeRestoreConfiguration"></a>

The configuration for creating an Autonomous Database by restoring to a point in time.

## Contents
<a name="API_PointInTimeRestoreConfiguration_Contents"></a>

 ** cloneType **   <a name="odb-Type-PointInTimeRestoreConfiguration-cloneType"></a>
The type of clone to create from the point-in-time restore.
Type: String
Valid Values: `FULL | METADATA | PARTIAL`
Required: Yes

 ** sourceAutonomousDatabaseId **   <a name="odb-Type-PointInTimeRestoreConfiguration-sourceAutonomousDatabaseId"></a>
The unique identifier of the source Autonomous Database to restore from.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** cloneTableSpaceList **   <a name="odb-Type-PointInTimeRestoreConfiguration-cloneTableSpaceList"></a>
The list of tablespace identifiers to clone from the point-in-time restore.
Type: Array of integers
Required: No

 ** timestamp **   <a name="odb-Type-PointInTimeRestoreConfiguration-timestamp"></a>
The date and time to which to restore the Autonomous Database.
Type: Timestamp
Required: No

 ** useLatestAvailableBackupTimestamp **   <a name="odb-Type-PointInTimeRestoreConfiguration-useLatestAvailableBackupTimestamp"></a>
Indicates whether to use the latest available backup timestamp for the restore.
Type: Boolean
Required: No

## See Also
<a name="API_PointInTimeRestoreConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/PointInTimeRestoreConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/PointInTimeRestoreConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/PointInTimeRestoreConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
