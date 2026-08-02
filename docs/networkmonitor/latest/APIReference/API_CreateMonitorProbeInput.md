---
source_url: https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_CreateMonitorProbeInput.html
---

# CreateMonitorProbeInput
<a name="API_CreateMonitorProbeInput"></a>

Creates a monitor probe.

## Contents
<a name="API_CreateMonitorProbeInput_Contents"></a>

 ** destination **   <a name="networksyntheticmonitor-Type-CreateMonitorProbeInput-destination"></a>
The destination IP address. This must be either `IPV4` or `IPV6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** protocol **   <a name="networksyntheticmonitor-Type-CreateMonitorProbeInput-protocol"></a>
The protocol used for the network traffic between the `source` and `destination`. This must be either `TCP` or `ICMP`.
Type: String
Valid Values: `TCP | ICMP`
Required: Yes

 ** sourceArn **   <a name="networksyntheticmonitor-Type-CreateMonitorProbeInput-sourceArn"></a>
The ARN of the subnet.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** destinationPort **   <a name="networksyntheticmonitor-Type-CreateMonitorProbeInput-destinationPort"></a>
The port associated with the `destination`. This is required only if the `protocol` is `TCP` and must be a number between `1` and `65536`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65536.
Required: No

 ** packetSize **   <a name="networksyntheticmonitor-Type-CreateMonitorProbeInput-packetSize"></a>
The size of the packets sent between the source and destination. This must be a number between `56` and `8500`.
Type: Integer
Valid Range: Minimum value of 56. Maximum value of 8500.
Required: No

 ** probeTags **   <a name="networksyntheticmonitor-Type-CreateMonitorProbeInput-probeTags"></a>
The list of key-value pairs created and assigned to the monitor.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_CreateMonitorProbeInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmonitor-2023-08-01/CreateMonitorProbeInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmonitor-2023-08-01/CreateMonitorProbeInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmonitor-2023-08-01/CreateMonitorProbeInput)
