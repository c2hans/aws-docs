---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AcceleratorPartitionConfig.html
---

# AcceleratorPartitionConfig
<a name="API_AcceleratorPartitionConfig"></a>

Configuration for allocating accelerator partitions.

## Contents
<a name="API_AcceleratorPartitionConfig_Contents"></a>

 ** Count **   <a name="sagemaker-Type-AcceleratorPartitionConfig-Count"></a>
The number of accelerator partitions to allocate with the specified partition type. If you don't specify a value for vCPU and MemoryInGiB, SageMaker AI automatically allocates ratio-based values for those parameters based on the accelerator partition count you provide.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000000.
Required: Yes

 ** Type **   <a name="sagemaker-Type-AcceleratorPartitionConfig-Type"></a>
The Multi-Instance GPU (MIG) profile type that defines the partition configuration. The profile specifies the compute and memory allocation for each partition instance. The available profile types depend on the instance type specified in the compute quota configuration.
Type: String
Valid Values: `mig-1g.5gb | mig-1g.10gb | mig-1g.18gb | mig-1g.20gb | mig-1g.23gb | mig-1g.35gb | mig-1g.45gb | mig-1g.47gb | mig-2g.10gb | mig-2g.20gb | mig-2g.35gb | mig-2g.45gb | mig-2g.47gb | mig-3g.20gb | mig-3g.40gb | mig-3g.71gb | mig-3g.90gb | mig-3g.93gb | mig-4g.20gb | mig-4g.40gb | mig-4g.71gb | mig-4g.90gb | mig-4g.93gb | mig-7g.40gb | mig-7g.80gb | mig-7g.141gb | mig-7g.180gb | mig-7g.186gb`
Required: Yes

## See Also
<a name="API_AcceleratorPartitionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AcceleratorPartitionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AcceleratorPartitionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AcceleratorPartitionConfig)
