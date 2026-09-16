---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_GetTestExecutionArtifactsUrl.html
---

# GetTestExecutionArtifactsUrl
<a name="API_GetTestExecutionArtifactsUrl"></a>

The pre-signed Amazon S3 URL to download the test execution result artifacts.

## Request Syntax
<a name="API_GetTestExecutionArtifactsUrl_RequestSyntax"></a>

```
GET /testexecutions/{{testExecutionId}}/artifacturl HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTestExecutionArtifactsUrl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [testExecutionId](#API_GetTestExecutionArtifactsUrl_RequestSyntax) **   <a name="lexv2-GetTestExecutionArtifactsUrl-request-uri-testExecutionId"></a>
The unique identifier of the completed test execution.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_GetTestExecutionArtifactsUrl_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTestExecutionArtifactsUrl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "downloadArtifactsUrl": "string",
   "testExecutionId": "string"
}
```

## Response Elements
<a name="API_GetTestExecutionArtifactsUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [downloadArtifactsUrl](#API_GetTestExecutionArtifactsUrl_ResponseSyntax) **   <a name="lexv2-GetTestExecutionArtifactsUrl-response-downloadArtifactsUrl"></a>
The pre-signed Amazon S3 URL to download completed test execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [testExecutionId](#API_GetTestExecutionArtifactsUrl_ResponseSyntax) **   <a name="lexv2-GetTestExecutionArtifactsUrl-response-testExecutionId"></a>
The unique identifier of the completed test execution.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

## Errors
<a name="API_GetTestExecutionArtifactsUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have reached a quota for your bot.
HTTP Status Code: 402

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_GetTestExecutionArtifactsUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/GetTestExecutionArtifactsUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/GetTestExecutionArtifactsUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/GetTestExecutionArtifactsUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/GetTestExecutionArtifactsUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/GetTestExecutionArtifactsUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/GetTestExecutionArtifactsUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/GetTestExecutionArtifactsUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/GetTestExecutionArtifactsUrl)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/GetTestExecutionArtifactsUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/GetTestExecutionArtifactsUrl)
