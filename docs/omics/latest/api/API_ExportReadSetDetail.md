---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ExportReadSetDetail.html
---

# ExportReadSetDetail
<a name="API_ExportReadSetDetail"></a>

Details about a read set.

## Contents
<a name="API_ExportReadSetDetail_Contents"></a>

 ** id **   <a name="omics-Type-ExportReadSetDetail-id"></a>
The set's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** status **   <a name="omics-Type-ExportReadSetDetail-status"></a>
The set's status.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | FINISHED | FAILED`
Required: Yes

 ** statusMessage **   <a name="omics-Type-ExportReadSetDetail-statusMessage"></a>
The set's status message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

## See Also
<a name="API_ExportReadSetDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ExportReadSetDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ExportReadSetDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ExportReadSetDetail)
