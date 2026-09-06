---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeMapRun.html
---

# DescribeMapRun
<a name="API_DescribeMapRun"></a>

Provides information about a Map Run's configuration, progress, and results. If you've [redriven](https://docs.aws.amazon.com/step-functions/latest/dg/redrive-map-run.html) a Map Run, this API action also returns information about the redrives of that Map Run. For more information, see [Examining Map Run](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html) in the * AWS Step Functions Developer Guide*.

## Request Syntax
<a name="API_DescribeMapRun_RequestSyntax"></a>

```
{
   "mapRunArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMapRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [mapRunArn](#API_DescribeMapRun_RequestSyntax) **   <a name="StepFunctions-DescribeMapRun-request-mapRunArn"></a>
The Amazon Resource Name (ARN) that identifies a Map Run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: Yes

## Response Syntax
<a name="API_DescribeMapRun_ResponseSyntax"></a>

```
{
   "executionArn": "string",
   "executionCounts": {
      "aborted": number,
      "failed": number,
      "failuresNotRedrivable": number,
      "pending": number,
      "pendingRedrive": number,
      "resultsWritten": number,
      "running": number,
      "succeeded": number,
      "timedOut": number,
      "total": number
   },
   "itemCounts": {
      "aborted": number,
      "failed": number,
      "failuresNotRedrivable": number,
      "pending": number,
      "pendingRedrive": number,
      "resultsWritten": number,
      "running": number,
      "succeeded": number,
      "timedOut": number,
      "total": number
   },
   "mapRunArn": "string",
   "maxConcurrency": number,
   "redriveCount": number,
   "redriveDate": number,
   "startDate": number,
   "status": "string",
   "stopDate": number,
   "toleratedFailureCount": number,
   "toleratedFailurePercentage": number
}
```

## Response Elements
<a name="API_DescribeMapRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executionArn](#API_DescribeMapRun_ResponseSyntax) **   <a name="StepFunctions-DescribeMapRun-response-executionArn"></a>
The Amazon Resource Name (ARN) that identifies the execution in which the Map Run was started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [executionCounts](#API_DescribeMapRun_ResponseSyntax) **   <a name="StepFunctions-DescribeMapRun-response-executionCounts"></a>
A JSON object that contains information about the total number of child workflow executions for the Map Run, and the count of child workflow executions for each status, such as `failed` and `succeeded`.
Type: [MapRunExecutionCounts](API_MapRunExecutionCounts.md) object

 ** [itemCounts](#API_DescribeMapRun_ResponseSyntax) **   <a name="StepFunctions-DescribeMapRun-response-itemCounts"></a>
A JSON object that contains information about the total number of items, and the item count for each processing status, such as `pending` and `failed`.
Type: [MapRunItemCounts](API_MapRunItemCounts.md) object

 ** [mapRunArn](#API_DescribeMapRun_ResponseSyntax) **   <a name="StepFunctions-DescribeMapRun-response-mapRunArn"></a>
The Amazon Resource Name (ARN) that identifies a Map Run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [maxConcurrency](#API_DescribeMapRun_ResponseSyntax) **   <a name="StepFunctions-DescribeMapRun-response-maxConcurrency"></a>
The maximum number of child workflow executions configured to run in parallel for the Map Run at the same time.
Type: Integer
Valid Range: Minimum value of 0.

 ** [redriveCount](#API_DescribeMapRun_ResponseSyntax) **   <a name="StepFunctions-DescribeMapRun-response-redriveCount"></a>
The number of times you've redriven a Map Run. If you have not yet redriven a Map Run, the `redriveCount` is 0. This count is only updated if you successfully redrive a Map Run.
Type: Integer

 ** [redriveDate](#API_DescribeMapRun_ResponseSyntax) **   <a name="StepFunctions-DescribeMapRun-response-redriveDate"></a>
The date a Map Run was last redriven. If you have not yet redriven a Map Run, the `redriveDate` is null.
Type: Timestamp

 ** [startDate](#API_DescribeMapRun_ResponseSyntax) **   <a name="StepFunctions-DescribeMapRun-response-startDate"></a>
The date when the Map Run was started.
Type: Timestamp

 ** [status](#API_DescribeMapRun_ResponseSyntax) **   <a name="StepFunctions-DescribeMapRun-response-status"></a>
The current status of the Map Run.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | ABORTED`

 ** [stopDate](#API_DescribeMapRun_ResponseSyntax) **   <a name="StepFunctions-DescribeMapRun-response-stopDate"></a>
The date when the Map Run was stopped.
Type: Timestamp

 ** [toleratedFailureCount](#API_DescribeMapRun_ResponseSyntax) **   <a name="StepFunctions-DescribeMapRun-response-toleratedFailureCount"></a>
The maximum number of failed child workflow executions before the Map Run fails.
Type: Long
Valid Range: Minimum value of 0.

 ** [toleratedFailurePercentage](#API_DescribeMapRun_ResponseSyntax) **   <a name="StepFunctions-DescribeMapRun-response-toleratedFailurePercentage"></a>
The maximum percentage of failed child workflow executions before the Map Run fails.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.

## Errors
<a name="API_DescribeMapRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

 ** ResourceNotFound **
Could not find the referenced resource.
HTTP Status Code: 400

## See Also
<a name="API_DescribeMapRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/DescribeMapRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/DescribeMapRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/DescribeMapRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/DescribeMapRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/DescribeMapRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/DescribeMapRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/DescribeMapRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/DescribeMapRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/DescribeMapRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/DescribeMapRun)
