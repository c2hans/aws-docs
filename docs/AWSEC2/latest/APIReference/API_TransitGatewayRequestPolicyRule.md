---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayRequestPolicyRule.html
---

# TransitGatewayRequestPolicyRule
<a name="API_TransitGatewayRequestPolicyRule"></a>

The matching criteria for a transit gateway policy table entry.

## Contents
<a name="API_TransitGatewayRequestPolicyRule_Contents"></a>

 ** DestinationCidrBlock **
The destination CIDR block for the policy rule.
Type: String
Required: No

 ** DestinationPortRange **
The destination port or port range for the policy rule. You can specify a port range only when `Protocol` is `6` (TCP) or `17` (UDP); for all other protocols, this value must be `*`.
Type: String
Required: No

 ** MetaData **
The metadata key-value pair for the policy rule.
Type: [TransitGatewayRequestPolicyRuleMetaData](API_TransitGatewayRequestPolicyRuleMetaData.md) object
Required: No

 ** Protocol **
The protocol for the policy rule. Valid values are `1` (ICMP), `6` (TCP), `17` (UDP), `47` (GRE), or `*` for all protocols.
Type: String
Required: No

 ** SourceCidrBlock **
The source CIDR block for the policy rule.
Type: String
Required: No

 ** SourcePortRange **
The source port or port range for the policy rule. You can specify a port range only when `Protocol` is `6` (TCP) or `17` (UDP); for all other protocols, this value must be `*`.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayRequestPolicyRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayRequestPolicyRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayRequestPolicyRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayRequestPolicyRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
