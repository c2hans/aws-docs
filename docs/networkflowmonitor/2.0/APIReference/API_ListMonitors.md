---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_ListMonitors.html
---

# ListMonitors
<a name="API_ListMonitors"></a>

List all monitors in an account. Optionally, you can list only monitors that have a specific status, by using the `STATUS` parameter.

## Request Syntax
<a name="API_ListMonitors_RequestSyntax"></a>

```
GET /monitors?maxResults={{maxResults}}&monitorStatus={{monitorStatus}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMonitors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListMonitors_RequestSyntax) **   <a name="networkflowmonitor-ListMonitors-request-uri-maxResults"></a>
The number of query results that you want to return with this call.
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [monitorStatus](#API_ListMonitors_RequestSyntax) **   <a name="networkflowmonitor-ListMonitors-request-uri-monitorStatus"></a>
The status of a monitor. The status can be one of the following
+  `PENDING`: The monitor is in the process of being created.
+  `ACTIVE`: The monitor is active.
+  `INACTIVE`: The monitor is inactive.
+  `ERROR`: Monitor creation failed due to an error.
+  `DELETING`: The monitor is in the process of being deleted.
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR | DELETING`

 ** [nextToken](#API_ListMonitors_RequestSyntax) **   <a name="networkflowmonitor-ListMonitors-request-uri-nextToken"></a>
The token for the next set of results. You receive this token from a previous call.

## Request Body
<a name="API_ListMonitors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMonitors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "monitors": [
      {
         "monitorArn": "string",
         "monitorName": "string",
         "monitorStatus": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMonitors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [monitors](#API_ListMonitors_ResponseSyntax) **   <a name="networkflowmonitor-ListMonitors-response-monitors"></a>
The monitors that are in an account.
Type: Array of [MonitorSummary](API_MonitorSummary.md) objects

 ** [nextToken](#API_ListMonitors_ResponseSyntax) **   <a name="networkflowmonitor-ListMonitors-response-nextToken"></a>
The token for the next set of results. You receive this token from a previous call.
Type: String

## Errors
<a name="API_ListMonitors_Errors"></a>

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
<a name="API_ListMonitors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/ListMonitors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/ListMonitors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/ListMonitors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/ListMonitors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/ListMonitors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/ListMonitors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/ListMonitors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/ListMonitors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/ListMonitors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/ListMonitors)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Network Flow Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkflowmonitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
