---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AcceleratorSelection.html
---

# AcceleratorSelection
<a name="API_AcceleratorSelection"></a>

Describes a specific GPU accelerator required for an Amazon Elastic Compute Cloud worker host.

## Contents
<a name="API_AcceleratorSelection_Contents"></a>

 ** name **   <a name="deadlinecloud-Type-AcceleratorSelection-name"></a>
The name of the chip used by the GPU accelerator.
The available GPU accelerators are:
+  `t4` - NVIDIA T4 Tensor Core GPU (16 GiB memory)
+  `a10g` - NVIDIA A10G Tensor Core GPU (24 GiB memory)
+  `l4` - NVIDIA L4 Tensor Core GPU (24 GiB memory)
+  `l40s` - NVIDIA L40S Tensor Core GPU (48 GiB memory)
+  `rtx-pro-server-6000` - NVIDIA RTX PRO Server 6000 GPU (96 GiB memory)
Type: String
Valid Values: `t4 | a10g | l4 | l40s | rtx-pro-server-6000`
Required: Yes

 ** runtime **   <a name="deadlinecloud-Type-AcceleratorSelection-runtime"></a>
Specifies the runtime driver to use for the GPU accelerator. You must use the same runtime for all GPUs in a fleet.
You can choose from the following runtimes:
+  `latest` - Use the latest runtime available for the chip. If you specify `latest` and a new version of the runtime is released, the new version of the runtime is used.
+  `grid:r580` - [NVIDIA vGPU software 19](https://docs.nvidia.com/vgpu/19.0/index.html)
+  `grid:r570` - [NVIDIA vGPU software 18](https://docs.nvidia.com/vgpu/18.0/index.html)
+  `grid:r535` - [NVIDIA vGPU software 16](https://docs.nvidia.com/vgpu/16.0/index.html)
If you don't specify a runtime, AWS Deadline Cloud uses `latest` as the default. However, if you have multiple accelerators and specify `latest` for some and leave others blank, AWS Deadline Cloud raises an exception.
Not all runtimes are compatible with all accelerator types:
+  `t4` and `a10g`: Support all runtimes (`grid:r580`, `grid:r570`, `grid:r535`)
+  `l4` and `l40s`: Only support `grid:r570` and newer
+  `rtx-pro-server-6000`: Only supports `grid:r580`
All accelerators in a fleet must use the same runtime version. You cannot mix different runtime versions within a single fleet.
When you specify `latest`, it resolves to `grid:r580` for all currently supported accelerators.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_AcceleratorSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AcceleratorSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AcceleratorSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AcceleratorSelection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
