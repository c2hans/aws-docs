---
source_url: https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_CreateProbe.html
---

# CreateProbe
<a name="API_CreateProbe"></a>

Create a probe within a monitor. After you create a probe and it begins monitoring your network traffic, you will incur billing charges for that probe. This action requires the `monitorName` parameter. Run `ListMonitors` to get a list of monitor names, and note the name of the `monitorName` you want to create the probe for.

## Request Syntax
<a name="API_CreateProbe_RequestSyntax"></a>

```
POST /monitors/{{monitorName}}/probes HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "probe": {
      "destination": "{{string}}",
      "destinationPort": {{number}},
      "packetSize": {{number}},
      "protocol": "{{string}}",
      "sourceArn": "{{string}}",
      "tags": {
         "{{string}}" : "{{string}}"
      }
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateProbe_RequestParameters"></a>

The request uses the following URI parameters.

 ** [monitorName](#API_CreateProbe_RequestSyntax) **   <a name="networksyntheticmonitor-CreateProbe-request-uri-monitorName"></a>
The name of the monitor to associated with the probe.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_CreateProbe_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateProbe_RequestSyntax) **   <a name="networksyntheticmonitor-CreateProbe-request-clientToken"></a>
A unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.
Type: String
Required: No

 ** [probe](#API_CreateProbe_RequestSyntax) **   <a name="networksyntheticmonitor-CreateProbe-request-probe"></a>
Describes the details of an individual probe for a monitor.
Type: [ProbeInput](API_ProbeInput.md) object
Required: Yes

 ** [tags](#API_CreateProbe_RequestSyntax) **   <a name="networksyntheticmonitor-CreateProbe-request-tags"></a>
The list of key-value pairs created and assigned to the probe.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateProbe_ResponseSyntax"></a>

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
<a name="API_CreateProbe_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [addressFamily](#API_CreateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateProbe-response-addressFamily"></a>
Indicates whether the IP address is `IPV4` or `IPV6`.
Type: String
Valid Values: `IPV4 | IPV6`

 ** [createdAt](#API_CreateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateProbe-response-createdAt"></a>
The time and date that the probe was created.
Type: Timestamp

 ** [destination](#API_CreateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateProbe-response-destination"></a>
The destination IP address for the monitor. This must be either an IPv4 or IPv6 address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [destinationPort](#API_CreateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateProbe-response-destinationPort"></a>
The port associated with the `destination`. This is required only if the `protocol` is `TCP` and must be a number between `1` and `65536`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65536.

 ** [modifiedAt](#API_CreateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateProbe-response-modifiedAt"></a>
The time and date when the probe was last modified.
Type: Timestamp

 ** [packetSize](#API_CreateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateProbe-response-packetSize"></a>
The size of the packets sent between the source and destination. This must be a number between `56` and `8500`.
Type: Integer
Valid Range: Minimum value of 56. Maximum value of 8500.

 ** [probeArn](#API_CreateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateProbe-response-probeArn"></a>
The ARN of the probe.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`

 ** [probeId](#API_CreateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateProbe-response-probeId"></a>
The ID of the probe for which details are returned.
Type: String
Pattern: `probe-[a-z0-9A-Z-]{21,64}`

 ** [protocol](#API_CreateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateProbe-response-protocol"></a>
The protocol used for the network traffic between the `source` and `destination`. This must be either `TCP` or `ICMP`.
Type: String
Valid Values: `TCP | ICMP`

 ** [sourceArn](#API_CreateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateProbe-response-sourceArn"></a>
The ARN of the probe.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`

 ** [state](#API_CreateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateProbe-response-state"></a>
The state of the probe.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR | DELETING | DELETED`

 ** [tags](#API_CreateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateProbe-response-tags"></a>
The list of key-value pairs assigned to the probe.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [vpcId](#API_CreateProbe_ResponseSyntax) **   <a name="networksyntheticmonitor-CreateProbe-response-vpcId"></a>
The ID of the source VPC or subnet.
Type: String
Pattern: `vpc-[a-zA-Z0-9]{8,32}`

## Errors
<a name="API_CreateProbe_Errors"></a>

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
<a name="API_CreateProbe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmonitor-2023-08-01/CreateProbe)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmonitor-2023-08-01/CreateProbe)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmonitor-2023-08-01/CreateProbe)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmonitor-2023-08-01/CreateProbe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmonitor-2023-08-01/CreateProbe)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmonitor-2023-08-01/CreateProbe)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmonitor-2023-08-01/CreateProbe)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmonitor-2023-08-01/CreateProbe)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmonitor-2023-08-01/CreateProbe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmonitor-2023-08-01/CreateProbe)
