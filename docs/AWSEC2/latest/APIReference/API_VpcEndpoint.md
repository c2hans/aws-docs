---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpcEndpoint.html
---

# VpcEndpoint
<a name="API_VpcEndpoint"></a>

Describes a VPC endpoint.

## Contents
<a name="API_VpcEndpoint_Contents"></a>

 ** creationTimestamp **
The date and time that the endpoint was created.
Type: Timestamp
Required: No

 ** DnsEntrySet.N **
(Interface endpoint) The DNS entries for the endpoint.
Type: Array of [DnsEntry](API_DnsEntry.md) objects
Required: No

 ** dnsOptions **
The DNS options for the endpoint.
Type: [DnsOptions](API_DnsOptions.md) object
Required: No

 ** failureReason **
Reason for the failure.
Type: String
Required: No

 ** GroupSet.N **
(Interface endpoint) Information about the security groups that are associated with the network interface.
Type: Array of [SecurityGroupIdentifier](API_SecurityGroupIdentifier.md) objects
Required: No

 ** ipAddressType **
The IP address type for the endpoint.
Type: String
Valid Values: `ipv4 | dualstack | ipv6`
Required: No

 ** Ipv4PrefixSet.N **
Array of IPv4 prefixes.
Type: Array of [SubnetIpPrefixes](API_SubnetIpPrefixes.md) objects
Required: No

 ** Ipv6PrefixSet.N **
Array of IPv6 prefixes.
Type: Array of [SubnetIpPrefixes](API_SubnetIpPrefixes.md) objects
Required: No

 ** lastError **
The last error that occurred for endpoint.
Type: [LastError](API_LastError.md) object
Required: No

 ** NetworkInterfaceIdSet.N **
(Interface endpoint) The network interfaces for the endpoint.
Type: Array of strings
Required: No

 ** ownerId **
The ID of the AWS account that owns the endpoint.
Type: String
Required: No

 ** PayerResponsibilitySet.N **
The payer responsibility settings for the endpoint.
Type: Array of [PayerResponsibilityEntry](API_PayerResponsibilityEntry.md) objects
Required: No

 ** policyDocument **
The policy document associated with the endpoint, if applicable.
Type: String
Required: No

 ** privateDnsEnabled **
(Interface endpoint) Indicates whether the VPC is associated with a private hosted zone.
Type: Boolean
Required: No

 ** requesterManaged **
Indicates whether the endpoint is being managed by its service.
Type: Boolean
Required: No

 ** resourceConfigurationArn **
The Amazon Resource Name (ARN) of the resource configuration.
Type: String
Required: No

 ** RouteTableIdSet.N **
(Gateway endpoint) The IDs of the route tables associated with the endpoint.
Type: Array of strings
Required: No

 ** serviceName **
The name of the service to which the endpoint is associated.
Type: String
Required: No

 ** serviceNetworkArn **
The Amazon Resource Name (ARN) of the service network.
Type: String
Required: No

 ** serviceRegion **
The Region where the service is hosted.
Type: String
Required: No

 ** state **
The state of the endpoint.
Type: String
Valid Values: `PendingAcceptance | Pending | Available | Deleting | Deleted | Rejected | Failed | Expired | Partial`
Required: No

 ** SubnetIdSet.N **
(Interface endpoint) The subnets for the endpoint.
Type: Array of strings
Required: No

 ** TagSet.N **
The tags assigned to the endpoint.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcEndpointId **
The ID of the endpoint.
Type: String
Required: No

 ** vpcEndpointType **
The type of endpoint.
Type: String
Valid Values: `Interface | Gateway | GatewayLoadBalancer | Resource | ServiceNetwork`
Required: No

 ** vpcId **
The ID of the VPC to which the endpoint is associated.
Type: String
Required: No

## See Also
<a name="API_VpcEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpcEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpcEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpcEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
