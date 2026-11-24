---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_CloneConfiguration.html
---

# CloneConfiguration

Describes the parent volume, and the snapshot if one was specified, that an FSx for ONTAP volume clone was created from.

## Contents
<a name="API_CloneConfiguration_Contents"></a>

 ** ParentVolumeId **   <a name="FSx-Type-CloneConfiguration-ParentVolumeId"></a>
The ID of the parent volume that the clone was created from.
Type: String
Length Constraints: Fixed length of 23.
Pattern: `^(fsvol-[0-9a-f]{17,})$`
Required: No

 ** SnapshotId **   <a name="FSx-Type-CloneConfiguration-SnapshotId"></a>
The ID of the snapshot of the parent volume that the clone was created from, if you specified one when you created the clone.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 28.
Pattern: `^((fs)?volsnap-[0-9a-f]{8,})$`
Required: No

## See Also
<a name="API_CloneConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CloneConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CloneConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CloneConfiguration)
