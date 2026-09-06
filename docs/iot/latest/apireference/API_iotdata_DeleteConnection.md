---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_DeleteConnection.html
---

# DeleteConnection
<a name="API_iotdata_DeleteConnection"></a>

Disconnects a connected MQTT client from AWS IoT Core. When you disconnect a client, AWS IoT Core closes the client's network connection and optionally cleans the session state.

Requires permission to access the [DeleteConnection](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iotdata_DeleteConnection_RequestSyntax"></a>

```
DELETE /connections/{{clientId}}?cleanSession={{cleanSession}}&preventWillMessage={{preventWillMessage}} HTTP/1.1
```

## URI Request Parameters
<a name="API_iotdata_DeleteConnection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [cleanSession](#API_iotdata_DeleteConnection_RequestSyntax) **   <a name="iot-iotdata_DeleteConnection-request-uri-cleanSession"></a>
Specifies whether to remove the client's persistent session state when disconnecting. Set to `TRUE` to delete all session information, including subscriptions and queued messages. Set to `FALSE` to preserve the session state for [persistent sessions](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html#mqtt-persistent-sessions). For clean sessions this parameter will be ignored. By default, this is set to `FALSE` (preserves the session state).

 ** [clientId](#API_iotdata_DeleteConnection_RequestSyntax) **   <a name="iot-iotdata_DeleteConnection-request-uri-clientId"></a>
The unique identifier of the MQTT client to disconnect. The client ID can't start with a dollar sign ($).
MQTT client IDs must be URL encoded (percent-encoded) when they contain characters that are not valid in HTTP requests, such as spaces, forward slashes (/), and UTF-8 characters.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[^$].*`
Required: Yes

 ** [preventWillMessage](#API_iotdata_DeleteConnection_RequestSyntax) **   <a name="iot-iotdata_DeleteConnection-request-uri-preventWillMessage"></a>
Controls if AWS IoT Core publishes the client's Last Will and Testament (LWT) message upon disconnection. Set to `TRUE` to prevent publishing the LWT message. Set to `FALSE` to ensure that LWT is published. By default, this is set to `FALSE` (LWT message is published).

## Request Body
<a name="API_iotdata_DeleteConnection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_iotdata_DeleteConnection_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_iotdata_DeleteConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_iotdata_DeleteConnection_Errors"></a>

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
<a name="API_iotdata_DeleteConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-data-2015-05-28/DeleteConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-data-2015-05-28/DeleteConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-data-2015-05-28/DeleteConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-data-2015-05-28/DeleteConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-data-2015-05-28/DeleteConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-data-2015-05-28/DeleteConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-data-2015-05-28/DeleteConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-data-2015-05-28/DeleteConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-data-2015-05-28/DeleteConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-data-2015-05-28/DeleteConnection)
