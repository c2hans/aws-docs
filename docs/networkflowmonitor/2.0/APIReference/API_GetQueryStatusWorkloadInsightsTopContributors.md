---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusWorkloadInsightsTopContributors.html
---

# GetQueryStatusWorkloadInsightsTopContributors
<a name="API_GetQueryStatusWorkloadInsightsTopContributors"></a>

Return the data for a query with the Network Flow Monitor query interface. Specify the query that you want to return results for by providing a query ID and a monitor name. This query returns the top contributors for workload insights.

When you start a query, use this call to check the status of the query to make sure that it has has `SUCCEEDED` before you review the results. Use the same query ID that you used for the corresponding API call to start the query, `StartQueryWorkloadInsightsTopContributors`.

Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable call for the top contributors that you want to be returned.

## Request Syntax
<a name="API_GetQueryStatusWorkloadInsightsTopContributors_RequestSyntax"></a>

```
GET /workloadInsights/{{scopeId}}/topContributorsQueries/{{queryId}}/status HTTP/1.1
```

## URI Request Parameters
<a name="API_GetQueryStatusWorkloadInsightsTopContributors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [queryId](#API_GetQueryStatusWorkloadInsightsTopContributors_RequestSyntax) **   <a name="networkflowmonitor-GetQueryStatusWorkloadInsightsTopContributors-request-uri-queryId"></a>
The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.
Required: Yes

 ** [scopeId](#API_GetQueryStatusWorkloadInsightsTopContributors_RequestSyntax) **   <a name="networkflowmonitor-GetQueryStatusWorkloadInsightsTopContributors-request-uri-scopeId"></a>
The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.
Required: Yes

## Request Body
<a name="API_GetQueryStatusWorkloadInsightsTopContributors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetQueryStatusWorkloadInsightsTopContributors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string"
}
```

## Response Elements
<a name="API_GetQueryStatusWorkloadInsightsTopContributors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_GetQueryStatusWorkloadInsightsTopContributors_ResponseSyntax) **   <a name="networkflowmonitor-GetQueryStatusWorkloadInsightsTopContributors-response-status"></a>
When you run a query, use this call to check the status of the query to make sure that the query has `SUCCEEDED` before you review the results.
+  `QUEUED`: The query is scheduled to run.
+  `RUNNING`: The query is in progress but not complete.
+  `SUCCEEDED`: The query completed sucessfully.
+  `FAILED`: The query failed due to an error.
+  `CANCELED`: The query was canceled.
Type: String
Valid Values: `QUEUED | RUNNING | SUCCEEDED | FAILED | CANCELED`

## Errors
<a name="API_GetQueryStatusWorkloadInsightsTopContributors_Errors"></a>

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
<a name="API_GetQueryStatusWorkloadInsightsTopContributors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/GetQueryStatusWorkloadInsightsTopContributors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/GetQueryStatusWorkloadInsightsTopContributors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/GetQueryStatusWorkloadInsightsTopContributors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/GetQueryStatusWorkloadInsightsTopContributors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/GetQueryStatusWorkloadInsightsTopContributors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/GetQueryStatusWorkloadInsightsTopContributors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/GetQueryStatusWorkloadInsightsTopContributors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/GetQueryStatusWorkloadInsightsTopContributors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/GetQueryStatusWorkloadInsightsTopContributors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/GetQueryStatusWorkloadInsightsTopContributors)
