---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ListProfileTimes.html
---

# ListProfileTimes
<a name="API_ListProfileTimes"></a>

Lists the start times of the available aggregated profiles of a profiling group for an aggregation period within the specified time range.

## Request Syntax
<a name="API_ListProfileTimes_RequestSyntax"></a>

```
GET /profilingGroups/{{profilingGroupName}}/profileTimes?endTime={{endTime}}&maxResults={{maxResults}}&nextToken={{nextToken}}&orderBy={{orderBy}}&period={{period}}&startTime={{startTime}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListProfileTimes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endTime](#API_ListProfileTimes_RequestSyntax) **   <a name="profiler-ListProfileTimes-request-uri-endTime"></a>
The end time of the time range from which to list the profiles.
Required: Yes

 ** [maxResults](#API_ListProfileTimes_RequestSyntax) **   <a name="profiler-ListProfileTimes-request-uri-maxResults"></a>
The maximum number of profile time results returned by `ListProfileTimes` in paginated output. When this parameter is used, `ListProfileTimes` only returns `maxResults` results in a single page with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListProfileTimes` request with the returned `nextToken` value.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListProfileTimes_RequestSyntax) **   <a name="profiler-ListProfileTimes-request-uri-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListProfileTimes` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w-]+`

 ** [orderBy](#API_ListProfileTimes_RequestSyntax) **   <a name="profiler-ListProfileTimes-request-uri-orderBy"></a>
The order (ascending or descending by start time of the profile) to use when listing profiles. Defaults to `TIMESTAMP_DESCENDING`.
Valid Values: `TimestampDescending | TimestampAscending`

 ** [period](#API_ListProfileTimes_RequestSyntax) **   <a name="profiler-ListProfileTimes-request-uri-period"></a>
 The aggregation period. This specifies the period during which an aggregation profile collects posted agent profiles for a profiling group. There are 3 valid values.
+  `P1D` — 1 day
+  `PT1H` — 1 hour
+  `PT5M` — 5 minutes
Valid Values: `PT5M | PT1H | P1D`
Required: Yes

 ** [profilingGroupName](#API_ListProfileTimes_RequestSyntax) **   <a name="profiler-ListProfileTimes-request-uri-profilingGroupName"></a>
The name of the profiling group.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`
Required: Yes

 ** [startTime](#API_ListProfileTimes_RequestSyntax) **   <a name="profiler-ListProfileTimes-request-uri-startTime"></a>
The start time of the time range from which to list the profiles.
Required: Yes

## Request Body
<a name="API_ListProfileTimes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListProfileTimes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "profileTimes": [
      {
         "start": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListProfileTimes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListProfileTimes_ResponseSyntax) **   <a name="profiler-ListProfileTimes-response-nextToken"></a>
The `nextToken` value to include in a future `ListProfileTimes` request. When the results of a `ListProfileTimes` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w-]+`

 ** [profileTimes](#API_ListProfileTimes_ResponseSyntax) **   <a name="profiler-ListProfileTimes-response-profileTimes"></a>
The list of start times of the available profiles for the aggregation period in the specified time range.
Type: Array of [ProfileTime](API_ProfileTime.md) objects

## Errors
<a name="API_ListProfileTimes_Errors"></a>

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
<a name="API_ListProfileTimes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/ListProfileTimes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/ListProfileTimes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/ListProfileTimes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/ListProfileTimes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/ListProfileTimes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/ListProfileTimes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/ListProfileTimes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/ListProfileTimes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/ListProfileTimes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/ListProfileTimes)
