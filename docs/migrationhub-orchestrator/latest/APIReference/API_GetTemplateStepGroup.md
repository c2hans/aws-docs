---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetTemplateStepGroup.html
---

# GetTemplateStepGroup
<a name="API_GetTemplateStepGroup"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Get a step group in a template.

## Request Syntax
<a name="API_GetTemplateStepGroup_RequestSyntax"></a>

```
GET /templates/{{templateId}}/stepgroups/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTemplateStepGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetTemplateStepGroup_RequestSyntax) **   <a name="migrationhuborchestrator-GetTemplateStepGroup-request-uri-id"></a>
The ID of the step group.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [templateId](#API_GetTemplateStepGroup_RequestSyntax) **   <a name="migrationhuborchestrator-GetTemplateStepGroup-request-uri-templateId"></a>
The ID of the template.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
Required: Yes

## Request Body
<a name="API_GetTemplateStepGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTemplateStepGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": number,
   "description": "string",
   "id": "string",
   "lastModifiedTime": number,
   "name": "string",
   "next": [ "string" ],
   "previous": [ "string" ],
   "status": "string",
   "templateId": "string",
   "tools": [
      {
         "name": "string",
         "url": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetTemplateStepGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetTemplateStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStepGroup-response-creationTime"></a>
The time at which the step group was created.
Type: Timestamp

 ** [description](#API_GetTemplateStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStepGroup-response-description"></a>
The description of the step group.
Type: String

 ** [id](#API_GetTemplateStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStepGroup-response-id"></a>
The ID of the step group.
Type: String

 ** [lastModifiedTime](#API_GetTemplateStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStepGroup-response-lastModifiedTime"></a>
The time at which the step group was last modified.
Type: Timestamp

 ** [name](#API_GetTemplateStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStepGroup-response-name"></a>
The name of the step group.
Type: String

 ** [next](#API_GetTemplateStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStepGroup-response-next"></a>
The next step group.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [previous](#API_GetTemplateStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStepGroup-response-previous"></a>
The previous step group.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [status](#API_GetTemplateStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStepGroup-response-status"></a>
The status of the step group.
Type: String
Valid Values: `AWAITING_DEPENDENCIES | READY | IN_PROGRESS | COMPLETED | FAILED | PAUSED | PAUSING | USER_ATTENTION_REQUIRED`

 ** [templateId](#API_GetTemplateStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStepGroup-response-templateId"></a>
The ID of the template.
Type: String

 ** [tools](#API_GetTemplateStepGroup_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStepGroup-response-tools"></a>
List of AWS services utilized in a migration workflow.
Type: Array of [Tool](API_Tool.md) objects

## Errors
<a name="API_GetTemplateStepGroup_Errors"></a>

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
<a name="API_GetTemplateStepGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/GetTemplateStepGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/GetTemplateStepGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/GetTemplateStepGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/GetTemplateStepGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/GetTemplateStepGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/GetTemplateStepGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/GetTemplateStepGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/GetTemplateStepGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/GetTemplateStepGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/GetTemplateStepGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
