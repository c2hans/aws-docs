---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GetThingConnectivityData.html
---

# GetThingConnectivityData
<a name="API_GetThingConnectivityData"></a>

Retrieves the live connectivity status per device. If a device has never connected to IoT Core or was disconnected for more than 1 hour before fleet indexing's `thingConnectivityIndexingMode` was enabled, the response will have the `connected` field set to `false` with no additional session details.

## Request Syntax
<a name="API_GetThingConnectivityData_RequestSyntax"></a>

```
POST /things/{{thingName}}/connectivity-data HTTP/1.1
Content-type: application/json

{
   "includeSocketInformation": {{boolean}}
}
```

## URI Request Parameters
<a name="API_GetThingConnectivityData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingName](#API_GetThingConnectivityData_RequestSyntax) **   <a name="iot-GetThingConnectivityData-request-uri-thingName"></a>
The name of your IoT thing.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_GetThingConnectivityData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [includeSocketInformation](#API_GetThingConnectivityData_RequestSyntax) **   <a name="iot-GetThingConnectivityData-request-includeSocketInformation"></a>
Specifies if socket information (sourcePort, targetPort, sourceIp, targetIp, vpcEndpointId) should be included in the GetThingConnectivityData response. Set to `true` to include socket information. Set to `false` to omit socket information. By default, this is set to `false`.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetThingConnectivityData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "cleanSession": boolean,
   "clientId": "string",
   "connected": boolean,
   "disconnectReason": "string",
   "keepAliveDuration": number,
   "sessionExpiry": number,
   "sourceIp": "string",
   "sourcePort": number,
   "targetIp": "string",
   "targetPort": number,
   "thingName": "string",
   "timestamp": number,
   "vpcEndpointId": "string"
}
```

## Response Elements
<a name="API_GetThingConnectivityData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cleanSession](#API_GetThingConnectivityData_ResponseSyntax) **   <a name="iot-GetThingConnectivityData-response-cleanSession"></a>
Indicates whether the client is using a clean session. Returns `true` for clean sessions.
Type: Boolean

 ** [clientId](#API_GetThingConnectivityData_ResponseSyntax) **   <a name="iot-GetThingConnectivityData-response-clientId"></a>
The unique identifier of the MQTT client.
Type: String

 ** [connected](#API_GetThingConnectivityData_ResponseSyntax) **   <a name="iot-GetThingConnectivityData-response-connected"></a>
A Boolean that indicates the connectivity status.
Type: Boolean

 ** [disconnectReason](#API_GetThingConnectivityData_ResponseSyntax) **   <a name="iot-GetThingConnectivityData-response-disconnectReason"></a>
The reason that the client is disconnected.
Type: String
Valid Values: `AUTH_ERROR | CLIENT_INITIATED_DISCONNECT | CLIENT_ERROR | CONNECTION_LOST | DUPLICATE_CLIENTID | FORBIDDEN_ACCESS | MQTT_KEEP_ALIVE_TIMEOUT | SERVER_ERROR | SERVER_INITIATED_DISCONNECT | API_INITIATED_DISCONNECT | THROTTLED | WEBSOCKET_TTL_EXPIRATION | CUSTOMAUTH_TTL_EXPIRATION | UNKNOWN | NONE`

 ** [keepAliveDuration](#API_GetThingConnectivityData_ResponseSyntax) **   <a name="iot-GetThingConnectivityData-response-keepAliveDuration"></a>
The keep-alive interval in seconds that the client specified when establishing the connection.
Type: Integer

 ** [sessionExpiry](#API_GetThingConnectivityData_ResponseSyntax) **   <a name="iot-GetThingConnectivityData-response-sessionExpiry"></a>
The session expiry interval in seconds for the MQTT client connection. This value indicates how long the session will remain active after the client disconnects.
Type: Long

 ** [sourceIp](#API_GetThingConnectivityData_ResponseSyntax) **   <a name="iot-GetThingConnectivityData-response-sourceIp"></a>
The IP address of the client that initiated the connection.
Type: String

 ** [sourcePort](#API_GetThingConnectivityData_ResponseSyntax) **   <a name="iot-GetThingConnectivityData-response-sourcePort"></a>
The client's source port.
Type: Integer

 ** [targetIp](#API_GetThingConnectivityData_ResponseSyntax) **   <a name="iot-GetThingConnectivityData-response-targetIp"></a>
The IP address of the AWS IoT Core endpoint that the client connected to.
Type: String

 ** [targetPort](#API_GetThingConnectivityData_ResponseSyntax) **   <a name="iot-GetThingConnectivityData-response-targetPort"></a>
The port number of the AWS IoT Core endpoint that the client connected to.
Type: Integer

 ** [thingName](#API_GetThingConnectivityData_ResponseSyntax) **   <a name="iot-GetThingConnectivityData-response-thingName"></a>
The name of your IoT thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [timestamp](#API_GetThingConnectivityData_ResponseSyntax) **   <a name="iot-GetThingConnectivityData-response-timestamp"></a>
The timestamp of when the device connected or disconnected.
Type: Timestamp

 ** [vpcEndpointId](#API_GetThingConnectivityData_ResponseSyntax) **   <a name="iot-GetThingConnectivityData-response-vpcEndpointId"></a>
The ID of the VPC endpoint. Present for clients connected to AWS IoT Core via a VPC endpoint.
Type: String

## Errors
<a name="API_GetThingConnectivityData_Errors"></a>

 ** IndexNotReadyException **
The index is not ready.
 ** message **
The message for the exception.
HTTP Status Code: 400

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
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_GetThingConnectivityData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/GetThingConnectivityData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/GetThingConnectivityData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GetThingConnectivityData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/GetThingConnectivityData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GetThingConnectivityData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/GetThingConnectivityData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/GetThingConnectivityData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/GetThingConnectivityData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/GetThingConnectivityData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GetThingConnectivityData)
