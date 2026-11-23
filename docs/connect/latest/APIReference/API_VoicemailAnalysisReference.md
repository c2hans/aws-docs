---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_VoicemailAnalysisReference.html
---

# VoicemailAnalysisReference

Information about a reference when the `referenceType` is `VOICEMAIL_ANALYSIS` or `VOICEMAIL_ANALYSIS_REDACTED`. Otherwise, null.

## Contents
<a name="API_VoicemailAnalysisReference_Contents"></a>

 ** Arn **   <a name="connect-Type-VoicemailAnalysisReference-Arn"></a>
The Amazon Resource Name (ARN) of the voicemail analysis reference.
Type: String
Required: No

 ** Name **   <a name="connect-Type-VoicemailAnalysisReference-Name"></a>
Identifier of the voicemail analysis reference.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** Status **   <a name="connect-Type-VoicemailAnalysisReference-Status"></a>
Status of the voicemail analysis reference type.
Type: String
Valid Values: `AVAILABLE | DELETED | APPROVED | REJECTED | PROCESSING | FAILED | DRAFTING`
Required: No

 ** Value **   <a name="connect-Type-VoicemailAnalysisReference-Value"></a>
The location path of the voicemail analysis reference.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

## See Also
<a name="API_VoicemailAnalysisReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/VoicemailAnalysisReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/VoicemailAnalysisReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/VoicemailAnalysisReference)
