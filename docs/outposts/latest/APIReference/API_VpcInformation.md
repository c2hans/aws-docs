---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_VpcInformation.html
---

# VpcInformation
<a name="API_VpcInformation"></a>

Information about a VPC used for private connectivity, including its subnets and an associated VPC endpoint.

## Contents
<a name="API_VpcInformation_Contents"></a>

 ** SubnetIds **   <a name="outposts-Type-VpcInformation-SubnetIds"></a>
The IDs of the subnets associated with the VPC endpoint. Currently, only one subnet is supported.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `[a-z0-9-]+`
Required: No

 ** VpcEndpointId **   <a name="outposts-Type-VpcInformation-VpcEndpointId"></a>
The ID of the interface VPC endpoint for the AWS Outposts service. When specified, the endpoint must be in the `available` state and the specified subnets must be associated with it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `^vpce-[a-f0-9]+$`
Required: No

 ** VpcId **   <a name="outposts-Type-VpcInformation-VpcId"></a>
The ID of the VPC used for private connectivity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `[a-z0-9-]+`
Required: No

## See Also
<a name="API_VpcInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/VpcInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/VpcInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/VpcInformation)
