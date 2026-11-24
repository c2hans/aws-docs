---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_SnapmirrorSource.html
---

# SnapmirrorSource

Describes the source endpoint of an Amazon FSx for NetApp ONTAP SnapMirror relationship. The source volume can be on an Amazon FSx for NetApp ONTAP file system or on another ONTAP cluster.

## Contents
<a name="API_SnapmirrorSource_Contents"></a>

 ** Path **   <a name="FSx-Type-SnapmirrorSource-Path"></a>
The path of the source volume, in the format `svm_name:volume_name`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,512}$`
Required: No

## See Also
<a name="API_SnapmirrorSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SnapmirrorSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SnapmirrorSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SnapmirrorSource)
