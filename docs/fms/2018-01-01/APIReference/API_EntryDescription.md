---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_EntryDescription.html
---

# EntryDescription
<a name="API_EntryDescription"></a>

Describes a single rule in a network ACL.

## Contents
<a name="API_EntryDescription_Contents"></a>

 ** EntryDetail **   <a name="fms-Type-EntryDescription-EntryDetail"></a>
Describes a rule in a network ACL.
Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the network ACL, AWS processes the entries in the network ACL according to the rule numbers, in ascending order.
When you manage an individual network ACL, you explicitly specify the rule numbers. When you specify the network ACL rules in a Firewall Manager policy, you provide the rules to run first, in the order that you want them to run, and the rules to run last, in the order that you want them to run. Firewall Manager assigns the rule numbers for you when you save the network ACL policy specification.
Type: [NetworkAclEntry](API_NetworkAclEntry.md) object
Required: No

 ** EntryRuleNumber **   <a name="fms-Type-EntryDescription-EntryRuleNumber"></a>
The rule number for the entry. ACL entries are processed in ascending order by rule number. In a Firewall Manager network ACL policy, Firewall Manager assigns rule numbers.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** EntryType **   <a name="fms-Type-EntryDescription-EntryType"></a>
Specifies whether the entry is managed by Firewall Manager or by a user, and, for Firewall Manager-managed entries, specifies whether the entry is among those that run first in the network ACL or those that run last.
Type: String
Valid Values: `FMS_MANAGED_FIRST_ENTRY | FMS_MANAGED_LAST_ENTRY | CUSTOM_ENTRY`
Required: No

## See Also
<a name="API_EntryDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/EntryDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/EntryDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/EntryDescription)
