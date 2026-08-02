---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_StartThreatModelJob.html
---

# StartThreatModelJob
<a name="API_StartThreatModelJob"></a>

Starts a new threat model job for a threat model configuration.

## Request Syntax
<a name="API_StartThreatModelJob_RequestSyntax"></a>

```
POST /StartThreatModelJob HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "threatModelId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartThreatModelJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartThreatModelJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_StartThreatModelJob_RequestSyntax) **   <a name="securityagent-StartThreatModelJob-request-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: Yes

 ** [threatModelId](#API_StartThreatModelJob_RequestSyntax) **   <a name="securityagent-StartThreatModelJob-request-threatModelId"></a>
The unique identifier of the threat model to start a job for.
Type: String
Required: Yes

## Response Syntax
<a name="API_StartThreatModelJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentSpaceId": "string",
   "createdAt": "string",
   "status": "string",
   "threatModelId": "string",
   "threatModelJobId": "string",
   "title": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_StartThreatModelJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentSpaceId](#API_StartThreatModelJob_ResponseSyntax) **   <a name="securityagent-StartThreatModelJob-response-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String

 ** [createdAt](#API_StartThreatModelJob_ResponseSyntax) **   <a name="securityagent-StartThreatModelJob-response-createdAt"></a>
The date and time the threat model job was created, in UTC format.
Type: Timestamp

 ** [status](#API_StartThreatModelJob_ResponseSyntax) **   <a name="securityagent-StartThreatModelJob-response-status"></a>
The current status of the threat model job.
Type: String
Valid Values: `IN_PROGRESS | STOPPING | STOPPED | FAILED | COMPLETED`

 ** [threatModelId](#API_StartThreatModelJob_ResponseSyntax) **   <a name="securityagent-StartThreatModelJob-response-threatModelId"></a>
The unique identifier of the threat model.
Type: String

 ** [threatModelJobId](#API_StartThreatModelJob_ResponseSyntax) **   <a name="securityagent-StartThreatModelJob-response-threatModelJobId"></a>
The unique identifier of the started threat model job.
Type: String

 ** [title](#API_StartThreatModelJob_ResponseSyntax) **   <a name="securityagent-StartThreatModelJob-response-title"></a>
The title of the threat model job.
Type: String

 ** [updatedAt](#API_StartThreatModelJob_ResponseSyntax) **   <a name="securityagent-StartThreatModelJob-response-updatedAt"></a>
The date and time the threat model job was last updated, in UTC format.
Type: Timestamp

## Errors
<a name="API_StartThreatModelJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_StartThreatModelJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/StartThreatModelJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/StartThreatModelJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/StartThreatModelJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/StartThreatModelJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/StartThreatModelJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/StartThreatModelJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/StartThreatModelJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/StartThreatModelJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/StartThreatModelJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/StartThreatModelJob)
