---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MoveByoipCidrToIpam.html
---

# MoveByoipCidrToIpam
<a name="API_MoveByoipCidrToIpam"></a>

Move a BYOIPv4 CIDR to IPAM from a public IPv4 pool.

If you already have a BYOIPv4 CIDR with AWS, you can move the CIDR to IPAM from a public IPv4 pool. You cannot move an IPv6 CIDR to IPAM. If you are bringing a new IP address to AWS for the first time, complete the steps in [Tutorial: BYOIP address CIDRs to IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam.html).

## Request Parameters
<a name="API_MoveByoipCidrToIpam_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Cidr**
The BYOIP CIDR.
Type: String
Required: Yes

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamPoolId**
The IPAM pool ID.
Type: String
Required: Yes

 **IpamPoolOwner**
The AWS account ID of the owner of the IPAM pool.
Type: String
Required: Yes

## Response Elements
<a name="API_MoveByoipCidrToIpam_ResponseElements"></a>

The following elements are returned by the service.

 **byoipCidr**
The BYOIP CIDR.
Type: [ByoipCidr](API_ByoipCidr.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_MoveByoipCidrToIpam_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_MoveByoipCidrToIpam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/MoveByoipCidrToIpam)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/MoveByoipCidrToIpam)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/MoveByoipCidrToIpam)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/MoveByoipCidrToIpam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/MoveByoipCidrToIpam)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/MoveByoipCidrToIpam)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/MoveByoipCidrToIpam)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/MoveByoipCidrToIpam)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/MoveByoipCidrToIpam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/MoveByoipCidrToIpam)
