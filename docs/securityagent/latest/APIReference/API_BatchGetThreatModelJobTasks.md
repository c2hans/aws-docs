---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchGetThreatModelJobTasks.html
---

# BatchGetThreatModelJobTasks
<a name="API_BatchGetThreatModelJobTasks"></a>

Retrieves information about one or more tasks within a threat model job.

## Request Syntax
<a name="API_BatchGetThreatModelJobTasks_RequestSyntax"></a>

```
POST /BatchGetThreatModelJobTasks HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "threatModelJobTaskIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetThreatModelJobTasks_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetThreatModelJobTasks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_BatchGetThreatModelJobTasks_RequestSyntax) **   <a name="securityagent-BatchGetThreatModelJobTasks-request-agentSpaceId"></a>
The unique identifier of the agent space that contains the tasks.
Type: String
Required: Yes

 ** [threatModelJobTaskIds](#API_BatchGetThreatModelJobTasks_RequestSyntax) **   <a name="securityagent-BatchGetThreatModelJobTasks-request-threatModelJobTaskIds"></a>
The list of task identifiers to retrieve.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetThreatModelJobTasks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "notFound": [ "string" ],
   "threatModelJobTasks": [
      {
         "agentSpaceId": "string",
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
         "taskId": "string",
         "threatModelId": "string",
         "threatModelJobId": "string",
         "title": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetThreatModelJobTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [notFound](#API_BatchGetThreatModelJobTasks_ResponseSyntax) **   <a name="securityagent-BatchGetThreatModelJobTasks-response-notFound"></a>
The list of task identifiers that were not found.
Type: Array of strings

 ** [threatModelJobTasks](#API_BatchGetThreatModelJobTasks_ResponseSyntax) **   <a name="securityagent-BatchGetThreatModelJobTasks-response-threatModelJobTasks"></a>
The list of threat model job tasks that were found.
Type: Array of [ThreatModelJobTask](API_ThreatModelJobTask.md) objects

## Errors
<a name="API_BatchGetThreatModelJobTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_BatchGetThreatModelJobTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchGetThreatModelJobTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchGetThreatModelJobTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchGetThreatModelJobTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchGetThreatModelJobTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchGetThreatModelJobTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchGetThreatModelJobTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchGetThreatModelJobTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchGetThreatModelJobTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchGetThreatModelJobTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchGetThreatModelJobTasks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
