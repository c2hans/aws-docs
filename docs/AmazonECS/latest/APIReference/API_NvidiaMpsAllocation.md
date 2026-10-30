---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NvidiaMpsAllocation.html
---

# NvidiaMpsAllocation
<a name="API_NvidiaMpsAllocation"></a>

The GPU memory and compute limits for a container that shares a GPU by using NVIDIA Multi-Process Service (MPS). Amazon ECS assigns the container a single GPU that has enough memory available. Other containers that use MPS can share the same GPU.

## Contents
<a name="API_NvidiaMpsAllocation_Contents"></a>

 ** memory **   <a name="ECS-Type-NvidiaMpsAllocation-memory"></a>
The amount of GPU memory, in MiB, to allocate to the container. Amazon ECS assigns the container a GPU that has at least the specified amount of memory available, and sets the `CUDA_MPS_PINNED_DEVICE_MEM_LIMIT` environment variable in the container to limit its memory to this amount. The memory must be available on a single GPU. If more than one container in a task uses `nvidiaMps`, Amazon ECS assigns them the same GPU, which must have enough memory available for all of them.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** maxComputePercent **   <a name="ECS-Type-NvidiaMpsAllocation-maxComputePercent"></a>
The maximum percentage of the GPU's compute capacity that the container can use. Amazon ECS sets the `CUDA_MPS_ACTIVE_THREAD_PERCENTAGE` environment variable in the container to this value. This value is a limit, not a reservation.
If you don't specify this parameter, Amazon ECS doesn't set `CUDA_MPS_ACTIVE_THREAD_PERCENTAGE`, and the active thread percentage of the MPS server on the container instance applies. By default, this is 100 percent.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## See Also
<a name="API_NvidiaMpsAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/NvidiaMpsAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/NvidiaMpsAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/NvidiaMpsAllocation)
