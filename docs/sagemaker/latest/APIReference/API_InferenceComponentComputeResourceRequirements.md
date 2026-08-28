---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceComponentComputeResourceRequirements.html
---

# InferenceComponentComputeResourceRequirements
<a name="API_InferenceComponentComputeResourceRequirements"></a>

Defines the compute resources to allocate to run a model, plus any adapter models, that you assign to an inference component. These resources include CPU cores, accelerators, and memory.

## Contents
<a name="API_InferenceComponentComputeResourceRequirements_Contents"></a>

 ** MinMemoryRequiredInMb **   <a name="sagemaker-Type-InferenceComponentComputeResourceRequirements-MinMemoryRequiredInMb"></a>
The minimum MB of memory to allocate to run a model that you assign to an inference component.
Type: Integer
Valid Range: Minimum value of 128.
Required: Yes

 ** MaxMemoryRequiredInMb **   <a name="sagemaker-Type-InferenceComponentComputeResourceRequirements-MaxMemoryRequiredInMb"></a>
The maximum MB of memory to allocate to run a model that you assign to an inference component.
Type: Integer
Valid Range: Minimum value of 128.
Required: No

 ** NumberOfAcceleratorDevicesRequired **   <a name="sagemaker-Type-InferenceComponentComputeResourceRequirements-NumberOfAcceleratorDevicesRequired"></a>
The number of accelerators to allocate to run a model that you assign to an inference component. Accelerators include GPUs and AWS Inferentia.
Type: Float
Valid Range: Minimum value of 1.
Required: No

 ** NumberOfCpuCoresRequired **   <a name="sagemaker-Type-InferenceComponentComputeResourceRequirements-NumberOfCpuCoresRequired"></a>
The number of CPU cores to allocate to run a model that you assign to an inference component.
Type: Float
Valid Range: Minimum value of 0.25.
Required: No

## See Also
<a name="API_InferenceComponentComputeResourceRequirements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceComponentComputeResourceRequirements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceComponentComputeResourceRequirements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceComponentComputeResourceRequirements)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
