---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribedWebAppVpcConfig.html
---

# DescribedWebAppVpcConfig
<a name="API_DescribedWebAppVpcConfig"></a>

Contains the VPC configuration details for a web app endpoint, including the VPC identifier, subnet IDs, and VPC endpoint ID used for hosting the endpoint.

## Contents
<a name="API_DescribedWebAppVpcConfig_Contents"></a>

 ** SubnetIds **   <a name="TransferFamily-Type-DescribedWebAppVpcConfig-SubnetIds"></a>
The list of subnet IDs within the VPC where the web app endpoint is deployed. These subnets must be in the same VPC and provide network connectivity for the endpoint.
Type: Array of strings
Required: No

 ** VpcEndpointId **   <a name="TransferFamily-Type-DescribedWebAppVpcConfig-VpcEndpointId"></a>
The identifier of the VPC endpoint created for the web app.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `vpce-[0-9a-f]{17}`
Required: No

 ** VpcId **   <a name="TransferFamily-Type-DescribedWebAppVpcConfig-VpcId"></a>
The identifier of the VPC where the web app endpoint is hosted.
Type: String
Required: No

## See Also
<a name="API_DescribedWebAppVpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribedWebAppVpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribedWebAppVpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribedWebAppVpcConfig)
