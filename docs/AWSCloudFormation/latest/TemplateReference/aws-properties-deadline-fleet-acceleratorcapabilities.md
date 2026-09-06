---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-acceleratorcapabilities.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet AcceleratorCapabilities
<a name="aws-properties-deadline-fleet-acceleratorcapabilities"></a>

Provides information about the GPU accelerators used for jobs processed by a fleet.

**Important**
Accelerator capabilities cannot be used with wait-and-save fleets. If you specify accelerator capabilities, you must use either spot or on-demand instance market options.

**Note**
Each accelerator type maps to specific EC2 instance families:
`t4`: Uses G4dn instance family
`a10g`: Uses G5 instance family
`l4`: Uses G6 and Gr6 instance families
`l40s`: Uses G6e instance family
`rtx-pro-server-6000`: Uses G7e instance family

## Syntax
<a name="aws-properties-deadline-fleet-acceleratorcapabilities-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-acceleratorcapabilities-syntax.json"></a>

```
{
  "[Count](#cfn-deadline-fleet-acceleratorcapabilities-count)" : {{AcceleratorCountRange}},
  "[Selections](#cfn-deadline-fleet-acceleratorcapabilities-selections)" : {{[ AcceleratorSelection, ... ]}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-acceleratorcapabilities-syntax.yaml"></a>

```
  [Count](#cfn-deadline-fleet-acceleratorcapabilities-count): {{
    AcceleratorCountRange}}
  [Selections](#cfn-deadline-fleet-acceleratorcapabilities-selections): {{
    - AcceleratorSelection}}
```

## Properties
<a name="aws-properties-deadline-fleet-acceleratorcapabilities-properties"></a>

`Count`  <a name="cfn-deadline-fleet-acceleratorcapabilities-count"></a>
The number of GPU accelerators specified for worker hosts in this fleet.
You must specify either `acceleratorCapabilities.count.max` or `allowedInstanceTypes` when using accelerator capabilities. If you don't specify a maximum count, AWS Deadline Cloud uses the instance types you specify in `allowedInstanceTypes` to determine the maximum number of accelerators.
*Required*: No
*Type*: [AcceleratorCountRange](aws-properties-deadline-fleet-acceleratorcountrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Selections`  <a name="cfn-deadline-fleet-acceleratorcapabilities-selections"></a>
A list of accelerator capabilities requested for this fleet. Only Amazon Elastic Compute Cloud instances that provide these capabilities will be used. For example, if you specify both L4 and T4 chips, AWS Deadline Cloud will use Amazon EC2 instances that have either the L4 or the T4 chip installed.
+ You must specify at least one accelerator selection.
+ You cannot specify the same accelerator name multiple times in the selections list.
+ All accelerators in the selections must use the same runtime version.
*Required*: Yes
*Type*: Array of [AcceleratorSelection](aws-properties-deadline-fleet-acceleratorselection.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
