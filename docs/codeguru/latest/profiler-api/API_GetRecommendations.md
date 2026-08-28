---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetRecommendations.html
---

# GetRecommendations
<a name="API_GetRecommendations"></a>

 Returns a list of [`Recommendation`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Recommendation.html) objects that contain recommendations for a profiling group for a given time period. A list of [`Anomaly`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Anomaly.html) objects that contains details about anomalies detected in the profiling group for the same time period is also returned.

## Request Syntax
<a name="API_GetRecommendations_RequestSyntax"></a>

```
GET /internal/profilingGroups/{{profilingGroupName}}/recommendations?endTime={{endTime}}&locale={{locale}}&startTime={{startTime}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRecommendations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endTime](#API_GetRecommendations_RequestSyntax) **   <a name="profiler-GetRecommendations-request-uri-endTime"></a>
 The end time of the profile to get analysis data about. You must specify `startTime` and `endTime`. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Required: Yes

 ** [locale](#API_GetRecommendations_RequestSyntax) **   <a name="profiler-GetRecommendations-request-uri-locale"></a>
 The language used to provide analysis. Specify using a string that is one of the following `BCP 47` language codes.
+  `de-DE` - German, Germany
+  `en-GB` - English, United Kingdom
+  `en-US` - English, United States
+  `es-ES` - Spanish, Spain
+  `fr-FR` - French, France
+  `it-IT` - Italian, Italy
+  `ja-JP` - Japanese, Japan
+  `ko-KR` - Korean, Republic of Korea
+  `pt-BR` - Portugese, Brazil
+  `zh-CN` - Chinese, China
+  `zh-TW` - Chinese, Taiwan

 ** [profilingGroupName](#API_GetRecommendations_RequestSyntax) **   <a name="profiler-GetRecommendations-request-uri-profilingGroupName"></a>
 The name of the profiling group to get analysis data about.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`
Required: Yes

 ** [startTime](#API_GetRecommendations_RequestSyntax) **   <a name="profiler-GetRecommendations-request-uri-startTime"></a>
 The start time of the profile to get analysis data about. You must specify `startTime` and `endTime`. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Required: Yes

## Request Body
<a name="API_GetRecommendations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "anomalies": [
      {
         "instances": [
            {
               "endTime": "string",
               "id": "string",
               "startTime": "string",
               "userFeedback": {
                  "type": "string"
               }
            }
         ],
         "metric": {
            "frameName": "string",
            "threadStates": [ "string" ],
            "type": "string"
         },
         "reason": "string"
      }
   ],
   "profileEndTime": "string",
   "profileStartTime": "string",
   "profilingGroupName": "string",
   "recommendations": [
      {
         "allMatchesCount": number,
         "allMatchesSum": number,
         "endTime": "string",
         "pattern": {
            "countersToAggregate": [ "string" ],
            "description": "string",
            "id": "string",
            "name": "string",
            "resolutionSteps": "string",
            "targetFrames": [
               [ "string" ]
            ],
            "thresholdPercent": number
         },
         "startTime": "string",
         "topMatches": [
            {
               "frameAddress": "string",
               "targetFramesIndex": number,
               "thresholdBreachValue": number
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [anomalies](#API_GetRecommendations_ResponseSyntax) **   <a name="profiler-GetRecommendations-response-anomalies"></a>
 The list of anomalies that the analysis has found for this profile.
Type: Array of [Anomaly](API_Anomaly.md) objects

 ** [profileEndTime](#API_GetRecommendations_ResponseSyntax) **   <a name="profiler-GetRecommendations-response-profileEndTime"></a>
 The end time of the profile the analysis data is about. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp

 ** [profileStartTime](#API_GetRecommendations_ResponseSyntax) **   <a name="profiler-GetRecommendations-response-profileStartTime"></a>
 The start time of the profile the analysis data is about. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp

 ** [profilingGroupName](#API_GetRecommendations_ResponseSyntax) **   <a name="profiler-GetRecommendations-response-profilingGroupName"></a>
The name of the profiling group the analysis data is about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`

 ** [recommendations](#API_GetRecommendations_ResponseSyntax) **   <a name="profiler-GetRecommendations-response-recommendations"></a>
The list of recommendations that the analysis found for this profile.
Type: Array of [Recommendation](API_Recommendation.md) objects

## Errors
<a name="API_GetRecommendations_Errors"></a>

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
<a name="API_GetRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/GetRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/GetRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/GetRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/GetRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/GetRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/GetRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/GetRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/GetRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/GetRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/GetRecommendations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Profiler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
