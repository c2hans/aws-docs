---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIpamPool.html
---

# ModifyIpamPool
<a name="API_ModifyIpamPool"></a>

Modify the configurations of an IPAM pool.

For more information, see [Modify a pool](https://docs.aws.amazon.com/vpc/latest/ipam/mod-pool-ipam.html) in the *Amazon VPC IPAM User Guide*.

## Request Parameters
<a name="API_ModifyIpamPool_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AddAllocationResourceTag.N**
Add tag allocation rules to a pool. For more information about allocation rules, see [Create a top-level pool](https://docs.aws.amazon.com/vpc/latest/ipam/create-top-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: Array of [RequestIpamResourceTag](API_RequestIpamResourceTag.md) objects
Required: No

 **AllocationDefaultNetmaskLength**
The default netmask length for allocations added to this pool. If, for example, the CIDR assigned to this pool is 10.0.0.0/8 and you enter 16 here, new allocations will default to 10.0.0.0/16.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 128.
Required: No

 **AllocationMaxNetmaskLength**
The maximum netmask length possible for CIDR allocations in this IPAM pool to be compliant. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.The maximum netmask length must be greater than the minimum netmask length.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 128.
Required: No

 **AllocationMinNetmaskLength**
The minimum netmask length required for CIDR allocations in this IPAM pool to be compliant. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128. The minimum netmask length must be less than the maximum netmask length.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 128.
Required: No

 **AutoImport**
If true, IPAM will continuously look for resources within the CIDR range of this pool and automatically import them as allocations into your IPAM. The CIDRs that will be allocated for these resources must not already be allocated to other resources in order for the import to succeed. IPAM will import a CIDR regardless of its compliance with the pool's allocation rules, so a resource might be imported and subsequently marked as noncompliant. If IPAM discovers multiple CIDRs that overlap, IPAM will import the largest CIDR only. If IPAM discovers multiple CIDRs with matching CIDRs, IPAM will randomly import one of them only.
A locale must be set on the pool for this feature to work.
Type: Boolean
Required: No

 **ClearAllocationDefaultNetmaskLength**
Clear the default netmask length allocation rule for this pool.
Type: Boolean
Required: No

 **Description**
The description of the IPAM pool you want to modify.
Type: String
Required: No

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamPoolId**
The ID of the IPAM pool you want to modify.
Type: String
Required: Yes

 **RemoveAllocationResourceTag.N**
Remove tag allocation rules from a pool.
Type: Array of [RequestIpamResourceTag](API_RequestIpamResourceTag.md) objects
Required: No

## Response Elements
<a name="API_ModifyIpamPool_ResponseElements"></a>

The following elements are returned by the service.

 **ipamPool**
The results of the modification.
Type: [IpamPool](API_IpamPool.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ModifyIpamPool_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyIpamPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyIpamPool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyIpamPool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyIpamPool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyIpamPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyIpamPool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyIpamPool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyIpamPool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyIpamPool)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyIpamPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyIpamPool)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
