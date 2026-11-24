---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_SnapmirrorTransferState.html
---

# SnapmirrorTransferState

Describes the latest transfer of an Amazon FSx for NetApp ONTAP SnapMirror relationship.

## Contents
<a name="API_SnapmirrorTransferState_Contents"></a>

 ** BytesTransferred **   <a name="FSx-Type-SnapmirrorTransferState-BytesTransferred"></a>
The number of bytes that the transfer transferred.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** Duration **   <a name="FSx-Type-SnapmirrorTransferState-Duration"></a>
The duration of the transfer, in ISO 8601 duration format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** EndTime **   <a name="FSx-Type-SnapmirrorTransferState-EndTime"></a>
The time that the transfer ended.
Type: Timestamp
Required: No

 ** State **   <a name="FSx-Type-SnapmirrorTransferState-State"></a>
The state of the transfer that ONTAP reports.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** Type **   <a name="FSx-Type-SnapmirrorTransferState-Type"></a>
The type of the transfer that ONTAP reports.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

## See Also
<a name="API_SnapmirrorTransferState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SnapmirrorTransferState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SnapmirrorTransferState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SnapmirrorTransferState)
