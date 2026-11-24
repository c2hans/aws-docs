---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_SnapmirrorExportedSnapshot.html
---

# SnapmirrorExportedSnapshot

Describes the latest snapshot that SnapMirror transferred to the destination volume of an Amazon FSx for NetApp ONTAP SnapMirror relationship.

## Contents
<a name="API_SnapmirrorExportedSnapshot_Contents"></a>

 ** SnapshotId **   <a name="FSx-Type-SnapmirrorExportedSnapshot-SnapshotId"></a>
The ID of the snapshot, if Amazon FSx manages the snapshot.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 28.
Pattern: `^((fs)?volsnap-[0-9a-f]{8,})$`
Required: No

 ** SnapshotName **   <a name="FSx-Type-SnapmirrorExportedSnapshot-SnapshotName"></a>
The name of the snapshot in ONTAP.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_SnapmirrorExportedSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SnapmirrorExportedSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SnapmirrorExportedSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SnapmirrorExportedSnapshot)
