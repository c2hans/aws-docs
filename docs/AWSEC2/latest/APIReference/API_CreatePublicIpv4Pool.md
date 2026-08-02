---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreatePublicIpv4Pool.html
---

# CreatePublicIpv4Pool
<a name="API_CreatePublicIpv4Pool"></a>

Creates a public IPv4 address pool. A public IPv4 pool is an EC2 IP address pool required for the public IPv4 CIDRs that you own and bring to AWS to manage with IPAM. IPv6 addresses you bring to AWS, however, use IPAM pools only. To monitor the status of pool creation, use [DescribePublicIpv4Pools](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePublicIpv4Pools.html).

## Request Parameters
<a name="API_CreatePublicIpv4Pool_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **NetworkBorderGroup**
The Availability Zone (AZ) or Local Zone (LZ) network border group that the resource that the IP address is assigned to is in. Defaults to an AZ network border group. For more information on available Local Zones, see [Local Zone availability](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-zone-avail) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 **TagSpecification.N**
The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreatePublicIpv4Pool_ResponseElements"></a>

The following elements are returned by the service.

 **poolId**
The ID of the public IPv4 pool.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreatePublicIpv4Pool_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreatePublicIpv4Pool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreatePublicIpv4Pool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreatePublicIpv4Pool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreatePublicIpv4Pool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreatePublicIpv4Pool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreatePublicIpv4Pool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreatePublicIpv4Pool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreatePublicIpv4Pool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreatePublicIpv4Pool)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreatePublicIpv4Pool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreatePublicIpv4Pool)
