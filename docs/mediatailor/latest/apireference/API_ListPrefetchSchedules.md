---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListPrefetchSchedules.html
---

# ListPrefetchSchedules
<a name="API_ListPrefetchSchedules"></a>

Lists the prefetch schedules for a playback configuration.

## Request Syntax
<a name="API_ListPrefetchSchedules_RequestSyntax"></a>

```
POST /prefetchSchedule/{{PlaybackConfigurationName}} HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ScheduleType": "{{string}}",
   "StreamId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListPrefetchSchedules_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PlaybackConfigurationName](#API_ListPrefetchSchedules_RequestSyntax) **   <a name="mediatailor-ListPrefetchSchedules-request-uri-PlaybackConfigurationName"></a>
Retrieves the prefetch schedule(s) for a specific playback configuration.
Required: Yes

## Request Body
<a name="API_ListPrefetchSchedules_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListPrefetchSchedules_RequestSyntax) **   <a name="mediatailor-ListPrefetchSchedules-request-MaxResults"></a>
The maximum number of prefetch schedules that you want MediaTailor to return in response to the current request. If there are more than `MaxResults` prefetch schedules, use the value of `NextToken` in the response to get the next page of results.
The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than `MaxResults` items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the `NextToken` value from each response until the response no longer includes a `NextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListPrefetchSchedules_RequestSyntax) **   <a name="mediatailor-ListPrefetchSchedules-request-NextToken"></a>
Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
For the first `ListPrefetchSchedules` request, omit this value. For subsequent requests, get the value of `NextToken` from the previous response and specify that value for `NextToken` in the request. Continue making requests until the response no longer includes a `NextToken` value, which indicates that all results have been retrieved.
Type: String
Required: No

 ** [ScheduleType](#API_ListPrefetchSchedules_RequestSyntax) **   <a name="mediatailor-ListPrefetchSchedules-request-ScheduleType"></a>
The type of prefetch schedules that you want to list. `SINGLE` indicates that you want to list the configured single prefetch schedules. `RECURRING` indicates that you want to list the configured recurring prefetch schedules. `ALL` indicates that you want to list all configured prefetch schedules.
Type: String
Valid Values: `SINGLE | RECURRING | ALL`
Required: No

 ** [StreamId](#API_ListPrefetchSchedules_RequestSyntax) **   <a name="mediatailor-ListPrefetchSchedules-request-StreamId"></a>
An optional filtering parameter whereby MediaTailor filters the prefetch schedules to include only specific streams.
Type: String
Required: No

## Response Syntax
<a name="API_ListPrefetchSchedules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Arn": "string",
         "Consumption": {
            "AvailMatchingCriteria": [
               {
                  "DynamicVariable": "string",
                  "Operator": "string"
               }
            ],
            "EndTime": number,
            "StartTime": number
         },
         "Name": "string",
         "PlaybackConfigurationName": "string",
         "RecurringPrefetchConfiguration": {
            "EndTime": number,
            "RecurringConsumption": {
               "AvailMatchingCriteria": [
                  {
                     "DynamicVariable": "string",
                     "Operator": "string"
                  }
               ],
               "RetrievedAdExpirationSeconds": number
            },
            "RecurringRetrieval": {
               "DelayAfterAvailEndSeconds": number,
               "DynamicVariables": {
                  "string" : "string"
               },
               "TrafficShapingRetrievalWindow": {
                  "RetrievalWindowDurationSeconds": number
               },
               "TrafficShapingTpsConfiguration": {
                  "PeakConcurrentUsers": number,
                  "PeakTps": number
               },
               "TrafficShapingType": "string"
            },
            "StartTime": number
         },
         "Retrieval": {
            "DynamicVariables": {
               "string" : "string"
            },
            "EndTime": number,
            "StartTime": number,
            "TrafficShapingRetrievalWindow": {
               "RetrievalWindowDurationSeconds": number
            },
            "TrafficShapingTpsConfiguration": {
               "PeakConcurrentUsers": number,
               "PeakTps": number
            },
            "TrafficShapingType": "string"
         },
         "ScheduleType": "string",
         "StreamId": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListPrefetchSchedules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListPrefetchSchedules_ResponseSyntax) **   <a name="mediatailor-ListPrefetchSchedules-response-Items"></a>
Lists the prefetch schedules. An empty `Items` list doesn't mean there aren't more items to fetch, just that that page was empty.
Type: Array of [PrefetchSchedule](API_PrefetchSchedule.md) objects

 ** [NextToken](#API_ListPrefetchSchedules_ResponseSyntax) **   <a name="mediatailor-ListPrefetchSchedules-response-NextToken"></a>
Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
Type: String

## Errors
<a name="API_ListPrefetchSchedules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListPrefetchSchedules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/ListPrefetchSchedules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/ListPrefetchSchedules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/ListPrefetchSchedules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/ListPrefetchSchedules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/ListPrefetchSchedules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/ListPrefetchSchedules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/ListPrefetchSchedules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/ListPrefetchSchedules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/ListPrefetchSchedules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/ListPrefetchSchedules)
