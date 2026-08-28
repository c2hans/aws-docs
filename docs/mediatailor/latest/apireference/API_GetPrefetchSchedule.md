---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_GetPrefetchSchedule.html
---

# GetPrefetchSchedule
<a name="API_GetPrefetchSchedule"></a>

Retrieves a prefetch schedule for a playback configuration. A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens. For more information about ad prefetching, see [Using ad prefetching](https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html) in the *MediaTailor User Guide*.

## Request Syntax
<a name="API_GetPrefetchSchedule_RequestSyntax"></a>

```
GET /prefetchSchedule/{{PlaybackConfigurationName}}/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPrefetchSchedule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_GetPrefetchSchedule_RequestSyntax) **   <a name="mediatailor-GetPrefetchSchedule-request-uri-Name"></a>
The name of the prefetch schedule. The name must be unique among all prefetch schedules that are associated with the specified playback configuration.
Required: Yes

 ** [PlaybackConfigurationName](#API_GetPrefetchSchedule_RequestSyntax) **   <a name="mediatailor-GetPrefetchSchedule-request-uri-PlaybackConfigurationName"></a>
Returns information about the prefetch schedule for a specific playback configuration. If you call `GetPrefetchSchedule` on an expired prefetch schedule, MediaTailor returns an HTTP 404 status code.
Required: Yes

## Request Body
<a name="API_GetPrefetchSchedule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPrefetchSchedule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_GetPrefetchSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetPrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-GetPrefetchSchedule-response-Arn"></a>
The Amazon Resource Name (ARN) of the prefetch schedule.
Type: String

 ** [Consumption](#API_GetPrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-GetPrefetchSchedule-response-Consumption"></a>
The configuration settings for how and when MediaTailor consumes prefetched ads from the ad decision server for single prefetch schedules. Each consumption configuration contains an end time and an optional start time that define the *consumption window*. Prefetch schedules automatically expire no earlier than seven days after the end time.
Type: [PrefetchConsumption](API_PrefetchConsumption.md) object

 ** [Name](#API_GetPrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-GetPrefetchSchedule-response-Name"></a>
The name of the prefetch schedule. The name must be unique among all prefetch schedules that are associated with the specified playback configuration.
Type: String

 ** [PlaybackConfigurationName](#API_GetPrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-GetPrefetchSchedule-response-PlaybackConfigurationName"></a>
The name of the playback configuration to create the prefetch schedule for.
Type: String

 ** [RecurringPrefetchConfiguration](#API_GetPrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-GetPrefetchSchedule-response-RecurringPrefetchConfiguration"></a>
The configuration that defines how and when MediaTailor performs ad prefetching in a live event.
Type: [RecurringPrefetchConfiguration](API_RecurringPrefetchConfiguration.md) object

 ** [Retrieval](#API_GetPrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-GetPrefetchSchedule-response-Retrieval"></a>
A complex type that contains settings for prefetch retrieval from the ad decision server (ADS).
Type: [PrefetchRetrieval](API_PrefetchRetrieval.md) object

 ** [ScheduleType](#API_GetPrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-GetPrefetchSchedule-response-ScheduleType"></a>
The frequency that MediaTailor creates prefetch schedules. `SINGLE` indicates that this schedule applies to one ad break. `RECURRING` indicates that MediaTailor automatically creates a schedule for each ad avail in a live event.
Type: String
Valid Values: `SINGLE | RECURRING`

 ** [StreamId](#API_GetPrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-GetPrefetchSchedule-response-StreamId"></a>
An optional stream identifier that you can specify in order to prefetch for multiple streams that use the same playback configuration.
Type: String

 ** [tags](#API_GetPrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-GetPrefetchSchedule-response-tags"></a>
The tags assigned to the prefetch schedule. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

## Errors
<a name="API_GetPrefetchSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetPrefetchSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/GetPrefetchSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/GetPrefetchSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/GetPrefetchSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/GetPrefetchSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/GetPrefetchSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/GetPrefetchSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/GetPrefetchSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/GetPrefetchSchedule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/GetPrefetchSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/GetPrefetchSchedule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
