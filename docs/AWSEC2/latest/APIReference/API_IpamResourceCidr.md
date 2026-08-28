---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamResourceCidr.html
---

# IpamResourceCidr
<a name="API_IpamResourceCidr"></a>

The CIDR for an IPAM resource.

## Contents
<a name="API_IpamResourceCidr_Contents"></a>

 ** availabilityZoneId **
The Availability Zone ID.
Type: String
Required: No

 ** complianceStatus **
The compliance status of the IPAM resource. For more information on compliance statuses, see [Monitor CIDR usage by resource](https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: String
Valid Values: `compliant | noncompliant | unmanaged | ignored`
Required: No

 ** ipamId **
The IPAM ID for an IPAM resource.
Type: String
Required: No

 ** ipamPoolId **
The pool ID for an IPAM resource.
Type: String
Required: No

 ** ipamScopeId **
The scope ID for an IPAM resource.
Type: String
Required: No

 ** ipUsage **
The percentage of IP address space in use. To convert the decimal to a percentage, multiply the decimal by 100. Note the following:
+ For resources that are VPCs, this is the percentage of IP address space in the VPC that's taken up by subnet CIDRs.
+ For resources that are subnets, if the subnet has an IPv4 CIDR provisioned to it, this is the percentage of IPv4 address space in the subnet that's in use. If the subnet has an IPv6 CIDR provisioned to it, the percentage of IPv6 address space in use is not represented. The percentage of IPv6 address space in use cannot currently be calculated.
+ For resources that are public IPv4 pools, this is the percentage of IP address space in the pool that's been allocated to Elastic IP addresses (EIPs).
Type: Double
Required: No

 ** managementState **
The management state of the resource. For more information about management states, see [Monitor CIDR usage by resource](https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: String
Valid Values: `managed | unmanaged | ignored`
Required: No

 ** overlapStatus **
The overlap status of an IPAM resource. The overlap status tells you if the CIDR for a resource overlaps with another CIDR in the scope. For more information on overlap statuses, see [Monitor CIDR usage by resource](https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: String
Valid Values: `overlapping | nonoverlapping | ignored`
Required: No

 ** resourceCidr **
The CIDR for an IPAM resource.
Type: String
Required: No

 ** resourceId **
The ID of an IPAM resource.
Type: String
Required: No

 ** resourceName **
The name of an IPAM resource.
Type: String
Required: No

 ** resourceOwnerId **
The AWS account number of the owner of an IPAM resource.
Type: String
Required: No

 ** resourceRegion **
The AWS Region for an IPAM resource.
Type: String
Required: No

 ** ResourceTagSet.N **
The tags for an IPAM resource.
Type: Array of [IpamResourceTag](API_IpamResourceTag.md) objects
Required: No

 ** resourceType **
The type of IPAM resource.
Type: String
Valid Values: `vpc | subnet | eip | public-ipv4-pool | ipv6-pool | eni | anycast-ip-list`
Required: No

 ** vpcId **
The ID of a VPC.
Type: String
Required: No

## See Also
<a name="API_IpamResourceCidr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamResourceCidr)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamResourceCidr)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamResourceCidr)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
