---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateNotificationConfiguration.html
---

# CreateNotificationConfiguration
<a name="API_CreateNotificationConfiguration"></a>

Creates a notification configuration. A configuration is a connection between an event type and a destination that you have already created.

## Request Syntax
<a name="API_CreateNotificationConfiguration_RequestSyntax"></a>

```
POST /notification-configurations HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "DestinationName": "{{string}}",
   "EventType": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateNotificationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateNotificationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateNotificationConfiguration_RequestSyntax) **   <a name="managedintegrations-CreateNotificationConfiguration-request-ClientToken"></a>
An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9=_-]+`
Required: No

 ** [DestinationName](#API_CreateNotificationConfiguration_RequestSyntax) **   <a name="managedintegrations-CreateNotificationConfiguration-request-DestinationName"></a>
The name of the destination for the notification configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{N} ._-]+`
Required: Yes

 ** [EventType](#API_CreateNotificationConfiguration_RequestSyntax) **   <a name="managedintegrations-CreateNotificationConfiguration-request-EventType"></a>
The type of event triggering a device notification to the customer-managed destination.
Type: String
Valid Values: `DEVICE_COMMAND | DEVICE_COMMAND_REQUEST | DEVICE_DISCOVERY_STATUS | DEVICE_EVENT | DEVICE_LIFE_CYCLE | DEVICE_STATE | DEVICE_OTA | DEVICE_WSS | CONNECTOR_ASSOCIATION | ACCOUNT_ASSOCIATION | CONNECTOR_ERROR_REPORT`
Required: Yes

 ** [Tags](#API_CreateNotificationConfiguration_RequestSyntax) **   <a name="managedintegrations-CreateNotificationConfiguration-request-Tags"></a>
 *This parameter has been deprecated.*
A set of key/value pairs that are used to manage the notification configuration.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateNotificationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "EventType": "string"
}
```

## Response Elements
<a name="API_CreateNotificationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [EventType](#API_CreateNotificationConfiguration_ResponseSyntax) **   <a name="managedintegrations-CreateNotificationConfiguration-response-EventType"></a>
The type of event triggering a device notification to the customer-managed destination.
Type: String
Valid Values: `DEVICE_COMMAND | DEVICE_COMMAND_REQUEST | DEVICE_DISCOVERY_STATUS | DEVICE_EVENT | DEVICE_LIFE_CYCLE | DEVICE_STATE | DEVICE_OTA | DEVICE_WSS | CONNECTOR_ASSOCIATION | ACCOUNT_ASSOCIATION | CONNECTOR_ERROR_REPORT`

## Errors
<a name="API_CreateNotificationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict with the request.
HTTP Status Code: 409

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_CreateNotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/CreateNotificationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/CreateNotificationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CreateNotificationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/CreateNotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CreateNotificationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/CreateNotificationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/CreateNotificationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/CreateNotificationConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/CreateNotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CreateNotificationConfiguration)
