---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryMonitorTopContributors.html
---

# StartQueryMonitorTopContributors
<a name="API_StartQueryMonitorTopContributors"></a>

Create a query that you can use with the Network Flow Monitor query interface to return the top contributors for a monitor. Specify the monitor that you want to create the query for.

The call returns a query ID that you can use with [ GetQueryResultsMonitorTopContributors](https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorTopContributors.html) to run the query and return the top contributors for a specific monitor.

Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable APIs for the top contributors that you want to be returned.

## Request Syntax
<a name="API_StartQueryMonitorTopContributors_RequestSyntax"></a>

```
POST /monitors/{{monitorName}}/topContributorsQueries HTTP/1.1
Content-type: application/json

{
   "destinationCategory": "{{string}}",
   "endTime": "{{string}}",
   "limit": {{number}},
   "metricName": "{{string}}",
   "startTime": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartQueryMonitorTopContributors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [monitorName](#API_StartQueryMonitorTopContributors_RequestSyntax) **   <a name="networkflowmonitor-StartQueryMonitorTopContributors-request-uri-monitorName"></a>
The name of the monitor.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Request Body
<a name="API_StartQueryMonitorTopContributors_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [destinationCategory](#API_StartQueryMonitorTopContributors_RequestSyntax) **   <a name="networkflowmonitor-StartQueryMonitorTopContributors-request-destinationCategory"></a>
The category that you want to query top contributors for, for a specific monitor. Destination categories can be one of the following:
+  `INTRA_AZ`: Top contributor network flows within a single Availability Zone
+  `INTER_AZ`: Top contributor network flows between Availability Zones
+  `INTER_REGION`: Top contributor network flows between Regions (to the edge of another Region)
+  `INTER_VPC`: Top contributor network flows between VPCs
+  `AMAZON_S3`: Top contributor network flows to or from Amazon S3
+  `AMAZON_DYNAMODB`: Top contributor network flows to or from Amazon Dynamo DB
+  `UNCLASSIFIED`: Top contributor network flows that do not have a bucket classification
Type: String
Valid Values: `INTRA_AZ | INTER_AZ | INTER_VPC | UNCLASSIFIED | AMAZON_S3 | AMAZON_DYNAMODB | INTER_REGION`
Required: Yes

 ** [endTime](#API_StartQueryMonitorTopContributors_RequestSyntax) **   <a name="networkflowmonitor-StartQueryMonitorTopContributors-request-endTime"></a>
The timestamp that is the date and time end of the period that you want to retrieve results for with your query.
Type: Timestamp
Required: Yes

 ** [limit](#API_StartQueryMonitorTopContributors_RequestSyntax) **   <a name="networkflowmonitor-StartQueryMonitorTopContributors-request-limit"></a>
The maximum number of top contributors to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [metricName](#API_StartQueryMonitorTopContributors_RequestSyntax) **   <a name="networkflowmonitor-StartQueryMonitorTopContributors-request-metricName"></a>
The metric that you want to query top contributors for. That is, you can specify a metric with this call and return the top contributor network flows, for that type of metric, for a monitor and (optionally) within a specific category, such as network flows between Availability Zones.
Type: String
Valid Values: `ROUND_TRIP_TIME | TIMEOUTS | RETRANSMISSIONS | DATA_TRANSFERRED`
Required: Yes

 ** [startTime](#API_StartQueryMonitorTopContributors_RequestSyntax) **   <a name="networkflowmonitor-StartQueryMonitorTopContributors-request-startTime"></a>
The timestamp that is the date and time that is the beginning of the period that you want to retrieve results for with your query.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_StartQueryMonitorTopContributors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "queryId": "string"
}
```

## Response Elements
<a name="API_StartQueryMonitorTopContributors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [queryId](#API_StartQueryMonitorTopContributors_ResponseSyntax) **   <a name="networkflowmonitor-StartQueryMonitorTopContributors-response-queryId"></a>
The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.
Type: String

## Errors
<a name="API_StartQueryMonitorTopContributors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal error occurred.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request exceeded a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
Invalid request.
HTTP Status Code: 400

## See Also
<a name="API_StartQueryMonitorTopContributors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/StartQueryMonitorTopContributors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/StartQueryMonitorTopContributors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/StartQueryMonitorTopContributors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/StartQueryMonitorTopContributors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/StartQueryMonitorTopContributors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/StartQueryMonitorTopContributors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/StartQueryMonitorTopContributors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/StartQueryMonitorTopContributors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/StartQueryMonitorTopContributors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/StartQueryMonitorTopContributors)
