---
source_url: https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_DescribeHumanLoop.html
---

# DescribeHumanLoop
<a name="API_DescribeHumanLoop"></a>

Returns information about the specified human loop. If the human loop was deleted, this operation will return a `ResourceNotFoundException` error.

## Request Syntax
<a name="API_DescribeHumanLoop_RequestSyntax"></a>

```
GET /human-loops/{{HumanLoopName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeHumanLoop_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HumanLoopName](#API_DescribeHumanLoop_RequestSyntax) **   <a name="augmentedai-DescribeHumanLoop-request-uri-HumanLoopName"></a>
The name of the human loop that you want information about.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](-*[a-z0-9])*$`
Required: Yes

## Request Body
<a name="API_DescribeHumanLoop_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeHumanLoop_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": number,
   "FailureCode": "string",
   "FailureReason": "string",
   "FlowDefinitionArn": "string",
   "HumanLoopArn": "string",
   "HumanLoopName": "string",
   "HumanLoopOutput": {
      "OutputS3Uri": "string"
   },
   "HumanLoopStatus": "string"
}
```

## Response Elements
<a name="API_DescribeHumanLoop_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeHumanLoop_ResponseSyntax) **   <a name="augmentedai-DescribeHumanLoop-response-CreationTime"></a>
The creation time when Amazon Augmented AI created the human loop.
Type: Timestamp

 ** [FailureCode](#API_DescribeHumanLoop_ResponseSyntax) **   <a name="augmentedai-DescribeHumanLoop-response-FailureCode"></a>
A failure code that identifies the type of failure.
Possible values: `ValidationError`, `Expired`, `InternalError`
Type: String

 ** [FailureReason](#API_DescribeHumanLoop_ResponseSyntax) **   <a name="augmentedai-DescribeHumanLoop-response-FailureReason"></a>
The reason why a human loop failed. The failure reason is returned when the status of the human loop is `Failed`.
Type: String

 ** [FlowDefinitionArn](#API_DescribeHumanLoop_ResponseSyntax) **   <a name="augmentedai-DescribeHumanLoop-response-FlowDefinitionArn"></a>
The Amazon Resource Name (ARN) of the flow definition.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:flow-definition/.*`

 ** [HumanLoopArn](#API_DescribeHumanLoop_ResponseSyntax) **   <a name="augmentedai-DescribeHumanLoop-response-HumanLoopArn"></a>
The Amazon Resource Name (ARN) of the human loop.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:human-loop/.*`

 ** [HumanLoopName](#API_DescribeHumanLoop_ResponseSyntax) **   <a name="augmentedai-DescribeHumanLoop-response-HumanLoopName"></a>
The name of the human loop. The name must be lowercase, unique within the Region in your account, and can have up to 63 characters. Valid characters: a-z, 0-9, and - (hyphen).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](-*[a-z0-9])*$`

 ** [HumanLoopOutput](#API_DescribeHumanLoop_ResponseSyntax) **   <a name="augmentedai-DescribeHumanLoop-response-HumanLoopOutput"></a>
An object that contains information about the output of the human loop.
Type: [HumanLoopOutput](API_HumanLoopOutput.md) object

 ** [HumanLoopStatus](#API_DescribeHumanLoop_ResponseSyntax) **   <a name="augmentedai-DescribeHumanLoop-response-HumanLoopStatus"></a>
The status of the human loop.
Type: String
Valid Values: `InProgress | Failed | Completed | Stopped | Stopping`

## Errors
<a name="API_DescribeHumanLoop_Errors"></a>

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
<a name="API_DescribeHumanLoop_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-a2i-runtime-2019-11-07/DescribeHumanLoop)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-a2i-runtime-2019-11-07/DescribeHumanLoop)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-a2i-runtime-2019-11-07/DescribeHumanLoop)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-a2i-runtime-2019-11-07/DescribeHumanLoop)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-a2i-runtime-2019-11-07/DescribeHumanLoop)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-a2i-runtime-2019-11-07/DescribeHumanLoop)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-a2i-runtime-2019-11-07/DescribeHumanLoop)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-a2i-runtime-2019-11-07/DescribeHumanLoop)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-a2i-runtime-2019-11-07/DescribeHumanLoop)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-a2i-runtime-2019-11-07/DescribeHumanLoop)
