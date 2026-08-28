---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElbLoadBalancerDetails.html
---

# AwsElbLoadBalancerDetails
<a name="API_AwsElbLoadBalancerDetails"></a>

Contains details about a Classic Load Balancer.

## Contents
<a name="API_AwsElbLoadBalancerDetails_Contents"></a>

 ** AvailabilityZones **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-AvailabilityZones"></a>
The list of Availability Zones for the load balancer.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** BackendServerDescriptions **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-BackendServerDescriptions"></a>
Information about the configuration of the EC2 instances.
Type: Array of [AwsElbLoadBalancerBackendServerDescription](API_AwsElbLoadBalancerBackendServerDescription.md) objects
Required: No

 ** CanonicalHostedZoneName **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-CanonicalHostedZoneName"></a>
The name of the Amazon Route 53 hosted zone for the load balancer.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CanonicalHostedZoneNameID **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-CanonicalHostedZoneNameID"></a>
The ID of the Amazon Route 53 hosted zone for the load balancer.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CreatedTime **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-CreatedTime"></a>
Indicates when the load balancer was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** DnsName **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-DnsName"></a>
The DNS name of the load balancer.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HealthCheck **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-HealthCheck"></a>
Information about the health checks that are conducted on the load balancer.
Type: [AwsElbLoadBalancerHealthCheck](API_AwsElbLoadBalancerHealthCheck.md) object
Required: No

 ** Instances **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-Instances"></a>
List of EC2 instances for the load balancer.
Type: Array of [AwsElbLoadBalancerInstance](API_AwsElbLoadBalancerInstance.md) objects
Required: No

 ** ListenerDescriptions **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-ListenerDescriptions"></a>
The policies that are enabled for the load balancer listeners.
Type: Array of [AwsElbLoadBalancerListenerDescription](API_AwsElbLoadBalancerListenerDescription.md) objects
Required: No

 ** LoadBalancerAttributes **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-LoadBalancerAttributes"></a>
The attributes for a load balancer.
Type: [AwsElbLoadBalancerAttributes](API_AwsElbLoadBalancerAttributes.md) object
Required: No

 ** LoadBalancerName **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-LoadBalancerName"></a>
The name of the load balancer.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Policies **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-Policies"></a>
The policies for a load balancer.
Type: [AwsElbLoadBalancerPolicies](API_AwsElbLoadBalancerPolicies.md) object
Required: No

 ** Scheme **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-Scheme"></a>
The type of load balancer. Only provided if the load balancer is in a VPC.
If `Scheme` is `internet-facing`, the load balancer has a public DNS name that resolves to a public IP address.
If `Scheme` is `internal`, the load balancer has a public DNS name that resolves to a private IP address.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SecurityGroups **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-SecurityGroups"></a>
The security groups for the load balancer. Only provided if the load balancer is in a VPC.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SourceSecurityGroup **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-SourceSecurityGroup"></a>
Information about the security group for the load balancer. This is the security group that is used for inbound rules.
Type: [AwsElbLoadBalancerSourceSecurityGroup](API_AwsElbLoadBalancerSourceSecurityGroup.md) object
Required: No

 ** Subnets **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-Subnets"></a>
The list of subnet identifiers for the load balancer.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsElbLoadBalancerDetails-VpcId"></a>
The identifier of the VPC for the load balancer.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsElbLoadBalancerDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElbLoadBalancerDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElbLoadBalancerDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElbLoadBalancerDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
