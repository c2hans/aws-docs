---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_SqsAction.html
---

# SqsAction
<a name="API_SqsAction"></a>

Describes an action to publish data to an Amazon SQS queue.

## Contents
<a name="API_SqsAction_Contents"></a>

 ** queueUrl **   <a name="iot-Type-SqsAction-queueUrl"></a>
The URL of the Amazon SQS queue.
Type: String
Required: Yes

 ** roleArn **   <a name="iot-Type-SqsAction-roleArn"></a>
The ARN of the IAM role that grants access.
Type: String
Required: Yes

 ** useBase64 **   <a name="iot-Type-SqsAction-useBase64"></a>
Specifies whether to use Base64 encoding.
Type: Boolean
Required: No

## See Also
<a name="API_SqsAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/SqsAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/SqsAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/SqsAction)
