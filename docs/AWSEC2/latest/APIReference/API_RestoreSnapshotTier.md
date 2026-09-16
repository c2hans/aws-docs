---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RestoreSnapshotTier.html
---

# RestoreSnapshotTier
<a name="API_RestoreSnapshotTier"></a>

Restores an archived Amazon EBS snapshot for use temporarily or permanently, or modifies the restore period or restore type for a snapshot that was previously temporarily restored.

For more information see [ Restore an archived snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/working-with-snapshot-archiving.html#restore-archived-snapshot) and [ modify the restore period or restore type for a temporarily restored snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/working-with-snapshot-archiving.html#modify-temp-restore-period) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_RestoreSnapshotTier_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PermanentRestore**
Indicates whether to permanently restore an archived snapshot. To permanently restore an archived snapshot, specify `true` and omit the **RestoreSnapshotTierRequest$TemporaryRestoreDays** parameter.
Type: Boolean
Required: No

 **SnapshotId**
The ID of the snapshot to restore.
Type: String
Required: Yes

 **TemporaryRestoreDays**
Specifies the number of days for which to temporarily restore an archived snapshot. Required for temporary restores only. The snapshot will be automatically re-archived after this period.
To temporarily restore an archived snapshot, specify the number of days and omit the **PermanentRestore** parameter or set it to `false`.
Type: Integer
Required: No

## Response Elements
<a name="API_RestoreSnapshotTier_ResponseElements"></a>

The following elements are returned by the service.

 **isPermanentRestore**
Indicates whether the snapshot is permanently restored. `true` indicates a permanent restore. `false` indicates a temporary restore.
Type: Boolean

 **requestId**
The ID of the request.
Type: String

 **restoreDuration**
For temporary restores only. The number of days for which the archived snapshot is temporarily restored.
Type: Integer

 **restoreStartTime**
The date and time when the snapshot restore process started.
Type: Timestamp

 **snapshotId**
The ID of the snapshot.
Type: String

## Errors
<a name="API_RestoreSnapshotTier_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_RestoreSnapshotTier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/RestoreSnapshotTier)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/RestoreSnapshotTier)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RestoreSnapshotTier)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/RestoreSnapshotTier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RestoreSnapshotTier)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/RestoreSnapshotTier)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/RestoreSnapshotTier)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/RestoreSnapshotTier)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/RestoreSnapshotTier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RestoreSnapshotTier)
