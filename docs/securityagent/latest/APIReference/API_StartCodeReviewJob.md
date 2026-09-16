---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_StartCodeReviewJob.html
---

# StartCodeReviewJob
<a name="API_StartCodeReviewJob"></a>

Starts a new code review job for a code review configuration. The job executes the security-focused code analysis defined in the code review.

## Request Syntax
<a name="API_StartCodeReviewJob_RequestSyntax"></a>

```
POST /StartCodeReviewJob HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "codeReviewId": "{{string}}",
   "diffSource": { ... }
}
```

## URI Request Parameters
<a name="API_StartCodeReviewJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartCodeReviewJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_StartCodeReviewJob_RequestSyntax) **   <a name="securityagent-StartCodeReviewJob-request-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: Yes

 ** [codeReviewId](#API_StartCodeReviewJob_RequestSyntax) **   <a name="securityagent-StartCodeReviewJob-request-codeReviewId"></a>
The unique identifier of the code review to start a job for.
Type: String
Required: Yes

 ** [diffSource](#API_StartCodeReviewJob_RequestSyntax) **   <a name="securityagent-StartCodeReviewJob-request-diffSource"></a>
Source of the diff for a differential scan. When present, the job analyzes only the changed lines instead of performing a full scan.
Type: [DiffSource](API_DiffSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_StartCodeReviewJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentSpaceId": "string",
   "codeReviewId": "string",
   "codeReviewJobId": "string",
   "createdAt": "string",
   "status": "string",
   "title": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_StartCodeReviewJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentSpaceId](#API_StartCodeReviewJob_ResponseSyntax) **   <a name="securityagent-StartCodeReviewJob-response-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String

 ** [codeReviewId](#API_StartCodeReviewJob_ResponseSyntax) **   <a name="securityagent-StartCodeReviewJob-response-codeReviewId"></a>
The unique identifier of the code review.
Type: String

 ** [codeReviewJobId](#API_StartCodeReviewJob_ResponseSyntax) **   <a name="securityagent-StartCodeReviewJob-response-codeReviewJobId"></a>
The unique identifier of the started code review job.
Type: String

 ** [createdAt](#API_StartCodeReviewJob_ResponseSyntax) **   <a name="securityagent-StartCodeReviewJob-response-createdAt"></a>
The date and time the code review job was created, in UTC format.
Type: Timestamp

 ** [status](#API_StartCodeReviewJob_ResponseSyntax) **   <a name="securityagent-StartCodeReviewJob-response-status"></a>
The current status of the code review job.
Type: String
Valid Values: `IN_PROGRESS | STOPPING | STOPPED | FAILED | COMPLETED`

 ** [title](#API_StartCodeReviewJob_ResponseSyntax) **   <a name="securityagent-StartCodeReviewJob-response-title"></a>
The title of the code review job.
Type: String

 ** [updatedAt](#API_StartCodeReviewJob_ResponseSyntax) **   <a name="securityagent-StartCodeReviewJob-response-updatedAt"></a>
The date and time the code review job was last updated, in UTC format.
Type: Timestamp

## Errors
<a name="API_StartCodeReviewJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_StartCodeReviewJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/StartCodeReviewJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/StartCodeReviewJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/StartCodeReviewJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/StartCodeReviewJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/StartCodeReviewJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/StartCodeReviewJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/StartCodeReviewJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/StartCodeReviewJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/StartCodeReviewJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/StartCodeReviewJob)
