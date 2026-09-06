---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayMeteringPolicyRule.html
---

# TransitGatewayMeteringPolicyRule
<a name="API_TransitGatewayMeteringPolicyRule"></a>

Describes the traffic matching criteria for a transit gateway metering policy rule.

## Contents
<a name="API_TransitGatewayMeteringPolicyRule_Contents"></a>

 ** destinationCidrBlock **
The destination CIDR block for the rule.
Type: String
Required: No

 ** destinationPortRange **
The destination port range for the rule.
Type: String
Required: No

 ** destinationTransitGatewayAttachmentId **
The ID of the destination transit gateway attachment.
Type: String
Required: No

 ** destinationTransitGatewayAttachmentType **
The type of the destination transit gateway attachment. Note that the `tgw-peering` resource type has been deprecated. To configure metering policies for Connect, use the transport attachment type.
Type: String
Valid Values: `vpc | vpn | vpn-concentrator | direct-connect-gateway | connect | peering | tgw-peering | client-vpn`
Required: No

 ** protocol **
The protocol for the rule (1, 6, 17, etc.).
Type: String
Required: No

 ** sourceCidrBlock **
The source CIDR block for the rule.
Type: String
Required: No

 ** sourcePortRange **
The source port range for the rule.
Type: String
Required: No

 ** sourceTransitGatewayAttachmentId **
The ID of the source transit gateway attachment.
Type: String
Required: No

 ** sourceTransitGatewayAttachmentType **
The type of the source transit gateway attachment. Note that the `tgw-peering` resource type has been deprecated. To configure metering policies for Connect, use the transport attachment type.
Type: String
Valid Values: `vpc | vpn | vpn-concentrator | direct-connect-gateway | connect | peering | tgw-peering | client-vpn`
Required: No

## See Also
<a name="API_TransitGatewayMeteringPolicyRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayMeteringPolicyRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayMeteringPolicyRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayMeteringPolicyRule)
