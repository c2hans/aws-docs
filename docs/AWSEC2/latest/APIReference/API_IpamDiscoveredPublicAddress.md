---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamDiscoveredPublicAddress.html
---

# IpamDiscoveredPublicAddress
<a name="API_IpamDiscoveredPublicAddress"></a>

A public IP Address discovered by IPAM.

## Contents
<a name="API_IpamDiscoveredPublicAddress_Contents"></a>

 ** address **
The IP address.
Type: String
Required: No

 ** addressAllocationId **
The allocation ID of the resource the IP address is assigned to.
Type: String
Required: No

 ** addressOwnerId **
The ID of the owner of the resource the IP address is assigned to.
Type: String
Required: No

 ** addressRegion **
The Region of the resource the IP address is assigned to.
Type: String
Required: No

 ** addressType **
The IP address type.
Type: String
Valid Values: `service-managed-ip | service-managed-byoip | amazon-owned-eip | amazon-owned-contig | byoip | ec2-public-ip | anycast-ip-list-ip`
Required: No

 ** associationStatus **
The association status.
Type: String
Valid Values: `associated | disassociated`
Required: No

 ** instanceId **
The instance ID of the instance the assigned IP address is assigned to.
Type: String
Required: No

 ** ipamResourceDiscoveryId **
The resource discovery ID.
Type: String
Required: No

 ** networkBorderGroup **
The Availability Zone (AZ) or Local Zone (LZ) network border group that the resource that the IP address is assigned to is in. Defaults to an AZ network border group. For more information on available Local Zones, see [Local Zone availability](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-zone-avail) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 ** networkInterfaceDescription **
The description of the network interface that IP address is assigned to.
Type: String
Required: No

 ** networkInterfaceId **
The network interface ID of the resource with the assigned IP address.
Type: String
Required: No

 ** publicIpv4PoolId **
The ID of the public IPv4 pool that the resource with the assigned IP address is from.
Type: String
Required: No

 ** sampleTime **
The last successful resource discovery time.
Type: Timestamp
Required: No

 ** SecurityGroupSet.N **
Security groups associated with the resource that the IP address is assigned to.
Type: Array of [IpamPublicAddressSecurityGroup](API_IpamPublicAddressSecurityGroup.md) objects
Required: No

 ** service **
The AWS service associated with the IP address.
Type: String
Valid Values: `nat-gateway | database-migration-service | redshift | elastic-container-service | relational-database-service | site-to-site-vpn | load-balancer | global-accelerator | cloudfront | other`
Required: No

 ** serviceResource **
The resource ARN or ID.
Type: String
Required: No

 ** subnetId **
The ID of the subnet that the resource with the assigned IP address is in.
Type: String
Required: No

 ** tags **
Tags associated with the IP address.
Type: [IpamPublicAddressTags](API_IpamPublicAddressTags.md) object
Required: No

 ** vpcId **
The ID of the VPC that the resource with the assigned IP address is in.
Type: String
Required: No

## See Also
<a name="API_IpamDiscoveredPublicAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamDiscoveredPublicAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamDiscoveredPublicAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamDiscoveredPublicAddress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
