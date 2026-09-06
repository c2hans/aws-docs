---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_VoiceCallEntryPointParameters.html
---

# VoiceCallEntryPointParameters
<a name="API_VoiceCallEntryPointParameters"></a>

Parameters for initiating a voice call test.

## Contents
<a name="API_VoiceCallEntryPointParameters_Contents"></a>

 ** DestinationPhoneNumber **   <a name="connect-Type-VoiceCallEntryPointParameters-DestinationPhoneNumber"></a>
The destination phone number for the test.
Type: String
Pattern: `\\+[1-9]\\d{1,14}$`
Required: No

 ** FlowId **   <a name="connect-Type-VoiceCallEntryPointParameters-FlowId"></a>
The flow identifier for the test.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** SourcePhoneNumber **   <a name="connect-Type-VoiceCallEntryPointParameters-SourcePhoneNumber"></a>
The source phone number for the test.
Type: String
Pattern: `\\+[1-9]\\d{1,14}$`
Required: No

## See Also
<a name="API_VoiceCallEntryPointParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/VoiceCallEntryPointParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/VoiceCallEntryPointParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/VoiceCallEntryPointParameters)
