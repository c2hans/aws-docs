---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorTopContributors.html
---

# GetQueryResultsMonitorTopContributors
<a name="API_GetQueryResultsMonitorTopContributors"></a>

Return the data for a query with the Network Flow Monitor query interface. You specify the query that you want to return results for by providing a query ID and a monitor name. This query returns the top contributors for a specific monitor.

Create a query ID for this call by calling the corresponding API call to start the query, `StartQueryMonitorTopContributors`. Use the scope ID that was returned for your account by `CreateScope`.

Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable call for the top contributors that you want to be returned.

## Request Syntax
<a name="API_GetQueryResultsMonitorTopContributors_RequestSyntax"></a>

```
GET /monitors/{{monitorName}}/topContributorsQueries/{{queryId}}/results?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetQueryResultsMonitorTopContributors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_GetQueryResultsMonitorTopContributors_RequestSyntax) **   <a name="networkflowmonitor-GetQueryResultsMonitorTopContributors-request-uri-maxResults"></a>
The number of query results that you want to return with this call.

 ** [monitorName](#API_GetQueryResultsMonitorTopContributors_RequestSyntax) **   <a name="networkflowmonitor-GetQueryResultsMonitorTopContributors-request-uri-monitorName"></a>
The name of the monitor.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [nextToken](#API_GetQueryResultsMonitorTopContributors_RequestSyntax) **   <a name="networkflowmonitor-GetQueryResultsMonitorTopContributors-request-uri-nextToken"></a>
The token for the next set of results. You receive this token from a previous call.

 ** [queryId](#API_GetQueryResultsMonitorTopContributors_RequestSyntax) **   <a name="networkflowmonitor-GetQueryResultsMonitorTopContributors-request-uri-queryId"></a>
The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to create a query.
Required: Yes

## Request Body
<a name="API_GetQueryResultsMonitorTopContributors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetQueryResultsMonitorTopContributors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "topContributors": [
      {
         "destinationCategory": "string",
         "dnatIp": "string",
         "kubernetesMetadata": {
            "localPodName": "string",
            "localPodNamespace": "string",
            "localServiceName": "string",
            "remotePodName": "string",
            "remotePodNamespace": "string",
            "remoteServiceName": "string"
         },
         "localAz": "string",
         "localInstanceArn": "string",
         "localInstanceId": "string",
         "localIp": "string",
         "localRegion": "string",
         "localSubnetArn": "string",
         "localSubnetId": "string",
         "localVpcArn": "string",
         "localVpcId": "string",
         "remoteAz": "string",
         "remoteInstanceArn": "string",
         "remoteInstanceId": "string",
         "remoteIp": "string",
         "remoteRegion": "string",
         "remoteSubnetArn": "string",
         "remoteSubnetId": "string",
         "remoteVpcArn": "string",
         "remoteVpcId": "string",
         "snatIp": "string",
         "targetPort": number,
         "traversedConstructs": [
            {
               "componentArn": "string",
               "componentId": "string",
               "componentType": "string",
               "serviceName": "string"
            }
         ],
         "value": number
      }
   ],
   "unit": "string"
}
```

## Response Elements
<a name="API_GetQueryResultsMonitorTopContributors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetQueryResultsMonitorTopContributors_ResponseSyntax) **   <a name="networkflowmonitor-GetQueryResultsMonitorTopContributors-response-nextToken"></a>
The token for the next set of results. You receive this token from a previous call.
Type: String

 ** [topContributors](#API_GetQueryResultsMonitorTopContributors_ResponseSyntax) **   <a name="networkflowmonitor-GetQueryResultsMonitorTopContributors-response-topContributors"></a>
The top contributor network flows overall for a specific metric type, for example, the number of retransmissions.
Type: Array of [MonitorTopContributorsRow](API_MonitorTopContributorsRow.md) objects

 ** [unit](#API_GetQueryResultsMonitorTopContributors_ResponseSyntax) **   <a name="networkflowmonitor-GetQueryResultsMonitorTopContributors-response-unit"></a>
The units for a metric returned by the query.
Type: String
Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`

## Errors
<a name="API_GetQueryResultsMonitorTopContributors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request specifies a resource that doesn't exist.
HTTP Status Code: 404

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
<a name="API_GetQueryResultsMonitorTopContributors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/GetQueryResultsMonitorTopContributors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/GetQueryResultsMonitorTopContributors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/GetQueryResultsMonitorTopContributors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/GetQueryResultsMonitorTopContributors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/GetQueryResultsMonitorTopContributors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/GetQueryResultsMonitorTopContributors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/GetQueryResultsMonitorTopContributors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/GetQueryResultsMonitorTopContributors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/GetQueryResultsMonitorTopContributors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/GetQueryResultsMonitorTopContributors)
