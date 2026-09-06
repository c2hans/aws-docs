---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ThingConnectivity.html
---

# ThingConnectivity
<a name="API_ThingConnectivity"></a>

The connectivity status of the thing.

## Contents
<a name="API_ThingConnectivity_Contents"></a>

 ** cleanSession **   <a name="iot-Type-ThingConnectivity-cleanSession"></a>
Indicates whether the client is using a clean session. Returns `true` for clean sessions.
Type: Boolean
Required: No

 ** clientId **   <a name="iot-Type-ThingConnectivity-clientId"></a>
The unique identifier of the MQTT client.
Type: String
Required: No

 ** connected **   <a name="iot-Type-ThingConnectivity-connected"></a>
True if the thing is connected to the AWS IoT Core service; false if it is not connected.
Type: Boolean
Required: No

 ** disconnectReason **   <a name="iot-Type-ThingConnectivity-disconnectReason"></a>
The reason that the client is disconnected.
Type: String
Required: No

 ** keepAliveDuration **   <a name="iot-Type-ThingConnectivity-keepAliveDuration"></a>
The keep-alive interval in seconds that the client specified when establishing the connection.
Type: Integer
Required: No

 ** sessionExpiry **   <a name="iot-Type-ThingConnectivity-sessionExpiry"></a>
The session expiry interval in seconds for the MQTT client connection. This value indicates how long the session will remain active after the client disconnects.
Type: Long
Required: No

 ** timestamp **   <a name="iot-Type-ThingConnectivity-timestamp"></a>
The epoch time (in milliseconds) when the thing last connected or disconnected.
Type: Long
Required: No

## See Also
<a name="API_ThingConnectivity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ThingConnectivity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ThingConnectivity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ThingConnectivity)
