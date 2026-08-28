---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RecommendationJobVpcConfig.html
---

# RecommendationJobVpcConfig
<a name="API_RecommendationJobVpcConfig"></a>

Inference Recommender provisions SageMaker endpoints with access to VPC in the inference recommendation job.

## Contents
<a name="API_RecommendationJobVpcConfig_Contents"></a>

 ** SecurityGroupIds **   <a name="sagemaker-Type-RecommendationJobVpcConfig-SecurityGroupIds"></a>
The VPC security group IDs. IDs have the form of `sg-xxxxxxxx`. Specify the security groups for the VPC that is specified in the `Subnets` field.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`
Required: Yes

 ** Subnets **   <a name="sagemaker-Type-RecommendationJobVpcConfig-Subnets"></a>
The ID of the subnets in the VPC to which you want to connect your model.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`
Required: Yes

## See Also
<a name="API_RecommendationJobVpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RecommendationJobVpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RecommendationJobVpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RecommendationJobVpcConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
