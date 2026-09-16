---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PostAgentProfile.html
---

# PostAgentProfile
<a name="API_PostAgentProfile"></a>

 Submits profiling data to an aggregated profile of a profiling group. To get an aggregated profile that is created with this profiling data, use [`GetProfile`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetProfile.html).

## Request Syntax
<a name="API_PostAgentProfile_RequestSyntax"></a>

```
POST /profilingGroups/{{profilingGroupName}}/agentProfile?profileToken={{profileToken}} HTTP/1.1
Content-Type: {{contentType}}

{{agentProfile}}
```

## URI Request Parameters
<a name="API_PostAgentProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [contentType](#API_PostAgentProfile_RequestSyntax) **   <a name="profiler-PostAgentProfile-request-contentType"></a>
 The format of the submitted profiling data. The format maps to the `Accept` and `Content-Type` headers of the HTTP request. You can specify one of the following: or the default .
+  `application/json` — standard JSON format
+  `application/x-amzn-ion` — the Amazon Ion data format. For more information, see [Amazon Ion](http://amzn.github.io/ion-docs/).
Required: Yes

 ** [profileToken](#API_PostAgentProfile_RequestSyntax) **   <a name="profiler-PostAgentProfile-request-uri-profileToken"></a>
 Amazon CodeGuru Profiler uses this universally unique identifier (UUID) to prevent the accidental submission of duplicate profiling data if there are failures and retries.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w-]+`

 ** [profilingGroupName](#API_PostAgentProfile_RequestSyntax) **   <a name="profiler-PostAgentProfile-request-uri-profilingGroupName"></a>
 The name of the profiling group with the aggregated profile that receives the submitted profiling data.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`
Required: Yes

## Request Body
<a name="API_PostAgentProfile_RequestBody"></a>

The request accepts the following binary data.

 ** [agentProfile](#API_PostAgentProfile_RequestSyntax) **   <a name="profiler-PostAgentProfile-request-agentProfile"></a>
 The submitted profiling data.
Required: Yes

## Response Syntax
<a name="API_PostAgentProfile_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_PostAgentProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_PostAgentProfile_Errors"></a>

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
<a name="API_PostAgentProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/PostAgentProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/PostAgentProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/PostAgentProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/PostAgentProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/PostAgentProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/PostAgentProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/PostAgentProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/PostAgentProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/PostAgentProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/PostAgentProfile)
