---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_AdminFirewallTypeScope.html
---

# AdminFirewallTypeScope
<a name="API_AdminFirewallTypeScope"></a>

Defines the firewall types that an administrator can create and manage.

## Contents
<a name="API_AdminFirewallTypeScope_Contents"></a>

 ** allFirewallTypesEnabled **   <a name="networksecuritymanager-Type-AdminFirewallTypeScope-allFirewallTypesEnabled"></a>
Specifies whether the administrator can manage all firewall types, except for third-party firewall types.
Type: Boolean
Required: No

 ** firewallTypes **   <a name="networksecuritymanager-Type-AdminFirewallTypeScope-firewallTypes"></a>
The list of firewall types that the administrator can manage.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Valid Values: `WAF | SHIELD_ADVANCED`
Required: No

## See Also
<a name="API_AdminFirewallTypeScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/AdminFirewallTypeScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/AdminFirewallTypeScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/AdminFirewallTypeScope)
