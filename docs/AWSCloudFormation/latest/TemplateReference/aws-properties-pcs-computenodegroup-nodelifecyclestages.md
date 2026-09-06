---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-computenodegroup-nodelifecyclestages.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::ComputeNodeGroup NodeLifecycleStages
<a name="aws-properties-pcs-computenodegroup-nodelifecyclestages"></a>

The stages of a compute node's lifecycle where you can configure scripts to run.

## Syntax
<a name="aws-properties-pcs-computenodegroup-nodelifecyclestages-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-computenodegroup-nodelifecyclestages-syntax.json"></a>

```
{
  "[NodeBootstrapped](#cfn-pcs-computenodegroup-nodelifecyclestages-nodebootstrapped)" : {{[ NodeLifecycleScript, ... ]}},
  "[NodeReady](#cfn-pcs-computenodegroup-nodelifecyclestages-nodeready)" : {{[ NodeLifecycleScript, ... ]}}
}
```

### YAML
<a name="aws-properties-pcs-computenodegroup-nodelifecyclestages-syntax.yaml"></a>

```
  [NodeBootstrapped](#cfn-pcs-computenodegroup-nodelifecyclestages-nodebootstrapped): {{
    - NodeLifecycleScript}}
  [NodeReady](#cfn-pcs-computenodegroup-nodelifecyclestages-nodeready): {{
    - NodeLifecycleScript}}
```

## Properties
<a name="aws-properties-pcs-computenodegroup-nodelifecyclestages-properties"></a>

`NodeBootstrapped`  <a name="cfn-pcs-computenodegroup-nodelifecyclestages-nodebootstrapped"></a>
The scripts to run after AWS PCS finishes setting up the compute node and before the Slurm daemon (`slurmd`) starts. Use this stage for tasks that must complete before the node accepts jobs, such as mounting shared storage, configuring networking, or installing software packages.
*Required*: No
*Type*: Array of [NodeLifecycleScript](aws-properties-pcs-computenodegroup-nodelifecyclescript.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodeReady`  <a name="cfn-pcs-computenodegroup-nodelifecyclestages-nodeready"></a>
The scripts to run after the Slurm daemon (`slurmd`) starts and the compute node registers with the Slurm controller. Use this stage for tasks that require Slurm to be running, such as running Slurm commands.
*Required*: No
*Type*: Array of [NodeLifecycleScript](aws-properties-pcs-computenodegroup-nodelifecyclescript.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
