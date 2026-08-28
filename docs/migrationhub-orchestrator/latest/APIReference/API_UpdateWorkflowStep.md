---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_UpdateWorkflowStep.html
---

# UpdateWorkflowStep
<a name="API_UpdateWorkflowStep"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Update a step in a migration workflow.

## Request Syntax
<a name="API_UpdateWorkflowStep_RequestSyntax"></a>

```
POST /workflowstep/{{id}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}",
   "next": [ "{{string}}" ],
   "outputs": [
      {
         "dataType": "{{string}}",
         "name": "{{string}}",
         "required": {{boolean}},
         "value": { ... }
      }
   ],
   "previous": [ "{{string}}" ],
   "status": "{{string}}",
   "stepActionType": "{{string}}",
   "stepGroupId": "{{string}}",
   "stepTarget": [ "{{string}}" ],
   "workflowId": "{{string}}",
   "workflowStepAutomationConfiguration": {
      "command": {
         "linux": "{{string}}",
         "windows": "{{string}}"
      },
      "runEnvironment": "{{string}}",
      "scriptLocationS3Bucket": "{{string}}",
      "scriptLocationS3Key": {
         "linux": "{{string}}",
         "windows": "{{string}}"
      },
      "targetType": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateWorkflowStep_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-request-uri-id"></a>
The ID of the step.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Request Body
<a name="API_UpdateWorkflowStep_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-request-description"></a>
The description of the step.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[-a-zA-Z0-9_.+, ]*`
Required: No

 ** [name](#API_UpdateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-request-name"></a>
The name of the step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
Required: No

 ** [next](#API_UpdateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-request-next"></a>
The next step.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [outputs](#API_UpdateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-request-outputs"></a>
The outputs of a step.
Type: Array of [WorkflowStepOutput](API_WorkflowStepOutput.md) objects
Required: No

 ** [previous](#API_UpdateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-request-previous"></a>
The previous step.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [status](#API_UpdateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-request-status"></a>
The status of the step.
Type: String
Valid Values: `AWAITING_DEPENDENCIES | SKIPPED | READY | IN_PROGRESS | COMPLETED | FAILED | PAUSED | USER_ATTENTION_REQUIRED`
Required: No

 ** [stepActionType](#API_UpdateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-request-stepActionType"></a>
The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.
Type: String
Valid Values: `MANUAL | AUTOMATED`
Required: No

 ** [stepGroupId](#API_UpdateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-request-stepGroupId"></a>
The ID of the step group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [stepTarget](#API_UpdateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-request-stepTarget"></a>
The servers on which a step will be run.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [workflowId](#API_UpdateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-request-workflowId"></a>
The ID of the migration workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [workflowStepAutomationConfiguration](#API_UpdateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-request-workflowStepAutomationConfiguration"></a>
The custom script to run tests on the source and target environments.
Type: [WorkflowStepAutomationConfiguration](API_WorkflowStepAutomationConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateWorkflowStep_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "id": "string",
   "name": "string",
   "stepGroupId": "string",
   "workflowId": "string"
}
```

## Response Elements
<a name="API_UpdateWorkflowStep_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_UpdateWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-response-id"></a>
The ID of the step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`

 ** [name](#API_UpdateWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-response-name"></a>
The name of the step.
Type: String

 ** [stepGroupId](#API_UpdateWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-response-stepGroupId"></a>
The ID of the step group.
Type: String

 ** [workflowId](#API_UpdateWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStep-response-workflowId"></a>
The ID of the migration workflow.
Type: String

## Errors
<a name="API_UpdateWorkflowStep_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateWorkflowStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/UpdateWorkflowStep)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/UpdateWorkflowStep)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/UpdateWorkflowStep)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/UpdateWorkflowStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/UpdateWorkflowStep)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/UpdateWorkflowStep)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/UpdateWorkflowStep)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/UpdateWorkflowStep)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/UpdateWorkflowStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/UpdateWorkflowStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
