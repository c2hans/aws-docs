---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateOntapSnapshotConfiguration.html
---

# CreateOntapSnapshotConfiguration

Specifies the configuration of the ONTAP snapshot that you are creating.

## Contents
<a name="API_CreateOntapSnapshotConfiguration_Contents"></a>

 ** ExpiryTime **   <a name="FSx-Type-CreateOntapSnapshotConfiguration-ExpiryTime"></a>
Specifies the date and time when the snapshot expires. You can't delete the snapshot before this time.
Type: Timestamp
Required: No

 ** SnaplockExpiryTime **   <a name="FSx-Type-CreateOntapSnapshotConfiguration-SnaplockExpiryTime"></a>
Specifies the date and time until which the snapshot is locked. This setting takes effect only if snapshot locking is enabled on the volume. Snapshot locking is separate from SnapLock, and enabling SnapLock on a volume doesn't enable snapshot locking. You can't delete the snapshot before this time.
Type: Timestamp
Required: No

 ** SnapmirrorLabel **   <a name="FSx-Type-CreateOntapSnapshotConfiguration-SnapmirrorLabel"></a>
Specifies the SnapMirror label to assign to the snapshot. SnapMirror policies use labels to select which snapshots to replicate to a destination volume.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 31.
Required: No

## See Also
<a name="API_CreateOntapSnapshotConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateOntapSnapshotConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateOntapSnapshotConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateOntapSnapshotConfiguration)
