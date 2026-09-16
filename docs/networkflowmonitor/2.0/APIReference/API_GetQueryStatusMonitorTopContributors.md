---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryStatusMonitorTopContributors.html
---

# GetQueryStatusMonitorTopContributors
<a name="API_GetQueryStatusMonitorTopContributors"></a>

Returns the current status of a query for the Network Flow Monitor query interface, for a specified query ID and monitor. This call returns the query status for the top contributors for a monitor.

When you create a query, use this call to check the status of the query to make sure that it has has `SUCCEEDED` before you review the results. Use the same query ID that you used for the corresponding API call to start (create) the query, `StartQueryMonitorTopContributors`.

When you run a query, use this call to check the status of the query to make sure that the query has `SUCCEEDED` before you review the results.

## Request Syntax
<a name="API_GetQueryStatusMonitorTopContributors_RequestSyntax"></a>

```
GET /monitors/{{monitorName}}/topContributorsQueries/{{queryId}}/status HTTP/1.1
```

## URI Request Parameters
<a name="API_GetQueryStatusMonitorTopContributors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [monitorName](#API_GetQueryStatusMonitorTopContributors_RequestSyntax) **   <a name="networkflowmonitor-GetQueryStatusMonitorTopContributors-request-uri-monitorName"></a>
The name of the monitor.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [queryId](#API_GetQueryStatusMonitorTopContributors_RequestSyntax) **   <a name="networkflowmonitor-GetQueryStatusMonitorTopContributors-request-uri-queryId"></a>
The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.
Required: Yes

## Request Body
<a name="API_GetQueryStatusMonitorTopContributors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetQueryStatusMonitorTopContributors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string"
}
```

## Response Elements
<a name="API_GetQueryStatusMonitorTopContributors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_GetQueryStatusMonitorTopContributors_ResponseSyntax) **   <a name="networkflowmonitor-GetQueryStatusMonitorTopContributors-response-status"></a>
When you run a query, use this call to check the status of the query to make sure that the query has `SUCCEEDED` before you review the results.
+  `QUEUED`: The query is scheduled to run.
+  `RUNNING`: The query is in progress but not complete.
+  `SUCCEEDED`: The query completed sucessfully.
+  `FAILED`: The query failed due to an error.
+  `CANCELED`: The query was canceled.
Type: String
Valid Values: `QUEUED | RUNNING | SUCCEEDED | FAILED | CANCELED`

## Errors
<a name="API_GetQueryStatusMonitorTopContributors_Errors"></a>

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
<a name="API_GetQueryStatusMonitorTopContributors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/GetQueryStatusMonitorTopContributors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/GetQueryStatusMonitorTopContributors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/GetQueryStatusMonitorTopContributors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/GetQueryStatusMonitorTopContributors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/GetQueryStatusMonitorTopContributors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/GetQueryStatusMonitorTopContributors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/GetQueryStatusMonitorTopContributors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/GetQueryStatusMonitorTopContributors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/GetQueryStatusMonitorTopContributors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/GetQueryStatusMonitorTopContributors)
