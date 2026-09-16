---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_CreateTemplate.html
---

# CreateTemplate
<a name="API_CreateTemplate"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Creates a migration workflow template.

## Request Syntax
<a name="API_CreateTemplate_RequestSyntax"></a>

```
POST /template HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "templateDescription": "{{string}}",
   "templateName": "{{string}}",
   "templateSource": { ... }
}
```

## URI Request Parameters
<a name="API_CreateTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateTemplate_RequestSyntax) **   <a name="migrationhuborchestrator-CreateTemplate-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Idempotency](https://smithy.io/2.0/spec/behavior-traits.html#idempotencytoken-trait) in the Smithy documentation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-a-zA-Z0-9]*`
Required: No

 ** [tags](#API_CreateTemplate_RequestSyntax) **   <a name="migrationhuborchestrator-CreateTemplate-request-tags"></a>
The tags to add to the migration workflow template.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [templateDescription](#API_CreateTemplate_RequestSyntax) **   <a name="migrationhuborchestrator-CreateTemplate-request-templateDescription"></a>
A description of the migration workflow template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.
Pattern: `.*`
Required: No

 ** [templateName](#API_CreateTemplate_RequestSyntax) **   <a name="migrationhuborchestrator-CreateTemplate-request-templateName"></a>
The name of the migration workflow template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[ a-zA-Z0-9]*`
Required: Yes

 ** [templateSource](#API_CreateTemplate_RequestSyntax) **   <a name="migrationhuborchestrator-CreateTemplate-request-templateSource"></a>
The source of the migration workflow template.
Type: [TemplateSource](API_TemplateSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_CreateTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "tags": {
      "string" : "string"
   },
   "templateArn": "string",
   "templateId": "string"
}
```

## Response Elements
<a name="API_CreateTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_CreateTemplate_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateTemplate-response-tags"></a>
The tags added to the migration workflow template.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[a-zA-Z0-9-_ ()]+`
Value Length Constraints: Minimum length of 0. Maximum length of 100.

 ** [templateArn](#API_CreateTemplate_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateTemplate-response-templateArn"></a>
The Amazon Resource Name (ARN) of the migration workflow template. The format for an Migration Hub Orchestrator template ARN is `arn:aws:migrationhub-orchestrator:region:account:template/template-abcd1234`. For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) in the *AWS General Reference*.
Type: String

 ** [templateId](#API_CreateTemplate_ResponseSyntax) **   <a name="migrationhuborchestrator-CreateTemplate-response-templateId"></a>
The ID of the migration workflow template.
Type: String

## Errors
<a name="API_CreateTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
This exception is thrown when an attempt to update or delete a resource would cause an inconsistent state.
HTTP Status Code: 409

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
<a name="API_CreateTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/CreateTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/CreateTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/CreateTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/CreateTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/CreateTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/CreateTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/CreateTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/CreateTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/CreateTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/CreateTemplate)
