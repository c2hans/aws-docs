---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchGetCodeReviewJobTasks.html
---

# BatchGetCodeReviewJobTasks
<a name="API_BatchGetCodeReviewJobTasks"></a>

Retrieves information about one or more tasks within a code review job.

## Request Syntax
<a name="API_BatchGetCodeReviewJobTasks_RequestSyntax"></a>

```
POST /BatchGetCodeReviewJobTasks HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "codeReviewJobTaskIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetCodeReviewJobTasks_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetCodeReviewJobTasks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_BatchGetCodeReviewJobTasks_RequestSyntax) **   <a name="securityagent-BatchGetCodeReviewJobTasks-request-agentSpaceId"></a>
The unique identifier of the agent space that contains the tasks.
Type: String
Required: Yes

 ** [codeReviewJobTaskIds](#API_BatchGetCodeReviewJobTasks_RequestSyntax) **   <a name="securityagent-BatchGetCodeReviewJobTasks-request-codeReviewJobTaskIds"></a>
The list of task identifiers to retrieve.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetCodeReviewJobTasks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "codeReviewJobTasks": [
      {
         "agentSpaceId": "string",
         "categories": [
            {
               "isPrimary": boolean,
               "name": "string"
            }
         ],
         "codeReviewId": "string",
         "codeReviewJobId": "string",
         "createdAt": "string",
         "description": "string",
         "executionStatus": "string",
         "logsLocation": {
            "cloudWatchLog": {
               "logGroup": "string",
               "logStream": "string"
            },
            "logType": "string"
         },
         "riskType": "string",
         "taskId": "string",
         "title": "string",
         "updatedAt": "string"
      }
   ],
   "notFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetCodeReviewJobTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [codeReviewJobTasks](#API_BatchGetCodeReviewJobTasks_ResponseSyntax) **   <a name="securityagent-BatchGetCodeReviewJobTasks-response-codeReviewJobTasks"></a>
The list of code review job tasks that were found.
Type: Array of [CodeReviewJobTask](API_CodeReviewJobTask.md) objects

 ** [notFound](#API_BatchGetCodeReviewJobTasks_ResponseSyntax) **   <a name="securityagent-BatchGetCodeReviewJobTasks-response-notFound"></a>
The list of task identifiers that were not found.
Type: Array of strings

## Errors
<a name="API_BatchGetCodeReviewJobTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_BatchGetCodeReviewJobTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchGetCodeReviewJobTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchGetCodeReviewJobTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchGetCodeReviewJobTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchGetCodeReviewJobTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchGetCodeReviewJobTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchGetCodeReviewJobTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchGetCodeReviewJobTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchGetCodeReviewJobTasks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchGetCodeReviewJobTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchGetCodeReviewJobTasks)
