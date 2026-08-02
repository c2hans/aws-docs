---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ListProfilingGroups.html
---

# ListProfilingGroups
<a name="API_ListProfilingGroups"></a>

 Returns a list of profiling groups. The profiling groups are returned as [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html) objects.

## Request Syntax
<a name="API_ListProfilingGroups_RequestSyntax"></a>

```
GET /profilingGroups?includeDescription={{includeDescription}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListProfilingGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [includeDescription](#API_ListProfilingGroups_RequestSyntax) **   <a name="profiler-ListProfilingGroups-request-uri-includeDescription"></a>
A `Boolean` value indicating whether to include a description. If `true`, then a list of [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html) objects that contain detailed information about profiling groups is returned. If `false`, then a list of profiling group names is returned.

 ** [maxResults](#API_ListProfilingGroups_RequestSyntax) **   <a name="profiler-ListProfilingGroups-request-uri-maxResults"></a>
The maximum number of profiling groups results returned by `ListProfilingGroups` in paginated output. When this parameter is used, `ListProfilingGroups` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListProfilingGroups` request with the returned `nextToken` value.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListProfilingGroups_RequestSyntax) **   <a name="profiler-ListProfilingGroups-request-uri-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListProfilingGroups` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w-]+`

## Request Body
<a name="API_ListProfilingGroups_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListProfilingGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "profilingGroupNames": [ "string" ],
   "profilingGroups": [
      {
         "agentOrchestrationConfig": {
            "profilingEnabled": boolean
         },
         "arn": "string",
         "computePlatform": "string",
         "createdAt": "string",
         "name": "string",
         "profilingStatus": {
            "latestAgentOrchestratedAt": "string",
            "latestAgentProfileReportedAt": "string",
            "latestAggregatedProfile": {
               "period": "string",
               "start": "string"
            }
         },
         "tags": {
            "string" : "string"
         },
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListProfilingGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListProfilingGroups_ResponseSyntax) **   <a name="profiler-ListProfilingGroups-response-nextToken"></a>
The `nextToken` value to include in a future `ListProfilingGroups` request. When the results of a `ListProfilingGroups` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w-]+`

 ** [profilingGroupNames](#API_ListProfilingGroups_ResponseSyntax) **   <a name="profiler-ListProfilingGroups-response-profilingGroupNames"></a>
 A returned list of profiling group names. A list of the names is returned only if `includeDescription` is `false`, otherwise a list of [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html) objects is returned.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`

 ** [profilingGroups](#API_ListProfilingGroups_ResponseSyntax) **   <a name="profiler-ListProfilingGroups-response-profilingGroups"></a>
 A returned list [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html) objects. A list of [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html) objects is returned only if `includeDescription` is `true`, otherwise a list of profiling group names is returned.
Type: Array of [ProfilingGroupDescription](API_ProfilingGroupDescription.md) objects

## Errors
<a name="API_ListProfilingGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_ListProfilingGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/ListProfilingGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/ListProfilingGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/ListProfilingGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/ListProfilingGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/ListProfilingGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/ListProfilingGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/ListProfilingGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/ListProfilingGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/ListProfilingGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/ListProfilingGroups)
