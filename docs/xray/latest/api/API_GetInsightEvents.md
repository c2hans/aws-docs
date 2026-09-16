---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GetInsightEvents.html
---

# GetInsightEvents
<a name="API_GetInsightEvents"></a>

X-Ray reevaluates insights periodically until they're resolved, and records each intermediate state as an event. You can review an insight's events in the Impact Timeline on the Inspect page in the X-Ray console.

## Request Syntax
<a name="API_GetInsightEvents_RequestSyntax"></a>

```
POST /InsightEvents HTTP/1.1
Content-type: application/json

{
   "InsightId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetInsightEvents_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetInsightEvents_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InsightId](#API_GetInsightEvents_RequestSyntax) **   <a name="xray-GetInsightEvents-request-InsightId"></a>
The insight's unique identifier. Use the GetInsightSummaries action to retrieve an InsightId.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`
Required: Yes

 ** [MaxResults](#API_GetInsightEvents_RequestSyntax) **   <a name="xray-GetInsightEvents-request-MaxResults"></a>
Used to retrieve at most the specified value of events.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_GetInsightEvents_RequestSyntax) **   <a name="xray-GetInsightEvents-request-NextToken"></a>
Specify the pagination token returned by a previous request to retrieve the next page of events.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_GetInsightEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "InsightEvents": [
      {
         "ClientRequestImpactStatistics": {
            "FaultCount": number,
            "OkCount": number,
            "TotalCount": number
         },
         "EventTime": number,
         "RootCauseServiceRequestImpactStatistics": {
            "FaultCount": number,
            "OkCount": number,
            "TotalCount": number
         },
         "Summary": "string",
         "TopAnomalousServices": [
            {
               "ServiceId": {
                  "AccountId": "string",
                  "Name": "string",
                  "Names": [ "string" ],
                  "Type": "string"
               }
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetInsightEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InsightEvents](#API_GetInsightEvents_ResponseSyntax) **   <a name="xray-GetInsightEvents-response-InsightEvents"></a>
A detailed description of the event. This includes the time of the event, client and root cause impact statistics, and the top anomalous service at the time of the event.
Type: Array of [InsightEvent](API_InsightEvent.md) objects

 ** [NextToken](#API_GetInsightEvents_ResponseSyntax) **   <a name="xray-GetInsightEvents-response-NextToken"></a>
Use this token to retrieve the next page of insight events.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_GetInsightEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_GetInsightEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/GetInsightEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/GetInsightEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GetInsightEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/GetInsightEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetInsightEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/GetInsightEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/GetInsightEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/GetInsightEvents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/GetInsightEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GetInsightEvents)
