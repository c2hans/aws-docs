---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListInternetEvents.html
---

# ListInternetEvents
<a name="API_ListInternetEvents"></a>

Lists internet events that cause performance or availability issues for client locations. Internet Monitor displays information about recent global health events, called internet events, on a global outages map that is available to all AWS customers.

You can constrain the list of internet events returned by providing a start time and end time to define a total time frame for events you want to list. Both start time and end time specify the time when an event started. End time is optional. If you don't include it, the default end time is the current time.

You can also limit the events returned to a specific status (`ACTIVE` or `RESOLVED`) or type (`PERFORMANCE` or `AVAILABILITY`).

## Request Syntax
<a name="API_ListInternetEvents_RequestSyntax"></a>

```
GET /v20210603/InternetEvents?EndTime={{EndTime}}&EventStatus={{EventStatus}}&EventType={{EventType}}&InternetEventMaxResults={{MaxResults}}&NextToken={{NextToken}}&StartTime={{StartTime}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListInternetEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EndTime](#API_ListInternetEvents_RequestSyntax) **   <a name="internetmonitor-ListInternetEvents-request-uri-EndTime"></a>
The end time of the time window that you want to get a list of internet events for.

 ** [EventStatus](#API_ListInternetEvents_RequestSyntax) **   <a name="internetmonitor-ListInternetEvents-request-uri-EventStatus"></a>
The status of an internet event.

 ** [EventType](#API_ListInternetEvents_RequestSyntax) **   <a name="internetmonitor-ListInternetEvents-request-uri-EventType"></a>
The type of network impairment.

 ** [MaxResults](#API_ListInternetEvents_RequestSyntax) **   <a name="internetmonitor-ListInternetEvents-request-uri-MaxResults"></a>
The number of query results that you want to return with this call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListInternetEvents_RequestSyntax) **   <a name="internetmonitor-ListInternetEvents-request-uri-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.

 ** [StartTime](#API_ListInternetEvents_RequestSyntax) **   <a name="internetmonitor-ListInternetEvents-request-uri-StartTime"></a>
The start time of the time window that you want to get a list of internet events for.

## Request Body
<a name="API_ListInternetEvents_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListInternetEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "InternetEvents": [
      {
         "ClientLocation": {
            "ASName": "string",
            "ASNumber": number,
            "City": "string",
            "Country": "string",
            "Latitude": number,
            "Longitude": number,
            "Metro": "string",
            "Subdivision": "string"
         },
         "EndedAt": "string",
         "EventArn": "string",
         "EventId": "string",
         "EventStatus": "string",
         "EventType": "string",
         "StartedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInternetEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InternetEvents](#API_ListInternetEvents_ResponseSyntax) **   <a name="internetmonitor-ListInternetEvents-response-InternetEvents"></a>
A set of internet events returned for the list operation.
Type: Array of [InternetEventSummary](API_InternetEventSummary.md) objects

 ** [NextToken](#API_ListInternetEvents_ResponseSyntax) **   <a name="internetmonitor-ListInternetEvents-response-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.
Type: String

## Errors
<a name="API_ListInternetEvents_Errors"></a>

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
<a name="API_ListInternetEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/internetmonitor-2021-06-03/ListInternetEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/internetmonitor-2021-06-03/ListInternetEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/ListInternetEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/internetmonitor-2021-06-03/ListInternetEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/ListInternetEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/internetmonitor-2021-06-03/ListInternetEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/internetmonitor-2021-06-03/ListInternetEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/internetmonitor-2021-06-03/ListInternetEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/internetmonitor-2021-06-03/ListInternetEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/ListInternetEvents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Internet Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query internet-monitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
