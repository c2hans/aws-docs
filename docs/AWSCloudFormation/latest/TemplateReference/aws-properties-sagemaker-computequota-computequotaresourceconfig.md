---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-computequota-computequotaresourceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ComputeQuota ComputeQuotaResourceConfig
<a name="aws-properties-sagemaker-computequota-computequotaresourceconfig"></a>

Configuration of the resources used for the compute allocation definition.

## Syntax
<a name="aws-properties-sagemaker-computequota-computequotaresourceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-computequota-computequotaresourceconfig-syntax.json"></a>

```
{
  "[AcceleratorPartition](#cfn-sagemaker-computequota-computequotaresourceconfig-acceleratorpartition)" : {{AcceleratorPartitionConfig}},
  "[Accelerators](#cfn-sagemaker-computequota-computequotaresourceconfig-accelerators)" : {{Integer}},
  "[Count](#cfn-sagemaker-computequota-computequotaresourceconfig-count)" : {{Integer}},
  "[InstanceType](#cfn-sagemaker-computequota-computequotaresourceconfig-instancetype)" : {{String}},
  "[MemoryInGiB](#cfn-sagemaker-computequota-computequotaresourceconfig-memoryingib)" : {{Number}},
  "[VCpu](#cfn-sagemaker-computequota-computequotaresourceconfig-vcpu)" : {{Number}}
}
```

### YAML
<a name="aws-properties-sagemaker-computequota-computequotaresourceconfig-syntax.yaml"></a>

```
  [AcceleratorPartition](#cfn-sagemaker-computequota-computequotaresourceconfig-acceleratorpartition): {{
    AcceleratorPartitionConfig}}
  [Accelerators](#cfn-sagemaker-computequota-computequotaresourceconfig-accelerators): {{Integer}}
  [Count](#cfn-sagemaker-computequota-computequotaresourceconfig-count): {{Integer}}
  [InstanceType](#cfn-sagemaker-computequota-computequotaresourceconfig-instancetype): {{String}}
  [MemoryInGiB](#cfn-sagemaker-computequota-computequotaresourceconfig-memoryingib): {{Number}}
  [VCpu](#cfn-sagemaker-computequota-computequotaresourceconfig-vcpu): {{Number}}
```

## Properties
<a name="aws-properties-sagemaker-computequota-computequotaresourceconfig-properties"></a>

`AcceleratorPartition`  <a name="cfn-sagemaker-computequota-computequotaresourceconfig-acceleratorpartition"></a>
The accelerator partition configuration for fractional GPU allocation.
*Required*: No
*Type*: [AcceleratorPartitionConfig](aws-properties-sagemaker-computequota-acceleratorpartitionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Accelerators`  <a name="cfn-sagemaker-computequota-computequotaresourceconfig-accelerators"></a>
The number of accelerators to allocate. If you don't specify a value for vCPU and MemoryInGiB, SageMaker AI automatically allocates ratio-based values for those parameters based on the number of accelerators you provide. For example, if you allocate 16 out of 32 total accelerators, SageMaker AI uses the ratio of 0.5 and allocates values to vCPU and MemoryInGiB.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `10000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Count`  <a name="cfn-sagemaker-computequota-computequotaresourceconfig-count"></a>
The number of instances to add to the instance group of a SageMaker HyperPod cluster.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `10000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceType`  <a name="cfn-sagemaker-computequota-computequotaresourceconfig-instancetype"></a>
The instance type of the instance group for the cluster.
*Required*: Yes
*Type*: String
*Allowed values*: `ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p5.4xlarge | ml.p6e-gb200.36xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.c5.large | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.12xlarge | ml.c5.18xlarge | ml.c5.24xlarge | ml.c5n.large | ml.c5n.2xlarge | ml.c5n.4xlarge | ml.c5n.9xlarge | ml.c5n.18xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.8xlarge | ml.m5.12xlarge | ml.m5.16xlarge | ml.m5.24xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.16xlarge | ml.g6.12xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.gr6.4xlarge | ml.gr6.8xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.16xlarge | ml.g6e.12xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.p6-b200.48xlarge | ml.trn2.3xlarge | ml.trn2.48xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.i3en.large | ml.i3en.xlarge | ml.i3en.2xlarge | ml.i3en.3xlarge | ml.i3en.6xlarge | ml.i3en.12xlarge | ml.i3en.24xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.r5d.16xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.p6-b300.48xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.c6g.medium | ml.c6g.large | ml.c6g.xlarge | ml.c6g.2xlarge | ml.c6g.4xlarge | ml.c6g.8xlarge | ml.c6g.12xlarge | ml.c6g.16xlarge | ml.c7g.medium | ml.c7g.large | ml.c7g.xlarge | ml.c7g.2xlarge | ml.c7g.4xlarge | ml.c7g.8xlarge | ml.c7g.12xlarge | ml.c7g.16xlarge | ml.c8g.medium | ml.c8g.large | ml.c8g.xlarge | ml.c8g.2xlarge | ml.c8g.4xlarge | ml.c8g.8xlarge | ml.c8g.12xlarge | ml.c8g.16xlarge | ml.c8g.24xlarge | ml.c8g.48xlarge | ml.c6a.large | ml.c6a.xlarge | ml.c6a.2xlarge | ml.c6a.4xlarge | ml.c6a.8xlarge | ml.c6a.12xlarge | ml.c6a.16xlarge | ml.c6a.24xlarge | ml.c6a.32xlarge | ml.c6a.48xlarge | ml.m6a.large | ml.m6a.xlarge | ml.m6a.2xlarge | ml.m6a.4xlarge | ml.m6a.8xlarge | ml.m6a.12xlarge | ml.m6a.16xlarge | ml.m6a.24xlarge | ml.m6a.32xlarge | ml.m6a.48xlarge | ml.m6g.medium | ml.m6g.large | ml.m6g.xlarge | ml.m6g.2xlarge | ml.m6g.4xlarge | ml.m6g.8xlarge | ml.m6g.12xlarge | ml.m6g.16xlarge | ml.m7g.medium | ml.m7g.large | ml.m7g.xlarge | ml.m7g.2xlarge | ml.m7g.4xlarge | ml.m7g.8xlarge | ml.m7g.12xlarge | ml.m7g.16xlarge | ml.m8g.medium | ml.m8g.large | ml.m8g.xlarge | ml.m8g.2xlarge | ml.m8g.4xlarge | ml.m8g.8xlarge | ml.m8g.12xlarge | ml.m8g.16xlarge | ml.m8g.24xlarge | ml.m8g.48xlarge | ml.g7.2xlarge | ml.g7.4xlarge | ml.g7.8xlarge | ml.g7.12xlarge | ml.g7.24xlarge | ml.g7.48xlarge`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemoryInGiB`  <a name="cfn-sagemaker-computequota-computequotaresourceconfig-memoryingib"></a>
The amount of memory in GiB to allocate. If you specify a value only for this parameter, SageMaker AI automatically allocates a ratio-based value for vCPU based on this memory that you provide. For example, if you allocate 200 out of 400 total memory in GiB, SageMaker AI uses the ratio of 0.5 and allocates values to vCPU. Accelerators are set to 0.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `10000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VCpu`  <a name="cfn-sagemaker-computequota-computequotaresourceconfig-vcpu"></a>
The number of vCPU to allocate. If you specify a value only for vCPU, SageMaker AI automatically allocates ratio-based values for MemoryInGiB based on this vCPU parameter. For example, if you allocate 20 out of 40 total vCPU, SageMaker AI uses the ratio of 0.5 and allocates values to MemoryInGiB. Accelerators are set to 0.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `10000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
