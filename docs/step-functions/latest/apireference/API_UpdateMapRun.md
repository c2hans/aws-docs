---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateMapRun.html
---

# UpdateMapRun
<a name="API_UpdateMapRun"></a>

Updates an in-progress Map Run's configuration to include changes to the settings that control maximum concurrency and Map Run failure.

## Request Syntax
<a name="API_UpdateMapRun_RequestSyntax"></a>

```
{
   "mapRunArn": "{{string}}",
   "maxConcurrency": {{number}},
   "toleratedFailureCount": {{number}},
   "toleratedFailurePercentage": {{number}}
}
```

## Request Parameters
<a name="API_UpdateMapRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [mapRunArn](#API_UpdateMapRun_RequestSyntax) **   <a name="StepFunctions-UpdateMapRun-request-mapRunArn"></a>
The Amazon Resource Name (ARN) of a Map Run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: Yes

 ** [maxConcurrency](#API_UpdateMapRun_RequestSyntax) **   <a name="StepFunctions-UpdateMapRun-request-maxConcurrency"></a>
The maximum number of child workflow executions that can be specified to run in parallel for the Map Run at the same time.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [toleratedFailureCount](#API_UpdateMapRun_RequestSyntax) **   <a name="StepFunctions-UpdateMapRun-request-toleratedFailureCount"></a>
The maximum number of failed items before the Map Run fails.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** [toleratedFailurePercentage](#API_UpdateMapRun_RequestSyntax) **   <a name="StepFunctions-UpdateMapRun-request-toleratedFailurePercentage"></a>
The maximum percentage of failed items before the Map Run fails.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## Response Elements
<a name="API_UpdateMapRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateMapRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** ResourceNotFound **
Could not find the referenced resource.
HTTP Status Code: 400

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** reason **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateMapRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/UpdateMapRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/UpdateMapRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/UpdateMapRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/UpdateMapRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/UpdateMapRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/UpdateMapRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/UpdateMapRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/UpdateMapRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/UpdateMapRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/UpdateMapRun)
