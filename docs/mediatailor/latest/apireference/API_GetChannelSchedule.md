---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_GetChannelSchedule.html
---

# GetChannelSchedule
<a name="API_GetChannelSchedule"></a>

Retrieves information about your channel's schedule.

## Request Syntax
<a name="API_GetChannelSchedule_RequestSyntax"></a>

```
GET /channel/{{ChannelName}}/schedule?audience={{Audience}}&durationMinutes={{DurationMinutes}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetChannelSchedule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Audience](#API_GetChannelSchedule_RequestSyntax) **   <a name="mediatailor-GetChannelSchedule-request-uri-Audience"></a>
The single audience for GetChannelScheduleRequest.

 ** [ChannelName](#API_GetChannelSchedule_RequestSyntax) **   <a name="mediatailor-GetChannelSchedule-request-uri-ChannelName"></a>
The name of the channel associated with this Channel Schedule.
Required: Yes

 ** [DurationMinutes](#API_GetChannelSchedule_RequestSyntax) **   <a name="mediatailor-GetChannelSchedule-request-uri-DurationMinutes"></a>
The duration in minutes of the channel schedule.

 ** [MaxResults](#API_GetChannelSchedule_RequestSyntax) **   <a name="mediatailor-GetChannelSchedule-request-uri-MaxResults"></a>
The maximum number of channel schedules that you want MediaTailor to return in response to the current request. If there are more than `MaxResults` channel schedules, use the value of `NextToken` in the response to get the next page of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_GetChannelSchedule_RequestSyntax) **   <a name="mediatailor-GetChannelSchedule-request-uri-NextToken"></a>
(Optional) If the playback configuration has more than `MaxResults` channel schedules, use `NextToken` to get the second and subsequent pages of results.
For the first `GetChannelScheduleRequest` request, omit this value.
For the second and subsequent requests, get the value of `NextToken` from the previous response and specify that value for `NextToken` in the request.
If the previous response didn't include a `NextToken` element, there are no more channel schedules to get.

## Request Body
<a name="API_GetChannelSchedule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetChannelSchedule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "ApproximateDurationSeconds": number,
         "ApproximateStartTime": number,
         "Arn": "string",
         "Audiences": [ "string" ],
         "ChannelName": "string",
         "LiveSourceName": "string",
         "ProgramName": "string",
         "ScheduleAdBreaks": [
            {
               "ApproximateDurationSeconds": number,
               "ApproximateStartTime": number,
               "SourceLocationName": "string",
               "VodSourceName": "string"
            }
         ],
         "ScheduleEntryType": "string",
         "SourceLocationName": "string",
         "VodSourceName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetChannelSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_GetChannelSchedule_ResponseSyntax) **   <a name="mediatailor-GetChannelSchedule-response-Items"></a>
A list of schedule entries for the channel.
Type: Array of [ScheduleEntry](API_ScheduleEntry.md) objects

 ** [NextToken](#API_GetChannelSchedule_ResponseSyntax) **   <a name="mediatailor-GetChannelSchedule-response-NextToken"></a>
Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
Type: String

## Errors
<a name="API_GetChannelSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetChannelSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/GetChannelSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/GetChannelSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/GetChannelSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/GetChannelSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/GetChannelSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/GetChannelSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/GetChannelSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/GetChannelSchedule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/GetChannelSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/GetChannelSchedule)
