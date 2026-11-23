---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_IgwFirewallConfiguration.html
---

# IgwFirewallConfiguration

Contains the settings that configure an internet gateway firewall. An internet gateway firewall inspects all traffic between your VPC and its internet gateway, without changes to your subnets or route tables. You can describe and list internet gateway firewalls in Network Firewall, but you can't create, modify, or delete them directly, because AWS Network Security Manager creates and manages them on your behalf.

## Contents
<a name="API_IgwFirewallConfiguration_Contents"></a>

 ** EnforcementMode **   <a name="networkfirewall-Type-IgwFirewallConfiguration-EnforcementMode"></a>
How the internet gateway firewall enforces its rules. The only supported value is `POLICY_CONTROLLED`, which means that the enforcement mode is set by the firewall policy that AWS Network Security Manager associates with the firewall.
Type: String
Valid Values: `POLICY_CONTROLLED`
Required: Yes

## See Also
<a name="API_IgwFirewallConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/IgwFirewallConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/IgwFirewallConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/IgwFirewallConfiguration)
