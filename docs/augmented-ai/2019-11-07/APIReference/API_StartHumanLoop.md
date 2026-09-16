---
source_url: https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_StartHumanLoop.html
---

# StartHumanLoop
<a name="API_StartHumanLoop"></a>

Starts a human loop, provided that at least one activation condition is met.

## Request Syntax
<a name="API_StartHumanLoop_RequestSyntax"></a>

```
POST /human-loops HTTP/1.1
Content-type: application/json

{
   "DataAttributes": {
      "ContentClassifiers": [ "{{string}}" ]
   },
   "FlowDefinitionArn": "{{string}}",
   "HumanLoopInput": {
      "InputContent": "{{string}}"
   },
   "HumanLoopName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartHumanLoop_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartHumanLoop_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DataAttributes](#API_StartHumanLoop_RequestSyntax) **   <a name="augmentedai-StartHumanLoop-request-DataAttributes"></a>
Attributes of the specified data. Use `DataAttributes` to specify if your data is free of personally identifiable information and/or free of adult content.
Type: [HumanLoopDataAttributes](API_HumanLoopDataAttributes.md) object
Required: No

 ** [FlowDefinitionArn](#API_StartHumanLoop_RequestSyntax) **   <a name="augmentedai-StartHumanLoop-request-FlowDefinitionArn"></a>
The Amazon Resource Name (ARN) of the flow definition associated with this human loop.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:flow-definition/.*`
Required: Yes

 ** [HumanLoopInput](#API_StartHumanLoop_RequestSyntax) **   <a name="augmentedai-StartHumanLoop-request-HumanLoopInput"></a>
An object that contains information about the human loop.
Type: [HumanLoopInput](API_HumanLoopInput.md) object
Required: Yes

 ** [HumanLoopName](#API_StartHumanLoop_RequestSyntax) **   <a name="augmentedai-StartHumanLoop-request-HumanLoopName"></a>
The name of the human loop.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](-*[a-z0-9])*$`
Required: Yes

## Response Syntax
<a name="API_StartHumanLoop_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "HumanLoopArn": "string"
}
```

## Response Elements
<a name="API_StartHumanLoop_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HumanLoopArn](#API_StartHumanLoop_ResponseSyntax) **   <a name="augmentedai-StartHumanLoop-response-HumanLoopArn"></a>
The Amazon Resource Name (ARN) of the human loop.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:human-loop/.*`

## Errors
<a name="API_StartHumanLoop_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Your request has the same name as another active human loop but has different input data. You cannot start two human loops with the same name and different input data.
HTTP Status Code: 409

 ** InternalServerException **
We couldn't process your request because of an issue with the server. Try again later.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For a list of Amazon A2I service quotes, see [Amazon Augmented AI Service Quotes](https://docs.aws.amazon.com/general/latest/gr/a2i.html). Delete some resources or request an increase in your service quota. You can request a quota increase using Service Quotas or the AWS Support Center. To request an increase, see [AWS Service Quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) in the *AWS General Reference*.
HTTP Status Code: 402

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## See Also
<a name="API_StartHumanLoop_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-a2i-runtime-2019-11-07/StartHumanLoop)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-a2i-runtime-2019-11-07/StartHumanLoop)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-a2i-runtime-2019-11-07/StartHumanLoop)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-a2i-runtime-2019-11-07/StartHumanLoop)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-a2i-runtime-2019-11-07/StartHumanLoop)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-a2i-runtime-2019-11-07/StartHumanLoop)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-a2i-runtime-2019-11-07/StartHumanLoop)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-a2i-runtime-2019-11-07/StartHumanLoop)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-a2i-runtime-2019-11-07/StartHumanLoop)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-a2i-runtime-2019-11-07/StartHumanLoop)
