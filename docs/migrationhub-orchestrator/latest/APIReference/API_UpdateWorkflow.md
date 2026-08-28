---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_UpdateWorkflow.html
---

# UpdateWorkflow
<a name="API_UpdateWorkflow"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Update a migration workflow.

## Request Syntax
<a name="API_UpdateWorkflow_RequestSyntax"></a>

```
POST /migrationworkflow/{{id}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "inputParameters": {
      "{{string}}" : { ... }
   },
   "name": "{{string}}",
   "stepTargets": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateWorkflow_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-request-uri-id"></a>
The ID of the migration workflow.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Request Body
<a name="API_UpdateWorkflow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateWorkflow_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-request-description"></a>
The description of the migration workflow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[-a-zA-Z0-9_.+, ]*`
Required: No

 ** [inputParameters](#API_UpdateWorkflow_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-request-inputParameters"></a>
The input parameters required to update a migration workflow.
Type: String to [StepInput](API_StepInput.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[a-zA-Z0-9-_ ()]+`
Required: No

 ** [name](#API_UpdateWorkflow_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-request-name"></a>
The name of the migration workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
Required: No

 ** [stepTargets](#API_UpdateWorkflow_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-request-stepTargets"></a>
The servers on which a step will be run.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

## Response Syntax
<a name="API_UpdateWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "adsApplicationConfigurationId": "string",
   "arn": "string",
   "creationTime": number,
   "description": "string",
   "id": "string",
   "lastModifiedTime": number,
   "name": "string",
   "status": "string",
   "stepTargets": [ "string" ],
   "tags": {
      "string" : "string"
   },
   "templateId": "string",
   "workflowInputs": {
      "string" : { ... }
   }
}
```

## Response Elements
<a name="API_UpdateWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [adsApplicationConfigurationId](#API_UpdateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-response-adsApplicationConfigurationId"></a>
The ID of the application configured in Application Discovery Service.
Type: String

 ** [arn](#API_UpdateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-response-arn"></a>
The Amazon Resource Name (ARN) of the migration workflow.
Type: String

 ** [creationTime](#API_UpdateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-response-creationTime"></a>
The time at which the migration workflow was created.
Type: Timestamp

 ** [description](#API_UpdateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-response-description"></a>
The description of the migration workflow.
Type: String

 ** [id](#API_UpdateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-response-id"></a>
The ID of the migration workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`

 ** [lastModifiedTime](#API_UpdateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-response-lastModifiedTime"></a>
The time at which the migration workflow was last modified.
Type: Timestamp

 ** [name](#API_UpdateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-response-name"></a>
The name of the migration workflow.
Type: String

 ** [status](#API_UpdateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-response-status"></a>
The status of the migration workflow.
Type: String
Valid Values: `CREATING | NOT_STARTED | CREATION_FAILED | STARTING | IN_PROGRESS | WORKFLOW_FAILED | PAUSED | PAUSING | PAUSING_FAILED | USER_ATTENTION_REQUIRED | DELETING | DELETION_FAILED | DELETED | COMPLETED`

 ** [stepTargets](#API_UpdateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-response-stepTargets"></a>
The servers on which a step will be run.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [tags](#API_UpdateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-response-tags"></a>
The tags added to the migration workflow.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[a-zA-Z0-9-_ ()]+`
Value Length Constraints: Minimum length of 0. Maximum length of 100.

 ** [templateId](#API_UpdateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-response-templateId"></a>
The ID of the template.
Type: String

 ** [workflowInputs](#API_UpdateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflow-response-workflowInputs"></a>
The inputs required to update a migration workflow.
Type: String to [StepInput](API_StepInput.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[a-zA-Z0-9-_ ()]+`

## Errors
<a name="API_UpdateWorkflow_Errors"></a>

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
<a name="API_UpdateWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/UpdateWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/UpdateWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/UpdateWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/UpdateWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/UpdateWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/UpdateWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/UpdateWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/UpdateWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/UpdateWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/UpdateWorkflow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
