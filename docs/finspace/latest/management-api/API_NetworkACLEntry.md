---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_NetworkACLEntry.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# NetworkACLEntry
<a name="API_NetworkACLEntry"></a>

 The network access control list (ACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. The entry is a set of numbered ingress and egress rules that determine whether a packet should be allowed in or out of a subnet associated with the ACL. We process the entries in the ACL according to the rule numbers, in ascending order.

## Contents
<a name="API_NetworkACLEntry_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** cidrBlock **   <a name="finspace-Type-NetworkACLEntry-cidrBlock"></a>
 The IPv4 network range to allow or deny, in CIDR notation. For example, `172.16.0.0/24`. We modify the specified CIDR block to its canonical form. For example, if you specify `100.68.0.18/18`, we modify it to `100.68.0.0/18`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `^(?:\d{1,3}\.){3}\d{1,3}(?:\/(?:3[0-2]|[12]\d|\d))$`
Required: Yes

 ** protocol **   <a name="finspace-Type-NetworkACLEntry-protocol"></a>
 The protocol number. A value of *-1* means all the protocols.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^-1|[0-9]+$`
Required: Yes

 ** ruleAction **   <a name="finspace-Type-NetworkACLEntry-ruleAction"></a>
 Indicates whether to allow or deny the traffic that matches the rule.
Type: String
Valid Values: `allow | deny`
Required: Yes

 ** ruleNumber **   <a name="finspace-Type-NetworkACLEntry-ruleNumber"></a>
 The rule number for the entry. For example *100*. All the network ACL entries are processed in ascending order by rule number.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 32766.
Required: Yes

 ** icmpTypeCode **   <a name="finspace-Type-NetworkACLEntry-icmpTypeCode"></a>
 Defines the ICMP protocol that consists of the ICMP type and code.
Type: [IcmpTypeCode](API_IcmpTypeCode.md) object
Required: No

 ** portRange **   <a name="finspace-Type-NetworkACLEntry-portRange"></a>
 The range of ports the rule applies to.
Type: [PortRange](API_PortRange.md) object
Required: No

## See Also
<a name="API_NetworkACLEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/NetworkACLEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/NetworkACLEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/NetworkACLEntry)
