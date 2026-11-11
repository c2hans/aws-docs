---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_FirewallRule.html
---

# FirewallRule
<a name="API_FirewallRule"></a>

A single structured firewall engine rule, for use in a firewall engine rule group or as an embedded rule in a Next Generation policy. A firewall rule accepts, drops, or rejects traffic at a connection-state hook. For more information about authoring firewall engine rules, see [Rule groups for a firewall using a Next Generation policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-v2.html) in the * AWS Network Firewall Developer Guide*.

## Contents
<a name="API_FirewallRule_Contents"></a>

 ** Action **   <a name="networkfirewall-Type-FirewallRule-Action"></a>
The action that the firewall engine takes on traffic that matches the rule. The firewall engine supports the following actions:
+  `ACCEPT` - Allow the traffic.
+  `DROP` - Block the traffic and discontinue inspection.
+  `REJECT` - Block the traffic and send a TCP reset packet back to the client.
+  `REJECT_DST` - Block the traffic and send a TCP reset packet to the destination.
+  `REJECT_BOTH` - Block the traffic and send a TCP reset packet to both the client and the destination.
You combine the action with an action scope, for example `accept:flow`. To send accepted traffic straight to its destination and skip the IPS engine, pair an accept action with the `BypassIPSEnabled` setting. For more information, see [Rule groups for a firewall using a Next Generation policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-v2.html) in the * AWS Network Firewall Developer Guide*.
Type: String
Valid Values: `ACCEPT | DROP | REJECT | REJECT_DST | REJECT_BOTH`
Required: Yes

 ** ActionScope **   <a name="networkfirewall-Type-FirewallRule-ActionScope"></a>
The scope that controls how much of the matched traffic the action applies to. The valid scopes depend on the action: `ACCEPT` supports all four scopes, and `DROP`, `REJECT`, `REJECT_DST`, and `REJECT_BOTH` support only `PACKET` and `FLOW`.
+  `PACKET` - The current packet only.
+  `HOOK` - The current hook only. The firewall engine evaluates the connection again at the next hook.
+  `TX` - The current transaction. The firewall engine continues to evaluate later transactions on the connection.
+  `FLOW` - The entire connection. For an accept action, the connection skips the firewall engine's remaining hooks and advances to the IPS engine.
In a Suricata-compatible rule string, you write the scope in lowercase, for example `accept:flow`.
Type: String
Valid Values: `FLOW | TX | HOOK | PACKET`
Required: Yes

 ** Hook **   <a name="networkfirewall-Type-FirewallRule-Hook"></a>
