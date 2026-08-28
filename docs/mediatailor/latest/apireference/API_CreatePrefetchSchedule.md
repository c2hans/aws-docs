---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_CreatePrefetchSchedule.html
---

# CreatePrefetchSchedule
<a name="API_CreatePrefetchSchedule"></a>

Creates a prefetch schedule for a playback configuration. A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens. For more information about ad prefetching, see [Using ad prefetching](https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html) in the *MediaTailor User Guide*.

## Request Syntax
<a name="API_CreatePrefetchSchedule_RequestSyntax"></a>

```
POST /prefetchSchedule/{{PlaybackConfigurationName}}/{{Name}} HTTP/1.1
Content-type: application/json

{
   "Consumption": {
      "AvailMatchingCriteria": [
         {
            "DynamicVariable": "{{string}}",
            "Operator": "{{string}}"
         }
      ],
      "EndTime": {{number}},
      "StartTime": {{number}}
   },
   "RecurringPrefetchConfiguration": {
      "EndTime": {{number}},
      "RecurringConsumption": {
         "AvailMatchingCriteria": [
            {
               "DynamicVariable": "{{string}}",
               "Operator": "{{string}}"
            }
         ],
         "RetrievedAdExpirationSeconds": {{number}}
      },
      "RecurringRetrieval": {
         "DelayAfterAvailEndSeconds": {{number}},
         "DynamicVariables": {
            "{{string}}" : "{{string}}"
         },
         "TrafficShapingRetrievalWindow": {
            "RetrievalWindowDurationSeconds": {{number}}
         },
         "TrafficShapingTpsConfiguration": {
            "PeakConcurrentUsers": {{number}},
            "PeakTps": {{number}}
         },
         "TrafficShapingType": "{{string}}"
      },
      "StartTime": {{number}}
   },
   "Retrieval": {
      "DynamicVariables": {
         "{{string}}" : "{{string}}"
      },
      "EndTime": {{number}},
      "StartTime": {{number}},
      "TrafficShapingRetrievalWindow": {
         "RetrievalWindowDurationSeconds": {{number}}
      },
      "TrafficShapingTpsConfiguration": {
         "PeakConcurrentUsers": {{number}},
         "PeakTps": {{number}}
      },
      "TrafficShapingType": "{{string}}"
   },
   "ScheduleType": "{{string}}",
   "StreamId": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreatePrefetchSchedule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_CreatePrefetchSchedule_RequestSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-request-uri-Name"></a>
The name to assign to the schedule request.
Required: Yes

 ** [PlaybackConfigurationName](#API_CreatePrefetchSchedule_RequestSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-request-uri-PlaybackConfigurationName"></a>
The name to assign to the playback configuration.
Required: Yes

## Request Body
<a name="API_CreatePrefetchSchedule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Consumption](#API_CreatePrefetchSchedule_RequestSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-request-Consumption"></a>
The configuration settings for how and when MediaTailor consumes prefetched ads from the ad decision server for single prefetch schedules. Each consumption configuration contains an end time and an optional start time that define the *consumption window*. Prefetch schedules automatically expire no earlier than seven days after the end time.
Type: [PrefetchConsumption](API_PrefetchConsumption.md) object
Required: No

 ** [RecurringPrefetchConfiguration](#API_CreatePrefetchSchedule_RequestSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-request-RecurringPrefetchConfiguration"></a>
The configuration that defines how and when MediaTailor performs ad prefetching in a live event.
Type: [RecurringPrefetchConfiguration](API_RecurringPrefetchConfiguration.md) object
Required: No

 ** [Retrieval](#API_CreatePrefetchSchedule_RequestSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-request-Retrieval"></a>
The configuration settings for retrieval of prefetched ads from the ad decision server. Only one set of prefetched ads will be retrieved and subsequently consumed for each ad break.
Type: [PrefetchRetrieval](API_PrefetchRetrieval.md) object
Required: No

 ** [ScheduleType](#API_CreatePrefetchSchedule_RequestSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-request-ScheduleType"></a>
The frequency that MediaTailor creates prefetch schedules. `SINGLE` indicates that this schedule applies to one ad break. `RECURRING` indicates that MediaTailor automatically creates a schedule for each ad avail in a live event.
For more information about the prefetch types and when you might use each, see [Prefetching ads in AWS Elemental MediaTailor.](https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html)
Type: String
Valid Values: `SINGLE | RECURRING`
Required: No

 ** [StreamId](#API_CreatePrefetchSchedule_RequestSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-request-StreamId"></a>
An optional stream identifier that MediaTailor uses to prefetch ads for multiple streams that use the same playback configuration. If `StreamId` is specified, MediaTailor returns all of the prefetch schedules with an exact match on `StreamId`. If not specified, MediaTailor returns all of the prefetch schedules for the playback configuration, regardless of `StreamId`.
Type: String
Required: No

 ** [tags](#API_CreatePrefetchSchedule_RequestSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-request-tags"></a>
The tags to assign to the prefetch schedule. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreatePrefetchSchedule_ResponseSyntax"></a>

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
<a name="API_CreatePrefetchSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreatePrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-response-Arn"></a>
The ARN to assign to the prefetch schedule.
Type: String

 ** [Consumption](#API_CreatePrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-response-Consumption"></a>
The configuration settings for how and when MediaTailor consumes prefetched ads from the ad decision server for single prefetch schedules. Each consumption configuration contains an end time and an optional start time that define the *consumption window*. Prefetch schedules automatically expire no earlier than seven days after the end time.
Type: [PrefetchConsumption](API_PrefetchConsumption.md) object

 ** [Name](#API_CreatePrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-response-Name"></a>
The name to assign to the prefetch schedule.
Type: String

 ** [PlaybackConfigurationName](#API_CreatePrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-response-PlaybackConfigurationName"></a>
The name to assign to the playback configuration.
Type: String

 ** [RecurringPrefetchConfiguration](#API_CreatePrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-response-RecurringPrefetchConfiguration"></a>
The configuration that defines how MediaTailor performs recurring prefetch.
Type: [RecurringPrefetchConfiguration](API_RecurringPrefetchConfiguration.md) object

 ** [Retrieval](#API_CreatePrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-response-Retrieval"></a>
The configuration settings for retrieval of prefetched ads from the ad decision server. Only one set of prefetched ads will be retrieved and subsequently consumed for each ad break.
Type: [PrefetchRetrieval](API_PrefetchRetrieval.md) object

 ** [ScheduleType](#API_CreatePrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-response-ScheduleType"></a>
The frequency that MediaTailor creates prefetch schedules. `SINGLE` indicates that this schedule applies to one ad break. `RECURRING` indicates that MediaTailor automatically creates a schedule for each ad avail in a live event.
Type: String
Valid Values: `SINGLE | RECURRING`

 ** [StreamId](#API_CreatePrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-response-StreamId"></a>
An optional stream identifier that MediaTailor uses to prefetch ads for multiple streams that use the same playback configuration. If `StreamId` is specified, MediaTailor returns all of the prefetch schedules with an exact match on `StreamId`. If not specified, MediaTailor returns all of the prefetch schedules for the playback configuration, regardless of `StreamId`.
Type: String

 ** [tags](#API_CreatePrefetchSchedule_ResponseSyntax) **   <a name="mediatailor-CreatePrefetchSchedule-response-tags"></a>
The tags assigned to the prefetch schedule. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map

## Errors
<a name="API_CreatePrefetchSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreatePrefetchSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/CreatePrefetchSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/CreatePrefetchSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/CreatePrefetchSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/CreatePrefetchSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/CreatePrefetchSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/CreatePrefetchSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/CreatePrefetchSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/CreatePrefetchSchedule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/CreatePrefetchSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/CreatePrefetchSchedule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
