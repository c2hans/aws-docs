---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_StartWorkflow.html
---

# StartWorkflow
<a name="API_StartWorkflow"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Start a migration workflow.

## Request Syntax
<a name="API_StartWorkflow_RequestSyntax"></a>

```
POST /migrationworkflow/{{id}}/start HTTP/1.1
```

## URI Request Parameters
<a name="API_StartWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_StartWorkflow_RequestSyntax) **   <a name="migrationhuborchestrator-StartWorkflow-request-uri-id"></a>
The ID of the migration workflow.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Request Body
<a name="API_StartWorkflow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StartWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "lastStartTime": number,
   "status": "string",
   "statusMessage": "string"
}
```

## Response Elements
<a name="API_StartWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_StartWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-StartWorkflow-response-arn"></a>
The Amazon Resource Name (ARN) of the migration workflow.
Type: String

 ** [id](#API_StartWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-StartWorkflow-response-id"></a>
The ID of the migration workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`

 ** [lastStartTime](#API_StartWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-StartWorkflow-response-lastStartTime"></a>
The time at which the migration workflow was last started.
Type: Timestamp

 ** [status](#API_StartWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-StartWorkflow-response-status"></a>
The status of the migration workflow.
Type: String
Valid Values: `CREATING | NOT_STARTED | CREATION_FAILED | STARTING | IN_PROGRESS | WORKFLOW_FAILED | PAUSED | PAUSING | PAUSING_FAILED | USER_ATTENTION_REQUIRED | DELETING | DELETION_FAILED | DELETED | COMPLETED`

 ** [statusMessage](#API_StartWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-StartWorkflow-response-statusMessage"></a>
The status message of the migration workflow.
Type: String

## Errors
<a name="API_StartWorkflow_Errors"></a>

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
<a name="API_StartWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/StartWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/StartWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/StartWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/StartWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/StartWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/StartWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/StartWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/StartWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/StartWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/StartWorkflow)
