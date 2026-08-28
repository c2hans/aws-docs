---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetNotificationConfiguration.html
---

# GetNotificationConfiguration
<a name="API_GetNotificationConfiguration"></a>

 Get a notification configuration for a specified event type.

## Request Syntax
<a name="API_GetNotificationConfiguration_RequestSyntax"></a>

```
GET /notification-configurations/{{EventType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetNotificationConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EventType](#API_GetNotificationConfiguration_RequestSyntax) **   <a name="managedintegrations-GetNotificationConfiguration-request-uri-EventType"></a>
The type of event triggering a device notification to the customer-managed destination.
Valid Values: `DEVICE_COMMAND | DEVICE_COMMAND_REQUEST | DEVICE_DISCOVERY_STATUS | DEVICE_EVENT | DEVICE_LIFE_CYCLE | DEVICE_STATE | DEVICE_OTA | DEVICE_WSS | CONNECTOR_ASSOCIATION | ACCOUNT_ASSOCIATION | CONNECTOR_ERROR_REPORT`
Required: Yes

## Request Body
<a name="API_GetNotificationConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetNotificationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedAt": number,
   "DestinationName": "string",
   "EventType": "string",
   "Tags": {
      "string" : "string"
   },
   "UpdatedAt": number
}
```

## Response Elements
<a name="API_GetNotificationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_GetNotificationConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetNotificationConfiguration-response-CreatedAt"></a>
The timestamp value of when the notification configuration was created.
Type: Timestamp

 ** [DestinationName](#API_GetNotificationConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetNotificationConfiguration-response-DestinationName"></a>
The name of the destination for the notification configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{N} ._-]+`

 ** [EventType](#API_GetNotificationConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetNotificationConfiguration-response-EventType"></a>
The type of event triggering a device notification to the customer-managed destination.
Type: String
Valid Values: `DEVICE_COMMAND | DEVICE_COMMAND_REQUEST | DEVICE_DISCOVERY_STATUS | DEVICE_EVENT | DEVICE_LIFE_CYCLE | DEVICE_STATE | DEVICE_OTA | DEVICE_WSS | CONNECTOR_ASSOCIATION | ACCOUNT_ASSOCIATION | CONNECTOR_ERROR_REPORT`

 ** [Tags](#API_GetNotificationConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetNotificationConfiguration-response-Tags"></a>
 *This parameter has been deprecated.*
A set of key/value pairs that are used to manage the notification configuration.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [UpdatedAt](#API_GetNotificationConfiguration_ResponseSyntax) **   <a name="managedintegrations-GetNotificationConfiguration-response-UpdatedAt"></a>
The timestamp value of when the notification configuration was last updated.
Type: Timestamp

## Errors
<a name="API_GetNotificationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_GetNotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetNotificationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetNotificationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetNotificationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetNotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetNotificationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetNotificationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetNotificationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetNotificationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetNotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetNotificationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
