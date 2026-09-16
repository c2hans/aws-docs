---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_Publish.html
---

# Publish
<a name="API_iotdata_Publish"></a>

Publishes an MQTT message.

Requires permission to access the [Publish](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

For more information about MQTT messages, see [MQTT Protocol](http://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) in the AWS IoT Developer Guide.

For more information about messaging costs, see [AWS IoT Core pricing - Messaging](http://aws.amazon.com/iot-core/pricing/#Messaging).

## Request Syntax
<a name="API_iotdata_Publish_RequestSyntax"></a>

```
POST /topics/{{topic}}?contentType={{contentType}}&messageExpiry={{messageExpiry}}&qos={{qos}}&responseTopic={{responseTopic}}&retain={{retain}} HTTP/1.1
x-amz-mqtt5-user-properties: {{userProperties}}
x-amz-mqtt5-payload-format-indicator: {{payloadFormatIndicator}}
x-amz-mqtt5-correlation-data: {{correlationData}}

{{payload}}
```

## URI Request Parameters
<a name="API_iotdata_Publish_RequestParameters"></a>

The request uses the following URI parameters.

 ** [contentType](#API_iotdata_Publish_RequestSyntax) **   <a name="iot-iotdata_Publish-request-uri-contentType"></a>
A UTF-8 encoded string that describes the content of the publishing message.

 ** [correlationData](#API_iotdata_Publish_RequestSyntax) **   <a name="iot-iotdata_Publish-request-correlationData"></a>
The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when it's received. `correlationData` is an HTTP header value in the API.

 ** [messageExpiry](#API_iotdata_Publish_RequestSyntax) **   <a name="iot-iotdata_Publish-request-uri-messageExpiry"></a>
A user-defined integer value that represents the message expiry interval in seconds. If absent, the message doesn't expire. For more information about the limits of `messageExpiry`, see [AWS IoT Core message broker and protocol limits and quotas ](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits) from the AWS Reference Guide.

 ** [payloadFormatIndicator](#API_iotdata_Publish_RequestSyntax) **   <a name="iot-iotdata_Publish-request-payloadFormatIndicator"></a>
An `Enum` string value that indicates whether the payload is formatted as UTF-8. `payloadFormatIndicator` is an HTTP header value in the API.
Valid Values: `UNSPECIFIED_BYTES | UTF8_DATA`

 ** [qos](#API_iotdata_Publish_RequestSyntax) **   <a name="iot-iotdata_Publish-request-uri-qos"></a>
The Quality of Service (QoS) level. The default QoS level is 0.
Valid Range: Minimum value of 0. Maximum value of 1.

 ** [responseTopic](#API_iotdata_Publish_RequestSyntax) **   <a name="iot-iotdata_Publish-request-uri-responseTopic"></a>
A UTF-8 encoded string that's used as the topic name for a response message. The response topic is used to describe the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters.

 ** [retain](#API_iotdata_Publish_RequestSyntax) **   <a name="iot-iotdata_Publish-request-uri-retain"></a>
A Boolean value that determines whether to set the RETAIN flag when the message is published.
Setting the RETAIN flag causes the message to be retained and sent to new subscribers to the topic.
Valid values: `true` \| `false`
Default value: `false`

 ** [topic](#API_iotdata_Publish_RequestSyntax) **   <a name="iot-iotdata_Publish-request-uri-topic"></a>
The name of the MQTT topic.
Required: Yes

 ** [userProperties](#API_iotdata_Publish_RequestSyntax) **   <a name="iot-iotdata_Publish-request-userProperties"></a>
A JSON string that contains an array of JSON objects. If you don’t use AWS SDK or AWS CLI, you must encode the JSON string to base64 format before adding it to the HTTP header. `userProperties` is an HTTP header value in the API.
The following example `userProperties` parameter is a JSON string which represents two User Properties. Note that it needs to be base64-encoded:
 `[{"deviceName": "alpha"}, {"deviceCnt": "45"}]`

## Request Body
<a name="API_iotdata_Publish_RequestBody"></a>

The request accepts the following binary data.

 ** [payload](#API_iotdata_Publish_RequestSyntax) **   <a name="iot-iotdata_Publish-request-payload"></a>
The message body. MQTT accepts text, binary, and empty (null) message payloads.
Publishing an empty (null) payload with **retain** = `true` deletes the retained message identified by **topic** from AWS IoT Core.

## Response Syntax
<a name="API_iotdata_Publish_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_iotdata_Publish_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_iotdata_Publish_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** MethodNotAllowedException **
The specified combination of HTTP verb and URI is not supported.
 ** message **
The message for the exception.
HTTP Status Code: 405

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 429

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_iotdata_Publish_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-data-2015-05-28/Publish)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-data-2015-05-28/Publish)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-data-2015-05-28/Publish)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-data-2015-05-28/Publish)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-data-2015-05-28/Publish)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-data-2015-05-28/Publish)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-data-2015-05-28/Publish)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-data-2015-05-28/Publish)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-data-2015-05-28/Publish)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-data-2015-05-28/Publish)
