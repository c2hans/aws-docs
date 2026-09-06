---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2TransitGatewayDetails.html
---

# AwsEc2TransitGatewayDetails
<a name="API_AwsEc2TransitGatewayDetails"></a>

Information about an AWS Amazon EC2 Transit Gateway that interconnects virtual private clouds (VPCs) and on-premises networks.

## Contents
<a name="API_AwsEc2TransitGatewayDetails_Contents"></a>

 ** AmazonSideAsn **   <a name="securityhub-Type-AwsEc2TransitGatewayDetails-AmazonSideAsn"></a>
A private Autonomous System Number (ASN) for the Amazon side of a BGP session.
Type: Integer
Required: No

 ** AssociationDefaultRouteTableId **   <a name="securityhub-Type-AwsEc2TransitGatewayDetails-AssociationDefaultRouteTableId"></a>
The ID of the default association route table.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AutoAcceptSharedAttachments **   <a name="securityhub-Type-AwsEc2TransitGatewayDetails-AutoAcceptSharedAttachments"></a>
Turn on or turn off automatic acceptance of attachment requests.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DefaultRouteTableAssociation **   <a name="securityhub-Type-AwsEc2TransitGatewayDetails-DefaultRouteTableAssociation"></a>
Turn on or turn off automatic association with the default association route table.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DefaultRouteTablePropagation **   <a name="securityhub-Type-AwsEc2TransitGatewayDetails-DefaultRouteTablePropagation"></a>
Turn on or turn off automatic propagation of routes to the default propagation route table.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-AwsEc2TransitGatewayDetails-Description"></a>
The description of the transit gateway.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DnsSupport **   <a name="securityhub-Type-AwsEc2TransitGatewayDetails-DnsSupport"></a>
Turn on or turn off DNS support.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Id **   <a name="securityhub-Type-AwsEc2TransitGatewayDetails-Id"></a>
The ID of the transit gateway.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MulticastSupport **   <a name="securityhub-Type-AwsEc2TransitGatewayDetails-MulticastSupport"></a>
Indicates whether multicast is supported on the transit gateway.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PropagationDefaultRouteTableId **   <a name="securityhub-Type-AwsEc2TransitGatewayDetails-PropagationDefaultRouteTableId"></a>
The ID of the default propagation route table.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TransitGatewayCidrBlocks **   <a name="securityhub-Type-AwsEc2TransitGatewayDetails-TransitGatewayCidrBlocks"></a>
The transit gateway Classless Inter-Domain Routing (CIDR) blocks.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** VpnEcmpSupport **   <a name="securityhub-Type-AwsEc2TransitGatewayDetails-VpnEcmpSupport"></a>
Turn on or turn off Equal Cost Multipath Protocol (ECMP) support.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2TransitGatewayDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2TransitGatewayDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2TransitGatewayDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2TransitGatewayDetails)
