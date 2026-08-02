---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_CalculatedLifecycle.html
---

# CalculatedLifecycle
<a name="API_CalculatedLifecycle"></a>

Contains `DeleteAt` and `MoveToColdStorageAt` timestamps, which are used to specify a lifecycle for a recovery point.

The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define.

Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold.

Resource types that can transition to cold storage are listed in the [Feature availability by resource](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource) table. AWS Backup ignores this expression for other resource types.

## Contents
<a name="API_CalculatedLifecycle_Contents"></a>

 ** DeleteAt **   <a name="Backup-Type-CalculatedLifecycle-DeleteAt"></a>
A timestamp that specifies when to delete a recovery point.
Type: Timestamp
Required: No

 ** MoveToColdStorageAt **   <a name="Backup-Type-CalculatedLifecycle-MoveToColdStorageAt"></a>
A timestamp that specifies when to transition a recovery point to cold storage.
Type: Timestamp
Required: No

## See Also
<a name="API_CalculatedLifecycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/CalculatedLifecycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/CalculatedLifecycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/CalculatedLifecycle)
