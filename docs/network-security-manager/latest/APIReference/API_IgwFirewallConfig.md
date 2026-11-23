---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_IgwFirewallConfig.html
---

# IgwFirewallConfig

Policy configuration settings for Network Firewall automated internet firewall policies.

## Contents
<a name="API_IgwFirewallConfig_Contents"></a>

 ** defaultSubnetConnectivity **   <a name="networksecuritymanager-Type-IgwFirewallConfig-defaultSubnetConnectivity"></a>
The default internet connectivity treatment that AWS Network Security Manager applies to subnets in scope, unless a subnet connectivity override applies. Required for Network Firewall automated internet firewall policies. Valid values:
+  `flexible` – Sets the connectivity for each network interface in the subnet based on whether it is associated with a public IP address. A network interface with a public IP address gets bidirectional internet connectivity. A network interface without a public IP address gets outbound-only connectivity. All traffic is inspected against your firewall rules.
+  `bidirectional` – Provides bidirectional internet connectivity to every network interface that has a public IP association. Any network interface without a public IP cannot communicate with the internet unless a NAT device is explicitly inserted in the path. All inbound and outbound traffic is inspected against your firewall rules.
+  `outbound-only` – Provides egress-only connectivity for all network interfaces in the subnet. All outbound traffic and inbound responses are inspected against your firewall rules. Unsolicited inbound connections are dropped. For IPv4 traffic, the Network Firewall automated internet firewall performs NAT.
Type: String
Valid Values: `flexible | bidirectional | outbound-only`
Required: No

 ** subnetConnectivityOverrides **   <a name="networksecuritymanager-Type-IgwFirewallConfig-subnetConnectivityOverrides"></a>
An ordered list of overrides that apply a different connectivity treatment to the subnets that a scope selects. When a subnet matches more than one override, the first matching override in the list applies. You can specify at most one override for each connectivity type.
Type: Array of [SubnetConnectivityOverride](API_SubnetConnectivityOverride.md) objects
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Required: No

## See Also
<a name="API_IgwFirewallConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/IgwFirewallConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/IgwFirewallConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/IgwFirewallConfig)
