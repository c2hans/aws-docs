---
source_url: https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_DeleteProbe.html
---

# DeleteProbe
<a name="API_DeleteProbe"></a>

Deletes the specified probe. Once a probe is deleted you'll no longer incur any billing fees for that probe.

This action requires both the `monitorName` and `probeId` parameters. Run `ListMonitors` to get a list of monitor names. Run `GetMonitor` to get a list of probes and probe IDs. You can only delete a single probe at a time using this action.

## Request Syntax
<a name="API_DeleteProbe_RequestSyntax"></a>

```
DELETE /monitors/{{monitorName}}/probes/{{probeId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteProbe_RequestParameters"></a>

The request uses the following URI parameters.

 ** [monitorName](#API_DeleteProbe_RequestSyntax) **   <a name="networksyntheticmonitor-DeleteProbe-request-uri-monitorName"></a>
The name of the monitor to delete.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [probeId](#API_DeleteProbe_RequestSyntax) **   <a name="networksyntheticmonitor-DeleteProbe-request-uri-probeId"></a>
The ID of the probe to delete.
Pattern: `probe-[a-z0-9A-Z-]{21,64}`
Required: Yes

## Request Body
<a name="API_DeleteProbe_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteProbe_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteProbe_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteProbe_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
This request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling
HTTP Status Code: 429

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteProbe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmonitor-2023-08-01/DeleteProbe)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmonitor-2023-08-01/DeleteProbe)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmonitor-2023-08-01/DeleteProbe)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmonitor-2023-08-01/DeleteProbe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmonitor-2023-08-01/DeleteProbe)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmonitor-2023-08-01/DeleteProbe)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmonitor-2023-08-01/DeleteProbe)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmonitor-2023-08-01/DeleteProbe)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmonitor-2023-08-01/DeleteProbe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmonitor-2023-08-01/DeleteProbe)
