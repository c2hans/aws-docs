---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_MemoryMiBRequest.html
---

# MemoryMiBRequest
<a name="API_MemoryMiBRequest"></a>

The minimum and maximum amount of memory in mebibytes (MiB) for instance type selection. This ensures that selected instance types have adequate memory for your workloads.

## Contents
<a name="API_MemoryMiBRequest_Contents"></a>

 ** min **   <a name="ECS-Type-MemoryMiBRequest-min"></a>
The minimum amount of memory in MiB. Instance types with less memory than this value are excluded from selection.
Type: Integer
Required: Yes

 ** max **   <a name="ECS-Type-MemoryMiBRequest-max"></a>
The maximum amount of memory in MiB. Instance types with more memory than this value are excluded from selection.
Type: Integer
Required: No

## See Also
<a name="API_MemoryMiBRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/MemoryMiBRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/MemoryMiBRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/MemoryMiBRequest)
