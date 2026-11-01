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

 ** AcceleratorPartitionType **   <a name="sagemaker-Type-InferenceComponentComputeResourceRequirements-AcceleratorPartitionType"></a>
The accelerator partition profile this inference component occupies; on NVIDIA GPUs this is a Multi-Instance GPU (MIG) profile such as `mig-3g.40gb`. It must be one of the partition profiles declared in the target endpoint's accelerator partition layout, and when set, `NumberOfAcceleratorDevicesRequired` must be `1`. This field is required when the endpoint's production variant has an accelerator partition layout. For endpoints without a layout, omit this field to place the inference component on a whole accelerator.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `mig-[0-9]+g\.[0-9]+gb([+-][a-z0-9.]+)*`
Required: No

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
