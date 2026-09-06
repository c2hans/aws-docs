---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LockedSnapshotsInfo.html
---

# LockedSnapshotsInfo
<a name="API_LockedSnapshotsInfo"></a>

Information about a locked snapshot.

## Contents
<a name="API_LockedSnapshotsInfo_Contents"></a>

 ** coolOffPeriod **
The compliance mode cooling-off period, in hours.
Type: Integer
Required: No

 ** coolOffPeriodExpiresOn **
The date and time at which the compliance mode cooling-off period expires, in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`).
Type: Timestamp
Required: No

 ** lockCreatedOn **
The date and time at which the snapshot was locked, in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`).
Type: Timestamp
Required: No

 ** lockDuration **
The period of time for which the snapshot is locked, in days.
Type: Integer
Required: No

 ** lockDurationStartTime **
The date and time at which the lock duration started, in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`).
If you lock a snapshot that is in the `pending` state, the lock duration starts only once the snapshot enters the `completed` state.
Type: Timestamp
Required: No

 ** lockExpiresOn **
The date and time at which the lock will expire, in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`).
Type: Timestamp
Required: No

 ** lockState **
The state of the snapshot lock. Valid states include:
+  `compliance-cooloff` - The snapshot has been locked in compliance mode but it is still within the cooling-off period. The snapshot can't be deleted, but it can be unlocked and the lock settings can be modified by users with appropriate permissions.
+  `governance` - The snapshot is locked in governance mode. The snapshot can't be deleted, but it can be unlocked and the lock settings can be modified by users with appropriate permissions.
+  `compliance` - The snapshot is locked in compliance mode and the cooling-off period has expired. The snapshot can't be unlocked or deleted. The lock duration can only be increased by users with appropriate permissions.
+  `expired` - The snapshot was locked in compliance or governance mode but the lock duration has expired. The snapshot is not locked and can be deleted.
Type: String
Valid Values: `compliance | governance | compliance-cooloff | expired`
Required: No

 ** ownerId **
The account ID of the AWS account that owns the snapshot.
Type: String
Required: No

 ** snapshotId **
The ID of the snapshot.
Type: String
Required: No

## See Also
<a name="API_LockedSnapshotsInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LockedSnapshotsInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LockedSnapshotsInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LockedSnapshotsInfo)
