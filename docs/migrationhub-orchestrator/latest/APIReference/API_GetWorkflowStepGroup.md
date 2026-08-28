---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetWorkflowStepGroup.html
---

# GetWorkflowStepGroup
<a name="API_GetWorkflowStepGroup"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Get the step group of a migration workflow.

## Request Syntax
<a name="API_GetWorkflowStepGroup_RequestSyntax"></a>

```
GET /workflowstepgroup/{{id}}?workflowId={{workflowId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWorkflowStepGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetWorkflowStepGroup_RequestSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStepGroup-request-uri-id"></a>
The ID of the step group.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [workflowId](#API_GetWorkflowStepGroup_RequestSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStepGroup-request-uri-workflowId"></a>
The ID of the migration workflow.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Request Body
<a name="API_GetWorkflowStepGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWorkflowStepGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": number,
   "description": "string",
   "endTime": number,
   "id": "string",
   "lastModifiedTime": number,
   "name": "string",
   "next": [ "string" ],
   "owner": "string",
   "previous": [ "string" ],
   "status": "string",
   "tools": [
      {
         "name": "string",
         "url": "string"
      }
   ],
   "workflowId": "string"
}
```

## Response Elements
<a name="API_GetWorkflowStepGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStepGroup-response-creationTime"></a>
The time at which the step group was created.
Type: Timestamp

 ** [description](#API_GetWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStepGroup-response-description"></a>
The description of the step group.
Type: String

 ** [endTime](#API_GetWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStepGroup-response-endTime"></a>
The time at which the step group ended.
Type: Timestamp

 ** [id](#API_GetWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStepGroup-response-id"></a>
The ID of the step group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`

 ** [lastModifiedTime](#API_GetWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStepGroup-response-lastModifiedTime"></a>
The time at which the step group was last modified.
Type: Timestamp

 ** [name](#API_GetWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStepGroup-response-name"></a>
The name of the step group.
Type: String

 ** [next](#API_GetWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStepGroup-response-next"></a>
The next step group.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [owner](#API_GetWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStepGroup-response-owner"></a>
The owner of the step group.
Type: String
Valid Values: `AWS_MANAGED | CUSTOM`

 ** [previous](#API_GetWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStepGroup-response-previous"></a>
The previous step group.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [status](#API_GetWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStepGroup-response-status"></a>
The status of the step group.
Type: String
Valid Values: `AWAITING_DEPENDENCIES | READY | IN_PROGRESS | COMPLETED | FAILED | PAUSED | PAUSING | USER_ATTENTION_REQUIRED`

 ** [tools](#API_GetWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStepGroup-response-tools"></a>
List of AWS services utilized in a migration workflow.
Type: Array of [Tool](API_Tool.md) objects

 ** [workflowId](#API_GetWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetWorkflowStepGroup-response-workflowId"></a>
The ID of the migration workflow.
Type: String

## Errors
<a name="API_GetWorkflowStepGroup_Errors"></a>

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
<a name="API_GetWorkflowStepGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/GetWorkflowStepGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/GetWorkflowStepGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/GetWorkflowStepGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/GetWorkflowStepGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/GetWorkflowStepGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/GetWorkflowStepGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/GetWorkflowStepGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/GetWorkflowStepGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/GetWorkflowStepGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/GetWorkflowStepGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
