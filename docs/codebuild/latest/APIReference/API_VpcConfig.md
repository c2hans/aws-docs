---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_VpcConfig.html
---

# VpcConfig
<a name="API_VpcConfig"></a>

Information about the VPC configuration that AWS CodeBuild accesses.

## Contents
<a name="API_VpcConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** securityGroupIds **   <a name="CodeBuild-Type-VpcConfig-securityGroupIds"></a>
A list of one or more security groups IDs in your Amazon VPC.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1.
Required: No

 ** subnets **   <a name="CodeBuild-Type-VpcConfig-subnets"></a>
A list of one or more subnet IDs in your Amazon VPC.
Type: Array of strings
Array Members: Maximum number of 16 items.
Length Constraints: Minimum length of 1.
Required: No

 ** vpcId **   <a name="CodeBuild-Type-VpcConfig-vpcId"></a>
The ID of the Amazon VPC.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_VpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/VpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/VpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/VpcConfig)
