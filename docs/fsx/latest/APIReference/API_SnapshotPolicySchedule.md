---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_SnapshotPolicySchedule.html
---

# SnapshotPolicySchedule

Specifies a schedule for an Amazon FSx for NetApp ONTAP snapshot policy.

## Contents
<a name="API_SnapshotPolicySchedule_Contents"></a>

 ** Count **   <a name="FSx-Type-SnapshotPolicySchedule-Count"></a>
The number of snapshots to retain for the schedule.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1023.
Required: Yes

 ** Name **   <a name="FSx-Type-SnapshotPolicySchedule-Name"></a>
The name of the ONTAP schedule that determines when snapshots are created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** Prefix **   <a name="FSx-Type-SnapshotPolicySchedule-Prefix"></a>
The prefix for the schedule to use when creating snapshots.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** RetentionPeriod **   <a name="FSx-Type-SnapshotPolicySchedule-RetentionPeriod"></a>
The length of time that the snapshots that the schedule creates are locked. This setting applies only to volumes that have snapshot locking enabled.
Type: [SnapshotPolicyRetentionPeriod](API_SnapshotPolicyRetentionPeriod.md) object
Required: No

 ** SnapmirrorLabel **   <a name="FSx-Type-SnapshotPolicySchedule-SnapmirrorLabel"></a>
The SnapMirror label to assign to the snapshots that the schedule creates. SnapMirror policies use labels to select which snapshots to replicate to a destination volume.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 31.
Required: No

## See Also
<a name="API_SnapshotPolicySchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SnapshotPolicySchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SnapshotPolicySchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SnapshotPolicySchedule)
