---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamPoolAllocation.html
---

# IpamPoolAllocation
<a name="API_IpamPoolAllocation"></a>

In IPAM, an allocation is a CIDR assignment from an IPAM pool to another IPAM pool or to a resource.

## Contents
<a name="API_IpamPoolAllocation_Contents"></a>

 ** cidr **
The CIDR for the allocation. A CIDR is a representation of an IP address and its associated network mask (or netmask) and refers to a range of IP addresses. An IPv4 CIDR example is `10.24.34.0/23`. An IPv6 CIDR example is `2001:DB8::/32`.
Type: String
Required: No

 ** description **
A description of the pool allocation.
Type: String
Required: No

 ** ipamPoolAllocationId **
The ID of an allocation.
Type: String
Required: No

 ** resourceId **
The ID of the resource.
Type: String
Required: No

 ** resourceOwner **
The owner of the resource.
Type: String
Required: No

 ** resourceRegion **
The AWS Region of the resource.
Type: String
Required: No

 ** resourceType **
The type of the resource.
Type: String
Valid Values: `ipam-pool | vpc | ec2-public-ipv4-pool | custom | subnet | eip | anycast-ip-list`
Required: No

 ** TagSet.N **
The tags for the IPAM pool allocation.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_IpamPoolAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamPoolAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamPoolAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamPoolAllocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
