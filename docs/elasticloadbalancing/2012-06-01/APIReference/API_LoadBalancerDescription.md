---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_LoadBalancerDescription.html
---

# LoadBalancerDescription
<a name="API_LoadBalancerDescription"></a>

Information about a load balancer.

## Contents
<a name="API_LoadBalancerDescription_Contents"></a>

 ** AvailabilityZones.member.N **
The Availability Zones for the load balancer.
Type: Array of strings
Required: No

 ** BackendServerDescriptions.member.N **
Information about your EC2 instances.
Type: Array of [BackendServerDescription](API_BackendServerDescription.md) objects
Required: No

 ** CanonicalHostedZoneName **
The DNS name of the load balancer.
For more information, see [Configure a custom domain Name](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/using-domain-names-with-elb.html) in the *User Guide for Classic Load Balancers*.
Type: String
Required: No

 ** CanonicalHostedZoneNameID **
The ID of the Amazon Route 53 hosted zone for the load balancer.
Type: String
Required: No

 ** CreatedTime **
The date and time the load balancer was created.
Type: Timestamp
Required: No

 ** DNSName **
The DNS name of the load balancer.
Type: String
Required: No

 ** HealthCheck **
Information about the health checks conducted on the load balancer.
Type: [HealthCheck](API_HealthCheck.md) object
Required: No

 ** Instances.member.N **
The IDs of the instances for the load balancer.
Type: Array of [Instance](API_Instance.md) objects
Required: No

 ** ListenerDescriptions.member.N **
The listeners for the load balancer.
Type: Array of [ListenerDescription](API_ListenerDescription.md) objects
Required: No

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: No

 ** Policies **
The policies defined for the load balancer.
Type: [Policies](API_Policies.md) object
Required: No

 ** Scheme **
The type of load balancer. Valid only for load balancers in a VPC.
If `Scheme` is `internet-facing`, the load balancer has a public DNS name that resolves to a public IP address.
If `Scheme` is `internal`, the load balancer has a public DNS name that resolves to a private IP address.
Type: String
Required: No

 ** SecurityGroups.member.N **
The security groups for the load balancer. Valid only for load balancers in a VPC.
Type: Array of strings
Required: No

 ** SourceSecurityGroup **
The security group for the load balancer, which you can use as part of your inbound rules for your registered instances. To only allow traffic from load balancers, add a security group rule that specifies this source security group as the inbound source.
Type: [SourceSecurityGroup](API_SourceSecurityGroup.md) object
Required: No

 ** Subnets.member.N **
The IDs of the subnets for the load balancer.
Type: Array of strings
Required: No

 ** VPCId **
The ID of the VPC for the load balancer.
Type: String
Required: No

## See Also
<a name="API_LoadBalancerDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/LoadBalancerDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/LoadBalancerDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/LoadBalancerDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
