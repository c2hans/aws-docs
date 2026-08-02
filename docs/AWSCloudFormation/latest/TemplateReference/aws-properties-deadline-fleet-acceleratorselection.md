---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-acceleratorselection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet AcceleratorSelection
<a name="aws-properties-deadline-fleet-acceleratorselection"></a>

Describes a specific GPU accelerator required for an Amazon Elastic Compute Cloud worker host.

## Syntax
<a name="aws-properties-deadline-fleet-acceleratorselection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-acceleratorselection-syntax.json"></a>

```
{
  "[Name](#cfn-deadline-fleet-acceleratorselection-name)" : {{String}},
  "[Runtime](#cfn-deadline-fleet-acceleratorselection-runtime)" : {{String}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-acceleratorselection-syntax.yaml"></a>

```
  [Name](#cfn-deadline-fleet-acceleratorselection-name): {{String}}
  [Runtime](#cfn-deadline-fleet-acceleratorselection-runtime): {{String}}
```

## Properties
<a name="aws-properties-deadline-fleet-acceleratorselection-properties"></a>

`Name`  <a name="cfn-deadline-fleet-acceleratorselection-name"></a>
The name of the chip used by the GPU accelerator.
The available GPU accelerators are:
+ `t4` - NVIDIA T4 Tensor Core GPU (16 GiB memory)
+ `a10g` - NVIDIA A10G Tensor Core GPU (24 GiB memory)
+ `l4` - NVIDIA L4 Tensor Core GPU (24 GiB memory)
+ `l40s` - NVIDIA L40S Tensor Core GPU (48 GiB memory)
+ `rtx-pro-server-6000` - NVIDIA RTX PRO Server 6000 GPU (96 GiB memory)
*Required*: Yes
*Type*: String
*Allowed values*: `t4 | a10g | l4 | l40s | rtx-pro-server-6000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Runtime`  <a name="cfn-deadline-fleet-acceleratorselection-runtime"></a>
Specifies the runtime driver to use for the GPU accelerator. You must use the same runtime for all GPUs in a fleet.
You can choose from the following runtimes:
+ `latest` - Use the latest runtime available for the chip. If you specify `latest` and a new version of the runtime is released, the new version of the runtime is used.
+ `grid:r580` - [NVIDIA vGPU software 19](https://docs.nvidia.com/vgpu/19.0/index.html)
+ `grid:r570` - [NVIDIA vGPU software 18](https://docs.nvidia.com/vgpu/18.0/index.html)
+ `grid:r535` - [NVIDIA vGPU software 16](https://docs.nvidia.com/vgpu/16.0/index.html)
If you don't specify a runtime, AWS Deadline Cloud uses `latest` as the default. However, if you have multiple accelerators and specify `latest` for some and leave others blank, AWS Deadline Cloud raises an exception.
Not all runtimes are compatible with all accelerator types:
+ `t4` and `a10g`: Support all runtimes (`grid:r580`, `grid:r570`, `grid:r535`)
+ `l4` and `l40s`: Only support `grid:r570` and newer
+ `rtx-pro-server-6000`: Only supports `grid:r580`
All accelerators in a fleet must use the same runtime version. You cannot mix different runtime versions within a single fleet.
When you specify `latest`, it resolves to `grid:r580` for all currently supported accelerators.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
