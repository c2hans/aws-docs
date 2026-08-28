---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetInternetEvent.html
---

# GetInternetEvent
<a name="API_GetInternetEvent"></a>

Gets information that Internet Monitor has generated about an internet event. Internet Monitor displays information about recent global health events, called internet events, on a global outages map that is available to all AWS customers.

The information returned here includes the impacted location, when the event started and (if the event is over) ended, the type of event (`PERFORMANCE` or `AVAILABILITY`), and the status (`ACTIVE` or `RESOLVED`).

## Request Syntax
<a name="API_GetInternetEvent_RequestSyntax"></a>

```
GET /v20210603/InternetEvents/{{EventId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetInternetEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EventId](#API_GetInternetEvent_RequestSyntax) **   <a name="internetmonitor-GetInternetEvent-request-uri-EventId"></a>
The `EventId` of the internet event to return information for.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Request Body
<a name="API_GetInternetEvent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetInternetEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_GetInternetEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClientLocation](#API_GetInternetEvent_ResponseSyntax) **   <a name="internetmonitor-GetInternetEvent-response-ClientLocation"></a>
The impacted location, such as a city, where clients access AWS application resources.
Type: [ClientLocation](API_ClientLocation.md) object

 ** [EndedAt](#API_GetInternetEvent_ResponseSyntax) **   <a name="internetmonitor-GetInternetEvent-response-EndedAt"></a>
The time when the internet event ended. If the event hasn't ended yet, this value is empty.
Type: Timestamp

 ** [EventArn](#API_GetInternetEvent_ResponseSyntax) **   <a name="internetmonitor-GetInternetEvent-response-EventArn"></a>
The Amazon Resource Name (ARN) of the internet event.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`

 ** [EventId](#API_GetInternetEvent_ResponseSyntax) **   <a name="internetmonitor-GetInternetEvent-response-EventId"></a>
The internally-generated identifier of an internet event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`

 ** [EventStatus](#API_GetInternetEvent_ResponseSyntax) **   <a name="internetmonitor-GetInternetEvent-response-EventStatus"></a>
The status of the internet event.
Type: String
Valid Values: `ACTIVE | RESOLVED`

 ** [EventType](#API_GetInternetEvent_ResponseSyntax) **   <a name="internetmonitor-GetInternetEvent-response-EventType"></a>
The type of network impairment.
Type: String
Valid Values: `AVAILABILITY | PERFORMANCE`

 ** [StartedAt](#API_GetInternetEvent_ResponseSyntax) **   <a name="internetmonitor-GetInternetEvent-response-StartedAt"></a>
The time when the internet event started.
Type: Timestamp

## Errors
<a name="API_GetInternetEvent_Errors"></a>

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
<a name="API_GetInternetEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/internetmonitor-2021-06-03/GetInternetEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/internetmonitor-2021-06-03/GetInternetEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/GetInternetEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/internetmonitor-2021-06-03/GetInternetEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/GetInternetEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/internetmonitor-2021-06-03/GetInternetEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/internetmonitor-2021-06-03/GetInternetEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/internetmonitor-2021-06-03/GetInternetEvent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/internetmonitor-2021-06-03/GetInternetEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/GetInternetEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Internet Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query internet-monitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
