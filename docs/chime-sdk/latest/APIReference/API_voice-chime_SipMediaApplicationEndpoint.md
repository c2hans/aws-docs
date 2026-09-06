---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SipMediaApplicationEndpoint.html
---

# SipMediaApplicationEndpoint
<a name="API_voice-chime_SipMediaApplicationEndpoint"></a>

The endpoint assigned to a SIP media application.

## Contents
<a name="API_voice-chime_SipMediaApplicationEndpoint_Contents"></a>

 ** LambdaArn **   <a name="chimesdk-Type-voice-chime_SipMediaApplicationEndpoint-LambdaArn"></a>
Valid Amazon Resource Name (ARN) of the Lambda function, version, or alias. The function must be created in the same AWS Region as the SIP media application.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: No

## See Also
<a name="API_voice-chime_SipMediaApplicationEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/SipMediaApplicationEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/SipMediaApplicationEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/SipMediaApplicationEndpoint)
