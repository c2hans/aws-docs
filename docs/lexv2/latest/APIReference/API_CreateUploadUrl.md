---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateUploadUrl.html
---

# CreateUploadUrl
<a name="API_CreateUploadUrl"></a>

Gets a pre-signed S3 write URL that you use to upload the zip archive when importing a bot or a bot locale.

## Request Syntax
<a name="API_CreateUploadUrl_RequestSyntax"></a>

```
POST /createuploadurl/ HTTP/1.1
```

## URI Request Parameters
<a name="API_CreateUploadUrl_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateUploadUrl_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CreateUploadUrl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "importId": "string",
   "uploadUrl": "string"
}
```

## Response Elements
<a name="API_CreateUploadUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [importId](#API_CreateUploadUrl_ResponseSyntax) **   <a name="lexv2-CreateUploadUrl-response-importId"></a>
An identifier for a unique import job. Use it when you call the [StartImport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartImport.html) operation.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [uploadUrl](#API_CreateUploadUrl_ResponseSyntax) **   <a name="lexv2-CreateUploadUrl-response-uploadUrl"></a>
A pre-signed S3 write URL. Upload the zip archive file that contains the definition of your bot or bot locale.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_CreateUploadUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_CreateUploadUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/CreateUploadUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/CreateUploadUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/CreateUploadUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/CreateUploadUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/CreateUploadUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/CreateUploadUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/CreateUploadUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/CreateUploadUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/CreateUploadUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/CreateUploadUrl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
