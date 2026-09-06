---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_SubmitFeedback.html
---

# SubmitFeedback
<a name="API_SubmitFeedback"></a>

Sends feedback to CodeGuru Profiler about whether the anomaly detected by the analysis is useful or not.

## Request Syntax
<a name="API_SubmitFeedback_RequestSyntax"></a>

```
POST /internal/profilingGroups/{{profilingGroupName}}/anomalies/{{anomalyInstanceId}}/feedback HTTP/1.1
Content-type: application/json

{
   "comment": "{{string}}",
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SubmitFeedback_RequestParameters"></a>

The request uses the following URI parameters.

 ** [anomalyInstanceId](#API_SubmitFeedback_RequestSyntax) **   <a name="profiler-SubmitFeedback-request-uri-anomalyInstanceId"></a>
The universally unique identifier (UUID) of the [`AnomalyInstance`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AnomalyInstance.html) object that is included in the analysis data.
Pattern: `.*[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}.*`
Required: Yes

 ** [profilingGroupName](#API_SubmitFeedback_RequestSyntax) **   <a name="profiler-SubmitFeedback-request-uri-profilingGroupName"></a>
The name of the profiling group that is associated with the analysis data.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`
Required: Yes

## Request Body
<a name="API_SubmitFeedback_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [comment](#API_SubmitFeedback_RequestSyntax) **   <a name="profiler-SubmitFeedback-request-comment"></a>
Optional feedback about this anomaly.
Type: String
Required: No

 ** [type](#API_SubmitFeedback_RequestSyntax) **   <a name="profiler-SubmitFeedback-request-type"></a>
 The feedback tpye. Thee are two valid values, `Positive` and `Negative`.
Type: String
Valid Values: `Positive | Negative`
Required: Yes

## Response Syntax
<a name="API_SubmitFeedback_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_SubmitFeedback_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_SubmitFeedback_Errors"></a>

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
<a name="API_SubmitFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/SubmitFeedback)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/SubmitFeedback)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/SubmitFeedback)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/SubmitFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/SubmitFeedback)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/SubmitFeedback)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/SubmitFeedback)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/SubmitFeedback)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/SubmitFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/SubmitFeedback)
