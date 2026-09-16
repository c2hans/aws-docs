---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_StartDetectMitigationActionsTask.html
---

# StartDetectMitigationActionsTask
<a name="API_StartDetectMitigationActionsTask"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

 Starts a Device Defender ML Detect mitigation actions task.

Requires permission to access the [StartDetectMitigationActionsTask](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_StartDetectMitigationActionsTask_RequestSyntax"></a>

```
PUT /detect/mitigationactions/tasks/{{taskId}} HTTP/1.1
Content-type: application/json

{
   "actions": [ "{{string}}" ],
   "clientRequestToken": "{{string}}",
   "includeOnlyActiveViolations": {{boolean}},
   "includeSuppressedAlerts": {{boolean}},
   "target": {
      "behaviorName": "{{string}}",
      "securityProfileName": "{{string}}",
      "violationIds": [ "{{string}}" ]
   },
   "violationEventOccurrenceRange": {
      "endTime": {{number}},
      "startTime": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_StartDetectMitigationActionsTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [taskId](#API_StartDetectMitigationActionsTask_RequestSyntax) **   <a name="iot-StartDetectMitigationActionsTask-request-uri-taskId"></a>
 The unique identifier of the task.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_StartDetectMitigationActionsTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actions](#API_StartDetectMitigationActionsTask_RequestSyntax) **   <a name="iot-StartDetectMitigationActionsTask-request-actions"></a>
 The actions to be performed when a device has unexpected behavior.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [clientRequestToken](#API_StartDetectMitigationActionsTask_RequestSyntax) **   <a name="iot-StartDetectMitigationActionsTask-request-clientRequestToken"></a>
 Each mitigation action task must have a unique client request token. If you try to create a new task with the same token as a task that already exists, an exception occurs. If you omit this value, AWS SDKs will automatically generate a unique client request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: Yes

 ** [includeOnlyActiveViolations](#API_StartDetectMitigationActionsTask_RequestSyntax) **   <a name="iot-StartDetectMitigationActionsTask-request-includeOnlyActiveViolations"></a>
 Specifies to list only active violations.
Type: Boolean
Required: No

 ** [includeSuppressedAlerts](#API_StartDetectMitigationActionsTask_RequestSyntax) **   <a name="iot-StartDetectMitigationActionsTask-request-includeSuppressedAlerts"></a>
 Specifies to include suppressed alerts.
Type: Boolean
Required: No

 ** [target](#API_StartDetectMitigationActionsTask_RequestSyntax) **   <a name="iot-StartDetectMitigationActionsTask-request-target"></a>
 Specifies the ML Detect findings to which the mitigation actions are applied.
Type: [DetectMitigationActionsTaskTarget](API_DetectMitigationActionsTaskTarget.md) object
Required: Yes

 ** [violationEventOccurrenceRange](#API_StartDetectMitigationActionsTask_RequestSyntax) **   <a name="iot-StartDetectMitigationActionsTask-request-violationEventOccurrenceRange"></a>
 Specifies the time period of which violation events occurred between.
Type: [ViolationEventOccurrenceRange](API_ViolationEventOccurrenceRange.md) object
Required: No

## Response Syntax
<a name="API_StartDetectMitigationActionsTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "taskId": "string"
}
```

## Response Elements
<a name="API_StartDetectMitigationActionsTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [taskId](#API_StartDetectMitigationActionsTask_ResponseSyntax) **   <a name="iot-StartDetectMitigationActionsTask-response-taskId"></a>
 The unique identifier of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_StartDetectMitigationActionsTask_Errors"></a>

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

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** TaskAlreadyExistsException **
 This exception occurs if you attempt to start a task with the same task-id as an existing task but with a different clientRequestToken.
HTTP Status Code: 400

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_StartDetectMitigationActionsTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/StartDetectMitigationActionsTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/StartDetectMitigationActionsTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/StartDetectMitigationActionsTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/StartDetectMitigationActionsTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/StartDetectMitigationActionsTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/StartDetectMitigationActionsTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/StartDetectMitigationActionsTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/StartDetectMitigationActionsTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/StartDetectMitigationActionsTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/StartDetectMitigationActionsTask)
