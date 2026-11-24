---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_OntapSnapshotConfiguration.html
---

# OntapSnapshotConfiguration

The configuration of an Amazon FSx for NetApp ONTAP snapshot.

## Contents
<a name="API_OntapSnapshotConfiguration_Contents"></a>

 ** ExpiryTime **   <a name="FSx-Type-OntapSnapshotConfiguration-ExpiryTime"></a>
The date and time when the snapshot expires. You can't delete the snapshot before this time.
Type: Timestamp
Required: No

 ** SizeInMegabytes **   <a name="FSx-Type-OntapSnapshotConfiguration-SizeInMegabytes"></a>
The configured size of the snapshot, in megabytes (MBs).
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** SnaplockExpiryTime **   <a name="FSx-Type-OntapSnapshotConfiguration-SnaplockExpiryTime"></a>
The date and time until which the snapshot is locked. This setting takes effect only if snapshot locking is enabled on the volume. Snapshot locking is separate from SnapLock, and enabling SnapLock on a volume doesn't enable snapshot locking. You can't delete the snapshot before this time.
Type: Timestamp
Required: No

 ** SnapmirrorLabel **   <a name="FSx-Type-OntapSnapshotConfiguration-SnapmirrorLabel"></a>
The SnapMirror label of the snapshot. SnapMirror policies use labels to select which snapshots to replicate to a destination volume.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 31.
Required: No

 ** UUID **   <a name="FSx-Type-OntapSnapshotConfiguration-UUID"></a>
The snapshot's universally unique identifier (UUID).
Type: String
Length Constraints: Maximum length of 36.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,36}$`
Required: No

## See Also
<a name="API_OntapSnapshotConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/OntapSnapshotConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/OntapSnapshotConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/OntapSnapshotConfiguration)
