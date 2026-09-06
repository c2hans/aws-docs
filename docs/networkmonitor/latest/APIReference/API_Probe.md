---
source_url: https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_Probe.html
---

# Probe
<a name="API_Probe"></a>

Describes information about a network monitor probe.

## Contents
<a name="API_Probe_Contents"></a>

 ** destination **   <a name="networksyntheticmonitor-Type-Probe-destination"></a>
The destination for the probe. This should be either an `IPV4` or `IPV6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** protocol **   <a name="networksyntheticmonitor-Type-Probe-protocol"></a>
The network protocol for the destination. This can be either `TCP` or `ICMP`. If the protocol is `TCP`, then `port` is also required.
Type: String
Valid Values: `TCP | ICMP`
Required: Yes

 ** sourceArn **   <a name="networksyntheticmonitor-Type-Probe-sourceArn"></a>
The ARN of the probe source subnet.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** addressFamily **   <a name="networksyntheticmonitor-Type-Probe-addressFamily"></a>
The IPv4 or IPv6 address for the probe.
Type: String
Valid Values: `IPV4 | IPV6`
Required: No

 ** createdAt **   <a name="networksyntheticmonitor-Type-Probe-createdAt"></a>
The time and date the probe was created.
Type: Timestamp
Required: No

 ** destinationPort **   <a name="networksyntheticmonitor-Type-Probe-destinationPort"></a>
The destination port for the probe. This is required only if the `protocol` is `TCP` and must be a number between `1` and `65536`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65536.
Required: No

 ** modifiedAt **   <a name="networksyntheticmonitor-Type-Probe-modifiedAt"></a>
The time and date that the probe was last modified.
Type: Timestamp
Required: No

 ** packetSize **   <a name="networksyntheticmonitor-Type-Probe-packetSize"></a>
The size of the packets traveling between the `source` and `destination`. This must be a number between `56` and
Type: Integer
Valid Range: Minimum value of 56. Maximum value of 8500.
Required: No

 ** probeArn **   <a name="networksyntheticmonitor-Type-Probe-probeArn"></a>
The ARN of the probe.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** probeId **   <a name="networksyntheticmonitor-Type-Probe-probeId"></a>
The ID of the probe.
Type: String
Pattern: `probe-[a-z0-9A-Z-]{21,64}`
Required: No

 ** state **   <a name="networksyntheticmonitor-Type-Probe-state"></a>
The state of the probe.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR | DELETING | DELETED`
Required: No

 ** tags **   <a name="networksyntheticmonitor-Type-Probe-tags"></a>
The list of key-value pairs created and assigned to the probe.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** vpcId **   <a name="networksyntheticmonitor-Type-Probe-vpcId"></a>
The ID of the source VPC subnet.
Type: String
Pattern: `vpc-[a-zA-Z0-9]{8,32}`
Required: No

## See Also
<a name="API_Probe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmonitor-2023-08-01/Probe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmonitor-2023-08-01/Probe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmonitor-2023-08-01/Probe)
