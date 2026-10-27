---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayNatRule.html
---

# TransitGatewayNatRule
<a name="API_TransitGatewayNatRule"></a>

Contains information about a NAT gateway rule for a transit gateway attachment, including the rule number, the source CIDR block, the translated CIDR block, and the state of the rule.

## Contents
<a name="API_TransitGatewayNatRule_Contents"></a>

 ** matchSourceCidr **
The IPv4 CIDR block of the source addresses to translate.
Type: String
Required: No

 ** natCidr **
The IPv4 CIDR block that the transit gateway translates the source addresses to.
Type: String
Required: No

 ** ruleNumber **
The rule number.
Type: Integer
Required: No

 ** state **
The state of the NAT gateway rule. The possible values are:
+  `pending` - The transit gateway is applying a change to the rule.
+  `activated` - The rule is in effect because NAT gateway support is enabled for the attachment.
+  `deactivated` - The rule isn't in effect because NAT gateway support is disabled for the attachment.
Type: String
Valid Values: `pending | activated | deactivated | deleting`
Required: No

## See Also
<a name="API_TransitGatewayNatRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayNatRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayNatRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayNatRule)
