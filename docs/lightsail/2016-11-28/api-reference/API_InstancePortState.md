---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_InstancePortState.html
---

# InstancePortState
<a name="API_InstancePortState"></a>

Describes open ports on an instance, the IP addresses allowed to connect to the instance through the ports, and the protocol.

## Contents
<a name="API_InstancePortState_Contents"></a>

 ** cidrListAliases **   <a name="Lightsail-Type-InstancePortState-cidrListAliases"></a>
An alias that defines access for a preconfigured range of IP addresses.
The only alias currently supported is `lightsail-connect`, which allows IP addresses of the browser-based RDP/SSH client in the Lightsail console to connect to your instance.
Type: Array of strings
Required: No

 ** cidrs **   <a name="Lightsail-Type-InstancePortState-cidrs"></a>
The IPv4 address, or range of IPv4 addresses (in CIDR notation) that are allowed to connect to an instance through the ports, and the protocol.
The `ipv6Cidrs` parameter lists the IPv6 addresses that are allowed to connect to an instance.
For more information about CIDR block notation, see [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation) on *Wikipedia*.
Type: Array of strings
Required: No

 ** fromPort **   <a name="Lightsail-Type-InstancePortState-fromPort"></a>
The first port in a range of open ports on an instance.
Allowed ports:
+ TCP and UDP - `0` to `65535`
+ ICMP - The ICMP type for IPv4 addresses. For example, specify `8` as the `fromPort` (ICMP type), and `-1` as the `toPort` (ICMP code), to enable ICMP Ping. For more information, see [Control Messages](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Control_messages) on *Wikipedia*.
+ ICMPv6 - The ICMP type for IPv6 addresses. For example, specify `128` as the `fromPort` (ICMPv6 type), and `0` as `toPort` (ICMPv6 code). For more information, see [Internet Control Message Protocol for IPv6](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol_for_IPv6).
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 65535.
Required: No

 ** ipv6Cidrs **   <a name="Lightsail-Type-InstancePortState-ipv6Cidrs"></a>
The IPv6 address, or range of IPv6 addresses (in CIDR notation) that are allowed to connect to an instance through the ports, and the protocol. Only devices with an IPv6 address can connect to an instance through IPv6; otherwise, IPv4 should be used.
The `cidrs` parameter lists the IPv4 addresses that are allowed to connect to an instance.
For more information about CIDR block notation, see [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation) on *Wikipedia*.
Type: Array of strings
Required: No

 ** protocol **   <a name="Lightsail-Type-InstancePortState-protocol"></a>
The IP protocol name.
The name can be one of the following:
+  `tcp` - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn't require reliable data stream service, use UDP instead.
+  `all` - All transport layer protocol types. For more general information, see [Transport layer](https://en.wikipedia.org/wiki/Transport_layer) on *Wikipedia*.
+  `udp` - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don't require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.
+  `icmp` - Internet Control Message Protocol (ICMP) is used to send error messages and operational information indicating success or failure when communicating with an instance. For example, an error is indicated when an instance could not be reached. When you specify `icmp` as the `protocol`, you must specify the ICMP type using the `fromPort` parameter, and ICMP code using the `toPort` parameter.
+  `icmp6` - Internet Control Message Protocol (ICMP) for IPv6. When you specify `icmp6` as the `protocol`, you must specify the ICMP type using the `fromPort` parameter, and ICMP code using the `toPort` parameter.
Type: String
Valid Values: `tcp | all | udp | icmp | icmpv6`
Required: No

 ** state **   <a name="Lightsail-Type-InstancePortState-state"></a>
Specifies whether the instance port is `open` or `closed`.
The port state for Lightsail instances is always `open`.
Type: String
Valid Values: `open | closed`
Required: No

 ** toPort **   <a name="Lightsail-Type-InstancePortState-toPort"></a>
The last port in a range of open ports on an instance.
Allowed ports:
+ TCP and UDP - `0` to `65535`
+ ICMP - The ICMP code for IPv4 addresses. For example, specify `8` as the `fromPort` (ICMP type), and `-1` as the `toPort` (ICMP code), to enable ICMP Ping. For more information, see [Control Messages](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Control_messages) on *Wikipedia*.
+ ICMPv6 - The ICMP code for IPv6 addresses. For example, specify `128` as the `fromPort` (ICMPv6 type), and `0` as `toPort` (ICMPv6 code). For more information, see [Internet Control Message Protocol for IPv6](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol_for_IPv6).
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 65535.
Required: No

## See Also
<a name="API_InstancePortState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/InstancePortState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/InstancePortState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/InstancePortState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
