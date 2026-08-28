---
source_url: https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_DeleteHumanLoop.html
---

# DeleteHumanLoop
<a name="API_DeleteHumanLoop"></a>

Deletes the specified human loop for a flow definition.

If the human loop was deleted, this operation will return a `ResourceNotFoundException`.

## Request Syntax
<a name="API_DeleteHumanLoop_RequestSyntax"></a>

```
DELETE /human-loops/{{HumanLoopName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteHumanLoop_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HumanLoopName](#API_DeleteHumanLoop_RequestSyntax) **   <a name="augmentedai-DeleteHumanLoop-request-uri-HumanLoopName"></a>
The name of the human loop that you want to delete.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](-*[a-z0-9])*$`
Required: Yes

## Request Body
<a name="API_DeleteHumanLoop_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteHumanLoop_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteHumanLoop_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteHumanLoop_Errors"></a>

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
<a name="API_DeleteHumanLoop_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-a2i-runtime-2019-11-07/DeleteHumanLoop)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-a2i-runtime-2019-11-07/DeleteHumanLoop)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-a2i-runtime-2019-11-07/DeleteHumanLoop)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-a2i-runtime-2019-11-07/DeleteHumanLoop)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-a2i-runtime-2019-11-07/DeleteHumanLoop)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-a2i-runtime-2019-11-07/DeleteHumanLoop)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-a2i-runtime-2019-11-07/DeleteHumanLoop)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-a2i-runtime-2019-11-07/DeleteHumanLoop)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-a2i-runtime-2019-11-07/DeleteHumanLoop)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-a2i-runtime-2019-11-07/DeleteHumanLoop)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Augmented AI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query augmented-ai` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
