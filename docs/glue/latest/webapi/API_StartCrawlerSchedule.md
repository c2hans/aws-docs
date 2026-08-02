---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StartCrawlerSchedule.html
---

# StartCrawlerSchedule
<a name="API_StartCrawlerSchedule"></a>

Changes the schedule state of the specified crawler to `SCHEDULED`, unless the crawler is already running or the schedule state is already `SCHEDULED`.

## Request Syntax
<a name="API_StartCrawlerSchedule_RequestSyntax"></a>

```
{
   "CrawlerName": "{{string}}"
}
```

## Request Parameters
<a name="API_StartCrawlerSchedule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CrawlerName](#API_StartCrawlerSchedule_RequestSyntax) **   <a name="Glue-StartCrawlerSchedule-request-CrawlerName"></a>
Name of the crawler to schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Elements
<a name="API_StartCrawlerSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartCrawlerSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** NoScheduleException **
There is no applicable schedule.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** SchedulerRunningException **
The specified scheduler is already running.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** SchedulerTransitioningException **
The specified scheduler is transitioning.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_StartCrawlerSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/StartCrawlerSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/StartCrawlerSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StartCrawlerSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/StartCrawlerSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StartCrawlerSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/StartCrawlerSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/StartCrawlerSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/StartCrawlerSchedule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/StartCrawlerSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StartCrawlerSchedule)
