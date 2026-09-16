---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_CreateWorkflowStepGroup.html
---

# CreateWorkflowStepGroup
<a name="API_CreateWorkflowStepGroup"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Create a step group in a migration workflow.

## Request Syntax
<a name="API_CreateWorkflowStepGroup_RequestSyntax"></a>

```
POST /workflowstepgroups HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}",
   "next": [ "{{string}}" ],
   "previous": [ "{{string}}" ],
   "workflowId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWorkflowStepGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWorkflowStepGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateWorkflowStepGroup_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStepGroup-request-description"></a>
The description of the step group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[-a-zA-Z0-9_.+, ]*`
Required: No

 ** [name](#API_CreateWorkflowStepGroup_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStepGroup-request-name"></a>
The name of the step group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
Required: Yes

 ** [next](#API_CreateWorkflowStepGroup_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStepGroup-request-next"></a>
The next step group.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [previous](#API_CreateWorkflowStepGroup_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStepGroup-request-previous"></a>
The previous step group.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [workflowId](#API_CreateWorkflowStepGroup_RequestSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStepGroup-request-workflowId"></a>
The ID of the migration workflow that will contain the step group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_CreateWorkflowStepGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": number,
   "description": "string",
   "id": "string",
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
<a name="API_CreateWorkflowStepGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_CreateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStepGroup-response-creationTime"></a>
The time at which the step group is created.
Type: Timestamp

 ** [description](#API_CreateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStepGroup-response-description"></a>
The description of the step group.
Type: String

 ** [id](#API_CreateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStepGroup-response-id"></a>
The ID of the step group.
Type: String

 ** [name](#API_CreateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStepGroup-response-name"></a>
The name of the step group.
Type: String

 ** [next](#API_CreateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStepGroup-response-next"></a>
The next step group.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [previous](#API_CreateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStepGroup-response-previous"></a>
The previous step group.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [tools](#API_CreateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStepGroup-response-tools"></a>
List of AWS services utilized in a migration workflow.
Type: Array of [Tool](API_Tool.md) objects

 ** [workflowId](#API_CreateWorkflowStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateWorkflowStepGroup-response-workflowId"></a>
The ID of the migration workflow that contains the step group.
Type: String

## Errors
<a name="API_CreateWorkflowStepGroup_Errors"></a>

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
<a name="API_CreateWorkflowStepGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/CreateWorkflowStepGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/CreateWorkflowStepGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/CreateWorkflowStepGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/CreateWorkflowStepGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/CreateWorkflowStepGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/CreateWorkflowStepGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/CreateWorkflowStepGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/CreateWorkflowStepGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/CreateWorkflowStepGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/CreateWorkflowStepGroup)
