---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_TableRestoreStatus.html
---

# TableRestoreStatus
<a name="API_TableRestoreStatus"></a>

Contains information about a table restore request.

## Contents
<a name="API_TableRestoreStatus_Contents"></a>

 ** message **   <a name="redshiftserverless-Type-TableRestoreStatus-message"></a>
A message that explains the returned status. For example, if the status of the operation is `FAILED`, the message explains why the operation failed.
Type: String
Required: No

 ** namespaceName **   <a name="redshiftserverless-Type-TableRestoreStatus-namespaceName"></a>
The namespace of the table being restored from.
Type: String
Required: No

 ** newTableName **   <a name="redshiftserverless-Type-TableRestoreStatus-newTableName"></a>
The name of the table to create from the restore operation.
Type: String
Required: No

 ** progressInMegaBytes **   <a name="redshiftserverless-Type-TableRestoreStatus-progressInMegaBytes"></a>
The amount of data restored to the new table so far, in megabytes (MB).
Type: Long
Required: No

 ** recoveryPointId **   <a name="redshiftserverless-Type-TableRestoreStatus-recoveryPointId"></a>
The ID of the recovery point being restored from.
Type: String
Required: No

 ** requestTime **   <a name="redshiftserverless-Type-TableRestoreStatus-requestTime"></a>
The time that the table restore request was made, in Universal Coordinated Time (UTC).
Type: Timestamp
Required: No

 ** snapshotName **   <a name="redshiftserverless-Type-TableRestoreStatus-snapshotName"></a>
The name of the snapshot being restored from.
Type: String
Required: No

 ** sourceDatabaseName **   <a name="redshiftserverless-Type-TableRestoreStatus-sourceDatabaseName"></a>
The name of the source database being restored from.
Type: String
Required: No

 ** sourceSchemaName **   <a name="redshiftserverless-Type-TableRestoreStatus-sourceSchemaName"></a>
The name of the source schema being restored from.
Type: String
Required: No

 ** sourceTableName **   <a name="redshiftserverless-Type-TableRestoreStatus-sourceTableName"></a>
The name of the source table being restored from.
Type: String
Required: No

 ** status **   <a name="redshiftserverless-Type-TableRestoreStatus-status"></a>
A value that describes the current state of the table restore request. Possible values are `SUCCEEDED`, `FAILED`, `CANCELED`, `PENDING`, and `IN_PROGRESS`.
Type: String
Required: No

 ** tableRestoreRequestId **   <a name="redshiftserverless-Type-TableRestoreStatus-tableRestoreRequestId"></a>
The ID of the RestoreTableFromSnapshot request.
Type: String
Required: No

 ** targetDatabaseName **   <a name="redshiftserverless-Type-TableRestoreStatus-targetDatabaseName"></a>
The name of the database to restore to.
Type: String
Required: No

 ** targetSchemaName **   <a name="redshiftserverless-Type-TableRestoreStatus-targetSchemaName"></a>
The name of the schema to restore to.
Type: String
Required: No

 ** totalDataInMegaBytes **   <a name="redshiftserverless-Type-TableRestoreStatus-totalDataInMegaBytes"></a>
The total amount of data to restore to the new table, in megabytes (MB).
Type: Long
Required: No

 ** workgroupName **   <a name="redshiftserverless-Type-TableRestoreStatus-workgroupName"></a>
The name of the workgroup being restored from.
Type: String
Required: No

## See Also
<a name="API_TableRestoreStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/TableRestoreStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/TableRestoreStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/TableRestoreStatus)
