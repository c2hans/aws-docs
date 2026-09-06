---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayPolicyRule.html
---

# TransitGatewayPolicyRule
<a name="API_TransitGatewayPolicyRule"></a>

Describes a rule associated with a transit gateway policy.

## Contents
<a name="API_TransitGatewayPolicyRule_Contents"></a>

 ** destinationCidrBlock **
The destination CIDR block for the transit gateway policy rule.
Type: String
Required: No

 ** destinationPortRange **
The destination port or port range for the transit gateway policy rule.
Type: String
Required: No

 ** metaData **
The meta data tags used for the transit gateway policy rule.
Type: [TransitGatewayPolicyRuleMetaData](API_TransitGatewayPolicyRuleMetaData.md) object
Required: No

 ** protocol **
The protocol used by the transit gateway policy rule.
Type: String
Required: No

 ** sourceCidrBlock **
The source CIDR block for the transit gateway policy rule.
Type: String
Required: No

 ** sourcePortRange **
The source port or port range for the transit gateway policy rule.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayPolicyRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayPolicyRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayPolicyRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayPolicyRule)
