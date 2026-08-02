---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PolicyTypeScope.html
---

# PolicyTypeScope
<a name="API_PolicyTypeScope"></a>

Defines the policy types that the specified Firewall Manager administrator can manage.

## Contents
<a name="API_PolicyTypeScope_Contents"></a>

 ** AllPolicyTypesEnabled **   <a name="fms-Type-PolicyTypeScope-AllPolicyTypesEnabled"></a>
Allows the specified Firewall Manager administrator to manage all Firewall Manager policy types, except for third-party policy types. Third-party policy types can only be managed by the Firewall Manager default administrator.
Type: Boolean
Required: No

 ** PolicyTypes **   <a name="fms-Type-PolicyTypeScope-PolicyTypes"></a>
The list of policy types that the specified Firewall Manager administrator can manage.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Valid Values: `WAF | WAFV2 | SHIELD_ADVANCED | SECURITY_GROUPS_COMMON | SECURITY_GROUPS_CONTENT_AUDIT | SECURITY_GROUPS_USAGE_AUDIT | NETWORK_FIREWALL | DNS_FIREWALL | THIRD_PARTY_FIREWALL | IMPORT_NETWORK_FIREWALL | NETWORK_ACL_COMMON`
Required: No

## See Also
<a name="API_PolicyTypeScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/PolicyTypeScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/PolicyTypeScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/PolicyTypeScope)
