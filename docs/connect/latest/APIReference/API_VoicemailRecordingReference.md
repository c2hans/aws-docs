---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_VoicemailRecordingReference.html
---

# VoicemailRecordingReference

Information about a reference when the `referenceType` is `VOICEMAIL_RECORDING` or `VOICEMAIL_RECORDING_REDACTED`. Otherwise, null.

## Contents
<a name="API_VoicemailRecordingReference_Contents"></a>

 ** Arn **   <a name="connect-Type-VoicemailRecordingReference-Arn"></a>
The Amazon Resource Name (ARN) of the voicemail recording reference.
Type: String
Required: No

 ** Name **   <a name="connect-Type-VoicemailRecordingReference-Name"></a>
Identifier of the voicemail recording reference.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** Status **   <a name="connect-Type-VoicemailRecordingReference-Status"></a>
Status of the voicemail recording reference type.
Type: String
Valid Values: `AVAILABLE | DELETED | APPROVED | REJECTED | PROCESSING | FAILED | DRAFTING`
Required: No

 ** Value **   <a name="connect-Type-VoicemailRecordingReference-Value"></a>
The location path of the voicemail recording reference.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

## See Also
<a name="API_VoicemailRecordingReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/VoicemailRecordingReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/VoicemailRecordingReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/VoicemailRecordingReference)
