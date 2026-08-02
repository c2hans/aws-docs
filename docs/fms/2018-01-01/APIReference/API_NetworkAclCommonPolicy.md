---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_NetworkAclCommonPolicy.html
---

# NetworkAclCommonPolicy
<a name="API_NetworkAclCommonPolicy"></a>

Defines a Firewall Manager network ACL policy. This is used in the `PolicyOption` of a `SecurityServicePolicyData` for a `Policy`, when the `SecurityServicePolicyData` type is set to `NETWORK_ACL_COMMON`.

For information about network ACLs, see [Control traffic to subnets using network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) in the *Amazon Virtual Private Cloud User Guide*.

## Contents
<a name="API_NetworkAclCommonPolicy_Contents"></a>

 ** NetworkAclEntrySet **   <a name="fms-Type-NetworkAclCommonPolicy-NetworkAclEntrySet"></a>
The definition of the first and last rules for the network ACL policy.
Type: [NetworkAclEntrySet](API_NetworkAclEntrySet.md) object
Required: Yes

## See Also
<a name="API_NetworkAclCommonPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/NetworkAclCommonPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/NetworkAclCommonPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/NetworkAclCommonPolicy)
