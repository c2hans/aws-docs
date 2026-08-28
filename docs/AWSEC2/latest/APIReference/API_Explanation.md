---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Explanation.html
---

# Explanation
<a name="API_Explanation"></a>

Describes an explanation code for an unreachable path. For more information, see [Reachability Analyzer explanation codes](https://docs.aws.amazon.com/vpc/latest/reachability/explanation-codes.html).

## Contents
<a name="API_Explanation_Contents"></a>

 ** acl **
The network ACL.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** aclRule **
The network ACL rule.
Type: [AnalysisAclRule](API_AnalysisAclRule.md) object
Required: No

 ** address **
The IPv4 address, in CIDR notation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 15.
Pattern: `^([0-9]{1,3}.){3}[0-9]{1,3}$`
Required: No

 ** AddressSet.N **
The IPv4 addresses, in CIDR notation.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 15.
Pattern: `^([0-9]{1,3}.){3}[0-9]{1,3}$`
Required: No

 ** attachedTo **
The resource to which the component is attached.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** AvailabilityZoneIdSet.N **
The IDs of the Availability Zones.
Type: Array of strings
Required: No

 ** AvailabilityZoneSet.N **
The Availability Zones.
Type: Array of strings
Required: No

 ** CidrSet.N **
The CIDR ranges.
Type: Array of strings
Required: No

 ** classicLoadBalancerListener **
The listener for a Classic Load Balancer.
Type: [AnalysisLoadBalancerListener](API_AnalysisLoadBalancerListener.md) object
Required: No

 ** component **
The component.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** componentAccount **
The AWS account for the component.
Type: String
Pattern: `\d{12}`
Required: No

 ** componentRegion **
The Region for the component.
Type: String
Pattern: `[a-z]{2}-[a-z]+-[1-9]+`
Required: No

 ** customerGateway **
The customer gateway.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** destination **
The destination.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** destinationVpc **
The destination VPC.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** direction **
The direction. The following are the possible values:
+ egress
+ ingress
Type: String
Required: No

 ** elasticLoadBalancerListener **
The load balancer listener.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** explanationCode **
The explanation code.
Type: String
Required: No

 ** firewallStatefulRule **
The Network Firewall stateful rule.
Type: [FirewallStatefulRule](API_FirewallStatefulRule.md) object
Required: No

 ** firewallStatelessRule **
The Network Firewall stateless rule.
Type: [FirewallStatelessRule](API_FirewallStatelessRule.md) object
Required: No

 ** ingressRouteTable **
The route table.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** internetGateway **
The internet gateway.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** loadBalancerArn **
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** loadBalancerListenerPort **
The listener port of the load balancer.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

 ** loadBalancerTarget **
The target.
Type: [AnalysisLoadBalancerTarget](API_AnalysisLoadBalancerTarget.md) object
Required: No

 ** loadBalancerTargetGroup **
The target group.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** LoadBalancerTargetGroupSet.N **
The target groups.
Type: Array of [AnalysisComponent](API_AnalysisComponent.md) objects
Required: No

 ** loadBalancerTargetPort **
The target port.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

 ** missingComponent **
The missing component.
Type: String
Required: No

 ** natGateway **
The NAT gateway.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** networkInterface **
The network interface.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** packetField **
The packet field.
Type: String
Required: No

 ** port **
The port.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

 ** PortRangeSet.N **
The port ranges.
Type: Array of [PortRange](API_PortRange.md) objects
Required: No

 ** prefixList **
The prefix list.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** ProtocolSet.N **
The protocols.
Type: Array of strings
Required: No

 ** routeTable **
The route table.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** routeTableRoute **
The route table route.
Type: [AnalysisRouteTableRoute](API_AnalysisRouteTableRoute.md) object
Required: No

 ** securityGroup **
The security group.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** securityGroupRule **
The security group rule.
Type: [AnalysisSecurityGroupRule](API_AnalysisSecurityGroupRule.md) object
Required: No

 ** SecurityGroupSet.N **
The security groups.
Type: Array of [AnalysisComponent](API_AnalysisComponent.md) objects
Required: No

 ** sourceVpc **
The source VPC.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** state **
The state.
Type: String
Required: No

 ** subnet **
The subnet.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** subnetRouteTable **
The route table for the subnet.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** transitGateway **
The transit gateway.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** transitGatewayAttachment **
The transit gateway attachment.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** transitGatewayRouteTable **
The transit gateway route table.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** transitGatewayRouteTableRoute **
The transit gateway route table route.
Type: [TransitGatewayRouteTableRoute](API_TransitGatewayRouteTableRoute.md) object
Required: No

 ** vpc **
The component VPC.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** vpcEndpoint **
The VPC endpoint.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** vpcPeeringConnection **
The VPC peering connection.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** vpnConnection **
The VPN connection.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

 ** vpnGateway **
The VPN gateway.
Type: [AnalysisComponent](API_AnalysisComponent.md) object
Required: No

## See Also
<a name="API_Explanation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Explanation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Explanation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Explanation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
