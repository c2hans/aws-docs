---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_KinesisAction.html
---

# KinesisAction
<a name="API_KinesisAction"></a>

Describes an action to write data to an Amazon Kinesis stream.

## Contents
<a name="API_KinesisAction_Contents"></a>

 ** roleArn **   <a name="iot-Type-KinesisAction-roleArn"></a>
The ARN of the IAM role that grants access to the Amazon Kinesis stream.
Type: String
Required: Yes

 ** streamName **   <a name="iot-Type-KinesisAction-streamName"></a>
The name of the Amazon Kinesis stream.
Type: String
Required: Yes

 ** partitionKey **   <a name="iot-Type-KinesisAction-partitionKey"></a>
The partition key.
Type: String
Required: No

## See Also
<a name="API_KinesisAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/KinesisAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/KinesisAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/KinesisAction)
