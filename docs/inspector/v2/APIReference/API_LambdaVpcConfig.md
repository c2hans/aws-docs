---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_LambdaVpcConfig.html
---

# LambdaVpcConfig
<a name="API_LambdaVpcConfig"></a>

The VPC security groups and subnets that are attached to an AWS Lambda function. For more information, see [VPC Settings](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html).

## Contents
<a name="API_LambdaVpcConfig_Contents"></a>

 ** securityGroupIds **   <a name="inspector2-Type-LambdaVpcConfig-securityGroupIds"></a>
The VPC security groups and subnets that are attached to an AWS Lambda function. For more information, see [VPC Settings](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Pattern: `sg-([a-z0-9]{8}|[a-z0-9]{17}|\*)`
Required: No

 ** subnetIds **   <a name="inspector2-Type-LambdaVpcConfig-subnetIds"></a>
A list of VPC subnet IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 16 items.
Pattern: `subnet-([a-z0-9]{8}|[a-z0-9]{17}|\*)`
Required: No

 ** vpcId **   <a name="inspector2-Type-LambdaVpcConfig-vpcId"></a>
The ID of the VPC.
Type: String
Pattern: `vpc-([a-z0-9]{8}|[a-z0-9]{17}|\*)`
Required: No

## See Also
<a name="API_LambdaVpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/LambdaVpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/LambdaVpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/LambdaVpcConfig)
