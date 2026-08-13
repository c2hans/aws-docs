---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetProfile.html
---

# GetProfile
<a name="API_GetProfile"></a>

 Gets the aggregated profile of a profiling group for a specified time range. Amazon CodeGuru Profiler collects posted agent profiles for a profiling group into aggregated profiles.

**Note**
 Because aggregated profiles expire over time `GetProfile` is not idempotent.

 Specify the time range for the requested aggregated profile using 1 or 2 of the following parameters: `startTime`, `endTime`, `period`. The maximum time range allowed is 7 days. If you specify all 3 parameters, an exception is thrown. If you specify only `period`, the latest aggregated profile is returned.

 Aggregated profiles are available with aggregation periods of 5 minutes, 1 hour, and 1 day, aligned to UTC. The aggregation period of an aggregated profile determines how long it is retained. For more information, see [`AggregatedProfileTime`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AggregatedProfileTime.html). The aggregated profile's aggregation period determines how long it is retained by CodeGuru Profiler.
+  If the aggregation period is 5 minutes, the aggregated profile is retained for 15 days.
+  If the aggregation period is 1 hour, the aggregated profile is retained for 60 days.
+  If the aggregation period is 1 day, the aggregated profile is retained for 3 years.

There are two use cases for calling `GetProfile`.

1.  If you want to return an aggregated profile that already exists, use [`ListProfileTimes`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ListProfileTimes.html) to view the time ranges of existing aggregated profiles. Use them in a `GetProfile` request to return a specific, existing aggregated profile.

1.  If you want to return an aggregated profile for a time range that doesn't align with an existing aggregated profile, then CodeGuru Profiler makes a best effort to combine existing aggregated profiles from the requested time range and return them as one aggregated profile.

    If aggregated profiles do not exist for the full time range requested, then aggregated profiles for a smaller time range are returned. For example, if the requested time range is from 00:00 to 00:20, and the existing aggregated profiles are from 00:15 and 00:25, then the aggregated profiles from 00:15 to 00:20 are returned.

## Request Syntax
<a name="API_GetProfile_RequestSyntax"></a>

```
GET /profilingGroups/{{profilingGroupName}}/profile?endTime={{endTime}}&maxDepth={{maxDepth}}&period={{period}}&startTime={{startTime}} HTTP/1.1
Accept: {{accept}}
```

## URI Request Parameters
<a name="API_GetProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accept](#API_GetProfile_RequestSyntax) **   <a name="profiler-GetProfile-request-accept"></a>
 The format of the returned profiling data. The format maps to the `Accept` and `Content-Type` headers of the HTTP request. You can specify one of the following: or the default .
+  `application/json` — standard JSON format
+  `application/x-amzn-ion` — the Amazon Ion data format. For more information, see [Amazon Ion](http://amzn.github.io/ion-docs/).

 ** [endTime](#API_GetProfile_RequestSyntax) **   <a name="profiler-GetProfile-request-uri-endTime"></a>
 The end time of the requested profile. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
 If you specify `endTime`, then you must also specify `period` or `startTime`, but not both.

 ** [maxDepth](#API_GetProfile_RequestSyntax) **   <a name="profiler-GetProfile-request-uri-maxDepth"></a>
 The maximum depth of the stacks in the code that is represented in the aggregated profile. For example, if CodeGuru Profiler finds a method `A`, which calls method `B`, which calls method `C`, which calls method `D`, then the depth is 4. If the `maxDepth` is set to 2, then the aggregated profile contains representations of methods `A` and `B`.
Valid Range: Minimum value of 1. Maximum value of 10000.

 ** [period](#API_GetProfile_RequestSyntax) **   <a name="profiler-GetProfile-request-uri-period"></a>
 Used with `startTime` or `endTime` to specify the time range for the returned aggregated profile. Specify using the ISO 8601 format. For example, `P1DT1H1M1S`.
 To get the latest aggregated profile, specify only `period`.
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [profilingGroupName](#API_GetProfile_RequestSyntax) **   <a name="profiler-GetProfile-request-uri-profilingGroupName"></a>
The name of the profiling group to get.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`
Required: Yes

 ** [startTime](#API_GetProfile_RequestSyntax) **   <a name="profiler-GetProfile-request-uri-startTime"></a>
The start time of the profile to get. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
 If you specify `startTime`, then you must also specify `period` or `endTime`, but not both.

## Request Body
<a name="API_GetProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{contentType}}
Content-Encoding: {{contentEncoding}}

{{profile}}
```

## Response Elements
<a name="API_GetProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [contentEncoding](#API_GetProfile_ResponseSyntax) **   <a name="profiler-GetProfile-response-contentEncoding"></a>
The content encoding of the profile.

 ** [contentType](#API_GetProfile_ResponseSyntax) **   <a name="profiler-GetProfile-response-contentType"></a>
The content type of the profile in the payload. It is either `application/json` or the default `application/x-amzn-ion`.

The response returns the following as the HTTP body.

 ** [profile](#API_GetProfile_ResponseSyntax) **   <a name="profiler-GetProfile-response-profile"></a>
Information about the profile.

## Errors
<a name="API_GetProfile_Errors"></a>

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
<a name="API_GetProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/GetProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/GetProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/GetProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/GetProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/GetProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/GetProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/GetProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/GetProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/GetProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/GetProfile)
