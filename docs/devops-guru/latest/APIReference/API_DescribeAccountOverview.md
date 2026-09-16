---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeAccountOverview.html
---

# DescribeAccountOverview
<a name="API_DescribeAccountOverview"></a>

 For the time range passed in, returns the number of open reactive insight that were created, the number of open proactive insights that were created, and the Mean Time to Recover (MTTR) for all closed reactive insights.

## Request Syntax
<a name="API_DescribeAccountOverview_RequestSyntax"></a>

```
POST /accounts/overview HTTP/1.1
Content-type: application/json

{
   "FromTime": {{number}},
   "ToTime": {{number}}
}
```

## URI Request Parameters
<a name="API_DescribeAccountOverview_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeAccountOverview_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [FromTime](#API_DescribeAccountOverview_RequestSyntax) **   <a name="DevOpsGuru-DescribeAccountOverview-request-FromTime"></a>
 The start of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred after this day.
Type: Timestamp
Required: Yes

 ** [ToTime](#API_DescribeAccountOverview_RequestSyntax) **   <a name="DevOpsGuru-DescribeAccountOverview-request-ToTime"></a>
 The end of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred before this day. If this is not specified, then the current day is used.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_DescribeAccountOverview_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MeanTimeToRecoverInMilliseconds": number,
   "ProactiveInsights": number,
   "ReactiveInsights": number
}
```

## Response Elements
<a name="API_DescribeAccountOverview_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MeanTimeToRecoverInMilliseconds](#API_DescribeAccountOverview_ResponseSyntax) **   <a name="DevOpsGuru-DescribeAccountOverview-response-MeanTimeToRecoverInMilliseconds"></a>
 The Mean Time to Recover (MTTR) for all closed insights that were created during the time range passed in.
Type: Long

 ** [ProactiveInsights](#API_DescribeAccountOverview_ResponseSyntax) **   <a name="DevOpsGuru-DescribeAccountOverview-response-ProactiveInsights"></a>
 An integer that specifies the number of open proactive insights in your AWS account that were created during the time range passed in.
Type: Integer

 ** [ReactiveInsights](#API_DescribeAccountOverview_ResponseSyntax) **   <a name="DevOpsGuru-DescribeAccountOverview-response-ReactiveInsights"></a>
 An integer that specifies the number of open reactive insights in your AWS account that were created during the time range passed in.
Type: Integer

## Errors
<a name="API_DescribeAccountOverview_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 403

 ** InternalServerException **
An internal failure in an Amazon service occurred.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the internal server exception can be retried.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to a request throttling.
 ** QuotaCode **
 The code of the quota that was exceeded, causing the throttling exception.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the throttling exception can be retried.
 ** ServiceCode **
 The code of the service that caused the throttling exception.
HTTP Status Code: 429

 ** ValidationException **
 Contains information about data passed in to a field during a request that is not valid.
 ** Fields **
 An array of fields that are associated with the validation exception.
 ** Message **
 A message that describes the validation exception.
 ** Reason **
 The reason the validation exception was thrown.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAccountOverview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/DescribeAccountOverview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/DescribeAccountOverview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/DescribeAccountOverview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/DescribeAccountOverview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/DescribeAccountOverview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/DescribeAccountOverview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/DescribeAccountOverview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/DescribeAccountOverview)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/DescribeAccountOverview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/DescribeAccountOverview)
