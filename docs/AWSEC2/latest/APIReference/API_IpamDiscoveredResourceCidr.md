---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamDiscoveredResourceCidr.html
---

# IpamDiscoveredResourceCidr
<a name="API_IpamDiscoveredResourceCidr"></a>

An IPAM discovered resource CIDR. A discovered resource is a resource CIDR monitored under a resource discovery. The following resources can be discovered: VPCs, Public IPv4 pools, VPC subnets, and Elastic IP addresses. The discovered resource CIDR is the IP address range in CIDR notation that is associated with the resource.

## Contents
<a name="API_IpamDiscoveredResourceCidr_Contents"></a>

 ** availabilityZoneId **
The Availability Zone ID.
Type: String
Required: No

 ** ipamResourceDiscoveryId **
The resource discovery ID.
Type: String
Required: No

 ** ipSource **
The source that allocated the IP address space. `byoip` or `amazon` indicates public IP address space allocated by Amazon or space that you have allocated with Bring your own IP (BYOIP). `none` indicates private space.
Type: String
Valid Values: `amazon | byoip | none`
Required: No

 ** ipUsage **
The percentage of IP address space in use. To convert the decimal to a percentage, multiply the decimal by 100. Note the following:
+ For resources that are VPCs, this is the percentage of IP address space in the VPC that's taken up by subnet CIDRs.
+ For resources that are subnets, if the subnet has an IPv4 CIDR provisioned to it, this is the percentage of IPv4 address space in the subnet that's in use. If the subnet has an IPv6 CIDR provisioned to it, the percentage of IPv6 address space in use is not represented. The percentage of IPv6 address space in use cannot currently be calculated.
+ For resources that are public IPv4 pools, this is the percentage of IP address space in the pool that's been allocated to Elastic IP addresses (EIPs).
Type: Double
Required: No

 ** networkInterfaceAttachmentStatus **
For elastic network interfaces, this is the status of whether or not the elastic network interface is attached.
Type: String
Valid Values: `available | in-use`
Required: No

 ** resourceCidr **
The resource CIDR.
Type: String
Required: No

 ** resourceId **
The resource ID.
Type: String
Required: No

 ** resourceOwnerId **
The resource owner ID.
Type: String
Required: No

 ** resourceRegion **
The resource Region.
Type: String
Required: No

 ** ResourceTagSet.N **
The resource tags.
Type: Array of [IpamResourceTag](API_IpamResourceTag.md) objects
Required: No

 ** resourceType **
The resource type.
Type: String
Valid Values: `vpc | subnet | eip | public-ipv4-pool | ipv6-pool | eni | anycast-ip-list`
Required: No

 ** sampleTime **
The last successful resource discovery time.
Type: Timestamp
Required: No

 ** subnetId **
The subnet ID.
Type: String
Required: No

 ** vpcId **
The VPC ID.
Type: String
Required: No

## See Also
<a name="API_IpamDiscoveredResourceCidr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamDiscoveredResourceCidr)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamDiscoveredResourceCidr)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamDiscoveredResourceCidr)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
