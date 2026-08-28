---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetTemplate.html
---

# GetTemplate
<a name="API_GetTemplate"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Get the template you want to use for creating a migration workflow.

## Request Syntax
<a name="API_GetTemplate_RequestSyntax"></a>

```
GET /migrationworkflowtemplate/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetTemplate_RequestSyntax) **   <a name="migrationhuborchestrator-GetTemplate-request-uri-id"></a>
The ID of the template.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
Required: Yes

## Request Body
<a name="API_GetTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": number,
   "description": "string",
   "id": "string",
   "inputs": [
      {
         "dataType": "string",
         "inputName": "string",
         "required": boolean
      }
   ],
   "name": "string",
   "owner": "string",
   "status": "string",
   "statusMessage": "string",
   "tags": {
      "string" : "string"
   },
   "templateArn": "string",
   "templateClass": "string",
   "tools": [
      {
         "name": "string",
         "url": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetTemplate_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplate-response-creationTime"></a>
The time at which the template was last created.
Type: Timestamp

 ** [description](#API_GetTemplate_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplate-response-description"></a>
The time at which the template was last created.
Type: String

 ** [id](#API_GetTemplate_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplate-response-id"></a>
The ID of the template.
Type: String

 ** [inputs](#API_GetTemplate_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplate-response-inputs"></a>
The inputs provided for the creation of the migration workflow.
Type: Array of [TemplateInput](API_TemplateInput.md) objects

 ** [name](#API_GetTemplate_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplate-response-name"></a>
The name of the template.
Type: String

 ** [owner](#API_GetTemplate_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplate-response-owner"></a>
The owner of the migration workflow template.
Type: String

 ** [status](#API_GetTemplate_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplate-response-status"></a>
The status of the template.
Type: String
Valid Values: `CREATED | READY | PENDING_CREATION | CREATING | CREATION_FAILED`

 ** [statusMessage](#API_GetTemplate_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplate-response-statusMessage"></a>
The status message of retrieving migration workflow templates.
Type: String

 ** [tags](#API_GetTemplate_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplate-response-tags"></a>
The tags added to the migration workflow template.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[a-zA-Z0-9-_ ()]+`
Value Length Constraints: Minimum length of 0. Maximum length of 100.

 ** [templateArn](#API_GetTemplate_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplate-response-templateArn"></a>
>The Amazon Resource Name (ARN) of the migration workflow template. The format for an Migration Hub Orchestrator template ARN is `arn:aws:migrationhub-orchestrator:region:account:template/template-abcd1234`. For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) in the *AWS General Reference*.
Type: String

 ** [templateClass](#API_GetTemplate_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplate-response-templateClass"></a>
The class of the migration workflow template. The available template classes are:
+ A2C
+ MGN
+ SAP\_MULTI
+ SQL\_EC2
+ SQL\_RDS
+ VMIE
Type: String

 ** [tools](#API_GetTemplate_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplate-response-tools"></a>
List of AWS services utilized in a migration workflow.
Type: Array of [Tool](API_Tool.md) objects

## Errors
<a name="API_GetTemplate_Errors"></a>

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
<a name="API_GetTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/GetTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/GetTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/GetTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/GetTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/GetTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/GetTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/GetTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/GetTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/GetTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/GetTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
