---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_CreateWorkflow.html
---

# CreateWorkflow
<a name="API_CreateWorkflow"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Create a workflow to orchestrate your migrations.

## Request Syntax
<a name="API_CreateWorkflow_RequestSyntax"></a>

```
POST /migrationworkflow/ HTTP/1.1
Content-type: application/json

{
   "applicationConfigurationId": "{{string}}",
   "description": "{{string}}",
   "inputParameters": {
      "{{string}}" : { ... }
   },
   "name": "{{string}}",
   "stepTargets": [ "{{string}}" ],
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "templateId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWorkflow_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWorkflow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicationConfigurationId](#API_CreateWorkflow_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-request-applicationConfigurationId"></a>
The configuration ID of the application configured in Application Discovery Service.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]*`
Required: No

 ** [description](#API_CreateWorkflow_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-request-description"></a>
The description of the migration workflow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[-a-zA-Z0-9_.+, ]*`
Required: No

 ** [inputParameters](#API_CreateWorkflow_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-request-inputParameters"></a>
The input parameters required to create a migration workflow.
Type: String to [StepInput](API_StepInput.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[a-zA-Z0-9-_ ()]+`
Required: Yes

 ** [name](#API_CreateWorkflow_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-request-name"></a>
The name of the migration workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
Required: Yes

 ** [stepTargets](#API_CreateWorkflow_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-request-stepTargets"></a>
The servers on which a step will be run.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [tags](#API_CreateWorkflow_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-request-tags"></a>
The tags to add on a migration workflow.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[a-zA-Z0-9-_ ()]+`
Value Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** [templateId](#API_CreateWorkflow_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-request-templateId"></a>
The ID of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
Required: Yes

## Response Syntax
<a name="API_CreateWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "adsApplicationConfigurationId": "string",
   "arn": "string",
   "creationTime": number,
   "description": "string",
   "id": "string",
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
<a name="API_CreateWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [adsApplicationConfigurationId](#API_CreateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-response-adsApplicationConfigurationId"></a>
The configuration ID of the application configured in Application Discovery Service.
Type: String

 ** [arn](#API_CreateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-response-arn"></a>
The Amazon Resource Name (ARN) of the migration workflow.
Type: String

 ** [creationTime](#API_CreateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-response-creationTime"></a>
The time at which the migration workflow was created.
Type: Timestamp

 ** [description](#API_CreateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-response-description"></a>
The description of the migration workflow.
Type: String

 ** [id](#API_CreateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-response-id"></a>
The ID of the migration workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`

 ** [name](#API_CreateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-response-name"></a>
The name of the migration workflow.
Type: String

 ** [status](#API_CreateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-response-status"></a>
The status of the migration workflow.
Type: String
Valid Values: `CREATING | NOT_STARTED | CREATION_FAILED | STARTING | IN_PROGRESS | WORKFLOW_FAILED | PAUSED | PAUSING | PAUSING_FAILED | USER_ATTENTION_REQUIRED | DELETING | DELETION_FAILED | DELETED | COMPLETED`

 ** [stepTargets](#API_CreateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-response-stepTargets"></a>
The servers on which a step will be run.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [tags](#API_CreateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-response-tags"></a>
The tags to add on a migration workflow.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[a-zA-Z0-9-_ ()]+`
Value Length Constraints: Minimum length of 0. Maximum length of 100.

 ** [templateId](#API_CreateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-response-templateId"></a>
The ID of the template.
Type: String

 ** [workflowInputs](#API_CreateWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflow-response-workflowInputs"></a>
The inputs for creating a migration workflow.
Type: String to [StepInput](API_StepInput.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[a-zA-Z0-9-_ ()]+`

## Errors
<a name="API_CreateWorkflow_Errors"></a>

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
<a name="API_CreateWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/CreateWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/CreateWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/CreateWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/CreateWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/CreateWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/CreateWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/CreateWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/CreateWorkflow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/CreateWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/CreateWorkflow)
