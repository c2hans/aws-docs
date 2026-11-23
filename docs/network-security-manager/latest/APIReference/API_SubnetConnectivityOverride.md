---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_SubnetConnectivityOverride.html
---

# SubnetConnectivityOverride

An override that applies a connectivity treatment to the subnets that a scope selects, instead of the policy's `defaultSubnetConnectivity`.

## Contents
<a name="API_SubnetConnectivityOverride_Contents"></a>

 ** connectivityType **   <a name="networksecuritymanager-Type-SubnetConnectivityOverride-connectivityType"></a>
The connectivity treatment to apply to the selected subnets. You select both the override value as well as the subnets they apply to. The Network Firewall automated internet firewall applies the override value to the specified subnets, and applies the default connectivity to the rest of the subnets. Valid values:
+  `flexible` – Sets the connectivity for each network interface in the subnet based on whether it is associated with a public IP address. A network interface with a public IP address gets bidirectional internet connectivity. A network interface without a public IP address gets outbound-only connectivity. All traffic is inspected against your firewall rules.
+  `bidirectional` – Provides bidirectional internet connectivity to every network interface that has a public IP association. Any network interface without a public IP cannot communicate with the internet unless a NAT device is explicitly inserted in the path. All inbound and outbound traffic is inspected against your firewall rules.
+  `outbound-only` – Provides egress-only connectivity for all network interfaces in the subnet. All outbound traffic and inbound responses are inspected against your firewall rules. Unsolicited inbound connections are dropped. For IPv4 traffic, the Network Firewall automated internet firewall performs NAT.
+  `exclude` – The Network Firewall automated internet firewall doesn't inspect traffic for the selected subnets. The subnets bypass the firewall entirely, and their traffic passes directly through the internet gateway. You can specify this value only in an override, not as the `defaultSubnetConnectivity`.
Type: String
Valid Values: `flexible | bidirectional | outbound-only | exclude`
Required: Yes

 ** scopes **   <a name="networksecuritymanager-Type-SubnetConnectivityOverride-scopes"></a>
A list that contains the Amazon Resource Name (ARN) of the scope that selects the subnets to override. The list must contain exactly one scope ARN. The deployment determines which accounts are in scope, and the referenced scope selects subnets within those accounts.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: Yes

## See Also
<a name="API_SubnetConnectivityOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/SubnetConnectivityOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/SubnetConnectivityOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/SubnetConnectivityOverride)
