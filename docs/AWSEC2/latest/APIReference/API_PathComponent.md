---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PathComponent.html
---

# PathComponent
<a name="API_PathComponent"></a>

Describes a path component.

## Contents
<a name="API_PathComponent_Contents"></a>

 ** aclRule **
The network ACL rule.
Type: [AnalysisAclRule](API_AnalysisAclRule.md) object
Required: No

 ** AdditionalDetailSet.N **
The additional details.
Type: Array of [AdditionalDetail](API_AdditionalDetail.md) objects
Required: No

 ** attachedTo **
The resource to which the path component is attached.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** component **
The component.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** destinationVpc **
The destination VPC.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** elasticLoadBalancerListener **
The load balancer listener.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** ExplanationSet.N **
The explanation codes.
Type: Array of [Explanation](API_Explanation.md) objects
Required: No

 ** firewallStatefulRule **
The Network Firewall stateful rule.
Type: [FirewallStatefulRule](API_FirewallStatefulRule.md) object
Required: No

 ** firewallStatelessRule **
The Network Firewall stateless rule.
Type: [FirewallStatelessRule](API_FirewallStatelessRule.md) object
Required: No

 ** inboundHeader **
The inbound header.
Type: [AnalysisPacketHeader](API_AnalysisPacketHeader.md) object
Required: No

 ** outboundHeader **
The outbound header.
Type: [AnalysisPacketHeader](API_AnalysisPacketHeader.md) object
Required: No

 ** routeTableRoute **
The route table route.
Type: [AnalysisRouteTableRoute](API_AnalysisRouteTableRoute.md) object
Required: No

 ** securityGroupRule **
The security group rule.
Type: [AnalysisSecurityGroupRule](API_AnalysisSecurityGroupRule.md) object
Required: No

 ** sequenceNumber **
The sequence number.
Type: Integer
Required: No

 ** serviceName **
The name of the VPC endpoint service.
Type: String
Required: No

 ** sourceVpc **
The source VPC.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** subnet **
The subnet.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** transitGateway **
The transit gateway.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** transitGatewayRouteTableRoute **
The route in a transit gateway route table.
Type: [TransitGatewayRouteTableRoute](API_TransitGatewayRouteTableRoute.md) object
Required: No

 ** vpc **
The component VPC.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

## See Also
<a name="API_PathComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PathComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PathComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PathComponent)
