---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ServerCertificateScope.html
---

# ServerCertificateScope

Settings that define the Secure Sockets Layer/Transport Layer Security (SSL/TLS) traffic that Network Firewall should decrypt for inspection by the stateful rule engine.

## Contents
<a name="API_ServerCertificateScope_Contents"></a>

 ** DecryptionAction **   <a name="networkfirewall-Type-ServerCertificateScope-DecryptionAction"></a>
Whether the firewall decrypts traffic that matches this scope. You can choose from the following values:
+  `DECRYPT` - The firewall decrypts the traffic for inspection.
+  `BYPASS` - The firewall doesn't decrypt the traffic.
Type: String
Valid Values: `DECRYPT | BYPASS`
Required: No

 ** DeploymentMode **   <a name="networkfirewall-Type-ServerCertificateScope-DeploymentMode"></a>
The type of firewall that this scope applies to. If you don't specify a value, the scope applies to both types, the same as `ALL`. You can choose from the following values:
+  `ALL` - The scope applies to both transparent firewalls and proxy mode firewalls.
+  `TRANSPARENT_FIREWALL_ONLY` - The scope applies only to transparent firewalls.
+  `EXPLICIT_PROXY_ONLY` - The scope applies only to proxy mode firewalls. A scope that specifies `DomainMatch` must use this value.
Type: String
Valid Values: `TRANSPARENT_FIREWALL_ONLY | EXPLICIT_PROXY_ONLY | ALL`
Required: No

 ** DestinationPorts **   <a name="networkfirewall-Type-ServerCertificateScope-DestinationPorts"></a>
The destination ports to decrypt for inspection, in Transmission Control Protocol (TCP) format. If not specified, this matches with any destination port.
You can specify individual ports, for example `1994`, and you can specify port ranges, such as `1990:1994`.
Type: Array of [PortRange](API_PortRange.md) objects
Required: No

 ** Destinations **   <a name="networkfirewall-Type-ServerCertificateScope-Destinations"></a>
The destination IP addresses and address ranges to decrypt for inspection, in CIDR notation. If not specified, this matches with any destination address.
Type: Array of [Address](API_Address.md) objects
Required: No

 ** DomainMatch **   <a name="networkfirewall-Type-ServerCertificateScope-DomainMatch"></a>
The domains that this scope matches, based on the host name in the client's HTTP CONNECT request. Domain matching applies only to proxy mode firewalls. If you specify `DomainMatch`, you must set `DeploymentMode` to `EXPLICIT_PROXY_ONLY`. If you don't specify `DomainMatch`, the scope matches traffic by its source, destination, ports, and protocols only.
Type: [DomainMatch](API_DomainMatch.md) object
Required: No

 ** Protocols **   <a name="networkfirewall-Type-ServerCertificateScope-Protocols"></a>
The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.
Network Firewall currently supports only TCP.
Type: Array of integers
Valid Range: Minimum value of 0. Maximum value of 255.
Required: No

 ** SourcePorts **   <a name="networkfirewall-Type-ServerCertificateScope-SourcePorts"></a>
The source ports to decrypt for inspection, in Transmission Control Protocol (TCP) format. If not specified, this matches with any source port.
You can specify individual ports, for example `1994`, and you can specify port ranges, such as `1990:1994`.
Type: Array of [PortRange](API_PortRange.md) objects
Required: No

 ** Sources **   <a name="networkfirewall-Type-ServerCertificateScope-Sources"></a>
The source IP addresses and address ranges to decrypt for inspection, in CIDR notation. If not specified, this matches with any source address.
Type: Array of [Address](API_Address.md) objects
Required: No

## See Also
<a name="API_ServerCertificateScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ServerCertificateScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ServerCertificateScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ServerCertificateScope)
