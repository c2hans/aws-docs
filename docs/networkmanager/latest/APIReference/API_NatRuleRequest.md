---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_NatRuleRequest.html
---

# NatRuleRequest
<a name="API_NatRuleRequest"></a>

Describes a NAT rule to configure on an attachment. Source addresses in the source CIDR block of traffic from the attachment are translated to the same host addresses in the NAT CIDR block. Traffic to an address in the NAT CIDR block is translated back to the matching address in the source CIDR block.

## Contents
<a name="API_NatRuleRequest_Contents"></a>

 ** MatchSourceCidr **   <a name="networkmanager-Type-NatRuleRequest-MatchSourceCidr"></a>
The IPv4 CIDR block to match against the source address of traffic from the attachment. The CIDR block can't overlap with the multicast range (224.0.0.0/4).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

 ** NatCidr **   <a name="networkmanager-Type-NatRuleRequest-NatCidr"></a>
The IPv4 CIDR block to translate matching source addresses to. The prefix length must be the same as the prefix length of `MatchSourceCidr`. The CIDR block must be within a private (RFC 1918) or shared address space (RFC 6598) range. The CIDR blocks of the NAT rules of an attachment can't overlap with each other.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

 ** RuleNumber **   <a name="networkmanager-Type-NatRuleRequest-RuleNumber"></a>
The rule number, from 1 to 32766. Each rule number must be unique for the attachment.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 32766.
Required: Yes

## See Also
<a name="API_NatRuleRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NatRuleRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NatRuleRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NatRuleRequest)
