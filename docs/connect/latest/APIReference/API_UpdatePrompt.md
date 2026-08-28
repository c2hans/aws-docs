---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePrompt.html
---

# UpdatePrompt
<a name="API_UpdatePrompt"></a>

Updates a prompt.

## Request Syntax
<a name="API_UpdatePrompt_RequestSyntax"></a>

```
POST /prompts/{{InstanceId}}/{{PromptId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "S3Uri": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePrompt_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdatePrompt_RequestSyntax) **   <a name="connect-UpdatePrompt-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [PromptId](#API_UpdatePrompt_RequestSyntax) **   <a name="connect-UpdatePrompt-request-uri-PromptId"></a>
A unique identifier for the prompt.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_UpdatePrompt_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdatePrompt_RequestSyntax) **   <a name="connect-UpdatePrompt-request-Description"></a>
A description of the prompt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** [Name](#API_UpdatePrompt_RequestSyntax) **   <a name="connect-UpdatePrompt-request-Name"></a>
The name of the prompt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

 ** [S3Uri](#API_UpdatePrompt_RequestSyntax) **   <a name="connect-UpdatePrompt-request-S3Uri"></a>
The URI for the S3 bucket where the prompt is stored. You can provide S3 pre-signed URLs returned by the [GetPromptFile](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetPromptFile.html) API instead of providing S3 URIs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `s3://\S+/.+|https://\\S+\\.s3\\.\\S+\\.amazonaws\\.com/\\S+`
Required: No

## Response Syntax
<a name="API_UpdatePrompt_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PromptARN": "string",
   "PromptId": "string"
}
```

## Response Elements
<a name="API_UpdatePrompt_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PromptARN](#API_UpdatePrompt_ResponseSyntax) **   <a name="connect-UpdatePrompt-response-PromptARN"></a>
The Amazon Resource Name (ARN) of the prompt.
Type: String

 ** [PromptId](#API_UpdatePrompt_ResponseSyntax) **   <a name="connect-UpdatePrompt-response-PromptId"></a>
A unique identifier for the prompt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_UpdatePrompt_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdatePrompt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdatePrompt)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdatePrompt)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdatePrompt)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdatePrompt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdatePrompt)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdatePrompt)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdatePrompt)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdatePrompt)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdatePrompt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdatePrompt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
