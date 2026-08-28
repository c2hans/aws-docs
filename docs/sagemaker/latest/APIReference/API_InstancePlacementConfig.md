---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InstancePlacementConfig.html
---

# InstancePlacementConfig
<a name="API_InstancePlacementConfig"></a>

Configuration for how instances are placed and allocated within UltraServers. This is only applicable for UltraServer capacity.

## Contents
<a name="API_InstancePlacementConfig_Contents"></a>

 ** EnableMultipleJobs **   <a name="sagemaker-Type-InstancePlacementConfig-EnableMultipleJobs"></a>
If set to true, allows multiple jobs to share the same UltraServer instances. If set to false, ensures this job's instances are placed on an UltraServer exclusively, with no other jobs sharing the same UltraServer. Default is false.
Type: Boolean
Required: No

 ** PlacementSpecifications **   <a name="sagemaker-Type-InstancePlacementConfig-PlacementSpecifications"></a>
A list of specifications for how instances should be placed on specific UltraServers. Maximum of 10 items is supported.
Type: Array of [PlacementSpecification](API_PlacementSpecification.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_InstancePlacementConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InstancePlacementConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InstancePlacementConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InstancePlacementConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
