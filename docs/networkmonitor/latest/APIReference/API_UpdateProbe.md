---
source_url: https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_UpdateProbe.html
---

# UpdateProbe
<a name="API_UpdateProbe"></a>

Updates a monitor probe. This action requires both the `monitorName` and `probeId` parameters. Run `ListMonitors` to get a list of monitor names. Run `GetMonitor` to get a list of probes and probe IDs.

You can update the following para create a monitor with probes using this command. For each probe, you define the following:
+  `state`—The state of the probe.
+  `destination`— The target destination IP address for the probe.
+  `destinationPort`—Required only if the protocol is `TCP`.
+  `protocol`—The communication protocol between the source and destination. This will be either `TCP` or `ICMP`.
+  `packetSize`—The size of the packets. This must be a number between `56` and `8500`.
+ (Optional) `tags` —Key-value pairs created and assigned to the probe.

## Request Syntax
<a name="API_UpdateProbe_RequestSyntax"></a>

```
PATCH /monitors/{{monitorName}}/probes/{{probeId}} HTTP/1.1
Content-type: application/json

{
   "destination": "{{string}}",
   "destinationPort": {{number}},
   "packetSize": {{number}},
   "protocol": "{{string}}",
   "state": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateProbe_RequestParameters"></a>

The request uses the following URI parameters.

 ** [monitorName](#API_UpdateProbe_RequestSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-request-uri-monitorName"></a>
The name of the monitor that the probe was updated for.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [probeId](#API_UpdateProbe_RequestSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-request-uri-probeId"></a>
The ID of the probe to update.
Pattern: `probe-[a-z0-9A-Z-]{21,64}`
Required: Yes

## Request Body
<a name="API_UpdateProbe_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [destination](#API_UpdateProbe_RequestSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-request-destination"></a>
The updated IP address for the probe destination. This must be either an IPv4 or IPv6 address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [destinationPort](#API_UpdateProbe_RequestSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-request-destinationPort"></a>
The updated port for the probe destination. This is required only if the `protocol` is `TCP` and must be a number between `1` and `65536`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65536.
Required: No

 ** [packetSize](#API_UpdateProbe_RequestSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-request-packetSize"></a>
he updated packets size for network traffic between the source and destination. This must be a number between `56` and `8500`.
Type: Integer
Valid Range: Minimum value of 56. Maximum value of 8500.
Required: No

 ** [protocol](#API_UpdateProbe_RequestSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-request-protocol"></a>
The updated network protocol for the destination. This can be either `TCP` or `ICMP`. If the protocol is `TCP`, then `port` is also required.
Type: String
Valid Values: `TCP | ICMP`
Required: No

 ** [state](#API_UpdateProbe_RequestSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-request-state"></a>
The state of the probe update.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR | DELETING | DELETED`
Required: No

## Response Syntax
<a name="API_UpdateProbe_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_UpdateProbe_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [addressFamily](#API_UpdateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-response-addressFamily"></a>
The updated IP address family. This must be either `IPV4` or `IPV6`.
Type: String
Valid Values: `IPV4 | IPV6`

 ** [createdAt](#API_UpdateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-response-createdAt"></a>
The time and date that the probe was created.
Type: Timestamp

 ** [destination](#API_UpdateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-response-destination"></a>
The updated destination IP address for the probe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [destinationPort](#API_UpdateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-response-destinationPort"></a>
The updated destination port. This must be a number between `1` and `65536`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65536.

 ** [modifiedAt](#API_UpdateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-response-modifiedAt"></a>
The time and date that the probe was last updated.
Type: Timestamp

 ** [packetSize](#API_UpdateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-response-packetSize"></a>
The updated packet size for the probe.
Type: Integer
Valid Range: Minimum value of 56. Maximum value of 8500.

 ** [probeArn](#API_UpdateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-response-probeArn"></a>
The updated ARN of the probe.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`

 ** [probeId](#API_UpdateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-response-probeId"></a>
The updated ID of the probe.
Type: String
Pattern: `probe-[a-z0-9A-Z-]{21,64}`

 ** [protocol](#API_UpdateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-response-protocol"></a>
The updated protocol for the probe.
Type: String
Valid Values: `TCP | ICMP`

 ** [sourceArn](#API_UpdateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-response-sourceArn"></a>
The updated ARN of the source subnet.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`

 ** [state](#API_UpdateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-response-state"></a>
The state of the updated probe.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR | DELETING | DELETED`

 ** [tags](#API_UpdateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-response-tags"></a>
Update tags for a probe.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [vpcId](#API_UpdateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-UpdateProbe-response-vpcId"></a>
The updated ID of the source VPC subnet ID.
Type: String
Pattern: `vpc-[a-zA-Z0-9]{8,32}`

## Errors
<a name="API_UpdateProbe_Errors"></a>

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
<a name="API_UpdateProbe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmonitor-2023-08-01/UpdateProbe)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmonitor-2023-08-01/UpdateProbe)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmonitor-2023-08-01/UpdateProbe)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmonitor-2023-08-01/UpdateProbe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmonitor-2023-08-01/UpdateProbe)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmonitor-2023-08-01/UpdateProbe)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmonitor-2023-08-01/UpdateProbe)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmonitor-2023-08-01/UpdateProbe)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmonitor-2023-08-01/UpdateProbe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmonitor-2023-08-01/UpdateProbe)
