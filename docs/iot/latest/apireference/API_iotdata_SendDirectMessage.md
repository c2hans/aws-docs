---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_SendDirectMessage.html
---

# SendDirectMessage
<a name="API_iotdata_SendDirectMessage"></a>

Sends an MQTT message directly to a specific client identified by its client ID.

 `SendDirectMessage` targets a single client ID. The receiving client does not need to subscribe to the topic, but the receiver's policy must allow `iot:Receive` on the specified topic.

Requires permission to access the [SendDirectMessage](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

For more information about messaging costs, see [AWS IoT Core pricing](http://aws.amazon.com/iot-core/pricing/).

## Request Syntax
<a name="API_iotdata_SendDirectMessage_RequestSyntax"></a>

```
POST /connections/{{clientId}}/messages?confirmation={{confirmation}}&contentType={{contentType}}&responseTopic={{responseTopic}}&timeout={{timeout}}&topic={{topic}} HTTP/1.1
x-amz-mqtt5-user-properties: {{userProperties}}
x-amz-mqtt5-payload-format-indicator: {{payloadFormatIndicator}}
x-amz-mqtt5-correlation-data: {{correlationData}}

{{payload}}
```

## URI Request Parameters
<a name="API_iotdata_SendDirectMessage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientId](#API_iotdata_SendDirectMessage_RequestSyntax) **   <a name="iot-iotdata_SendDirectMessage-request-uri-clientId"></a>
The unique identifier of the MQTT client to send the message to.
Client IDs must not exceed 128 characters and can't start with a dollar sign ($). MQTT client IDs must be URL encoded (percent-encoded) when they contain characters that are not valid in HTTP requests, such as spaces, forward slashes (/), and UTF-8 characters. For more information, see [AWS IoT Core message broker and protocol limits and quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits).
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[^$].*`
Required: Yes

 ** [confirmation](#API_iotdata_SendDirectMessage_RequestSyntax) **   <a name="iot-iotdata_SendDirectMessage-request-uri-confirmation"></a>
A Boolean value that specifies whether to wait for delivery confirmation from the receiving client.
When set to `true`, the API delivers the message at QoS 1 and waits for the client to send a delivery confirmation (PUBACK) before returning a successful response. If delivery confirmation is not received within the specified `timeout` period, the API returns HTTP 504.
When set to `false`, the API delivers the message at QoS 0 and returns after AWS IoT Core attempts to deliver the message.
Valid values: `true` \| `false`
Default value: `false`

 ** [contentType](#API_iotdata_SendDirectMessage_RequestSyntax) **   <a name="iot-iotdata_SendDirectMessage-request-uri-contentType"></a>
The MQTT5 content type property forwarded to the receiving client (for example, `application/json`).

 ** [correlationData](#API_iotdata_SendDirectMessage_RequestSyntax) **   <a name="iot-iotdata_SendDirectMessage-request-correlationData"></a>
The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when it's received. `correlationData` is an HTTP header value in the API.

 ** [payloadFormatIndicator](#API_iotdata_SendDirectMessage_RequestSyntax) **   <a name="iot-iotdata_SendDirectMessage-request-payloadFormatIndicator"></a>
An `Enum` string value that indicates whether the payload is formatted as UTF-8. `payloadFormatIndicator` is an HTTP header value in the API.
Valid Values: `UNSPECIFIED_BYTES | UTF8_DATA`

 ** [responseTopic](#API_iotdata_SendDirectMessage_RequestSyntax) **   <a name="iot-iotdata_SendDirectMessage-request-uri-responseTopic"></a>
A UTF-8 encoded string that's used as the topic name for a response message. The response topic describes the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters. For more information, see [AWS IoT Core message broker and protocol limits and quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits).

 ** [timeout](#API_iotdata_SendDirectMessage_RequestSyntax) **   <a name="iot-iotdata_SendDirectMessage-request-uri-timeout"></a>
An integer that represents the maximum time, in seconds, to wait for a delivery confirmation (PUBACK) from the receiving client after the message has been delivered. This parameter is only used when `confirmation` is set to `true`. If `confirmation` is `false`, this parameter is ignored.
The total API response time may be higher than this value due to internal processing. Set your HTTP client timeout to a value greater than this parameter.
Valid range: 1 to 15 seconds.
Default value: `5` seconds.

 ** [topic](#API_iotdata_SendDirectMessage_RequestSyntax) **   <a name="iot-iotdata_SendDirectMessage-request-uri-topic"></a>
The topic of the outbound MQTT Publish message to the receiving client. For more information, see [AWS IoT Core message broker and protocol limits and quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits).
Required: Yes

 ** [userProperties](#API_iotdata_SendDirectMessage_RequestSyntax) **   <a name="iot-iotdata_SendDirectMessage-request-userProperties"></a>
A JSON string that contains an array of JSON objects. If you don't use AWS SDK or AWS CLI, you must encode the JSON string to base64 format before adding it to the HTTP header. `userProperties` is an HTTP header value in the API.
For MQTT 3.1.1 clients, user properties are silently dropped.
The following example `userProperties` parameter is a JSON string which represents two User Properties. Note that it needs to be base64-encoded:
 `[{"deviceName": "alpha"}, {"deviceCnt": "45"}]`

## Request Body
<a name="API_iotdata_SendDirectMessage_RequestBody"></a>

The request accepts the following binary data.

 ** [payload](#API_iotdata_SendDirectMessage_RequestSyntax) **   <a name="iot-iotdata_SendDirectMessage-request-payload"></a>
The message body. MQTT accepts text, binary, and empty (null) message payloads.

## Response Syntax
<a name="API_iotdata_SendDirectMessage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "message": "string",
   "traceId": "string"
}
```

## Response Elements
<a name="API_iotdata_SendDirectMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [message](#API_iotdata_SendDirectMessage_ResponseSyntax) **   <a name="iot-iotdata_SendDirectMessage-response-message"></a>
The status message indicating the result of the operation.
Type: String

 ** [traceId](#API_iotdata_SendDirectMessage_ResponseSyntax) **   <a name="iot-iotdata_SendDirectMessage-response-traceId"></a>
A unique identifier for the request. Include this value when contacting AWS Support for troubleshooting.
Type: String

## Errors
<a name="API_iotdata_SendDirectMessage_Errors"></a>

 ** ForbiddenException **
The caller isn't authorized to make the request.
HTTP Status Code: 403

 ** GatewayTimeoutException **
The delivery confirmation was not received from the client within the specified timeout period.
 ** message **
The message for the exception.
HTTP Status Code: 504

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

 ** RequestEntityTooLargeException **
The payload exceeds the maximum size allowed.
 ** message **
The message for the exception.
HTTP Status Code: 413

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

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
<a name="API_iotdata_SendDirectMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-data-2015-05-28/SendDirectMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-data-2015-05-28/SendDirectMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-data-2015-05-28/SendDirectMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-data-2015-05-28/SendDirectMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-data-2015-05-28/SendDirectMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-data-2015-05-28/SendDirectMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-data-2015-05-28/SendDirectMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-data-2015-05-28/SendDirectMessage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-data-2015-05-28/SendDirectMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-data-2015-05-28/SendDirectMessage)
