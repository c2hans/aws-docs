---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_GetRetainedMessage.html
---

# GetRetainedMessage
<a name="API_iotdata_GetRetainedMessage"></a>

Gets the details of a single retained message for the specified topic.

This action returns the message payload of the retained message, which can incur messaging costs. To list only the topic names of the retained messages, call [ListRetainedMessages](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_ListRetainedMessages.html).

Requires permission to access the [GetRetainedMessage](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html) action.

For more information about messaging costs, see [AWS IoT Core pricing - Messaging](http://aws.amazon.com/iot-core/pricing/#Messaging).

## Request Syntax
<a name="API_iotdata_GetRetainedMessage_RequestSyntax"></a>

```
GET /retainedMessage/{{topic}} HTTP/1.1
```

## URI Request Parameters
<a name="API_iotdata_GetRetainedMessage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [topic](#API_iotdata_GetRetainedMessage_RequestSyntax) **   <a name="iot-iotdata_GetRetainedMessage-request-uri-topic"></a>
The topic name of the retained message to retrieve.
Required: Yes

## Request Body
<a name="API_iotdata_GetRetainedMessage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_iotdata_GetRetainedMessage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "lastModifiedTime": number,
   "payload": blob,
   "qos": number,
   "topic": "string",
   "userProperties": blob
}
```

## Response Elements
<a name="API_iotdata_GetRetainedMessage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lastModifiedTime](#API_iotdata_GetRetainedMessage_ResponseSyntax) **   <a name="iot-iotdata_GetRetainedMessage-response-lastModifiedTime"></a>
The Epoch date and time, in milliseconds, when the retained message was stored by AWS IoT.
Type: Long

 ** [payload](#API_iotdata_GetRetainedMessage_ResponseSyntax) **   <a name="iot-iotdata_GetRetainedMessage-response-payload"></a>
The Base64-encoded message payload of the retained message body.
Type: Base64-encoded binary data object

 ** [qos](#API_iotdata_GetRetainedMessage_ResponseSyntax) **   <a name="iot-iotdata_GetRetainedMessage-response-qos"></a>
The quality of service (QoS) level used to publish the retained message.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1.

 ** [topic](#API_iotdata_GetRetainedMessage_ResponseSyntax) **   <a name="iot-iotdata_GetRetainedMessage-response-topic"></a>
The topic name to which the retained message was published.
Type: String

 ** [userProperties](#API_iotdata_GetRetainedMessage_ResponseSyntax) **   <a name="iot-iotdata_GetRetainedMessage-response-userProperties"></a>
A base64-encoded JSON string that includes an array of JSON objects, or null if the retained message doesn't include any user properties.
The following example `userProperties` parameter is a JSON string that represents two user properties. Note that it will be base64-encoded:
 `[{"deviceName": "alpha"}, {"deviceCnt": "45"}]`
Type: Base64-encoded binary data object

## Errors
<a name="API_iotdata_GetRetainedMessage_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

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
<a name="API_iotdata_GetRetainedMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-data-2015-05-28/GetRetainedMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-data-2015-05-28/GetRetainedMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-data-2015-05-28/GetRetainedMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-data-2015-05-28/GetRetainedMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-data-2015-05-28/GetRetainedMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-data-2015-05-28/GetRetainedMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-data-2015-05-28/GetRetainedMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-data-2015-05-28/GetRetainedMessage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-data-2015-05-28/GetRetainedMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-data-2015-05-28/GetRetainedMessage)
