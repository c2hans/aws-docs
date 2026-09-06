---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_VpcConfigOutput.html
---

# VpcConfigOutput
<a name="API_VpcConfigOutput"></a>

If this canary is to test an endpoint in a VPC, this structure contains information about the subnets and security groups of the VPC endpoint. For more information, see [ Running a Canary in a VPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html).

## Contents
<a name="API_VpcConfigOutput_Contents"></a>

 ** Ipv6AllowedForDualStack **   <a name="synthetics-Type-VpcConfigOutput-Ipv6AllowedForDualStack"></a>
Indicates whether this canary allows outbound IPv6 traffic if it is connected to dual-stack subnets.
Type: Boolean
Required: No

 ** SecurityGroupIds **   <a name="synthetics-Type-VpcConfigOutput-SecurityGroupIds"></a>
The IDs of the security groups for this canary.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** SubnetIds **   <a name="synthetics-Type-VpcConfigOutput-SubnetIds"></a>
The IDs of the subnets where this canary is to run.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 16 items.
Required: No

 ** VpcId **   <a name="synthetics-Type-VpcConfigOutput-VpcId"></a>
The IDs of the VPC where this canary is to run.
Type: String
Required: No

## See Also
<a name="API_VpcConfigOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/VpcConfigOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/VpcConfigOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/VpcConfigOutput)
