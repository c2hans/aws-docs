---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelShardingConfig.html
---

# ModelShardingConfig
<a name="API_ModelShardingConfig"></a>

Settings for the model sharding technique that's applied by a model optimization job.

## Contents
<a name="API_ModelShardingConfig_Contents"></a>

 ** Image **   <a name="sagemaker-Type-ModelShardingConfig-Image"></a>
The URI of an LMI DLC in Amazon ECR. SageMaker uses this image to run the optimization.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\S]+`
Required: No

 ** OverrideEnvironment **   <a name="sagemaker-Type-ModelShardingConfig-OverrideEnvironment"></a>
Environment variables that override the default ones in the model container.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 25 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `(?!\s*$).+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_ModelShardingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelShardingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelShardingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelShardingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
