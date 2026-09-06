---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributors.html
---

# GetQueryResultsWorkloadInsightsTopContributors
<a name="API_GetQueryResultsWorkloadInsightsTopContributors"></a>

Return the data for a query with the Network Flow Monitor query interface. You specify the query that you want to return results for by providing a query ID and a monitor name.

This query returns the top contributors for a scope for workload insights. Workload insights provide a high level view of network flow performance data collected by agents. To return the data for the top contributors, see `GetQueryResultsWorkloadInsightsTopContributorsData`.

Create a query ID for this call by calling the corresponding API call to start the query, `StartQueryWorkloadInsightsTopContributors`. Use the scope ID that was returned for your account by `CreateScope`.

Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable call for the top contributors that you want to be returned.

## Request Syntax
<a name="API_GetQueryResultsWorkloadInsightsTopContributors_RequestSyntax"></a>

```
GET /workloadInsights/{{scopeId}}/topContributorsQueries/{{queryId}}/results?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetQueryResultsWorkloadInsightsTopContributors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_GetQueryResultsWorkloadInsightsTopContributors_RequestSyntax) **   <a name="networkflowmonitor-GetQueryResultsWorkloadInsightsTopContributors-request-uri-maxResults"></a>
The number of query results that you want to return with this call.

 ** [nextToken](#API_GetQueryResultsWorkloadInsightsTopContributors_RequestSyntax) **   <a name="networkflowmonitor-GetQueryResultsWorkloadInsightsTopContributors-request-uri-nextToken"></a>
The token for the next set of results. You receive this token from a previous call.

 ** [queryId](#API_GetQueryResultsWorkloadInsightsTopContributors_RequestSyntax) **   <a name="networkflowmonitor-GetQueryResultsWorkloadInsightsTopContributors-request-uri-queryId"></a>
The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to create a query.
Required: Yes

 ** [scopeId](#API_GetQueryResultsWorkloadInsightsTopContributors_RequestSyntax) **   <a name="networkflowmonitor-GetQueryResultsWorkloadInsightsTopContributors-request-uri-scopeId"></a>
The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.
Required: Yes

## Request Body
<a name="API_GetQueryResultsWorkloadInsightsTopContributors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetQueryResultsWorkloadInsightsTopContributors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "topContributors": [
      {
         "accountId": "string",
         "localAz": "string",
         "localRegion": "string",
         "localSubnetArn": "string",
         "localSubnetId": "string",
         "localVpcArn": "string",
         "localVpcId": "string",
         "remoteIdentifier": "string",
         "value": number
      }
   ]
}
```

## Response Elements
<a name="API_GetQueryResultsWorkloadInsightsTopContributors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetQueryResultsWorkloadInsightsTopContributors_ResponseSyntax) **   <a name="networkflowmonitor-GetQueryResultsWorkloadInsightsTopContributors-response-nextToken"></a>
The token for the next set of results. You receive this token from a previous call.
Type: String

 ** [topContributors](#API_GetQueryResultsWorkloadInsightsTopContributors_ResponseSyntax) **   <a name="networkflowmonitor-GetQueryResultsWorkloadInsightsTopContributors-response-topContributors"></a>
The top contributor network flows overall for a specific metric type, for example, the number of retransmissions.
Type: Array of [WorkloadInsightsTopContributorsRow](API_WorkloadInsightsTopContributorsRow.md) objects

## Errors
<a name="API_GetQueryResultsWorkloadInsightsTopContributors_Errors"></a>

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
<a name="API_GetQueryResultsWorkloadInsightsTopContributors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/GetQueryResultsWorkloadInsightsTopContributors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/GetQueryResultsWorkloadInsightsTopContributors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/GetQueryResultsWorkloadInsightsTopContributors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/GetQueryResultsWorkloadInsightsTopContributors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/GetQueryResultsWorkloadInsightsTopContributors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/GetQueryResultsWorkloadInsightsTopContributors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/GetQueryResultsWorkloadInsightsTopContributors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/GetQueryResultsWorkloadInsightsTopContributors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/GetQueryResultsWorkloadInsightsTopContributors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/GetQueryResultsWorkloadInsightsTopContributors)
