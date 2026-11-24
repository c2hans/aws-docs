---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_SnapmirrorDestination.html
---

# SnapmirrorDestination

Describes the destination endpoint of an Amazon FSx for NetApp ONTAP SnapMirror relationship. The destination volume is always an Amazon FSx for NetApp ONTAP volume.

## Contents
<a name="API_SnapmirrorDestination_Contents"></a>

 ** Path **   <a name="FSx-Type-SnapmirrorDestination-Path"></a>
The path of the destination volume, in the format `svm_name:volume_name`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,512}$`
Required: No

 ** VolumeId **   <a name="FSx-Type-SnapmirrorDestination-VolumeId"></a>
The ID of the destination volume.
Type: String
Length Constraints: Fixed length of 23.
Pattern: `^(fsvol-[0-9a-f]{17,})$`
Required: No

## See Also
<a name="API_SnapmirrorDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SnapmirrorDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SnapmirrorDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SnapmirrorDestination)
