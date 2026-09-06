---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Snapshot.html
---

# Snapshot
<a name="API_Snapshot"></a>

A snapshot object that contains databases.

## Contents
<a name="API_Snapshot_Contents"></a>

 ** accountsWithProvisionedRestoreAccess **   <a name="redshiftserverless-Type-Snapshot-accountsWithProvisionedRestoreAccess"></a>
All of the AWS accounts that have access to restore a snapshot to a provisioned cluster.
Type: Array of strings
Required: No

 ** accountsWithRestoreAccess **   <a name="redshiftserverless-Type-Snapshot-accountsWithRestoreAccess"></a>
All of the AWS accounts that have access to restore a snapshot to a namespace.
Type: Array of strings
Required: No

 ** actualIncrementalBackupSizeInMegaBytes **   <a name="redshiftserverless-Type-Snapshot-actualIncrementalBackupSizeInMegaBytes"></a>
The size of the incremental backup in megabytes.
Type: Double
Required: No

 ** adminPasswordSecretArn **   <a name="redshiftserverless-Type-Snapshot-adminPasswordSecretArn"></a>
The Amazon Resource Name (ARN) for the namespace's admin user credentials secret.
Type: String
Required: No

 ** adminPasswordSecretKmsKeyId **   <a name="redshiftserverless-Type-Snapshot-adminPasswordSecretKmsKeyId"></a>
The ID of the AWS Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.
Type: String
Required: No

 ** adminUsername **   <a name="redshiftserverless-Type-Snapshot-adminUsername"></a>
The username of the database within a snapshot.
Type: String
Required: No

 ** backupProgressInMegaBytes **   <a name="redshiftserverless-Type-Snapshot-backupProgressInMegaBytes"></a>
The size in megabytes of the data that has been backed up to a snapshot.
Type: Double
Required: No

 ** currentBackupRateInMegaBytesPerSecond **   <a name="redshiftserverless-Type-Snapshot-currentBackupRateInMegaBytesPerSecond"></a>
The rate at which data is backed up into a snapshot in megabytes per second.
Type: Double
Required: No

 ** elapsedTimeInSeconds **   <a name="redshiftserverless-Type-Snapshot-elapsedTimeInSeconds"></a>
The amount of time it took to back up data into a snapshot.
Type: Long
Required: No

 ** estimatedSecondsToCompletion **   <a name="redshiftserverless-Type-Snapshot-estimatedSecondsToCompletion"></a>
The estimated amount of seconds until the snapshot completes backup.
Type: Long
Required: No

 ** kmsKeyId **   <a name="redshiftserverless-Type-Snapshot-kmsKeyId"></a>
The unique identifier of the KMS key used to encrypt the snapshot.
Type: String
Required: No

 ** namespaceArn **   <a name="redshiftserverless-Type-Snapshot-namespaceArn"></a>
The Amazon Resource Name (ARN) of the namespace the snapshot was created from.
Type: String
Required: No

 ** namespaceName **   <a name="redshiftserverless-Type-Snapshot-namespaceName"></a>
The name of the namepsace.
Type: String
Required: No

 ** ownerAccount **   <a name="redshiftserverless-Type-Snapshot-ownerAccount"></a>
The owner AWS; account of the snapshot.
Type: String
Required: No

 ** snapshotArn **   <a name="redshiftserverless-Type-Snapshot-snapshotArn"></a>
The Amazon Resource Name (ARN) of the snapshot.
Type: String
Required: No

 ** snapshotCreateTime **   <a name="redshiftserverless-Type-Snapshot-snapshotCreateTime"></a>
The timestamp of when the snapshot was created.
Type: Timestamp
Required: No

 ** snapshotName **   <a name="redshiftserverless-Type-Snapshot-snapshotName"></a>
The name of the snapshot.
Type: String
Required: No

 ** snapshotRemainingDays **   <a name="redshiftserverless-Type-Snapshot-snapshotRemainingDays"></a>
The amount of days until the snapshot is deleted.
Type: Integer
Required: No

 ** snapshotRetentionPeriod **   <a name="redshiftserverless-Type-Snapshot-snapshotRetentionPeriod"></a>
The period of time, in days, of how long the snapshot is retained.
Type: Integer
Required: No

 ** snapshotRetentionStartTime **   <a name="redshiftserverless-Type-Snapshot-snapshotRetentionStartTime"></a>
The timestamp of when data within the snapshot started getting retained.
Type: Timestamp
Required: No

 ** status **   <a name="redshiftserverless-Type-Snapshot-status"></a>
The status of the snapshot.
Type: String
Valid Values: `AVAILABLE | CREATING | DELETED | CANCELLED | FAILED | COPYING`
Required: No

 ** totalBackupSizeInMegaBytes **   <a name="redshiftserverless-Type-Snapshot-totalBackupSizeInMegaBytes"></a>
The total size, in megabytes, of how big the snapshot is.
Type: Double
Required: No

## See Also
<a name="API_Snapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/Snapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/Snapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/Snapshot)
