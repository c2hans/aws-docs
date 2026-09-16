---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_ListMonitors.html
---

# ListMonitors
<a name="API_ListMonitors"></a>

Lists all of your monitors for Internet Monitor and their statuses, along with the Amazon Resource Name (ARN) and name of each monitor.

## Request Syntax
<a name="API_ListMonitors_RequestSyntax"></a>

```
GET /v20210603/Monitors?IncludeLinkedAccounts={{IncludeLinkedAccounts}}&MaxResults={{MaxResults}}&MonitorStatus={{MonitorStatus}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMonitors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IncludeLinkedAccounts](#API_ListMonitors_RequestSyntax) **   <a name="internetmonitor-ListMonitors-request-uri-IncludeLinkedAccounts"></a>
A boolean option that you can set to `TRUE` to include monitors for linked accounts in a list of monitors, when you've set up cross-account sharing in Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see [Internet Monitor cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html) in the Internet Monitor User Guide.

 ** [MaxResults](#API_ListMonitors_RequestSyntax) **   <a name="internetmonitor-ListMonitors-request-uri-MaxResults"></a>
The number of monitor objects that you want to return with this call.
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [MonitorStatus](#API_ListMonitors_RequestSyntax) **   <a name="internetmonitor-ListMonitors-request-uri-MonitorStatus"></a>
The status of a monitor. This includes the status of the data processing for the monitor and the status of the monitor itself.
For information about the statuses for a monitor, see [ Monitor](https://docs.aws.amazon.com/internet-monitor/latest/api/API_Monitor.html).

 ** [NextToken](#API_ListMonitors_RequestSyntax) **   <a name="internetmonitor-ListMonitors-request-uri-NextToken"></a>
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
   "Monitors": [
      {
         "MonitorArn": "string",
         "MonitorName": "string",
         "ProcessingStatus": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMonitors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Monitors](#API_ListMonitors_ResponseSyntax) **   <a name="internetmonitor-ListMonitors-response-Monitors"></a>
A list of monitors.
Type: Array of [Monitor](API_Monitor.md) objects

 ** [NextToken](#API_ListMonitors_ResponseSyntax) **   <a name="internetmonitor-ListMonitors-response-NextToken"></a>
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
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/internetmonitor-2021-06-03/ListMonitors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/internetmonitor-2021-06-03/ListMonitors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/ListMonitors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/internetmonitor-2021-06-03/ListMonitors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/ListMonitors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/internetmonitor-2021-06-03/ListMonitors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/internetmonitor-2021-06-03/ListMonitors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/internetmonitor-2021-06-03/ListMonitors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/internetmonitor-2021-06-03/ListMonitors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/ListMonitors)
