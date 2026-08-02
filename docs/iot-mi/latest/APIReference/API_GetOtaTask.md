---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetOtaTask.html
---

# GetOtaTask
<a name="API_GetOtaTask"></a>

Get details of the over-the-air (OTA) task by its task id.

## Request Syntax
<a name="API_GetOtaTask_RequestSyntax"></a>

```
GET /ota-tasks/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetOtaTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetOtaTask_RequestSyntax) **   <a name="managedintegrations-GetOtaTask-request-uri-Identifier"></a>
The over-the-air (OTA) task id.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`
Required: Yes

## Request Body
<a name="API_GetOtaTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetOtaTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedAt": number,
   "Description": "string",
   "LastUpdatedAt": number,
   "OtaMechanism": "string",
   "OtaSchedulingConfig": {
      "EndBehavior": "string",
      "EndTime": "string",
      "MaintenanceWindows": [
         {
            "DurationInMinutes": number,
            "StartTime": "string"
         }
      ],
      "StartTime": "string"
   },
   "OtaTargetQueryString": "string",
   "OtaTaskExecutionRetryConfig": {
      "RetryConfigCriteria": [
         {
            "FailureType": "string",
            "MinNumberOfRetries": number
         }
      ]
   },
   "OtaType": "string",
   "Protocol": "string",
   "S3Url": "string",
   "Status": "string",
   "Tags": {
      "string" : "string"
   },
   "Target": [ "string" ],
   "TaskArn": "string",
   "TaskConfigurationId": "string",
   "TaskId": "string",
   "TaskProcessingDetails": {
      "NumberOfCanceledThings": number,
      "NumberOfFailedThings": number,
      "NumberOfInProgressThings": number,
      "numberOfQueuedThings": number,
      "numberOfRejectedThings": number,
      "numberOfRemovedThings": number,
      "numberOfSucceededThings": number,
      "numberOfTimedOutThings": number,
      "processingTargets": [ "string" ]
   }
}
```

## Response Elements
<a name="API_GetOtaTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-CreatedAt"></a>
The timestamp value of when the over-the-air (OTA) task was created.
Type: Timestamp

 ** [Description](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-Description"></a>
The description of the over-the-air (OTA) task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`

 ** [LastUpdatedAt](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-LastUpdatedAt"></a>
The timestamp value of when the over-the-air (OTA) task was last updated at.
Type: Timestamp

 ** [OtaMechanism](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-OtaMechanism"></a>
The deployment mechanism for the over-the-air (OTA) task.
Type: String
Valid Values: `PUSH`

 ** [OtaSchedulingConfig](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-OtaSchedulingConfig"></a>
Over-the-air (OTA) task scheduling config.
Type: [OtaTaskSchedulingConfig](API_OtaTaskSchedulingConfig.md) object

 ** [OtaTargetQueryString](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-OtaTargetQueryString"></a>
The query string to add things to the thing group.
Type: String

 ** [OtaTaskExecutionRetryConfig](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-OtaTaskExecutionRetryConfig"></a>
Over-the-air (OTA) task retry config.
Type: [OtaTaskExecutionRetryConfig](API_OtaTaskExecutionRetryConfig.md) object

 ** [OtaType](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-OtaType"></a>
The frequency type for the over-the-air (OTA) task.
Type: String
Valid Values: `ONE_TIME | CONTINUOUS`

 ** [Protocol](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-Protocol"></a>
The connection protocol the over-the-air (OTA) task uses to update the device.
Type: String
Valid Values: `HTTP`

 ** [S3Url](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-S3Url"></a>
The URL to the Amazon S3 bucket where the over-the-air (OTA) task is stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [Status](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-Status"></a>
The status of the over-the-air (OTA) task.
Type: String
Valid Values: `IN_PROGRESS | CANCELED | COMPLETED | DELETION_IN_PROGRESS | SCHEDULED`

 ** [Tags](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-Tags"></a>
A set of key/value pairs that are used to manage the over-the-air (OTA) task.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [Target](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-Target"></a>
The device targeted for the over-the-air (OTA) task.
Type: Array of strings

 ** [TaskArn](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-TaskArn"></a>
The Amazon Resource Name (ARN) of the over-the-air (OTA) task
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:ota-task/[0-9a-zA-Z]+`

 ** [TaskConfigurationId](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-TaskConfigurationId"></a>
The identifier for the over-the-air (OTA) task configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`

 ** [TaskId](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-TaskId"></a>
The id of the over-the-air (OTA) task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`

 ** [TaskProcessingDetails](#API_GetOtaTask_ResponseSyntax) **   <a name="managedintegrations-GetOtaTask-response-TaskProcessingDetails"></a>
The processing details of all over-the-air (OTA) tasks.
Type: [TaskProcessingDetails](API_TaskProcessingDetails.md) object

## Errors
<a name="API_GetOtaTask_Errors"></a>

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
<a name="API_GetOtaTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetOtaTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetOtaTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetOtaTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetOtaTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetOtaTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetOtaTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetOtaTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetOtaTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetOtaTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetOtaTask)
