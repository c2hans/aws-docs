---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_DeleteMonitor.html
---

# DeleteMonitor
<a name="API_DeleteMonitor"></a>

Deletes a monitor in Internet Monitor.

## Request Syntax
<a name="API_DeleteMonitor_RequestSyntax"></a>

```
DELETE /v20210603/Monitors/{{MonitorName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteMonitor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MonitorName](#API_DeleteMonitor_RequestSyntax) **   <a name="internetmonitor-DeleteMonitor-request-uri-MonitorName"></a>
The name of the monitor to delete.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Request Body
<a name="API_DeleteMonitor_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteMonitor_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteMonitor_Errors"></a>

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
<a name="API_DeleteMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/internetmonitor-2021-06-03/DeleteMonitor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/internetmonitor-2021-06-03/DeleteMonitor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/DeleteMonitor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/internetmonitor-2021-06-03/DeleteMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/DeleteMonitor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/internetmonitor-2021-06-03/DeleteMonitor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/internetmonitor-2021-06-03/DeleteMonitor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/internetmonitor-2021-06-03/DeleteMonitor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/internetmonitor-2021-06-03/DeleteMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/DeleteMonitor)
