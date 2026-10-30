---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_SharingStrategy.html
---

# SharingStrategy
<a name="API_SharingStrategy"></a>

The strategy that a container uses to share a GPU with other containers. Specify exactly one member.

## Contents
<a name="API_SharingStrategy_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** nvidiaMps **   <a name="ECS-Type-SharingStrategy-nvidiaMps"></a>
Shares a GPU between containers by using NVIDIA Multi-Process Service (MPS). You specify the GPU memory to allocate to the container and, optionally, the maximum percentage of the GPU's compute capacity that the container can use.
Type: [NvidiaMpsAllocation](API_NvidiaMpsAllocation.md) object
Required: No

## See Also
<a name="API_SharingStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/SharingStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/SharingStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/SharingStrategy)
