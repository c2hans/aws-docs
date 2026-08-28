---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetWorkflow.html
---

# GetWorkflow
<a name="API_GetWorkflow"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Get migration workflow.

## Request Syntax
<a name="API_GetWorkflow_RequestSyntax"></a>

```
GET /migrationworkflow/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetWorkflow_RequestSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-request-uri-id"></a>
The ID of the migration workflow.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Request Body
<a name="API_GetWorkflow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "adsApplicationConfigurationId": "string",
   "adsApplicationName": "string",
   "arn": "string",
   "completedSteps": number,
   "creationTime": number,
   "description": "string",
   "endTime": number,
   "id": "string",
   "lastModifiedTime": number,
   "lastStartTime": number,
   "lastStopTime": number,
   "name": "string",
   "status": "string",
   "statusMessage": "string",
   "tags": {
      "string" : "string"
   },
   "templateId": "string",
   "tools": [
      {
         "name": "string",
         "url": "string"
      }
   ],
   "totalSteps": number,
   "workflowBucket": "string",
   "workflowInputs": {
      "string" : { ... }
   }
}
```

## Response Elements
<a name="API_GetWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [adsApplicationConfigurationId](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-adsApplicationConfigurationId"></a>
The configuration ID of the application configured in Application Discovery Service.
Type: String

 ** [adsApplicationName](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-adsApplicationName"></a>
The name of the application configured in Application Discovery Service.
Type: String

 ** [arn](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-arn"></a>
The Amazon Resource Name (ARN) of the migration workflow.
Type: String

 ** [completedSteps](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-completedSteps"></a>
Get a list of completed steps in the migration workflow.
Type: Integer

 ** [creationTime](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-creationTime"></a>
The time at which the migration workflow was created.
Type: Timestamp

 ** [description](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-description"></a>
The description of the migration workflow.
Type: String

 ** [endTime](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-endTime"></a>
The time at which the migration workflow ended.
Type: Timestamp

 ** [id](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-id"></a>
The ID of the migration workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`

 ** [lastModifiedTime](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-lastModifiedTime"></a>
The time at which the migration workflow was last modified.
Type: Timestamp

 ** [lastStartTime](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-lastStartTime"></a>
The time at which the migration workflow was last started.
Type: Timestamp

 ** [lastStopTime](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-lastStopTime"></a>
The time at which the migration workflow was last stopped.
Type: Timestamp

 ** [name](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-name"></a>
The name of the migration workflow.
Type: String

 ** [status](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-status"></a>
The status of the migration workflow.
Type: String
Valid Values: `CREATING | NOT_STARTED | CREATION_FAILED | STARTING | IN_PROGRESS | WORKFLOW_FAILED | PAUSED | PAUSING | PAUSING_FAILED | USER_ATTENTION_REQUIRED | DELETING | DELETION_FAILED | DELETED | COMPLETED`

 ** [statusMessage](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-statusMessage"></a>
The status message of the migration workflow.
Type: String

 ** [tags](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-tags"></a>
The tags added to the migration workflow.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[a-zA-Z0-9-_ ()]+`
Value Length Constraints: Minimum length of 0. Maximum length of 100.

 ** [templateId](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-templateId"></a>
The ID of the template.
Type: String

 ** [tools](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-tools"></a>
List of AWS services utilized in a migration workflow.
Type: Array of [Tool](API_Tool.md) objects

 ** [totalSteps](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-totalSteps"></a>
The total number of steps in the migration workflow.
Type: Integer

 ** [workflowBucket](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-workflowBucket"></a>
The Amazon S3 bucket where the migration logs are stored.
Type: String

 ** [workflowInputs](#API_GetWorkflow_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflow-response-workflowInputs"></a>
The inputs required for creating the migration workflow.
Type: String to [StepInput](API_StepInput.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[a-zA-Z0-9-_ ()]+`

## Errors
<a name="API_GetWorkflow_Errors"></a>

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
<a name="API_GetWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/GetWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/GetWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/GetWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/GetWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/GetWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/GetWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/GetWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/GetWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/GetWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/GetWorkflow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
