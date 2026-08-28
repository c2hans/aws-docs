---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_UpdateWorkflowStepGroup.html
---

# UpdateWorkflowStepGroup
<a name="API_UpdateWorkflowStepGroup"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Update the step group in a migration workflow.

## Request Syntax
<a name="API_UpdateWorkflowStepGroup_RequestSyntax"></a>

```
POST /workflowstepgroup/{{id}}?workflowId={{workflowId}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}",
   "next": [ "{{string}}" ],
   "previous": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateWorkflowStepGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateWorkflowStepGroup_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStepGroup-request-uri-id"></a>
The ID of the step group.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [workflowId](#API_UpdateWorkflowStepGroup_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStepGroup-request-uri-workflowId"></a>
The ID of the migration workflow.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Request Body
<a name="API_UpdateWorkflowStepGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateWorkflowStepGroup_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStepGroup-request-description"></a>
The description of the step group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[-a-zA-Z0-9_.+, ]*`
Required: No

 ** [name](#API_UpdateWorkflowStepGroup_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStepGroup-request-name"></a>
The name of the step group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
Required: No

 ** [next](#API_UpdateWorkflowStepGroup_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStepGroup-request-next"></a>
The next step group.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [previous](#API_UpdateWorkflowStepGroup_RequestSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStepGroup-request-previous"></a>
The previous step group.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

## Response Syntax
<a name="API_UpdateWorkflowStepGroup_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "description": "string",
   "id": "string",
   "lastModifiedTime": number,
   "name": "string",
   "next": [ "string" ],
   "previous": [ "string" ],
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
<a name="API_UpdateWorkflowStepGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [description](#API_UpdateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStepGroup-response-description"></a>
The description of the step group.
Type: String

 ** [id](#API_UpdateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStepGroup-response-id"></a>
The ID of the step group.
Type: String

 ** [lastModifiedTime](#API_UpdateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStepGroup-response-lastModifiedTime"></a>
The time at which the step group was last modified.
Type: Timestamp

 ** [name](#API_UpdateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStepGroup-response-name"></a>
The name of the step group.
Type: String

 ** [next](#API_UpdateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStepGroup-response-next"></a>
The next step group.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [previous](#API_UpdateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStepGroup-response-previous"></a>
The previous step group.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [tools](#API_UpdateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStepGroup-response-tools"></a>
List of AWS services utilized in a migration workflow.
Type: Array of [Tool](API_Tool.md) objects

 ** [workflowId](#API_UpdateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-UpdateWorkflowStepGroup-response-workflowId"></a>
The ID of the migration workflow.
Type: String

## Errors
<a name="API_UpdateWorkflowStepGroup_Errors"></a>

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
<a name="API_UpdateWorkflowStepGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/UpdateWorkflowStepGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/UpdateWorkflowStepGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/UpdateWorkflowStepGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/UpdateWorkflowStepGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/UpdateWorkflowStepGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/UpdateWorkflowStepGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/UpdateWorkflowStepGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/UpdateWorkflowStepGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/UpdateWorkflowStepGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/UpdateWorkflowStepGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
