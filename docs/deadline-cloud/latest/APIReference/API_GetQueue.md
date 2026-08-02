---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetQueue.html
---

# GetQueue
<a name="API_GetQueue"></a>

Gets a queue.

## Request Syntax
<a name="API_GetQueue_RequestSyntax"></a>

```
GET /2023-10-12/farms/{{farmId}}/queues/{{queueId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetQueue_RequestParameters"></a>

The request uses the following URI parameters.

 ** [farmId](#API_GetQueue_RequestSyntax) **   <a name="deadlinecloud-GetQueue-request-uri-farmId"></a>
The farm ID of the farm in the queue.
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** [queueId](#API_GetQueue_RequestSyntax) **   <a name="deadlinecloud-GetQueue-request-uri-queueId"></a>
The queue ID for the queue to retrieve.
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_GetQueue_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetQueue_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "allowedStorageProfileIds": [ "string" ],
   "blockedReason": "string",
   "createdAt": "string",
   "createdBy": "string",
   "defaultBudgetAction": "string",
   "description": "string",
   "displayName": "string",
   "farmId": "string",
   "jobAttachmentSettings": {
      "rootPrefix": "string",
      "s3BucketName": "string"
   },
   "jobRunAsUser": {
      "posix": {
         "group": "string",
         "user": "string"
      },
      "runAs": "string",
      "windows": {
         "passwordArn": "string",
         "user": "string"
      }
   },
   "queueId": "string",
   "requiredFileSystemLocationNames": [ "string" ],
   "roleArn": "string",
   "schedulingConfiguration": { ... },
   "status": "string",
   "updatedAt": "string",
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_GetQueue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [allowedStorageProfileIds](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-allowedStorageProfileIds"></a>
The storage profile IDs for the queue.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Pattern: `sp-[0-9a-f]{32}`

 ** [blockedReason](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-blockedReason"></a>
The reason the queue was blocked.
Type: String
Valid Values: `NO_BUDGET_CONFIGURED | BUDGET_THRESHOLD_REACHED`

 ** [createdAt](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-createdAt"></a>
The date and time the resource was created.
Type: Timestamp

 ** [createdBy](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-createdBy"></a>
The user or system that created this resource.
Type: String

 ** [defaultBudgetAction](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-defaultBudgetAction"></a>
The default action taken on a queue if a budget wasn't configured.
Type: String
Valid Values: `NONE | STOP_SCHEDULING_AND_COMPLETE_TASKS | STOP_SCHEDULING_AND_CANCEL_TASKS`

 ** [description](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-description"></a>
The description of the queue.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.

 ** [displayName](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-displayName"></a>
The display name of the queue.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [farmId](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-farmId"></a>
The farm ID for the queue.
Type: String
Pattern: `farm-[0-9a-f]{32}`

 ** [jobAttachmentSettings](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-jobAttachmentSettings"></a>
The job attachment settings for the queue.
Type: [JobAttachmentSettings](API_JobAttachmentSettings.md) object

 ** [jobRunAsUser](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-jobRunAsUser"></a>
The jobs in the queue ran as this specified POSIX user.
Type: [JobRunAsUser](API_JobRunAsUser.md) object

 ** [queueId](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-queueId"></a>
The queue ID.
Type: String
Pattern: `queue-[0-9a-f]{32}`

 ** [requiredFileSystemLocationNames](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-requiredFileSystemLocationNames"></a>
A list of the required file system location names in the queue.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9A-Za-z ]*`

 ** [roleArn](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-roleArn"></a>
The IAM role ARN.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):iam::\d{12}:role(/[!-.0-~]+)*/[\w+=,.@-]+`

 ** [schedulingConfiguration](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-schedulingConfiguration"></a>
The scheduling configuration for the queue. This configuration determines how workers are assigned to jobs in the queue.
Type: [SchedulingConfiguration](API_SchedulingConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-status"></a>
The status of the queue.
+  `ACTIVE`–The queue is active.
+  `SCHEDULING`–The queue is scheduling.
+  `SCHEDULING_BLOCKED`–The queue scheduling is blocked. See the provided reason.
Type: String
Valid Values: `IDLE | SCHEDULING | SCHEDULING_BLOCKED`

 ** [updatedAt](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp

 ** [updatedBy](#API_GetQueue_ResponseSyntax) **   <a name="deadlinecloud-GetQueue-response-updatedBy"></a>
The user or system that updated this resource.
Type: String

## Errors
<a name="API_GetQueue_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 ** context **
Information about the resources in use when the exception was thrown.
HTTP Status Code: 403

 ** InternalServerErrorException **
Deadline Cloud can't process your request right now. Try again later.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** context **
Information about the resources in use when the exception was thrown.
 ** resourceId **
The identifier of the resource that couldn't be found.
 ** resourceType **
The type of the resource that couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a request rate quota.
 ** context **
Information about the resources in use when the exception was thrown.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service that is being throttled.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** context **
Information about the resources in use when the exception was thrown.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_GetQueue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetQueue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/GetQueue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetQueue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetQueue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetQueue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetQueue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetQueue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetQueue)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetQueue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetQueue)
