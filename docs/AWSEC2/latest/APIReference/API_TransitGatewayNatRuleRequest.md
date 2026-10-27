---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayNatRuleRequest.html
---

# TransitGatewayNatRuleRequest
<a name="API_TransitGatewayNatRuleRequest"></a>

Describes a NAT gateway rule to apply to a transit gateway attachment. A NAT gateway rule translates source addresses in the `MatchSourceCidr` range to the corresponding addresses in the `NatCidr` range.

## Contents
<a name="API_TransitGatewayNatRuleRequest_Contents"></a>

 ** MatchSourceCidr **
The IPv4 CIDR block of the source addresses to translate. The CIDR block can't overlap the multicast range (`224.0.0.0/4`) or the link-local range (`169.254.0.0/16`).
Type: String
Required: No

 ** NatCidr **
The IPv4 CIDR block to translate the source addresses to. The CIDR block must be in a private (RFC 1918) or shared address space (RFC 6598) range, and must have the same prefix length as `MatchSourceCidr`. The CIDR blocks in the rules for an attachment can't overlap each other.
Type: String
Required: No

 ** RuleNumber **
The rule number. Valid values are 1 to 32766. Each rule number must be unique within the request.
Type: Integer
Required: No

## See Also
<a name="API_TransitGatewayNatRuleRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayNatRuleRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayNatRuleRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayNatRuleRequest)
