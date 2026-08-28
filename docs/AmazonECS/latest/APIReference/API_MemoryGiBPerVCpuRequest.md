---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_MemoryGiBPerVCpuRequest.html
---

# MemoryGiBPerVCpuRequest
<a name="API_MemoryGiBPerVCpuRequest"></a>

The minimum and maximum amount of memory per vCPU in gibibytes (GiB). This helps ensure that instance types have the appropriate memory-to-CPU ratio for your workloads.

## Contents
<a name="API_MemoryGiBPerVCpuRequest_Contents"></a>

 ** max **   <a name="ECS-Type-MemoryGiBPerVCpuRequest-max"></a>
The maximum amount of memory per vCPU in GiB. Instance types with a higher memory-to-vCPU ratio are excluded from selection.
Type: Double
Required: No

 ** min **   <a name="ECS-Type-MemoryGiBPerVCpuRequest-min"></a>
The minimum amount of memory per vCPU in GiB. Instance types with a lower memory-to-vCPU ratio are excluded from selection.
Type: Double
Required: No

## See Also
<a name="API_MemoryGiBPerVCpuRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/MemoryGiBPerVCpuRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/MemoryGiBPerVCpuRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/MemoryGiBPerVCpuRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
