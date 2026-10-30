---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GpuDevice.html
---

# GpuDevice
<a name="API_GpuDevice"></a>

The state of a GPU on a container instance, including its sharing mode and the memory that's available for new containers.

## Contents
<a name="API_GpuDevice_Contents"></a>

 ** containerCount **   <a name="ECS-Type-GpuDevice-containerCount"></a>
The number of containers that Amazon ECS assigned to the GPU. This value is `0` when the sharing mode is `IDLE` and `1` when the sharing mode is `DEDICATED`. Amazon ECS counts the containers that it assigned to the GPU, not the processes that are running on it.
Type: Integer
Required: No

 ** gpuId **   <a name="ECS-Type-GpuDevice-gpuId"></a>
The ID of the GPU. This ID matches the GPU IDs in the `gpuIds` of the containers that Amazon ECS assigned to the GPU.
Type: String
Required: No

 ** remainingMemoryInMiB **   <a name="ECS-Type-GpuDevice-remainingMemoryInMiB"></a>
The amount of GPU memory, in MiB, that's available to allocate to new containers that use the `nvidiaMps` sharing strategy. Amazon ECS calculates this value from the memory that it allocated to containers on the GPU, not from the memory that the containers use.
Type: Integer
Required: No

 ** sharingMode **   <a name="ECS-Type-GpuDevice-sharingMode"></a>
How the GPU is shared between containers.
Valid values:
+  `IDLE` - No containers are assigned to the GPU, and all of its memory is available.
+  `NVIDIA_MPS` - One or more containers share the GPU by using NVIDIA Multi-Process Service (MPS).
+  `DEDICATED` - One container has exclusive use of the GPU.
Type: String
Valid Values: `IDLE | NVIDIA_MPS | DEDICATED`
Required: No

 ** totalMemoryInMiB **   <a name="ECS-Type-GpuDevice-totalMemoryInMiB"></a>
The total amount of GPU memory, in MiB, that the Amazon ECS container agent reported for the GPU. This is the memory that's available to containers, and it can be less than the nominal memory of the GPU.
Type: Integer
Required: No

## See Also
<a name="API_GpuDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GpuDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GpuDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GpuDevice)
