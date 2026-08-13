---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_IotAnalyticsAction.html
---

# IotAnalyticsAction
<a name="API_IotAnalyticsAction"></a>

Sends message data to an AWS IoT Analytics channel.

## Contents
<a name="API_IotAnalyticsAction_Contents"></a>

 ** batchMode **   <a name="iot-Type-IotAnalyticsAction-batchMode"></a>
Whether to process the action as a batch. The default value is `false`.
When `batchMode` is `true` and the rule SQL statement evaluates to an Array, each Array element is delivered as a separate message when passed by [`BatchPutMessage`](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_BatchPutMessage.html) to the AWS IoT Analytics channel. The resulting array can't have more than 100 messages.
Type: Boolean
Required: No

 ** channelArn **   <a name="iot-Type-IotAnalyticsAction-channelArn"></a>
(deprecated) The ARN of the IoT Analytics channel to which message data will be sent.
Type: String
Required: No

 ** channelName **   <a name="iot-Type-IotAnalyticsAction-channelName"></a>
The name of the IoT Analytics channel to which message data will be sent.
Type: String
Required: No

 ** roleArn **   <a name="iot-Type-IotAnalyticsAction-roleArn"></a>
The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).
Type: String
Required: No

## See Also
<a name="API_IotAnalyticsAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/IotAnalyticsAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/IotAnalyticsAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/IotAnalyticsAction)
