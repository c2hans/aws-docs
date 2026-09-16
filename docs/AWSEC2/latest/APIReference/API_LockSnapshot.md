---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LockSnapshot.html
---

# LockSnapshot
<a name="API_LockSnapshot"></a>

Locks an Amazon EBS snapshot in either *governance* or *compliance* mode to protect it against accidental or malicious deletions for a specific duration. A locked snapshot can't be deleted.

You can also use this action to modify the lock settings for a snapshot that is already locked. The allowed modifications depend on the lock mode and lock state:
+ If the snapshot is locked in governance mode, you can modify the lock mode and the lock duration or lock expiration date.
+ If the snapshot is locked in compliance mode and it is in the cooling-off period, you can modify the lock mode and the lock duration or lock expiration date.
+ If the snapshot is locked in compliance mode and the cooling-off period has lapsed, you can only increase the lock duration or extend the lock expiration date.

## Request Parameters
<a name="API_LockSnapshot_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CoolOffPeriod**
The cooling-off period during which you can unlock the snapshot or modify the lock settings after locking the snapshot in compliance mode, in hours. After the cooling-off period expires, you can't unlock or delete the snapshot, decrease the lock duration, or change the lock mode. You can increase the lock duration after the cooling-off period expires.
The cooling-off period is optional when locking a snapshot in compliance mode. If you are locking the snapshot in governance mode, omit this parameter.
To lock the snapshot in compliance mode immediately without a cooling-off period, omit this parameter.
If you are extending the lock duration for a snapshot that is locked in compliance mode after the cooling-off period has expired, omit this parameter. If you specify a cooling-period in a such a request, the request fails.
Allowed values: Min 1, max 72.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 72.
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ExpirationDate**
The date and time at which the snapshot lock is to automatically expire, in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`).
You must specify either this parameter or **LockDuration**, but not both.
Type: Timestamp
Required: No

 **LockDuration**
The period of time for which to lock the snapshot, in days. The snapshot lock will automatically expire after this period lapses.
You must specify either this parameter or **ExpirationDate**, but not both.
Allowed values: Min: 1, max 36500
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 36500.
Required: No

 **LockMode**
The mode in which to lock the snapshot. Specify one of the following:
+  `governance` - Locks the snapshot in governance mode. Snapshots locked in governance mode can't be deleted until one of the following conditions are met:
  + The lock duration expires.
  + The snapshot is unlocked by a user with the appropriate permissions.

  Users with the appropriate IAM permissions can unlock the snapshot, increase or decrease the lock duration, and change the lock mode to `compliance` at any time.

  If you lock a snapshot in `governance` mode, omit ** CoolOffPeriod**.
+  `compliance` - Locks the snapshot in compliance mode. Snapshots locked in compliance mode can't be unlocked by any user. They can be deleted only after the lock duration expires. Users can't decrease the lock duration or change the lock mode to `governance`. However, users with appropriate IAM permissions can increase the lock duration at any time.

  If you lock a snapshot in `compliance` mode, you can optionally specify **CoolOffPeriod**.
Type: String
Valid Values: `compliance | governance`
Required: Yes

 **SnapshotId**
The ID of the snapshot to lock.
Type: String
Required: Yes

## Response Elements
<a name="API_LockSnapshot_ResponseElements"></a>

The following elements are returned by the service.

 **coolOffPeriod**
The compliance mode cooling-off period, in hours.
Type: Integer

 **coolOffPeriodExpiresOn**
The date and time at which the compliance mode cooling-off period expires, in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`).
Type: Timestamp

 **lockCreatedOn**
The date and time at which the snapshot was locked, in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`).
Type: Timestamp

 **lockDuration**
The period of time for which the snapshot is locked, in days.
Type: Integer

 **lockDurationStartTime**
The date and time at which the lock duration started, in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`).
Type: Timestamp

 **lockExpiresOn**
The date and time at which the lock will expire, in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`).
Type: Timestamp

 **lockState**
The state of the snapshot lock. Valid states include:
+  `compliance-cooloff` - The snapshot has been locked in compliance mode but it is still within the cooling-off period. The snapshot can't be deleted, but it can be unlocked and the lock settings can be modified by users with appropriate permissions.
+  `governance` - The snapshot is locked in governance mode. The snapshot can't be deleted, but it can be unlocked and the lock settings can be modified by users with appropriate permissions.
+  `compliance` - The snapshot is locked in compliance mode and the cooling-off period has expired. The snapshot can't be unlocked or deleted. The lock duration can only be increased by users with appropriate permissions.
+  `expired` - The snapshot was locked in compliance or governance mode but the lock duration has expired. The snapshot is not locked and can be deleted.
Type: String
Valid Values: `compliance | governance | compliance-cooloff | expired`

 **requestId**
The ID of the request.
Type: String

 **snapshotId**
The ID of the snapshot
Type: String

## Errors
<a name="API_LockSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_LockSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/LockSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/LockSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LockSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/LockSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LockSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/LockSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/LockSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/LockSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/LockSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LockSnapshot)
