---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateTargetAccountConfiguration.html
---

# CreateTargetAccountConfiguration
<a name="API_CreateTargetAccountConfiguration"></a>

Creates a target account configuration for the experiment template. A target account configuration is required when `accountTargeting` of `experimentOptions` is set to `multi-account`. For more information, see [experiment options](https://docs.aws.amazon.com/fis/latest/userguide/experiment-options.html) in the * AWS Fault Injection Service User Guide*.

## Request Syntax
<a name="API_CreateTargetAccountConfiguration_RequestSyntax"></a>

```
POST /experimentTemplates/{{id}}/targetAccountConfigurations/{{accountId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateTargetAccountConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_CreateTargetAccountConfiguration_RequestSyntax) **   <a name="fis-CreateTargetAccountConfiguration-request-uri-accountId"></a>
The AWS account ID of the target account.
Length Constraints: Minimum length of 12. Maximum length of 48.
Pattern: `[\S]+`
Required: Yes

 ** [id](#API_CreateTargetAccountConfiguration_RequestSyntax) **   <a name="fis-CreateTargetAccountConfiguration-request-uri-experimentTemplateId"></a>
The experiment template ID.
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: Yes

## Request Body
<a name="API_CreateTargetAccountConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateTargetAccountConfiguration_RequestSyntax) **   <a name="fis-CreateTargetAccountConfiguration-request-clientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S]+`
Required: No

 ** [description](#API_CreateTargetAccountConfiguration_RequestSyntax) **   <a name="fis-CreateTargetAccountConfiguration-request-description"></a>
The description of the target account.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]*`
Required: No

 ** [roleArn](#API_CreateTargetAccountConfiguration_RequestSyntax) **   <a name="fis-CreateTargetAccountConfiguration-request-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role for the target account.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: Yes

## Response Syntax
<a name="API_CreateTargetAccountConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "targetAccountConfiguration": {
      "accountId": "string",
      "description": "string",
      "roleArn": "string"
   }
}
```

## Response Elements
<a name="API_CreateTargetAccountConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [targetAccountConfiguration](#API_CreateTargetAccountConfiguration_ResponseSyntax) **   <a name="fis-CreateTargetAccountConfiguration-response-targetAccountConfiguration"></a>
Information about the target account configuration.
Type: [TargetAccountConfiguration](API_TargetAccountConfiguration.md) object

## Errors
<a name="API_CreateTargetAccountConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be processed because of a conflict.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have exceeded your service quota.
HTTP Status Code: 402

 ** ValidationException **
The specified input is not valid, or fails to satisfy the constraints for the request.
HTTP Status Code: 400

## See Also
<a name="API_CreateTargetAccountConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fis-2020-12-01/CreateTargetAccountConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fis-2020-12-01/CreateTargetAccountConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/CreateTargetAccountConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fis-2020-12-01/CreateTargetAccountConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/CreateTargetAccountConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fis-2020-12-01/CreateTargetAccountConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fis-2020-12-01/CreateTargetAccountConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fis-2020-12-01/CreateTargetAccountConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fis-2020-12-01/CreateTargetAccountConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/CreateTargetAccountConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
