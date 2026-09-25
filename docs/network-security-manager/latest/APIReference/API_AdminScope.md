---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_AdminScope.html
---

# AdminScope
<a name="API_AdminScope"></a>

Defines the accounts, organizational units, and firewall types that an administrator can manage.

## Contents
<a name="API_AdminScope_Contents"></a>

 ** firewallTypeScope **   <a name="networksecuritymanager-Type-AdminScope-firewallTypeScope"></a>
The firewall types that the administrator can create and manage.
Type: [AdminFirewallTypeScope](API_AdminFirewallTypeScope.md) object
Required: No

 ** scopeFilter **   <a name="networksecuritymanager-Type-AdminScope-scopeFilter"></a>
The filter that determines which accounts and organizational units are in the administrator's scope.
Type: [AdminScopeFilter](API_AdminScopeFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_AdminScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/AdminScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/AdminScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/AdminScope)
