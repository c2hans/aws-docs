---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ContainerConfiguration.html
---

# ContainerConfiguration
<a name="API_ContainerConfiguration"></a>

 Describes the container configurations within the tasks of your Amazon ECS service.

## Contents
<a name="API_ContainerConfiguration_Contents"></a>

 ** containerName **   <a name="computeoptimizer-Type-ContainerConfiguration-containerName"></a>
 The name of the container.
Type: String
Required: No

 ** cpu **   <a name="computeoptimizer-Type-ContainerConfiguration-cpu"></a>
 The number of CPU units reserved for the container.
Type: Integer
Required: No

 ** memorySizeConfiguration **   <a name="computeoptimizer-Type-ContainerConfiguration-memorySizeConfiguration"></a>
 The memory size configurations for the container.
Type: [MemorySizeConfiguration](API_MemorySizeConfiguration.md) object
Required: No

## See Also
<a name="API_ContainerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/ContainerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/ContainerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/ContainerConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
