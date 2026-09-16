---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListHealthEvents.html
---

# ListHealthEvents
<a name="API_ListHealthEvents"></a>

Lists all health events for a monitor in Internet Monitor. Returns information for health events including the event start and end times, and the status.

**Note**
Health events that have start times during the time frame that is requested are not included in the list of health events.

## Request Syntax
<a name="API_ListHealthEvents_RequestSyntax"></a>

```
GET /v20210603/Monitors/{{MonitorName}}/HealthEvents?EndTime={{EndTime}}&EventStatus={{EventStatus}}&LinkedAccountId={{LinkedAccountId}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&StartTime={{StartTime}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListHealthEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EndTime](#API_ListHealthEvents_RequestSyntax) **   <a name="internetmonitor-ListHealthEvents-request-uri-EndTime"></a>
The time when a health event ended. If the health event is still ongoing, then the end time is not set.

 ** [EventStatus](#API_ListHealthEvents_RequestSyntax) **   <a name="internetmonitor-ListHealthEvents-request-uri-EventStatus"></a>
The status of a health event.
Valid Values: `ACTIVE | RESOLVED`

 ** [LinkedAccountId](#API_ListHealthEvents_RequestSyntax) **   <a name="internetmonitor-ListHealthEvents-request-uri-LinkedAccountId"></a>
The account ID for an account that you've set up cross-account sharing for in Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see [Internet Monitor cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html) in the Internet Monitor User Guide.
Length Constraints: Fixed length of 12.

 ** [MaxResults](#API_ListHealthEvents_RequestSyntax) **   <a name="internetmonitor-ListHealthEvents-request-uri-MaxResults"></a>
The number of health event objects that you want to return with this call.
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [MonitorName](#API_ListHealthEvents_RequestSyntax) **   <a name="internetmonitor-ListHealthEvents-request-uri-MonitorName"></a>
The name of the monitor.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [NextToken](#API_ListHealthEvents_RequestSyntax) **   <a name="internetmonitor-ListHealthEvents-request-uri-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.

 ** [StartTime](#API_ListHealthEvents_RequestSyntax) **   <a name="internetmonitor-ListHealthEvents-request-uri-StartTime"></a>
The time when a health event started.

## Request Body
<a name="API_ListHealthEvents_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListHealthEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "HealthEvents": [
      {
         "CreatedAt": "string",
         "EndedAt": "string",
         "EventArn": "string",
         "EventId": "string",
         "HealthScoreThreshold": number,
         "ImpactedLocations": [
            {
               "ASName": "string",
               "ASNumber": number,
               "CausedBy": {
                  "AsPath": [
                     {
                        "ASName": "string",
                        "ASNumber": number
                     }
                  ],
                  "NetworkEventType": "string",
                  "Networks": [
                     {
                        "ASName": "string",
                        "ASNumber": number
                     }
                  ]
               },
               "City": "string",
               "Country": "string",
               "CountryCode": "string",
               "InternetHealth": {
                  "Availability": {
                     "ExperienceScore": number,
                     "PercentOfClientLocationImpacted": number,
                     "PercentOfTotalTrafficImpacted": number
                  },
                  "Performance": {
                     "ExperienceScore": number,
                     "PercentOfClientLocationImpacted": number,
                     "PercentOfTotalTrafficImpacted": number,
                     "RoundTripTime": {
                        "P50": number,
                        "P90": number,
                        "P95": number
                     }
                  }
               },
               "Ipv4Prefixes": [ "string" ],
               "Latitude": number,
               "Longitude": number,
               "Metro": "string",
               "ServiceLocation": "string",
               "Status": "string",
               "Subdivision": "string",
               "SubdivisionCode": "string"
            }
         ],
         "ImpactType": "string",
         "LastUpdatedAt": "string",
         "PercentOfTotalTrafficImpacted": number,
         "StartedAt": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListHealthEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HealthEvents](#API_ListHealthEvents_ResponseSyntax) **   <a name="internetmonitor-ListHealthEvents-response-HealthEvents"></a>
A list of health events.
Type: Array of [HealthEvent](API_HealthEvent.md) objects

 ** [NextToken](#API_ListHealthEvents_ResponseSyntax) **   <a name="internetmonitor-ListHealthEvents-response-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.
Type: String

## Errors
<a name="API_ListHealthEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal error occurred.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
Invalid request.
HTTP Status Code: 400

## See Also
<a name="API_ListHealthEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/internetmonitor-2021-06-03/ListHealthEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/internetmonitor-2021-06-03/ListHealthEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/ListHealthEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/internetmonitor-2021-06-03/ListHealthEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/ListHealthEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/internetmonitor-2021-06-03/ListHealthEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/internetmonitor-2021-06-03/ListHealthEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/internetmonitor-2021-06-03/ListHealthEvents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/internetmonitor-2021-06-03/ListHealthEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/ListHealthEvents)
