---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateOtaTask.html
---

# CreateOtaTask
<a name="API_CreateOtaTask"></a>

Create an over-the-air (OTA) task to target a device.

## Request Syntax
<a name="API_CreateOtaTask_RequestSyntax"></a>

```
POST /ota-tasks HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "OtaMechanism": "{{string}}",
   "OtaSchedulingConfig": {
      "EndBehavior": "{{string}}",
      "EndTime": "{{string}}",
      "MaintenanceWindows": [
         {
            "DurationInMinutes": {{number}},
            "StartTime": "{{string}}"
         }
      ],
      "StartTime": "{{string}}"
   },
   "OtaTargetQueryString": "{{string}}",
   "OtaTaskExecutionRetryConfig": {
      "RetryConfigCriteria": [
         {
            "FailureType": "{{string}}",
            "MinNumberOfRetries": {{number}}
         }
      ]
   },
   "OtaType": "{{string}}",
   "Protocol": "{{string}}",
   "S3Url": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Target": [ "{{string}}" ],
   "TaskConfigurationId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateOtaTask_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateOtaTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateOtaTask_RequestSyntax) **   <a name="managedintegrations-CreateOtaTask-request-ClientToken"></a>
An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9=_-]+`
Required: No

 ** [Description](#API_CreateOtaTask_RequestSyntax) **   <a name="managedintegrations-CreateOtaTask-request-Description"></a>
The description of the over-the-air (OTA) task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`
Required: No

 ** [OtaMechanism](#API_CreateOtaTask_RequestSyntax) **   <a name="managedintegrations-CreateOtaTask-request-OtaMechanism"></a>
The deployment mechanism for the over-the-air (OTA) task.
Type: String
Valid Values: `PUSH`
Required: No

 ** [OtaSchedulingConfig](#API_CreateOtaTask_RequestSyntax) **   <a name="managedintegrations-CreateOtaTask-request-OtaSchedulingConfig"></a>
Over-the-air (OTA) task scheduling config.
Type: [OtaTaskSchedulingConfig](API_OtaTaskSchedulingConfig.md) object
Required: No

 ** [OtaTargetQueryString](#API_CreateOtaTask_RequestSyntax) **   <a name="managedintegrations-CreateOtaTask-request-OtaTargetQueryString"></a>
The query string to add things to the thing group.
Type: String
Required: No

 ** [OtaTaskExecutionRetryConfig](#API_CreateOtaTask_RequestSyntax) **   <a name="managedintegrations-CreateOtaTask-request-OtaTaskExecutionRetryConfig"></a>
Over-the-air (OTA) task retry config.
Type: [OtaTaskExecutionRetryConfig](API_OtaTaskExecutionRetryConfig.md) object
Required: No

 ** [OtaType](#API_CreateOtaTask_RequestSyntax) **   <a name="managedintegrations-CreateOtaTask-request-OtaType"></a>
The frequency type for the over-the-air (OTA) task.
Type: String
Valid Values: `ONE_TIME | CONTINUOUS`
Required: Yes

 ** [Protocol](#API_CreateOtaTask_RequestSyntax) **   <a name="managedintegrations-CreateOtaTask-request-Protocol"></a>
The connection protocol the over-the-air (OTA) task uses to update the device.
Type: String
Valid Values: `HTTP`
Required: No

 ** [S3Url](#API_CreateOtaTask_RequestSyntax) **   <a name="managedintegrations-CreateOtaTask-request-S3Url"></a>
The URL to the Amazon S3 bucket where the over-the-air (OTA) task is stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** [Tags](#API_CreateOtaTask_RequestSyntax) **   <a name="managedintegrations-CreateOtaTask-request-Tags"></a>
A set of key/value pairs that are used to manage the over-the-air (OTA) task.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [Target](#API_CreateOtaTask_RequestSyntax) **   <a name="managedintegrations-CreateOtaTask-request-Target"></a>
The device targeted for the over-the-air (OTA) task.
Type: Array of strings
Required: No

 ** [TaskConfigurationId](#API_CreateOtaTask_RequestSyntax) **   <a name="managedintegrations-CreateOtaTask-request-TaskConfigurationId"></a>
The identifier for the over-the-air (OTA) task configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`
Required: No

## Response Syntax
<a name="API_CreateOtaTask_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Description": "string",
   "TaskArn": "string",
   "TaskId": "string"
}
```

## Response Elements
<a name="API_CreateOtaTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_CreateOtaTask_ResponseSyntax) **   <a name="managedintegrations-CreateOtaTask-response-Description"></a>
A description of the over-the-air (OTA) task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`

 ** [TaskArn](#API_CreateOtaTask_ResponseSyntax) **   <a name="managedintegrations-CreateOtaTask-response-TaskArn"></a>
The Amazon Resource Name (ARN) of the over-the-air (OTA) task.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:ota-task/[0-9a-zA-Z]+`

 ** [TaskId](#API_CreateOtaTask_ResponseSyntax) **   <a name="managedintegrations-CreateOtaTask-response-TaskId"></a>
The identifier of the over-the-air (OTA) task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`

## Errors
<a name="API_CreateOtaTask_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** UnauthorizedException **
You are not authorized to perform this operation.
HTTP Status Code: 401

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_CreateOtaTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/CreateOtaTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/CreateOtaTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CreateOtaTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/CreateOtaTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CreateOtaTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/CreateOtaTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/CreateOtaTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/CreateOtaTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/CreateOtaTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CreateOtaTask)
