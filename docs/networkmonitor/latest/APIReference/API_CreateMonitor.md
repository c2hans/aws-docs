---
source_url: https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_CreateMonitor.html
---

# CreateMonitor
<a name="API_CreateMonitor"></a>

Creates a monitor between a source subnet and destination IP address. Within a monitor, you create one or more probes. The probes monitor network traffic between your source VPC subnets in AWS and your destination IP addresses. Each probe aggregates metrics, and then sends them to Network Synthetic Monitor.

You can also use this command to create a monitor that includes probes. For each probe, you must define the following:
+  `source`—The subnet IDs where the probes will be created.
+  `destination`—The target destination IP address for the probe.
+  `destinationPort`—Required only if the protocol is `TCP`.
+  `protocol`—The communication protocol between the source and destination. This will be either `TCP` or `ICMP`.
+  `packetSize`—The size of the packets. This must be a number between `56` and `8500`.
+ (Optional) `tags`—Key-value pairs created and assigned to the probe.

## Request Syntax
<a name="API_CreateMonitor_RequestSyntax"></a>

```
POST /monitors HTTP/1.1
Content-type: application/json

{
   "aggregationPeriod": {{number}},
   "clientToken": "{{string}}",
   "monitorName": "{{string}}",
   "probes": [
      {
         "destination": "{{string}}",
         "destinationPort": {{number}},
         "packetSize": {{number}},
         "probeTags": {
            "{{string}}" : "{{string}}"
         },
         "protocol": "{{string}}",
         "sourceArn": "{{string}}"
      }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateMonitor_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMonitor_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [aggregationPeriod](#API_CreateMonitor_RequestSyntax) **   <a name="networksyntheticmonitor-CreateMonitor-request-aggregationPeriod"></a>
The period of time, in seconds, over which metrics are aggregated and sent to Network Synthetic Monitor. Valid values are `30` and `60`. The value `60` is the default, if no period is specified.
Type: Long
Valid Range: Minimum value of 30.
Required: No

 ** [clientToken](#API_CreateMonitor_RequestSyntax) **   <a name="networksyntheticmonitor-CreateMonitor-request-clientToken"></a>
A unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.
Type: String
Required: No

 ** [monitorName](#API_CreateMonitor_RequestSyntax) **   <a name="networksyntheticmonitor-CreateMonitor-request-monitorName"></a>
The name that identifies the monitor. A monitor name must contain only letters, underscores (\_), or dashes (-), and include up to 200 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [probes](#API_CreateMonitor_RequestSyntax) **   <a name="networksyntheticmonitor-CreateMonitor-request-probes"></a>
Displays a list of all of the probes created for a monitor.
Type: Array of [CreateMonitorProbeInput](API_CreateMonitorProbeInput.md) objects
Required: No

 ** [tags](#API_CreateMonitor_RequestSyntax) **   <a name="networksyntheticmonitor-CreateMonitor-request-tags"></a>
The list of key-value pair tags created and assigned to the monitor.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateMonitor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "aggregationPeriod": number,
   "monitorArn": "string",
   "monitorName": "string",
   "state": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aggregationPeriod](#API_CreateMonitor_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateMonitor-response-aggregationPeriod"></a>
The period of time, in seconds, over which metrics are aggregated and sent to Network Synthetic Monitor. Valid values are `30` and `60`.
Type: Long
Valid Range: Minimum value of 30.

 ** [monitorArn](#API_CreateMonitor_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateMonitor-response-monitorArn"></a>
The ARN of the monitor.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 512.
Pattern: `arn:.*`

 ** [monitorName](#API_CreateMonitor_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateMonitor-response-monitorName"></a>
The name of the monitor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9_-]+`

 ** [state](#API_CreateMonitor_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateMonitor-response-state"></a>
The state of the monitor.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR | DELETING`

 ** [tags](#API_CreateMonitor_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateMonitor-response-tags"></a>
The list of key-value pair tags assigned to the monitor.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateMonitor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
This operation attempted to create a resource that already exists.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

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
<a name="API_CreateMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmonitor-2023-08-01/CreateMonitor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmonitor-2023-08-01/CreateMonitor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmonitor-2023-08-01/CreateMonitor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmonitor-2023-08-01/CreateMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmonitor-2023-08-01/CreateMonitor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmonitor-2023-08-01/CreateMonitor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmonitor-2023-08-01/CreateMonitor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmonitor-2023-08-01/CreateMonitor)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmonitor-2023-08-01/CreateMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmonitor-2023-08-01/CreateMonitor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Network Synthetic Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmonitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
