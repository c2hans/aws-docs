---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetStep.html
---

# BatchGetStep
<a name="API_BatchGetStep"></a>

Retrieves multiple steps in a single request. This is a batch version of the `GetStep` API.

The result of getting each step is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.

## Request Syntax
<a name="API_BatchGetStep_RequestSyntax"></a>

```
POST /2023-10-12/batch-get-step HTTP/1.1
Content-type: application/json

{
   "identifiers": [
      {
         "farmId": "{{string}}",
         "jobId": "{{string}}",
         "queueId": "{{string}}",
         "stepId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchGetStep_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetStep_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [identifiers](#API_BatchGetStep_RequestSyntax) **   <a name="deadlinecloud-BatchGetStep-request-identifiers"></a>
The list of step identifiers to retrieve. You can specify up to 100 identifiers per request.
Type: Array of [BatchGetStepIdentifier](API_BatchGetStepIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_BatchGetStep_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "code": "string",
         "farmId": "string",
         "jobId": "string",
         "message": "string",
         "queueId": "string",
         "stepId": "string"
      }
   ],
   "steps": [
      {
         "createdAt": "string",
         "createdBy": "string",
         "dependencyCounts": {
            "consumersResolved": number,
            "consumersUnresolved": number,
            "dependenciesResolved": number,
            "dependenciesUnresolved": number
         },
         "description": "string",
         "endedAt": "string",
         "farmId": "string",
         "jobId": "string",
         "lifecycleStatus": "string",
         "lifecycleStatusMessage": "string",
         "name": "string",
         "parameterSpace": {
            "combination": "string",
            "parameters": [
               {
                  "chunks": {
                     "defaultTaskCount": number,
                     "rangeConstraint": "string",
                     "targetRuntimeSeconds": number
                  },
                  "name": "string",
                  "type": "string"
               }
            ]
         },
         "queueId": "string",
         "requiredCapabilities": {
            "amounts": [
               {
                  "max": number,
                  "min": number,
                  "name": "string",
                  "value": number
               }
            ],
            "attributes": [
               {
                  "allOf": [ "string" ],
                  "anyOf": [ "string" ],
                  "name": "string"
               }
            ]
         },
         "startedAt": "string",
         "stepId": "string",
         "targetTaskRunStatus": "string",
         "taskFailureRetryCount": number,
         "taskRunStatus": "string",
         "taskRunStatusCounts": {
            "string" : number
         },
         "updatedAt": "string",
         "updatedBy": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetStep_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetStep_ResponseSyntax) **   <a name="deadlinecloud-BatchGetStep-response-errors"></a>
A list of errors for steps that could not be retrieved.
Type: Array of [BatchGetStepError](API_BatchGetStepError.md) objects

 ** [steps](#API_BatchGetStep_ResponseSyntax) **   <a name="deadlinecloud-BatchGetStep-response-steps"></a>
A list of steps that were successfully retrieved.
Type: Array of [BatchGetStepItem](API_BatchGetStepItem.md) objects

## Errors
<a name="API_BatchGetStep_Errors"></a>

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
<a name="API_BatchGetStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/BatchGetStep)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/BatchGetStep)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetStep)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/BatchGetStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetStep)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/BatchGetStep)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/BatchGetStep)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/BatchGetStep)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/BatchGetStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetStep)
