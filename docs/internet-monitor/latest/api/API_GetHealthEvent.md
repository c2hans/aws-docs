---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetHealthEvent.html
---

# GetHealthEvent
<a name="API_GetHealthEvent"></a>

Gets information that Internet Monitor has created and stored about a health event for a specified monitor. This information includes the impacted locations, and all the information related to the event, by location.

The information returned includes the impact on performance, availability, and round-trip time, information about the network providers (ASNs), the event type, and so on.

Information rolled up at the global traffic level is also returned, including the impact type and total traffic impact.

## Request Syntax
<a name="API_GetHealthEvent_RequestSyntax"></a>

```
GET /v20210603/Monitors/{{MonitorName}}/HealthEvents/{{EventId}}?LinkedAccountId={{LinkedAccountId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetHealthEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EventId](#API_GetHealthEvent_RequestSyntax) **   <a name="internetmonitor-GetHealthEvent-request-uri-EventId"></a>
The internally-generated identifier of a health event. Because `EventID` contains the forward slash (“/”) character, you must URL-encode the `EventID` field in the request URL.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9/_.-]+`
Required: Yes

 ** [LinkedAccountId](#API_GetHealthEvent_RequestSyntax) **   <a name="internetmonitor-GetHealthEvent-request-uri-LinkedAccountId"></a>
The account ID for an account that you've set up cross-account sharing for in Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see [Internet Monitor cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html) in the Internet Monitor User Guide.
Length Constraints: Fixed length of 12.

 ** [MonitorName](#API_GetHealthEvent_RequestSyntax) **   <a name="internetmonitor-GetHealthEvent-request-uri-MonitorName"></a>
The name of the monitor.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Request Body
<a name="API_GetHealthEvent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetHealthEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_GetHealthEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_GetHealthEvent_ResponseSyntax) **   <a name="internetmonitor-GetHealthEvent-response-CreatedAt"></a>
The time when a health event was created.
Type: Timestamp

 ** [EndedAt](#API_GetHealthEvent_ResponseSyntax) **   <a name="internetmonitor-GetHealthEvent-response-EndedAt"></a>
The time when a health event was resolved. If the health event is still active, the end time is not set.
Type: Timestamp

 ** [EventArn](#API_GetHealthEvent_ResponseSyntax) **   <a name="internetmonitor-GetHealthEvent-response-EventArn"></a>
The Amazon Resource Name (ARN) of the event.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`

 ** [EventId](#API_GetHealthEvent_ResponseSyntax) **   <a name="internetmonitor-GetHealthEvent-response-EventId"></a>
The internally-generated identifier of a health event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9/_.-]+`

 ** [HealthScoreThreshold](#API_GetHealthEvent_ResponseSyntax) **   <a name="internetmonitor-GetHealthEvent-response-HealthScoreThreshold"></a>
The threshold percentage for a health score that determines, along with other configuration information, when Internet Monitor creates a health event when there's an internet issue that affects your application end users.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.

 ** [ImpactedLocations](#API_GetHealthEvent_ResponseSyntax) **   <a name="internetmonitor-GetHealthEvent-response-ImpactedLocations"></a>
The locations affected by a health event.
Type: Array of [ImpactedLocation](API_ImpactedLocation.md) objects

 ** [ImpactType](#API_GetHealthEvent_ResponseSyntax) **   <a name="internetmonitor-GetHealthEvent-response-ImpactType"></a>
The type of impairment of a specific health event.
Type: String
Valid Values: `AVAILABILITY | PERFORMANCE | LOCAL_AVAILABILITY | LOCAL_PERFORMANCE`

 ** [LastUpdatedAt](#API_GetHealthEvent_ResponseSyntax) **   <a name="internetmonitor-GetHealthEvent-response-LastUpdatedAt"></a>
The time when a health event was last updated or recalculated.
Type: Timestamp

 ** [PercentOfTotalTrafficImpacted](#API_GetHealthEvent_ResponseSyntax) **   <a name="internetmonitor-GetHealthEvent-response-PercentOfTotalTrafficImpacted"></a>
The impact on total traffic that a health event has, in increased latency or reduced availability. This is the percentage of how much latency has increased or availability has decreased during the event, compared to what is typical for traffic from this client location to the AWS location using this client network.
Type: Double

 ** [StartedAt](#API_GetHealthEvent_ResponseSyntax) **   <a name="internetmonitor-GetHealthEvent-response-StartedAt"></a>
The time when a health event started.
Type: Timestamp

 ** [Status](#API_GetHealthEvent_ResponseSyntax) **   <a name="internetmonitor-GetHealthEvent-response-Status"></a>
The status of a health event.
Type: String
Valid Values: `ACTIVE | RESOLVED`

## Errors
<a name="API_GetHealthEvent_Errors"></a>

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
<a name="API_GetHealthEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/internetmonitor-2021-06-03/GetHealthEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/internetmonitor-2021-06-03/GetHealthEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/GetHealthEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/internetmonitor-2021-06-03/GetHealthEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/GetHealthEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/internetmonitor-2021-06-03/GetHealthEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/internetmonitor-2021-06-03/GetHealthEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/internetmonitor-2021-06-03/GetHealthEvent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/internetmonitor-2021-06-03/GetHealthEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/GetHealthEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Internet Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query internet-monitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
