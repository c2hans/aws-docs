---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateSnapmirrorSource.html
---

# CreateSnapmirrorSource

Specifies the source endpoint of the Amazon FSx for NetApp ONTAP SnapMirror relationship that you are creating.

## Contents
<a name="API_CreateSnapmirrorSource_Contents"></a>

 ** Path **   <a name="FSx-Type-CreateSnapmirrorSource-Path"></a>
Specifies the path of the source volume, in the format `svm_name:volume_name`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,512}$`
Required: Yes

## See Also
<a name="API_CreateSnapmirrorSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateSnapmirrorSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateSnapmirrorSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateSnapmirrorSource)
