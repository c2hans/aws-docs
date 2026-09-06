---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_RetryWorkflowStep.html
---

# RetryWorkflowStep
<a name="API_RetryWorkflowStep"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Retry a failed step in a migration workflow.

## Request Syntax
<a name="API_RetryWorkflowStep_RequestSyntax"></a>

```
POST /retryworkflowstep/{{id}}?stepGroupId={{stepGroupId}}&workflowId={{workflowId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_RetryWorkflowStep_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_RetryWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-RetryWorkflowStep-request-uri-id"></a>
The ID of the step.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [stepGroupId](#API_RetryWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-RetryWorkflowStep-request-uri-stepGroupId"></a>
The ID of the step group.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [workflowId](#API_RetryWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-RetryWorkflowStep-request-uri-workflowId"></a>
The ID of the migration workflow.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Request Body
<a name="API_RetryWorkflowStep_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RetryWorkflowStep_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "id": "string",
   "status": "string",
   "stepGroupId": "string",
   "workflowId": "string"
}
```

## Response Elements
<a name="API_RetryWorkflowStep_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_RetryWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-RetryWorkflowStep-response-id"></a>
The ID of the step.
Type: String

 ** [status](#API_RetryWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-RetryWorkflowStep-response-status"></a>
The status of the step.
Type: String
Valid Values: `AWAITING_DEPENDENCIES | SKIPPED | READY | IN_PROGRESS | COMPLETED | FAILED | PAUSED | USER_ATTENTION_REQUIRED`

 ** [stepGroupId](#API_RetryWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-RetryWorkflowStep-response-stepGroupId"></a>
The ID of the step group.
Type: String

 ** [workflowId](#API_RetryWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-RetryWorkflowStep-response-workflowId"></a>
The ID of the migration workflow.
Type: String

## Errors
<a name="API_RetryWorkflowStep_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource is not available.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_RetryWorkflowStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/RetryWorkflowStep)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/RetryWorkflowStep)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/RetryWorkflowStep)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/RetryWorkflowStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/RetryWorkflowStep)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/RetryWorkflowStep)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/RetryWorkflowStep)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/RetryWorkflowStep)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/RetryWorkflowStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/RetryWorkflowStep)
