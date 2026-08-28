---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_NeoVpcConfig.html
---

# NeoVpcConfig
<a name="API_NeoVpcConfig"></a>

The [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) configuration object that specifies the VPC that you want the compilation jobs to connect to. For more information on controlling access to your Amazon S3 buckets used for compilation job, see [Give Amazon SageMaker AI Compilation Jobs Access to Resources in Your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-vpc.html).

## Contents
<a name="API_NeoVpcConfig_Contents"></a>

 ** SecurityGroupIds **   <a name="sagemaker-Type-NeoVpcConfig-SecurityGroupIds"></a>
The VPC security group IDs. IDs have the form of `sg-xxxxxxxx`. Specify the security groups for the VPC that is specified in the `Subnets` field.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`
Required: Yes

 ** Subnets **   <a name="sagemaker-Type-NeoVpcConfig-Subnets"></a>
The ID of the subnets in the VPC that you want to connect the compilation job to for accessing the model in Amazon S3.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`
Required: Yes

## See Also
<a name="API_NeoVpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/NeoVpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/NeoVpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/NeoVpcConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
