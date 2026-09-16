---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryMonitorTopContributors.html
---

# StopQueryMonitorTopContributors
<a name="API_StopQueryMonitorTopContributors"></a>

Stop a top contributors query for a monitor. Specify the query that you want to stop by providing a query ID and a monitor name.

Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable call for the top contributors that you want to be returned.

## Request Syntax
<a name="API_StopQueryMonitorTopContributors_RequestSyntax"></a>

```
DELETE /monitors/{{monitorName}}/topContributorsQueries/{{queryId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_StopQueryMonitorTopContributors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [monitorName](#API_StopQueryMonitorTopContributors_RequestSyntax) **   <a name="networkflowmonitor-StopQueryMonitorTopContributors-request-uri-monitorName"></a>
The name of the monitor.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [queryId](#API_StopQueryMonitorTopContributors_RequestSyntax) **   <a name="networkflowmonitor-StopQueryMonitorTopContributors-request-uri-queryId"></a>
The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to create a query.
Required: Yes

## Request Body
<a name="API_StopQueryMonitorTopContributors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StopQueryMonitorTopContributors_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StopQueryMonitorTopContributors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopQueryMonitorTopContributors_Errors"></a>

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
<a name="API_StopQueryMonitorTopContributors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/StopQueryMonitorTopContributors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/StopQueryMonitorTopContributors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/StopQueryMonitorTopContributors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/StopQueryMonitorTopContributors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/StopQueryMonitorTopContributors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/StopQueryMonitorTopContributors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/StopQueryMonitorTopContributors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/StopQueryMonitorTopContributors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/StopQueryMonitorTopContributors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/StopQueryMonitorTopContributors)
