---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_DeleteNotificationConfiguration.html
---

# DeleteNotificationConfiguration
<a name="API_DeleteNotificationConfiguration"></a>

Deletes a notification configuration.

## Request Syntax
<a name="API_DeleteNotificationConfiguration_RequestSyntax"></a>

```
DELETE /notification-configurations/{{EventType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteNotificationConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EventType](#API_DeleteNotificationConfiguration_RequestSyntax) **   <a name="managedintegrations-DeleteNotificationConfiguration-request-uri-EventType"></a>
The type of event triggering a device notification to the customer-managed destination.
Valid Values: `DEVICE_COMMAND | DEVICE_COMMAND_REQUEST | DEVICE_DISCOVERY_STATUS | DEVICE_EVENT | DEVICE_LIFE_CYCLE | DEVICE_STATE | DEVICE_OTA | DEVICE_WSS | CONNECTOR_ASSOCIATION | ACCOUNT_ASSOCIATION | CONNECTOR_ERROR_REPORT`
Required: Yes

## Request Body
<a name="API_DeleteNotificationConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteNotificationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteNotificationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteNotificationConfiguration_Errors"></a>

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
<a name="API_DeleteNotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/DeleteNotificationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/DeleteNotificationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/DeleteNotificationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/DeleteNotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/DeleteNotificationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/DeleteNotificationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/DeleteNotificationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/DeleteNotificationConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/DeleteNotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/DeleteNotificationConfiguration)
