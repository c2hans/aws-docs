---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetQueryStatus.html
---

# GetQueryStatus
<a name="API_GetQueryStatus"></a>

Returns the current status of a query for the Internet Monitor query interface, for a specified query ID and monitor. When you run a query, check the status to make sure that the query has `SUCCEEDED` before you review the results.
+  `QUEUED`: The query is scheduled to run.
+  `RUNNING`: The query is in progress but not complete.
+  `SUCCEEDED`: The query completed sucessfully.
+  `FAILED`: The query failed due to an error.
+  `CANCELED`: The query was canceled.

## Request Syntax
<a name="API_GetQueryStatus_RequestSyntax"></a>

```
GET /v20210603/Monitors/{{MonitorName}}/Queries/{{QueryId}}/Status HTTP/1.1
```

## URI Request Parameters
<a name="API_GetQueryStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MonitorName](#API_GetQueryStatus_RequestSyntax) **   <a name="internetmonitor-GetQueryStatus-request-uri-MonitorName"></a>
The name of the monitor.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [QueryId](#API_GetQueryStatus_RequestSyntax) **   <a name="internetmonitor-GetQueryStatus-request-uri-QueryId"></a>
The ID of the query that you want to return the status for. A `QueryId` is an internally-generated dentifier for a specific query.
Required: Yes

## Request Body
<a name="API_GetQueryStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetQueryStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Status": "string"
}
```

## Response Elements
<a name="API_GetQueryStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Status](#API_GetQueryStatus_ResponseSyntax) **   <a name="internetmonitor-GetQueryStatus-response-Status"></a>
The current status for a query.
Type: String
Valid Values: `QUEUED | RUNNING | SUCCEEDED | FAILED | CANCELED`

## Errors
<a name="API_GetQueryStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal error occurred.
HTTP Status Code: 500

 ** LimitExceededException **
The request exceeded a service quota.
HTTP Status Code: 403

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
Invalid request.
HTTP Status Code: 400

## See Also
<a name="API_GetQueryStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/internetmonitor-2021-06-03/GetQueryStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/internetmonitor-2021-06-03/GetQueryStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/GetQueryStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/internetmonitor-2021-06-03/GetQueryStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/GetQueryStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/internetmonitor-2021-06-03/GetQueryStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/internetmonitor-2021-06-03/GetQueryStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/internetmonitor-2021-06-03/GetQueryStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/internetmonitor-2021-06-03/GetQueryStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/GetQueryStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Internet Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query internet-monitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
