---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_NetworkAclEntrySet.html
---

# NetworkAclEntrySet
<a name="API_NetworkAclEntrySet"></a>

The configuration of the first and last rules for the network ACL policy, and the remediation settings for each.

## Contents
<a name="API_NetworkAclEntrySet_Contents"></a>

 ** ForceRemediateForFirstEntries **   <a name="fms-Type-NetworkAclEntrySet-ForceRemediateForFirstEntries"></a>
Applies only when remediation is enabled for the policy as a whole. Firewall Manager uses this setting when it finds policy violations that involve conflicts between the custom entries and the policy entries.
If forced remediation is disabled, Firewall Manager marks the network ACL as noncompliant and does not try to remediate. For more information about the remediation behavior, see [Remediation for managed network ACLs](https://docs.aws.amazon.com/waf/latest/developerguide/network-acl-policies.html#network-acls-remediation) in the * AWS Firewall Manager Developer Guide*.
Type: Boolean
Required: Yes

 ** ForceRemediateForLastEntries **   <a name="fms-Type-NetworkAclEntrySet-ForceRemediateForLastEntries"></a>
Applies only when remediation is enabled for the policy as a whole. Firewall Manager uses this setting when it finds policy violations that involve conflicts between the custom entries and the policy entries.
If forced remediation is disabled, Firewall Manager marks the network ACL as noncompliant and does not try to remediate. For more information about the remediation behavior, see [Remediation for managed network ACLs](https://docs.aws.amazon.com/waf/latest/developerguide/network-acl-policies.html#network-acls-remediation) in the * AWS Firewall Manager Developer Guide*.
Type: Boolean
Required: Yes

 ** FirstEntries **   <a name="fms-Type-NetworkAclEntrySet-FirstEntries"></a>
The rules that you want to run first in the Firewall Manager managed network ACLs.
Provide these in the order in which you want them to run. Firewall Manager will assign the specific rule numbers for you, in the network ACLs that it creates.
You must specify at least one first entry or one last entry in any network ACL policy.
Type: Array of [NetworkAclEntry](API_NetworkAclEntry.md) objects
Required: No

 ** LastEntries **   <a name="fms-Type-NetworkAclEntrySet-LastEntries"></a>
The rules that you want to run last in the Firewall Manager managed network ACLs.
Provide these in the order in which you want them to run. Firewall Manager will assign the specific rule numbers for you, in the network ACLs that it creates.
You must specify at least one first entry or one last entry in any network ACL policy.
Type: Array of [NetworkAclEntry](API_NetworkAclEntry.md) objects
Required: No

## See Also
<a name="API_NetworkAclEntrySet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/NetworkAclEntrySet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/NetworkAclEntrySet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/NetworkAclEntrySet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
