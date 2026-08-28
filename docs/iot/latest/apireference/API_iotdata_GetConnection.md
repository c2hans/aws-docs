---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_GetConnection.html
---

# GetConnection
<a name="API_iotdata_GetConnection"></a>

Retrieves connection information for the specified MQTT client.

Requires permission to access the [GetConnection](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iotdata_GetConnection_RequestSyntax"></a>

```
GET /connections/{{clientId}}?includeSocketInformation={{includeSocketInformation}} HTTP/1.1
```

## URI Request Parameters
<a name="API_iotdata_GetConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientId](#API_iotdata_GetConnection_RequestSyntax) **   <a name="iot-iotdata_GetConnection-request-uri-clientId"></a>
The unique identifier of the MQTT client to retrieve connection information. The client ID can't start with a dollar sign ($).
MQTT client IDs must be URL encoded (percent-encoded) when they contain characters that are not valid in HTTP requests, such as spaces, forward slashes (/), and UTF-8 characters.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[^$].*`
Required: Yes

 ** [includeSocketInformation](#API_iotdata_GetConnection_RequestSyntax) **   <a name="iot-iotdata_GetConnection-request-uri-includeSocketInformation"></a>
Specifies if socket information (sourcePort, targetPort, sourceIp, targetIp) should be included in the GetConnection response. Set to `TRUE` to include socket information. Set to `FALSE` to omit socket information. By default, this is set to `FALSE`. See the [developer guide](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html#mqtt-client-disconnect) for how to authorize this parameter.

## Request Body
<a name="API_iotdata_GetConnection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_iotdata_GetConnection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "cleanSession": boolean,
   "clientId": "string",
   "connected": boolean,
   "connectedSince": number,
   "disconnectedSince": number,
   "disconnectReason": "string",
   "keepAliveDuration": number,
   "sessionExpiry": number,
   "sourceIp": "string",
   "sourcePort": number,
   "targetIp": "string",
   "targetPort": number,
   "thingName": "string",
   "vpcEndpointId": "string"
}
```

## Response Elements
<a name="API_iotdata_GetConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cleanSession](#API_iotdata_GetConnection_ResponseSyntax) **   <a name="iot-iotdata_GetConnection-response-cleanSession"></a>
Indicates whether the client is using a clean session. Returns `true` for clean sessions or `false` for persistent sessions.
Type: Boolean

 ** [clientId](#API_iotdata_GetConnection_ResponseSyntax) **   <a name="iot-iotdata_GetConnection-response-clientId"></a>
The unique identifier of the MQTT client. This is the same client ID that was used when the client established the connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[^$].*`

 ** [connected](#API_iotdata_GetConnection_ResponseSyntax) **   <a name="iot-iotdata_GetConnection-response-connected"></a>
The connection state of the client. Returns `true` if the client is currently connected, or `false` if the client is not connected.
Type: Boolean

 ** [connectedSince](#API_iotdata_GetConnection_ResponseSyntax) **   <a name="iot-iotdata_GetConnection-response-connectedSince"></a>
Unix timestamp (in milliseconds) indicating when the client connected. Present only when connected is true.
Type: Long

 ** [disconnectedSince](#API_iotdata_GetConnection_ResponseSyntax) **   <a name="iot-iotdata_GetConnection-response-disconnectedSince"></a>
Unix timestamp (in milliseconds) indicating when the client disconnected. Present only when connected is false. This information is available for 30 minutes after the client disconnects.
Type: Long

 ** [disconnectReason](#API_iotdata_GetConnection_ResponseSyntax) **   <a name="iot-iotdata_GetConnection-response-disconnectReason"></a>
The reason for the last disconnection, if the client is currently disconnected. See the [developer guide](https://docs.aws.amazon.com/iot/latest/developerguide/life-cycle-events.html#connect-disconnect) for valid disconnect reasons.
Type: String

 ** [keepAliveDuration](#API_iotdata_GetConnection_ResponseSyntax) **   <a name="iot-iotdata_GetConnection-response-keepAliveDuration"></a>
The keep-alive interval in seconds that the client specified when establishing the connection.
Type: Integer

 ** [sessionExpiry](#API_iotdata_GetConnection_ResponseSyntax) **   <a name="iot-iotdata_GetConnection-response-sessionExpiry"></a>
The session expiry interval in seconds for the MQTT client connection. This is configured by the user. This value indicates how long the session will remain active after the client disconnects.
Type: Long

 ** [sourceIp](#API_iotdata_GetConnection_ResponseSyntax) **   <a name="iot-iotdata_GetConnection-response-sourceIp"></a>
The IP address of the client that initiated the connection.
Type: String

 ** [sourcePort](#API_iotdata_GetConnection_ResponseSyntax) **   <a name="iot-iotdata_GetConnection-response-sourcePort"></a>
The client's source port.
Type: Integer

 ** [targetIp](#API_iotdata_GetConnection_ResponseSyntax) **   <a name="iot-iotdata_GetConnection-response-targetIp"></a>
The IP address of the AWS IoT Core endpoint that the client connected to. For clients connected to VPC endpoints, this is the private IP address of the network interface the client is connected to.
Type: String

 ** [targetPort](#API_iotdata_GetConnection_ResponseSyntax) **   <a name="iot-iotdata_GetConnection-response-targetPort"></a>
The port number of the AWS IoT Core endpoint that the client connected to.
Type: Integer

 ** [thingName](#API_iotdata_GetConnection_ResponseSyntax) **   <a name="iot-iotdata_GetConnection-response-thingName"></a>
The name of the thing associated with the principal of the MQTT client, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [vpcEndpointId](#API_iotdata_GetConnection_ResponseSyntax) **   <a name="iot-iotdata_GetConnection-response-vpcEndpointId"></a>
The ID of the VPC endpoint. Present for clients connected to IoT Core via a [VPC endpoint](https://docs.aws.amazon.com/iot/latest/developerguide/IoTCore-VPC.html).
Type: String

## Errors
<a name="API_iotdata_GetConnection_Errors"></a>

 ** ForbiddenException **
The caller isn't authorized to make the request.
HTTP Status Code: 403

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

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 429

## See Also
<a name="API_iotdata_GetConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-data-2015-05-28/GetConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-data-2015-05-28/GetConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-data-2015-05-28/GetConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-data-2015-05-28/GetConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-data-2015-05-28/GetConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-data-2015-05-28/GetConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-data-2015-05-28/GetConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-data-2015-05-28/GetConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-data-2015-05-28/GetConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-data-2015-05-28/GetConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
