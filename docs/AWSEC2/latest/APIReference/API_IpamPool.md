---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamPool.html
---

# IpamPool
<a name="API_IpamPool"></a>

In IPAM, a pool is a collection of contiguous IP addresses CIDRs. Pools enable you to organize your IP addresses according to your routing and security needs. For example, if you have separate routing and security needs for development and production applications, you can create a pool for each.

## Contents
<a name="API_IpamPool_Contents"></a>

 ** addressFamily **
The address family of the pool.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** allocationDefaultNetmaskLength **
The default netmask length for allocations added to this pool. If, for example, the CIDR assigned to this pool is 10.0.0.0/8 and you enter 16 here, new allocations will default to 10.0.0.0/16.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 128.
Required: No

 ** allocationMaxNetmaskLength **
The maximum netmask length possible for CIDR allocations in this IPAM pool to be compliant. The maximum netmask length must be greater than the minimum netmask length. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 128.
Required: No

 ** allocationMinNetmaskLength **
The minimum netmask length required for CIDR allocations in this IPAM pool to be compliant. The minimum netmask length must be less than the maximum netmask length. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 128.
Required: No

 ** AllocationResourceTagSet.N **
Tags that are required for resources that use CIDRs from this IPAM pool. Resources that do not have these tags will not be allowed to allocate space from the pool. If the resources have their tags changed after they have allocated space or if the allocation tagging requirements are changed on the pool, the resource may be marked as noncompliant.
Type: Array of [IpamResourceTag](API_IpamResourceTag.md) objects
Required: No

 ** autoImport **
If selected, IPAM will continuously look for resources within the CIDR range of this pool and automatically import them as allocations into your IPAM. The CIDRs that will be allocated for these resources must not already be allocated to other resources in order for the import to succeed. IPAM will import a CIDR regardless of its compliance with the pool's allocation rules, so a resource might be imported and subsequently marked as noncompliant. If IPAM discovers multiple CIDRs that overlap, IPAM will import the largest CIDR only. If IPAM discovers multiple CIDRs with matching CIDRs, IPAM will randomly import one of them only.
A locale must be set on the pool for this feature to work.
Type: Boolean
Required: No

 ** awsService **
Limits which service in AWS that the pool can be used in. "ec2", for example, allows users to use space for Elastic IP addresses and VPCs.
Type: String
Valid Values: `ec2 | global-services`
Required: No

 ** description **
The description of the IPAM pool.
Type: String
Required: No

 ** ipamArn **
The ARN of the IPAM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** ipamPoolArn **
The Amazon Resource Name (ARN) of the IPAM pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** ipamPoolId **
The ID of the IPAM pool.
Type: String
Required: No

 ** ipamRegion **
The AWS Region of the IPAM pool.
Type: String
Required: No

 ** ipamScopeArn **
The ARN of the scope of the IPAM pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** ipamScopeType **
In IPAM, a scope is the highest-level container within IPAM. An IPAM contains two default scopes. Each scope represents the IP space for a single network. The private scope is intended for all private IP address space. The public scope is intended for all public IP address space. Scopes enable you to reuse IP addresses across multiple unconnected networks without causing IP address overlap or conflict.
Type: String
Valid Values: `public | private`
Required: No

 ** locale **
The locale of the IPAM pool.
The locale for the pool should be one of the following:
+ An AWS Region where you want this IPAM pool to be available for allocations.
+ The network border group for an AWS Local Zone where you want this IPAM pool to be available for allocations ([supported Local Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-zone-avail)). This option is only available for IPAM IPv4 pools in the public scope.
If you choose an AWS Region for locale that has not been configured as an operating Region for the IPAM, you'll get an error.
Type: String
Required: No

 ** ownerId **
The AWS account ID of the owner of the IPAM pool.
Type: String
Required: No

 ** poolDepth **
The depth of pools in your IPAM pool. The pool depth quota is 10. For more information, see [Quotas in IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: Integer
Required: No

 ** publicIpSource **
The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is `BYOIP`. For more information, see [Create IPv6 pools](https://docs.aws.amazon.com/vpc/latest/ipam/intro-create-ipv6-pools.html) in the *Amazon VPC IPAM User Guide*. By default, you can add only one Amazon-provided IPv6 CIDR block to a top-level IPv6 pool. For information on increasing the default limit, see [Quotas for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: String
Valid Values: `amazon | byoip`
Required: No

 ** publiclyAdvertisable **
Determines if a pool is publicly advertisable. This option is not available for pools with AddressFamily set to `ipv4`.
Type: Boolean
Required: No

 ** sourceIpamPoolId **
The ID of the source IPAM pool. You can use this option to create an IPAM pool within an existing source pool.
Type: String
Required: No

 ** sourceResource **
The resource used to provision CIDRs to a resource planning pool.
Type: [IpamPoolSourceResource](API_IpamPoolSourceResource.md) object
Required: No

 ** state **
The state of the IPAM pool.
Type: String
Valid Values: `create-in-progress | create-complete | create-failed | modify-in-progress | modify-complete | modify-failed | delete-in-progress | delete-complete | delete-failed | isolate-in-progress | isolate-complete | restore-in-progress`
Required: No

 ** stateMessage **
The state message.
Type: String
Required: No

 ** TagSet.N **
The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_IpamPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamPool)
