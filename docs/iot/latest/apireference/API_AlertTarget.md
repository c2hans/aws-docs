---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AlertTarget.html
---

# AlertTarget
<a name="API_AlertTarget"></a>

A structure containing the alert target ARN and the role ARN.

## Contents
<a name="API_AlertTarget_Contents"></a>

 ** alertTargetArn **   <a name="iot-Type-AlertTarget-alertTargetArn"></a>
The Amazon Resource Name (ARN) of the notification target to which alerts are sent.
Type: String
Required: Yes

 ** roleArn **   <a name="iot-Type-AlertTarget-roleArn"></a>
The ARN of the role that grants permission to send alerts to the notification target.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_AlertTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AlertTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AlertTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AlertTarget)