The connection-state hook at which the firewall engine evaluates the rule. The hook encodes both the protocol and the connection state, for example a TCP hook or a TLS `client_hello` hook. For the hooks that the firewall engine supports and how they map to the connection lifecycle, see [Rule groups for a firewall using a Next Generation policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-v2.html) in the * AWS Network Firewall Developer Guide* and the [Suricata firewall mode documentation](https://suricata.readthedocs.io/en/suricata-8.0.3/firewall/firewall-design.html).
Type: String
Valid Values: `TCP_ALL | TCP_FLOW_START | TCP_PRE_FLOW | TCP_PRE_STREAM | SCTP_ALL | SCTP_FLOW_START | SCTP_PRE_FLOW | SCTP_PRE_STREAM | IPV6_ALL | IPV6_FLOW_START | IPV6_PRE_FLOW | IPV6_PRE_STREAM | ICMPV6_ALL | ICMPV6_FLOW_START | ICMPV6_PRE_FLOW | ICMPV6_PRE_STREAM | UDP_ALL | UDP_FLOW_START | UDP_PRE_FLOW | UDP_PRE_STREAM | ICMP_ALL | ICMP_FLOW_START | ICMP_PRE_FLOW | ICMP_PRE_STREAM | ICMPV4_ALL | ICMPV4_FLOW_START | ICMPV4_PRE_FLOW | ICMPV4_PRE_STREAM | IP_ALL | IP_FLOW_START | IP_PRE_FLOW | IP_PRE_STREAM | IPV4_ALL | IPV4_FLOW_START | IPV4_PRE_FLOW | IPV4_PRE_STREAM | TLS_CLIENT_STARTED | TLS_CLIENT_HELLO | TLS_CLIENT_CERT | TLS_CLIENT_DATA | TLS_CLIENT_FINISHED | TLS_SERVER_STARTED | TLS_SERVER_HELLO | TLS_SERVER_CERT | TLS_SERVER_DATA | TLS_SERVER_FINISHED | HTTP1_REQUEST_STARTED | HTTP1_REQUEST_LINE | HTTP1_REQUEST_HEADERS | HTTP1_REQUEST_BODY | HTTP1_REQUEST_TRAILER | HTTP1_REQUEST_COMPLETE | HTTP1_RESPONSE_STARTED | HTTP1_RESPONSE_LINE | HTTP1_RESPONSE_HEADERS | HTTP1_RESPONSE_BODY | HTTP1_RESPONSE_TRAILER | HTTP1_RESPONSE_COMPLETE | HTTP2_STREAM_REQUEST_STARTED | HTTP2_STREAM_REQUEST_HEADERS | HTTP2_STREAM_REQUEST_DATA | HTTP2_STREAM_REQUEST_CLOSED | HTTP2_STREAM_REQUEST_COMPLETE | HTTP2_STREAM_RESPONSE_STARTED | HTTP2_STREAM_RESPONSE_HEADERS | HTTP2_STREAM_RESPONSE_DATA | HTTP2_STREAM_RESPONSE_CLOSED | HTTP2_STREAM_RESPONSE_COMPLETE | HTTP2_GLOBAL_REQUEST_STARTED | HTTP2_GLOBAL_REQUEST_COMPLETE | HTTP2_GLOBAL_RESPONSE_STARTED | HTTP2_GLOBAL_RESPONSE_COMPLETE | DOH2_STREAM_REQUEST_STARTED | DOH2_STREAM_REQUEST_HEADERS | DOH2_STREAM_REQUEST_DATA | DOH2_STREAM_REQUEST_CLOSED | DOH2_STREAM_REQUEST_COMPLETE | DOH2_STREAM_RESPONSE_STARTED | DOH2_STREAM_RESPONSE_HEADERS | DOH2_STREAM_RESPONSE_DATA | DOH2_STREAM_RESPONSE_CLOSED | DOH2_STREAM_RESPONSE_COMPLETE | DOH2_GLOBAL_REQUEST_STARTED | DOH2_GLOBAL_REQUEST_COMPLETE | DOH2_GLOBAL_RESPONSE_STARTED | DOH2_GLOBAL_RESPONSE_COMPLETE | DNS_REQUEST_STARTED | DNS_REQUEST_COMPLETE | DNS_RESPONSE_STARTED | DNS_RESPONSE_COMPLETE | SMTP_REQUEST_STARTED | SMTP_REQUEST_DATA | SMTP_REQUEST_COMPLETE | SMTP_RESPONSE_STARTED | SMTP_RESPONSE_DATA | SMTP_RESPONSE_COMPLETE | FTP_REQUEST_STARTED | FTP_REQUEST_COMPLETE | FTP_RESPONSE_STARTED | FTP_RESPONSE_COMPLETE | FTP_DATA_REQUEST_STARTED | FTP_DATA_REQUEST_COMPLETE | FTP_DATA_RESPONSE_STARTED | FTP_DATA_RESPONSE_COMPLETE | SMB_REQUEST_STARTED | SMB_REQUEST_COMPLETE | SMB_RESPONSE_STARTED | SMB_RESPONSE_COMPLETE | DCERPC_REQUEST_STARTED | DCERPC_REQUEST_COMPLETE | DCERPC_RESPONSE_STARTED | DCERPC_RESPONSE_COMPLETE | NFS_REQUEST_STARTED | NFS_REQUEST_COMPLETE | NFS_RESPONSE_STARTED | NFS_RESPONSE_COMPLETE | KRB5_REQUEST_STARTED | KRB5_REQUEST_COMPLETE | KRB5_RESPONSE_STARTED | KRB5_RESPONSE_COMPLETE | IKE_REQUEST_STARTED | IKE_REQUEST_COMPLETE | IKE_RESPONSE_STARTED | IKE_RESPONSE_COMPLETE | TFTP_REQUEST_STARTED | TFTP_REQUEST_COMPLETE | TFTP_RESPONSE_STARTED | TFTP_RESPONSE_COMPLETE | DHCP_REQUEST_STARTED | DHCP_REQUEST_COMPLETE | DHCP_RESPONSE_STARTED | DHCP_RESPONSE_COMPLETE | QUIC_REQUEST_STARTED | QUIC_REQUEST_COMPLETE | QUIC_RESPONSE_STARTED | QUIC_RESPONSE_COMPLETE | RDP_REQUEST_STARTED | RDP_REQUEST_COMPLETE | RDP_RESPONSE_STARTED | RDP_RESPONSE_COMPLETE | RFB_REQUEST_STARTED | RFB_REQUEST_COMPLETE | RFB_RESPONSE_STARTED | RFB_RESPONSE_COMPLETE | MQTT_REQUEST_STARTED | MQTT_REQUEST_COMPLETE | MQTT_RESPONSE_STARTED | MQTT_RESPONSE_COMPLETE | PGSQL_REQUEST_STARTED | PGSQL_REQUEST_COMPLETE | PGSQL_RESPONSE_STARTED | PGSQL_RESPONSE_COMPLETE | SNMP_REQUEST_STARTED | SNMP_REQUEST_COMPLETE | SNMP_RESPONSE_STARTED | SNMP_RESPONSE_COMPLETE | NTP_REQUEST_STARTED | NTP_REQUEST_COMPLETE | NTP_RESPONSE_STARTED | NTP_RESPONSE_COMPLETE | TELNET_REQUEST_STARTED | TELNET_REQUEST_COMPLETE | TELNET_RESPONSE_STARTED | TELNET_RESPONSE_COMPLETE | WEBSOCKET_REQUEST_STARTED | WEBSOCKET_REQUEST_COMPLETE | WEBSOCKET_RESPONSE_STARTED | WEBSOCKET_RESPONSE_COMPLETE | LDAP_REQUEST_STARTED | LDAP_REQUEST_COMPLETE | LDAP_RESPONSE_STARTED | LDAP_RESPONSE_COMPLETE | POP3_REQUEST_STARTED | POP3_REQUEST_COMPLETE | POP3_RESPONSE_STARTED | POP3_RESPONSE_COMPLETE | MDNS_REQUEST_STARTED | MDNS_REQUEST_COMPLETE | MDNS_RESPONSE_STARTED | MDNS_RESPONSE_COMPLETE | BITTORRENT_DHT_REQUEST_STARTED | BITTORRENT_DHT_REQUEST_COMPLETE | BITTORRENT_DHT_RESPONSE_STARTED | BITTORRENT_DHT_RESPONSE_COMPLETE | DNP3_REQUEST_STARTED | DNP3_REQUEST_COMPLETE | DNP3_RESPONSE_STARTED | DNP3_RESPONSE_COMPLETE | SSH_REQUEST_IN_PROGRESS | SSH_REQUEST_BANNER_WAIT_EOL | SSH_REQUEST_BANNER_DONE | SSH_REQUEST_FINISHED | SSH_RESPONSE_IN_PROGRESS | SSH_RESPONSE_BANNER_WAIT_EOL | SSH_RESPONSE_BANNER_DONE | SSH_RESPONSE_FINISHED`
Required: Yes

 ** Protocol **   <a name="networkfirewall-Type-FirewallRule-Protocol"></a>
The protocol of the rule's hook. The protocol is derived from the hook and must match the hook's protocol prefix. AWS Network Firewall rejects a rule whose protocol doesn't match its hook.
Type: String
Valid Values: `IP | TCP | UDP | ICMP | HTTP | FTP | TLS | SMB | DNS | DCERPC | SSH | SMTP | MSN | KRB5 | IKEV2 | TFTP | NTP | DHCP | HTTP2 | QUIC | ICMPV4 | ICMPV6 | SCTP | IPV4 | IPV6 | DOH2 | FTP_DATA | NFS | RDP | RFB | MQTT | PGSQL | SNMP | TELNET | WEBSOCKET | LDAP | POP3 | MDNS | BITTORRENT_DHT | DNP3`
Required: Yes

 ** AcceptPriorHooks **   <a name="networkfirewall-Type-FirewallRule-AcceptPriorHooks"></a>
Whether AWS Network Firewall automatically accepts the earlier application-layer hooks that a connection must pass to reach this rule's hook. Because the firewall engine is drop by default, accepting prior hooks lets you author a single rule for the hook you care about, instead of also authoring a rule for each earlier hook. This setting accepts the earlier application-layer hooks only; it doesn't accept the TCP layer. For more information, see [Rule groups for a firewall using a Next Generation policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-v2.html) in the * AWS Network Firewall Developer Guide*.
Type: Boolean
Required: No

 ** AlertEnabled **   <a name="networkfirewall-Type-FirewallRule-AlertEnabled"></a>
Specifies whether the rule also generates an alert log for the traffic that it matches. Turning on alerting adds a secondary alert action to the rule, so that AWS Network Firewall logs the match in addition to taking the rule's primary action.
Type: Boolean
Required: No

 ** BypassIPSEnabled **   <a name="networkfirewall-Type-FirewallRule-BypassIPSEnabled"></a>
Specifies whether an accepted connection bypasses the IPS engine. By default, traffic that the firewall engine accepts advances to the IPS engine for threat inspection. When you turn on this setting for an accept rule, the accepted traffic goes straight to its destination without IPS inspection. You can set the bypass only on accept rules, and it uses the same scope as the rule's accept action; only the `flow` and `packet` scopes support a bypass. For more information, see [Rule groups for a firewall using a Next Generation policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-v2.html) in the * AWS Network Firewall Developer Guide*.
Type: Boolean
Required: No

 ** DestIPs **   <a name="networkfirewall-Type-FirewallRule-DestIPs"></a>
The destination IP addresses and address ranges to inspect for, in CIDR notation. A firewall rule always compiles to a forward-direction rule, so you express inbound compared to outbound traffic through the source and destination addresses.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^.*$`
Required: No

 ** DestPorts **   <a name="networkfirewall-Type-FirewallRule-DestPorts"></a>
The destination ports to inspect for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^.*$`
Required: No

 ** RuleMetadata **   <a name="networkfirewall-Type-FirewallRule-RuleMetadata"></a>
Optional metadata for the rule: whether the rule is enabled and a description. Metadata doesn't change how the rule matches or acts on traffic.
Type: [RuleMetadata](API_RuleMetadata.md) object
Required: No

 ** RuleOptions **   <a name="networkfirewall-Type-FirewallRule-RuleOptions"></a>
Additional options for the rule. These are the Suricata `RuleOptions` settings, such as the signature ID (`sid`) and match keywords.
Type: Array of [RuleOption](API_RuleOption.md) objects
Required: No

 ** SourceIPs **   <a name="networkfirewall-Type-FirewallRule-SourceIPs"></a>
The source IP addresses and address ranges to inspect for, in CIDR notation. A firewall rule always compiles to a forward-direction rule, so you express inbound compared to outbound traffic through the source and destination addresses.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^.*$`
Required: No

 ** SourcePorts **   <a name="networkfirewall-Type-FirewallRule-SourcePorts"></a>
The source ports to inspect for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^.*$`
Required: No

## See Also
<a name="API_FirewallRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FirewallRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FirewallRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FirewallRule)
