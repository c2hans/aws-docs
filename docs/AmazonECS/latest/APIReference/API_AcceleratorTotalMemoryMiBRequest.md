---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_AcceleratorTotalMemoryMiBRequest.html
---

# AcceleratorTotalMemoryMiBRequest
<a name="API_AcceleratorTotalMemoryMiBRequest"></a>

The minimum and maximum total accelerator memory in mebibytes (MiB) for instance type selection. This is important for GPU workloads that require specific amounts of video memory.

## Contents
<a name="API_AcceleratorTotalMemoryMiBRequest_Contents"></a>

 ** max **   <a name="ECS-Type-AcceleratorTotalMemoryMiBRequest-max"></a>
The maximum total accelerator memory in MiB. Instance types with more accelerator memory are excluded from selection.
Type: Integer
Required: No

 ** min **   <a name="ECS-Type-AcceleratorTotalMemoryMiBRequest-min"></a>
The minimum total accelerator memory in MiB. Instance types with less accelerator memory are excluded from selection.
Type: Integer
Required: No

## See Also
<a name="API_AcceleratorTotalMemoryMiBRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/AcceleratorTotalMemoryMiBRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/AcceleratorTotalMemoryMiBRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/AcceleratorTotalMemoryMiBRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
