---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ListFindingsReports.html
---

# ListFindingsReports
<a name="API_ListFindingsReports"></a>

List the available reports for a given profiling group and time range.

## Request Syntax
<a name="API_ListFindingsReports_RequestSyntax"></a>

```
GET /internal/profilingGroups/{{profilingGroupName}}/findingsReports?dailyReportsOnly={{dailyReportsOnly}}&endTime={{endTime}}&maxResults={{maxResults}}&nextToken={{nextToken}}&startTime={{startTime}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFindingsReports_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dailyReportsOnly](#API_ListFindingsReports_RequestSyntax) **   <a name="profiler-ListFindingsReports-request-uri-dailyReportsOnly"></a>
A `Boolean` value indicating whether to only return reports from daily profiles. If set to `True`, only analysis data from daily profiles is returned. If set to `False`, analysis data is returned from smaller time windows (for example, one hour).

 ** [endTime](#API_ListFindingsReports_RequestSyntax) **   <a name="profiler-ListFindingsReports-request-uri-endTime"></a>
 The end time of the profile to get analysis data about. You must specify `startTime` and `endTime`. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Required: Yes

 ** [maxResults](#API_ListFindingsReports_RequestSyntax) **   <a name="profiler-ListFindingsReports-request-uri-maxResults"></a>
The maximum number of report results returned by `ListFindingsReports` in paginated output. When this parameter is used, `ListFindingsReports` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListFindingsReports` request with the returned `nextToken` value.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListFindingsReports_RequestSyntax) **   <a name="profiler-ListFindingsReports-request-uri-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListFindingsReportsRequest` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w-]+`

 ** [profilingGroupName](#API_ListFindingsReports_RequestSyntax) **   <a name="profiler-ListFindingsReports-request-uri-profilingGroupName"></a>
The name of the profiling group from which to search for analysis data.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`
Required: Yes

 ** [startTime](#API_ListFindingsReports_RequestSyntax) **   <a name="profiler-ListFindingsReports-request-uri-startTime"></a>
 The start time of the profile to get analysis data about. You must specify `startTime` and `endTime`. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Required: Yes

## Request Body
<a name="API_ListFindingsReports_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFindingsReports_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "findingsReportSummaries": [
      {
         "id": "string",
         "profileEndTime": "string",
         "profileStartTime": "string",
         "profilingGroupName": "string",
         "totalNumberOfFindings": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListFindingsReports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [findingsReportSummaries](#API_ListFindingsReports_ResponseSyntax) **   <a name="profiler-ListFindingsReports-response-findingsReportSummaries"></a>
The list of analysis results summaries.
Type: Array of [FindingsReportSummary](API_FindingsReportSummary.md) objects

 ** [nextToken](#API_ListFindingsReports_ResponseSyntax) **   <a name="profiler-ListFindingsReports-response-nextToken"></a>
The `nextToken` value to include in a future `ListFindingsReports` request. When the results of a `ListFindingsReports` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w-]+`

## Errors
<a name="API_ListFindingsReports_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListFindingsReports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/ListFindingsReports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/ListFindingsReports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/ListFindingsReports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/ListFindingsReports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/ListFindingsReports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/ListFindingsReports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/ListFindingsReports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/ListFindingsReports)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/ListFindingsReports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/ListFindingsReports)
