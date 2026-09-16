---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIpam.html
---

# ModifyIpam
<a name="API_ModifyIpam"></a>

Modify the configurations of an IPAM.

## Request Parameters
<a name="API_ModifyIpam_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AddOperatingRegion.N**
Choose the operating Regions for the IPAM. Operating Regions are AWS Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the AWS Regions you select as operating Regions.
For more information about operating Regions, see [Create an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: Array of [AddIpamOperatingRegion](API_AddIpamOperatingRegion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 **Description**
The description of the IPAM you want to modify.
Type: String
Required: No

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EnablePrivateGua**
Enable this option to use your own GUA ranges as private IPv6 addresses. This option is disabled by default.
Type: Boolean
Required: No

 **IpamId**
The ID of the IPAM you want to modify.
Type: String
Required: Yes

 **MeteredAccount**
A metered account is an AWS account that is charged for active IP addresses managed in IPAM. For more information, see [Enable cost distribution](https://docs.aws.amazon.com/vpc/latest/ipam/ipam-enable-cost-distro.html) in the *Amazon VPC IPAM User Guide*.
Possible values:
+  `ipam-owner` (default): The AWS account which owns the IPAM is charged for all active IP addresses managed in IPAM.
+  `resource-owner`: The AWS account that owns the IP address is charged for the active IP address.
Type: String
Valid Values: `ipam-owner | resource-owner`
Required: No

 **RemoveOperatingRegion.N**
The operating Regions to remove.
Type: Array of [RemoveIpamOperatingRegion](API_RemoveIpamOperatingRegion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 **Tier**
IPAM is offered in a Free Tier and an Advanced Tier. For more information about the features available in each tier and the costs associated with the tiers, see [Amazon VPC pricing > IPAM tab](http://aws.amazon.com/vpc/pricing/).
Type: String
Valid Values: `free | advanced`
Required: No

## Response Elements
<a name="API_ModifyIpam_ResponseElements"></a>

The following elements are returned by the service.

 **ipam**
The results of the modification.
Type: [Ipam](API_Ipam.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ModifyIpam_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyIpam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyIpam)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyIpam)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyIpam)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyIpam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyIpam)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyIpam)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyIpam)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyIpam)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyIpam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyIpam)
