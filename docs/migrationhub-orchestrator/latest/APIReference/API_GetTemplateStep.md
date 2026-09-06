---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetTemplateStep.html
---

# GetTemplateStep
<a name="API_GetTemplateStep"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Get a specific step in a template.

## Request Syntax
<a name="API_GetTemplateStep_RequestSyntax"></a>

```
GET /templatestep/{{id}}?stepGroupId={{stepGroupId}}&templateId={{templateId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTemplateStep_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetTemplateStep_RequestSyntax) **   <a name="migrationhuborchestrator-GetTemplateStep-request-uri-id"></a>
The ID of the step.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [stepGroupId](#API_GetTemplateStep_RequestSyntax) **   <a name="migrationhuborchestrator-GetTemplateStep-request-uri-stepGroupId"></a>
The ID of the step group.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [templateId](#API_GetTemplateStep_RequestSyntax) **   <a name="migrationhuborchestrator-GetTemplateStep-request-uri-templateId"></a>
The ID of the template.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
Required: Yes

## Request Body
<a name="API_GetTemplateStep_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTemplateStep_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "description": "string",
   "id": "string",
   "name": "string",
   "next": [ "string" ],
   "outputs": [
      {
         "dataType": "string",
         "name": "string",
         "required": boolean
      }
   ],
   "previous": [ "string" ],
   "stepActionType": "string",
   "stepAutomationConfiguration": {
      "command": {
         "linux": "string",
         "windows": "string"
      },
      "runEnvironment": "string",
      "scriptLocationS3Bucket": "string",
      "scriptLocationS3Key": {
         "linux": "string",
         "windows": "string"
      },
      "targetType": "string"
   },
   "stepGroupId": "string",
   "templateId": "string"
}
```

## Response Elements
<a name="API_GetTemplateStep_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetTemplateStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStep-response-creationTime"></a>
The time at which the step was created.
Type: String

 ** [description](#API_GetTemplateStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStep-response-description"></a>
The description of the step.
Type: String

 ** [id](#API_GetTemplateStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStep-response-id"></a>
The ID of the step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`

 ** [name](#API_GetTemplateStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStep-response-name"></a>
The name of the step.
Type: String

 ** [next](#API_GetTemplateStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStep-response-next"></a>
The next step.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [outputs](#API_GetTemplateStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStep-response-outputs"></a>
The outputs of the step.
Type: Array of [StepOutput](API_StepOutput.md) objects

 ** [previous](#API_GetTemplateStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStep-response-previous"></a>
The previous step.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [stepActionType](#API_GetTemplateStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStep-response-stepActionType"></a>
The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.
Type: String
Valid Values: `MANUAL | AUTOMATED`

 ** [stepAutomationConfiguration](#API_GetTemplateStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStep-response-stepAutomationConfiguration"></a>
The custom script to run tests on source or target environments.
Type: [StepAutomationConfiguration](API_StepAutomationConfiguration.md) object

 ** [stepGroupId](#API_GetTemplateStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStep-response-stepGroupId"></a>
The ID of the step group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`

 ** [templateId](#API_GetTemplateStep_ResponseSyntax) **   <a name="migrationhuborchestrator-GetTemplateStep-response-templateId"></a>
The ID of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`

## Errors
<a name="API_GetTemplateStep_Errors"></a>

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
<a name="API_GetTemplateStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhuborchestrator-2021-08-28/GetTemplateStep)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhuborchestrator-2021-08-28/GetTemplateStep)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/GetTemplateStep)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhuborchestrator-2021-08-28/GetTemplateStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/GetTemplateStep)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhuborchestrator-2021-08-28/GetTemplateStep)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhuborchestrator-2021-08-28/GetTemplateStep)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhuborchestrator-2021-08-28/GetTemplateStep)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhuborchestrator-2021-08-28/GetTemplateStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/GetTemplateStep)
