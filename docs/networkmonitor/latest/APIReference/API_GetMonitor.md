---
source_url: https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_GetMonitor.html
---

# GetMonitor
<a name="API_GetMonitor"></a>

Returns details about a specific monitor.

This action requires the `monitorName` parameter. Run `ListMonitors` to get a list of monitor names.

## Request Syntax
<a name="API_GetMonitor_RequestSyntax"></a>

```
GET /monitors/{{monitorName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMonitor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [monitorName](#API_GetMonitor_RequestSyntax) **   <a name="networksyntheticmonitor-GetMonitor-request-uri-monitorName"></a>
The name of the monitor that details are returned for.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_GetMonitor_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMonitor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "aggregationPeriod": number,
   "createdAt": number,
   "modifiedAt": number,
   "monitorArn": "string",
   "monitorName": "string",
   "probes": [
      {
         "addressFamily": "string",
         "createdAt": number,
         "destination": "string",
         "destinationPort": number,
         "modifiedAt": number,
         "packetSize": number,
         "probeArn": "string",
         "probeId": "string",
         "protocol": "string",
         "sourceArn": "string",
         "state": "string",
         "tags": {
            "string" : "string"
         },
         "vpcId": "string"
      }
   ],
   "state": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aggregationPeriod](#API_GetMonitor_ResponseSyntax) **   <a name="networksyntheticmonitor-GetMonitor-response-aggregationPeriod"></a>
The aggregation period for the specified monitor.
Type: Long
Valid Range: Minimum value of 30.

 ** [createdAt](#API_GetMonitor_ResponseSyntax) **   <a name="networksyntheticmonitor-GetMonitor-response-createdAt"></a>
The time and date when the monitor was created.
Type: Timestamp

 ** [modifiedAt](#API_GetMonitor_ResponseSyntax) **   <a name="networksyntheticmonitor-GetMonitor-response-modifiedAt"></a>
The time and date when the monitor was last modified.
Type: Timestamp

 ** [monitorArn](#API_GetMonitor_ResponseSyntax) **   <a name="networksyntheticmonitor-GetMonitor-response-monitorArn"></a>
The ARN of the selected monitor.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 512.
Pattern: `arn:.*`

 ** [monitorName](#API_GetMonitor_ResponseSyntax) **   <a name="networksyntheticmonitor-GetMonitor-response-monitorName"></a>
The name of the monitor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9_-]+`

 ** [probes](#API_GetMonitor_ResponseSyntax) **   <a name="networksyntheticmonitor-GetMonitor-response-probes"></a>
The details about each probe associated with that monitor.
Type: Array of [Probe](API_Probe.md) objects

 ** [state](#API_GetMonitor_ResponseSyntax) **   <a name="networksyntheticmonitor-GetMonitor-response-state"></a>
Lists the status of the `state` of each monitor.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR | DELETING`

 ** [tags](#API_GetMonitor_ResponseSyntax) **   <a name="networksyntheticmonitor-GetMonitor-response-tags"></a>
The list of key-value pairs assigned to the monitor.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_GetMonitor_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling
HTTP Status Code: 429

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_GetMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmonitor-2023-08-01/GetMonitor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmonitor-2023-08-01/GetMonitor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmonitor-2023-08-01/GetMonitor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmonitor-2023-08-01/GetMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmonitor-2023-08-01/GetMonitor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmonitor-2023-08-01/GetMonitor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmonitor-2023-08-01/GetMonitor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmonitor-2023-08-01/GetMonitor)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmonitor-2023-08-01/GetMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmonitor-2023-08-01/GetMonitor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Network Synthetic Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmonitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
