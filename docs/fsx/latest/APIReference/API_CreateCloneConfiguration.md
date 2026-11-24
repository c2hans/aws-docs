---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateCloneConfiguration.html
---

# CreateCloneConfiguration

Specifies the parent volume, and optionally the snapshot, that an FSx for ONTAP volume clone is created from.

## Contents
<a name="API_CreateCloneConfiguration_Contents"></a>

 ** ParentVolumeId **   <a name="FSx-Type-CreateCloneConfiguration-ParentVolumeId"></a>
Specifies the ID of the volume to clone.
Type: String
Length Constraints: Fixed length of 23.
Pattern: `^(fsvol-[0-9a-f]{17,})$`
Required: Yes

 ** SnapshotId **   <a name="FSx-Type-CreateCloneConfiguration-SnapshotId"></a>
Specifies the ID of a snapshot of the parent volume to create the clone from. The snapshot's lifecycle state must be `AVAILABLE`. If you don't specify a snapshot, ONTAP creates a new snapshot of the parent volume and creates the clone from it.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 28.
Pattern: `^((fs)?volsnap-[0-9a-f]{8,})$`
Required: No

## See Also
<a name="API_CreateCloneConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateCloneConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateCloneConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateCloneConfiguration)
