---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetWorkflowStep.html
---

# GetWorkflowStep
<a name="API_GetWorkflowStep"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Get a step in the migration workflow.

## Request Syntax
<a name="API_GetWorkflowStep_RequestSyntax"></a>

```
GET /workflowstep/{{id}}?stepGroupId={{stepGroupId}}&workflowId={{workflowId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWorkflowStep_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-request-uri-id"></a>
The ID of the step.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [stepGroupId](#API_GetWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-request-uri-stepGroupId"></a>
The ID of the step group.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [workflowId](#API_GetWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-request-uri-workflowId"></a>
The ID of the migration workflow.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Request Body
<a name="API_GetWorkflowStep_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWorkflowStep_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": number,
   "description": "string",
   "endTime": number,
   "lastStartTime": number,
   "name": "string",
   "next": [ "string" ],
   "noOfSrvCompleted": number,
   "noOfSrvFailed": number,
   "outputs": [
      {
         "dataType": "string",
         "name": "string",
         "required": boolean,
         "value": { ... }
      }
   ],
   "owner": "string",
   "previous": [ "string" ],
   "scriptOutputLocation": "string",
   "status": "string",
   "statusMessage": "string",
   "stepActionType": "string",
   "stepGroupId": "string",
   "stepId": "string",
   "stepTarget": [ "string" ],
   "totalNoOfSrv": number,
   "workflowId": "string",
   "workflowStepAutomationConfiguration": {
      "command": {
         "linux": "string",
         "windows": "string"
      },
      "runEnvironment": "string",
      "scriptLocationS3Bucket": "string",
      "scriptLocationS3Key": {
         "linux": "string",
         "windows": "string"
      },
      "targetType": "string"
   }
}
```

## Response Elements
<a name="API_GetWorkflowStep_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-creationTime"></a>
The time at which the step was created.
Type: Timestamp

 ** [description](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-description"></a>
The description of the step.
Type: String

 ** [endTime](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-endTime"></a>
The time at which the step ended.
Type: Timestamp

 ** [lastStartTime](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-lastStartTime"></a>
The time at which the workflow was last started.
Type: Timestamp

 ** [name](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-name"></a>
The name of the step.
Type: String

 ** [next](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-next"></a>
The next step.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [noOfSrvCompleted](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-noOfSrvCompleted"></a>
The number of servers that have been migrated.
Type: Integer

 ** [noOfSrvFailed](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-noOfSrvFailed"></a>
The number of servers that have failed to migrate.
Type: Integer

 ** [outputs](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-outputs"></a>
The outputs of the step.
Type: Array of [WorkflowStepOutput](API_WorkflowStepOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [owner](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-owner"></a>
The owner of the step.
Type: String
Valid Values: `AWS_MANAGED | CUSTOM`

 ** [previous](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-previous"></a>
The previous step.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [scriptOutputLocation](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-scriptOutputLocation"></a>
The output location of the script.
Type: String

 ** [status](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-status"></a>
The status of the step.
Type: String
Valid Values: `AWAITING_DEPENDENCIES | SKIPPED | READY | IN_PROGRESS | COMPLETED | FAILED | PAUSED | USER_ATTENTION_REQUIRED`

 ** [statusMessage](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-statusMessage"></a>
The status message of the migration workflow.
Type: String

 ** [stepActionType](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-stepActionType"></a>
The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.
Type: String
Valid Values: `MANUAL | AUTOMATED`

 ** [stepGroupId](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-stepGroupId"></a>
The ID of the step group.
Type: String

 ** [stepId](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-stepId"></a>
The ID of the step.
Type: String

 ** [stepTarget](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-stepTarget"></a>
The servers on which a step will be run.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [totalNoOfSrv](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-totalNoOfSrv"></a>
The total number of servers that have been migrated.
Type: Integer

 ** [workflowId](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-workflowId"></a>
The ID of the migration workflow.
Type: String

 ** [workflowStepAutomationConfiguration](#API_GetWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStep-response-workflowStepAutomationConfiguration"></a>
The custom script to run tests on source or target environments.
Type: [WorkflowStepAutomationConfiguration](API_WorkflowStepAutomationConfiguration.md) object

## Errors
<a name="API_GetWorkflowStep_Errors"></a>

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
<a name="API_GetWorkflowStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/GetWorkflowStep)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/GetWorkflowStep)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/GetWorkflowStep)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/GetWorkflowStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/GetWorkflowStep)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/GetWorkflowStep)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/GetWorkflowStep)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/GetWorkflowStep)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/GetWorkflowStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/GetWorkflowStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
