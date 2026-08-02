---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRedshiftClusterRestoreStatus.html
---

# AwsRedshiftClusterRestoreStatus
<a name="API_AwsRedshiftClusterRestoreStatus"></a>

Information about the status of a cluster restore action. It only applies if the cluster was created by restoring a snapshot.

## Contents
<a name="API_AwsRedshiftClusterRestoreStatus_Contents"></a>

 ** CurrentRestoreRateInMegaBytesPerSecond **   <a name="securityhub-Type-AwsRedshiftClusterRestoreStatus-CurrentRestoreRateInMegaBytesPerSecond"></a>
The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.
This field is only updated when you restore to DC2 and DS2 node types.
Type: Double
Required: No

 ** ElapsedTimeInSeconds **   <a name="securityhub-Type-AwsRedshiftClusterRestoreStatus-ElapsedTimeInSeconds"></a>
The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.
This field is only updated when you restore to DC2 and DS2 node types.
Type: Long
Required: No

 ** EstimatedTimeToCompletionInSeconds **   <a name="securityhub-Type-AwsRedshiftClusterRestoreStatus-EstimatedTimeToCompletionInSeconds"></a>
The estimate of the time remaining before the restore is complete. Returns 0 for a completed restore.
This field is only updated when you restore to DC2 and DS2 node types.
Type: Long
Required: No

 ** ProgressInMegaBytes **   <a name="securityhub-Type-AwsRedshiftClusterRestoreStatus-ProgressInMegaBytes"></a>
The number of megabytes that were transferred from snapshot storage.
This field is only updated when you restore to DC2 and DS2 node types.
Type: Long
Required: No

 ** SnapshotSizeInMegaBytes **   <a name="securityhub-Type-AwsRedshiftClusterRestoreStatus-SnapshotSizeInMegaBytes"></a>
The size of the set of snapshot data that was used to restore the cluster.
This field is only updated when you restore to DC2 and DS2 node types.
Type: Long
Required: No

 ** Status **   <a name="securityhub-Type-AwsRedshiftClusterRestoreStatus-Status"></a>
The status of the restore action.
Valid values: `starting` \| `restoring` \| `completed` \| `failed`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRedshiftClusterRestoreStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRedshiftClusterRestoreStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRedshiftClusterRestoreStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRedshiftClusterRestoreStatus)
