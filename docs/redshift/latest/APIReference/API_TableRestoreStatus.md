---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_TableRestoreStatus.html
---

# TableRestoreStatus
<a name="API_TableRestoreStatus"></a>

Describes the status of a [RestoreTableFromClusterSnapshot](API_RestoreTableFromClusterSnapshot.md) operation.

## Contents
<a name="API_TableRestoreStatus_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClusterIdentifier **
The identifier of the Amazon Redshift cluster that the table is being restored to.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Message **
A description of the status of the table restore request. Status values include `SUCCEEDED`, `FAILED`, `CANCELED`, `PENDING`, `IN_PROGRESS`.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** NewTableName **
The name of the table to create as a result of the table restore request.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ProgressInMegaBytes **
The amount of data restored to the new table so far, in megabytes (MB).
Type: Long
Required: No

 ** RequestTime **
The time that the table restore request was made, in Universal Coordinated Time (UTC).
Type: Timestamp
Required: No

 ** SnapshotIdentifier **
The identifier of the snapshot that the table is being restored from.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** SourceDatabaseName **
The name of the source database that contains the table being restored.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** SourceSchemaName **
The name of the source schema that contains the table being restored.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** SourceTableName **
The name of the source table being restored.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Status **
A value that describes the current state of the table restore request.
Valid Values: `SUCCEEDED`, `FAILED`, `CANCELED`, `PENDING`, `IN_PROGRESS`
Type: String
Valid Values: `PENDING | IN_PROGRESS | SUCCEEDED | FAILED | CANCELED`
Required: No

 ** TableRestoreRequestId **
The unique identifier for the table restore request.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** TargetDatabaseName **
The name of the database to restore the table to.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** TargetSchemaName **
The name of the schema to restore the table to.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** TotalDataInMegaBytes **
The total amount of data to restore to the new table, in megabytes (MB).
Type: Long
Required: No

## See Also
<a name="API_TableRestoreStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/TableRestoreStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/TableRestoreStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/TableRestoreStatus)
