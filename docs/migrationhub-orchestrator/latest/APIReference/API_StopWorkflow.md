---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_StopWorkflow.html
---

# StopWorkflow
<a name="API_StopWorkflow"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Stop an ongoing migration workflow.

## Request Syntax
<a name="API_StopWorkflow_RequestSyntax"></a>

```
POST /migrationworkflow/{{id}}/stop HTTP/1.1
```

## URI Request Parameters
<a name="API_StopWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_StopWorkflow_RequestSyntax) **   <a name="migrationhuborchestrator-StopWorkflow-request-uri-id"></a>
The ID of the migration workflow.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Request Body
<a name="API_StopWorkflow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StopWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "lastStopTime": number,
   "status": "string",
   "statusMessage": "string"
}
```

## Response Elements
<a name="API_StopWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_StopWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-StopWorkflow-response-arn"></a>
The Amazon Resource Name (ARN) of the migration workflow.
Type: String

 ** [id](#API_StopWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-StopWorkflow-response-id"></a>
The ID of the migration workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`

 ** [lastStopTime](#API_StopWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-StopWorkflow-response-lastStopTime"></a>
The time at which the migration workflow was stopped.
Type: Timestamp

 ** [status](#API_StopWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-StopWorkflow-response-status"></a>
The status of the migration workflow.
Type: String
Valid Values: `CREATING | NOT_STARTED | CREATION_FAILED | STARTING | IN_PROGRESS | WORKFLOW_FAILED | PAUSED | PAUSING | PAUSING_FAILED | USER_ATTENTION_REQUIRED | DELETING | DELETION_FAILED | DELETED | COMPLETED`

 ** [statusMessage](#API_StopWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-StopWorkflow-response-statusMessage"></a>
The status message of the migration workflow.
Type: String

## Errors
<a name="API_StopWorkflow_Errors"></a>

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

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StopWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/StopWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/StopWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/StopWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/StopWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/StopWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/StopWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/StopWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/StopWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/StopWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/StopWorkflow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
