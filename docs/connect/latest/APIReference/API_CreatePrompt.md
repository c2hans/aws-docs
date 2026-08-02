---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreatePrompt.html
---

# CreatePrompt
<a name="API_CreatePrompt"></a>

Creates a prompt. For more information about prompts, such as supported file types and maximum length, see [Create prompts](https://docs.aws.amazon.com/connect/latest/adminguide/prompts.html) in the *Connect Customer Administrator Guide*.

## Request Syntax
<a name="API_CreatePrompt_RequestSyntax"></a>

```
PUT /prompts/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "S3Uri": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreatePrompt_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreatePrompt_RequestSyntax) **   <a name="connect-CreatePrompt-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreatePrompt_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreatePrompt_RequestSyntax) **   <a name="connect-CreatePrompt-request-Description"></a>
The description of the prompt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** [Name](#API_CreatePrompt_RequestSyntax) **   <a name="connect-CreatePrompt-request-Name"></a>
The name of the prompt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: Yes

 ** [S3Uri](#API_CreatePrompt_RequestSyntax) **   <a name="connect-CreatePrompt-request-S3Uri"></a>
The URI for the S3 bucket where the prompt is stored. You can provide S3 pre-signed URLs returned by the [GetPromptFile](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetPromptFile.html) API instead of providing S3 URIs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `s3://\S+/.+|https://\\S+\\.s3\\.\\S+\\.amazonaws\\.com/\\S+`
Required: Yes

 ** [Tags](#API_CreatePrompt_RequestSyntax) **   <a name="connect-CreatePrompt-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreatePrompt_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PromptARN": "string",
   "PromptId": "string"
}
```

## Response Elements
<a name="API_CreatePrompt_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PromptARN](#API_CreatePrompt_ResponseSyntax) **   <a name="connect-CreatePrompt-response-PromptARN"></a>
The Amazon Resource Name (ARN) of the prompt.
Type: String

 ** [PromptId](#API_CreatePrompt_ResponseSyntax) **   <a name="connect-CreatePrompt-response-PromptId"></a>
A unique identifier for the prompt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_CreatePrompt_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

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

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreatePrompt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreatePrompt)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreatePrompt)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreatePrompt)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreatePrompt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreatePrompt)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreatePrompt)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreatePrompt)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreatePrompt)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreatePrompt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreatePrompt)
