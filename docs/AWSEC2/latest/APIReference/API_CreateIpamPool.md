---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateIpamPool.html
---

# CreateIpamPool
<a name="API_CreateIpamPool"></a>

Create an IP address pool for Amazon VPC IP Address Manager (IPAM). In IPAM, a pool is a collection of contiguous IP addresses CIDRs. Pools enable you to organize your IP addresses according to your routing and security needs. For example, if you have separate routing and security needs for development and production applications, you can create a pool for each.

For more information, see [Create a top-level pool](https://docs.aws.amazon.com/vpc/latest/ipam/create-top-ipam.html) in the *Amazon VPC IPAM User Guide*.

## Request Parameters
<a name="API_CreateIpamPool_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AddressFamily**
The IP protocol assigned to this IPAM pool. You must choose either IPv4 or IPv6 protocol for a pool.
Type: String
Valid Values: `ipv4 | ipv6`
Required: Yes

 **AllocationDefaultNetmaskLength**
The default netmask length for allocations added to this pool. If, for example, the CIDR assigned to this pool is 10.0.0.0/8 and you enter 16 here, new allocations will default to 10.0.0.0/16.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 128.
Required: No

 **AllocationMaxNetmaskLength**
The maximum netmask length possible for CIDR allocations in this IPAM pool to be compliant. The maximum netmask length must be greater than the minimum netmask length. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 128.
Required: No

 **AllocationMinNetmaskLength**
The minimum netmask length required for CIDR allocations in this IPAM pool to be compliant. The minimum netmask length must be less than the maximum netmask length. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 128.
Required: No

 **AllocationResourceTag.N**
Tags that are required for resources that use CIDRs from this IPAM pool. Resources that do not have these tags will not be allowed to allocate space from the pool. If the resources have their tags changed after they have allocated space or if the allocation tagging requirements are changed on the pool, the resource may be marked as noncompliant.
Type: Array of [RequestIpamResourceTag](API_RequestIpamResourceTag.md) objects
Required: No

 **AutoImport**
If selected, IPAM will continuously look for resources within the CIDR range of this pool and automatically import them as allocations into your IPAM. The CIDRs that will be allocated for these resources must not already be allocated to other resources in order for the import to succeed. IPAM will import a CIDR regardless of its compliance with the pool's allocation rules, so a resource might be imported and subsequently marked as noncompliant. If IPAM discovers multiple CIDRs that overlap, IPAM will import the largest CIDR only. If IPAM discovers multiple CIDRs with matching CIDRs, IPAM will randomly import one of them only.
A locale must be set on the pool for this feature to work.
Type: Boolean
Required: No

 **AwsService**
Limits which service in AWS that the pool can be used in. "ec2", for example, allows users to use space for Elastic IP addresses and VPCs.
Type: String
Valid Values: `ec2 | global-services`
Required: No

 **ClientToken**
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **Description**
A description for the IPAM pool.
Type: String
Required: No

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamScopeId**
The ID of the scope in which you would like to create the IPAM pool.
Type: String
Required: Yes

 **Locale**
The locale for the pool should be one of the following:
+ An AWS Region where you want this IPAM pool to be available for allocations.
+ The network border group for an AWS Local Zone where you want this IPAM pool to be available for allocations ([supported Local Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-zone-avail)). This option is only available for IPAM IPv4 pools in the public scope.
Possible values: Any AWS Region or supported AWS Local Zone. Default is `none` and means any locale.
Type: String
Required: No

 **PublicIpSource**
The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is `byoip`. For more information, see [Create IPv6 pools](https://docs.aws.amazon.com/vpc/latest/ipam/intro-create-ipv6-pools.html) in the *Amazon VPC IPAM User Guide*. By default, you can add only one Amazon-provided IPv6 CIDR block to a top-level IPv6 pool if PublicIpSource is `amazon`. For information on increasing the default limit, see [ Quotas for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: String
Valid Values: `amazon | byoip`
Required: No

 **PubliclyAdvertisable**
Determines if the pool is publicly advertisable. The request can only contain `PubliclyAdvertisable` if `AddressFamily` is `ipv6` and `PublicIpSource` is `byoip`.
Type: Boolean
Required: No

 **SourceIpamPoolId**
The ID of the source IPAM pool. Use this option to create a pool within an existing pool. Note that the CIDR you provision for the pool within the source pool must be available in the source pool's CIDR range.
Type: String
Required: No

 **SourceResource**
The resource used to provision CIDRs to a resource planning pool.
Type: [IpamPoolSourceResourceRequest](API_IpamPoolSourceResourceRequest.md) object
Required: No

 **TagSpecification.N**
The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateIpamPool_ResponseElements"></a>

The following elements are returned by the service.

 **ipamPool**
Information about the IPAM pool created.
Type: [IpamPool](API_IpamPool.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateIpamPool_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateIpamPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateIpamPool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateIpamPool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateIpamPool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateIpamPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateIpamPool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateIpamPool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateIpamPool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateIpamPool)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateIpamPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateIpamPool)
