---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_CreateWorkflowStep.html
---

# CreateWorkflowStep
<a name="API_CreateWorkflowStep"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Create a step in the migration workflow.

## Request Syntax
<a name="API_CreateWorkflowStep_RequestSyntax"></a>

```
POST /workflowstep HTTP/1.1
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
<a name="API_CreateWorkflowStep_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWorkflowStep_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStep-request-description"></a>
The description of the step.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[-a-zA-Z0-9_.+, ]*`
Required: No

 ** [name](#API_CreateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStep-request-name"></a>
The name of the step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
Required: Yes

 ** [next](#API_CreateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStep-request-next"></a>
The next step.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [outputs](#API_CreateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStep-request-outputs"></a>
The key value pairs added for the expected output.
Type: Array of [WorkflowStepOutput](API_WorkflowStepOutput.md) objects
Required: No

 ** [previous](#API_CreateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStep-request-previous"></a>
The previous step.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [stepActionType](#API_CreateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStep-request-stepActionType"></a>
The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.
Type: String
Valid Values: `MANUAL | AUTOMATED`
Required: Yes

 ** [stepGroupId](#API_CreateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStep-request-stepGroupId"></a>
The ID of the step group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [stepTarget](#API_CreateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStep-request-stepTarget"></a>
The servers on which a step will be run.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [workflowId](#API_CreateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStep-request-workflowId"></a>
The ID of the migration workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [workflowStepAutomationConfiguration](#API_CreateWorkflowStep_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStep-request-workflowStepAutomationConfiguration"></a>
The custom script to run tests on source or target environments.
Type: [WorkflowStepAutomationConfiguration](API_WorkflowStepAutomationConfiguration.md) object
Required: No

## Response Syntax
<a name="API_CreateWorkflowStep_ResponseSyntax"></a>

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
<a name="API_CreateWorkflowStep_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_CreateWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStep-response-id"></a>
The ID of the step.
Type: String

 ** [name](#API_CreateWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStep-response-name"></a>
The name of the step.
Type: String

 ** [stepGroupId](#API_CreateWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStep-response-stepGroupId"></a>
The ID of the step group.
Type: String

 ** [workflowId](#API_CreateWorkflowStep_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStep-response-workflowId"></a>
The ID of the migration workflow.
Type: String

## Errors
<a name="API_CreateWorkflowStep_Errors"></a>

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
<a name="API_CreateWorkflowStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/CreateWorkflowStep)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/CreateWorkflowStep)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/CreateWorkflowStep)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/CreateWorkflowStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/CreateWorkflowStep)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/CreateWorkflowStep)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/CreateWorkflowStep)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/CreateWorkflowStep)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/CreateWorkflowStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/CreateWorkflowStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
