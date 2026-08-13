---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetFindingsReportAccountSummary.html
---

# GetFindingsReportAccountSummary
<a name="API_GetFindingsReportAccountSummary"></a>

 Returns a list of [`FindingsReportSummary`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_FindingsReportSummary.html) objects that contain analysis results for all profiling groups in your AWS account.

## Request Syntax
<a name="API_GetFindingsReportAccountSummary_RequestSyntax"></a>

```
GET /internal/findingsReports?dailyReportsOnly={{dailyReportsOnly}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFindingsReportAccountSummary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dailyReportsOnly](#API_GetFindingsReportAccountSummary_RequestSyntax) **   <a name="profiler-GetFindingsReportAccountSummary-request-uri-dailyReportsOnly"></a>
A `Boolean` value indicating whether to only return reports from daily profiles. If set to `True`, only analysis data from daily profiles is returned. If set to `False`, analysis data is returned from smaller time windows (for example, one hour).

 ** [maxResults](#API_GetFindingsReportAccountSummary_RequestSyntax) **   <a name="profiler-GetFindingsReportAccountSummary-request-uri-maxResults"></a>
The maximum number of results returned by ` GetFindingsReportAccountSummary` in paginated output. When this parameter is used, `GetFindingsReportAccountSummary` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `GetFindingsReportAccountSummary` request with the returned `nextToken` value.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_GetFindingsReportAccountSummary_RequestSyntax) **   <a name="profiler-GetFindingsReportAccountSummary-request-uri-nextToken"></a>
The `nextToken` value returned from a previous paginated `GetFindingsReportAccountSummary` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w-]+`

## Request Body
<a name="API_GetFindingsReportAccountSummary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFindingsReportAccountSummary_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "reportSummaries": [
      {
         "id": "string",
         "profileEndTime": "string",
         "profileStartTime": "string",
         "profilingGroupName": "string",
         "totalNumberOfFindings": number
      }
   ]
}
```

## Response Elements
<a name="API_GetFindingsReportAccountSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetFindingsReportAccountSummary_ResponseSyntax) **   <a name="profiler-GetFindingsReportAccountSummary-response-nextToken"></a>
The `nextToken` value to include in a future `GetFindingsReportAccountSummary` request. When the results of a `GetFindingsReportAccountSummary` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w-]+`

 ** [reportSummaries](#API_GetFindingsReportAccountSummary_ResponseSyntax) **   <a name="profiler-GetFindingsReportAccountSummary-response-reportSummaries"></a>
The return list of [`FindingsReportSummary`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_FindingsReportSummary.html) objects taht contain summaries of analysis results for all profiling groups in your AWS account.
Type: Array of [FindingsReportSummary](API_FindingsReportSummary.md) objects

## Errors
<a name="API_GetFindingsReportAccountSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_GetFindingsReportAccountSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/GetFindingsReportAccountSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/GetFindingsReportAccountSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/GetFindingsReportAccountSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/GetFindingsReportAccountSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/GetFindingsReportAccountSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/GetFindingsReportAccountSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/GetFindingsReportAccountSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/GetFindingsReportAccountSummary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/GetFindingsReportAccountSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/GetFindingsReportAccountSummary)
