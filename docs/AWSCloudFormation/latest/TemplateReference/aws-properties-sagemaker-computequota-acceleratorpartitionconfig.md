---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-computequota-acceleratorpartitionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ComputeQuota AcceleratorPartitionConfig
<a name="aws-properties-sagemaker-computequota-acceleratorpartitionconfig"></a>

Configuration for allocating accelerator partitions.

## Syntax
<a name="aws-properties-sagemaker-computequota-acceleratorpartitionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-computequota-acceleratorpartitionconfig-syntax.json"></a>

```
{
  "[Count](#cfn-sagemaker-computequota-acceleratorpartitionconfig-count)" : {{Integer}},
  "[Type](#cfn-sagemaker-computequota-acceleratorpartitionconfig-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-computequota-acceleratorpartitionconfig-syntax.yaml"></a>

```
  [Count](#cfn-sagemaker-computequota-acceleratorpartitionconfig-count): {{Integer}}
  [Type](#cfn-sagemaker-computequota-acceleratorpartitionconfig-type): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-computequota-acceleratorpartitionconfig-properties"></a>

`Count`  <a name="cfn-sagemaker-computequota-acceleratorpartitionconfig-count"></a>
The number of accelerator partitions to allocate with the specified partition type. If you don't specify a value for vCPU and MemoryInGiB, SageMaker AI automatically allocates ratio-based values for those parameters based on the accelerator partition count you provide.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `10000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-sagemaker-computequota-acceleratorpartitionconfig-type"></a>
The Multi-Instance GPU (MIG) profile type that defines the partition configuration. The profile specifies the compute and memory allocation for each partition instance. The available profile types depend on the instance type specified in the compute quota configuration.
*Required*: Yes
*Type*: String
*Allowed values*: `mig-1g.5gb | mig-1g.10gb | mig-1g.18gb | mig-1g.20gb | mig-1g.23gb | mig-1g.35gb | mig-1g.45gb | mig-1g.47gb | mig-2g.10gb | mig-2g.20gb | mig-2g.35gb | mig-2g.45gb | mig-2g.47gb | mig-3g.20gb | mig-3g.40gb | mig-3g.71gb | mig-3g.90gb | mig-3g.93gb | mig-4g.20gb | mig-4g.40gb | mig-4g.71gb | mig-4g.90gb | mig-4g.93gb | mig-7g.40gb | mig-7g.80gb | mig-7g.141gb | mig-7g.180gb | mig-7g.186gb`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
