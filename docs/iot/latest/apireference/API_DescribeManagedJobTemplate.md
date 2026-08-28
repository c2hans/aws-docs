---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeManagedJobTemplate.html
---

# DescribeManagedJobTemplate
<a name="API_DescribeManagedJobTemplate"></a>

View details of a managed job template.

## Request Syntax
<a name="API_DescribeManagedJobTemplate_RequestSyntax"></a>

```
GET /managed-job-templates/{{templateName}}?templateVersion={{templateVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeManagedJobTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [templateName](#API_DescribeManagedJobTemplate_RequestSyntax) **   <a name="iot-DescribeManagedJobTemplate-request-uri-templateName"></a>
The unique name of a managed job template, which is required.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [templateVersion](#API_DescribeManagedJobTemplate_RequestSyntax) **   <a name="iot-DescribeManagedJobTemplate-request-uri-templateVersion"></a>
An optional parameter to specify version of a managed template. If not specified, the pre-defined default version is returned.
Pattern: `^[1-9]+.[0-9]+`

## Request Body
<a name="API_DescribeManagedJobTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeManagedJobTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "description": "string",
   "document": "string",
   "documentParameters": [
      {
         "description": "string",
         "example": "string",
         "key": "string",
         "optional": boolean,
         "regex": "string"
      }
   ],
   "environments": [ "string" ],
   "templateArn": "string",
   "templateName": "string",
   "templateVersion": "string"
}
```

## Response Elements
<a name="API_DescribeManagedJobTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_DescribeManagedJobTemplate_ResponseSyntax) **   <a name="iot-DescribeManagedJobTemplate-response-description"></a>
The unique description of a managed template.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`

 ** [document](#API_DescribeManagedJobTemplate_ResponseSyntax) **   <a name="iot-DescribeManagedJobTemplate-response-document"></a>
The document schema for a managed job template.
Type: String
Length Constraints: Maximum length of 32768.

 ** [documentParameters](#API_DescribeManagedJobTemplate_ResponseSyntax) **   <a name="iot-DescribeManagedJobTemplate-response-documentParameters"></a>
A map of key-value pairs that you can use as guidance to specify the inputs for creating a job from a managed template.
 `documentParameters` can only be used when creating jobs from AWS managed templates. This parameter can't be used with custom job templates or to create jobs from them.
Type: Array of [DocumentParameter](API_DocumentParameter.md) objects

 ** [environments](#API_DescribeManagedJobTemplate_ResponseSyntax) **   <a name="iot-DescribeManagedJobTemplate-response-environments"></a>
A list of environments that are supported with the managed job template.
Type: Array of strings
Pattern: `[^\p{C}]+`

 ** [templateArn](#API_DescribeManagedJobTemplate_ResponseSyntax) **   <a name="iot-DescribeManagedJobTemplate-response-templateArn"></a>
The unique Amazon Resource Name (ARN) of the managed template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:[!-~]+$`

 ** [templateName](#API_DescribeManagedJobTemplate_ResponseSyntax) **   <a name="iot-DescribeManagedJobTemplate-response-templateName"></a>
The unique name of a managed template, such as `AWS-Reboot`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [templateVersion](#API_DescribeManagedJobTemplate_ResponseSyntax) **   <a name="iot-DescribeManagedJobTemplate-response-templateVersion"></a>
The version for a managed template.
Type: String
Pattern: `^[1-9]+.[0-9]+`

## Errors
<a name="API_DescribeManagedJobTemplate_Errors"></a>

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeManagedJobTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeManagedJobTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeManagedJobTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeManagedJobTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeManagedJobTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeManagedJobTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeManagedJobTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeManagedJobTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeManagedJobTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeManagedJobTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeManagedJobTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
