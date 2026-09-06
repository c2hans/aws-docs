---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_StopCisSessionMessage.html
---

# StopCisSessionMessage
<a name="API_StopCisSessionMessage"></a>

The stop CIS session message.

## Contents
<a name="API_StopCisSessionMessage_Contents"></a>

 ** progress **   <a name="inspector2-Type-StopCisSessionMessage-progress"></a>
The progress of the message.
Type: [StopCisMessageProgress](API_StopCisMessageProgress.md) object
Required: Yes

 ** status **   <a name="inspector2-Type-StopCisSessionMessage-status"></a>
The status of the message.
Type: String
Valid Values: `SUCCESS | FAILED | INTERRUPTED | UNSUPPORTED_OS`
Required: Yes

 ** benchmarkProfile **   <a name="inspector2-Type-StopCisSessionMessage-benchmarkProfile"></a>
The message benchmark profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** benchmarkVersion **   <a name="inspector2-Type-StopCisSessionMessage-benchmarkVersion"></a>
The message benchmark version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8.
Required: No

 ** computePlatform **   <a name="inspector2-Type-StopCisSessionMessage-computePlatform"></a>
The message compute platform.
Type: [ComputePlatform](API_ComputePlatform.md) object
Required: No

 ** reason **   <a name="inspector2-Type-StopCisSessionMessage-reason"></a>
The reason for the message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_StopCisSessionMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/StopCisSessionMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/StopCisSessionMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/StopCisSessionMessage)
