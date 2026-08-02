---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-tieredstorageconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster TieredStorageConfig
<a name="aws-properties-sagemaker-cluster-tieredstorageconfig"></a>

Defines the configuration for managed tier checkpointing in a HyperPod cluster. Managed tier checkpointing uses multiple storage tiers, including cluster CPU memory, to provide faster checkpoint operations and improved fault tolerance for large-scale model training. The system automatically saves checkpoints at high frequency to memory and periodically persists them to durable storage, like Amazon S3.

## Syntax
<a name="aws-properties-sagemaker-cluster-tieredstorageconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-tieredstorageconfig-syntax.json"></a>

```
{
  "[InstanceMemoryAllocationPercentage](#cfn-sagemaker-cluster-tieredstorageconfig-instancememoryallocationpercentage)" : {{Integer}},
  "[Mode](#cfn-sagemaker-cluster-tieredstorageconfig-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-tieredstorageconfig-syntax.yaml"></a>

```
  [InstanceMemoryAllocationPercentage](#cfn-sagemaker-cluster-tieredstorageconfig-instancememoryallocationpercentage): {{Integer}}
  [Mode](#cfn-sagemaker-cluster-tieredstorageconfig-mode): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-tieredstorageconfig-properties"></a>

`InstanceMemoryAllocationPercentage`  <a name="cfn-sagemaker-cluster-tieredstorageconfig-instancememoryallocationpercentage"></a>
The percentage (int) of cluster memory to allocate for checkpointing.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-sagemaker-cluster-tieredstorageconfig-mode"></a>
Specifies whether managed tier checkpointing is enabled or disabled for the HyperPod cluster. When set to `Enable`, the system installs a memory management daemon that provides disaggregated memory as a service for checkpoint storage. When set to `Disable`, the feature is turned off and the memory management daemon is removed from the cluster.
*Required*: Yes
*Type*: String
*Allowed values*: `Enable | Disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
