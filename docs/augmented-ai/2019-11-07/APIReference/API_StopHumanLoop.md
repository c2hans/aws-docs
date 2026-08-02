---
source_url: https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_StopHumanLoop.html
---

# StopHumanLoop
<a name="API_StopHumanLoop"></a>

Stops the specified human loop.

## Request Syntax
<a name="API_StopHumanLoop_RequestSyntax"></a>

```
POST /human-loops/stop HTTP/1.1
Content-type: application/json

{
   "HumanLoopName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StopHumanLoop_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StopHumanLoop_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [HumanLoopName](#API_StopHumanLoop_RequestSyntax) **   <a name="augmentedai-StopHumanLoop-request-HumanLoopName"></a>
The name of the human loop that you want to stop.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](-*[a-z0-9])*$`
Required: Yes

## Response Syntax
<a name="API_StopHumanLoop_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StopHumanLoop_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopHumanLoop_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
We couldn't process your request because of an issue with the server. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## See Also
<a name="API_StopHumanLoop_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-a2i-runtime-2019-11-07/StopHumanLoop)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-a2i-runtime-2019-11-07/StopHumanLoop)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-a2i-runtime-2019-11-07/StopHumanLoop)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-a2i-runtime-2019-11-07/StopHumanLoop)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-a2i-runtime-2019-11-07/StopHumanLoop)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-a2i-runtime-2019-11-07/StopHumanLoop)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-a2i-runtime-2019-11-07/StopHumanLoop)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-a2i-runtime-2019-11-07/StopHumanLoop)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-a2i-runtime-2019-11-07/StopHumanLoop)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-a2i-runtime-2019-11-07/StopHumanLoop)
