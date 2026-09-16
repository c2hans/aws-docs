---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ProvisionPublicIpv4PoolCidr.html
---

# ProvisionPublicIpv4PoolCidr
<a name="API_ProvisionPublicIpv4PoolCidr"></a>

Provision a CIDR to a public IPv4 pool.

For more information about IPAM, see [What is IPAM?](https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.

## Request Parameters
<a name="API_ProvisionPublicIpv4PoolCidr_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamPoolId**
The ID of the IPAM pool you would like to use to allocate this CIDR.
Type: String
Required: Yes

 **NetmaskLength**
The netmask length of the CIDR you would like to allocate to the public IPv4 pool. The least specific netmask length you can define is 24.
Type: Integer
Required: Yes

 **NetworkBorderGroup**
The Availability Zone (AZ) or Local Zone (LZ) network border group that the resource that the IP address is assigned to is in. Defaults to an AZ network border group. For more information on available Local Zones, see [Local Zone availability](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-zone-avail) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 **PoolId**
The ID of the public IPv4 pool you would like to use for this CIDR.
Type: String
Required: Yes

## Response Elements
<a name="API_ProvisionPublicIpv4PoolCidr_ResponseElements"></a>

The following elements are returned by the service.

 **poolAddressRange**
Information about the address range of the public IPv4 pool.
Type: [PublicIpv4PoolRange](API_PublicIpv4PoolRange.md) object

 **poolId**
The ID of the pool that you want to provision the CIDR to.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ProvisionPublicIpv4PoolCidr_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ProvisionPublicIpv4PoolCidr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ProvisionPublicIpv4PoolCidr)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ProvisionPublicIpv4PoolCidr)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ProvisionPublicIpv4PoolCidr)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ProvisionPublicIpv4PoolCidr)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ProvisionPublicIpv4PoolCidr)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ProvisionPublicIpv4PoolCidr)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ProvisionPublicIpv4PoolCidr)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ProvisionPublicIpv4PoolCidr)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ProvisionPublicIpv4PoolCidr)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ProvisionPublicIpv4PoolCidr)
