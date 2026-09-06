---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusterslurmconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterSlurmConfig
<a name="aws-properties-sagemaker-cluster-clusterslurmconfig"></a>

The Slurm configuration for an instance group in a SageMaker HyperPod cluster.

## Syntax
<a name="aws-properties-sagemaker-cluster-clusterslurmconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusterslurmconfig-syntax.json"></a>

```
{
  "[NodeType](#cfn-sagemaker-cluster-clusterslurmconfig-nodetype)" : {{String}},
  "[PartitionNames](#cfn-sagemaker-cluster-clusterslurmconfig-partitionnames)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusterslurmconfig-syntax.yaml"></a>

```
  [NodeType](#cfn-sagemaker-cluster-clusterslurmconfig-nodetype): {{String}}
  [PartitionNames](#cfn-sagemaker-cluster-clusterslurmconfig-partitionnames): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusterslurmconfig-properties"></a>

`NodeType`  <a name="cfn-sagemaker-cluster-clusterslurmconfig-nodetype"></a>
The type of Slurm node for the instance group. Valid values are `Controller`, `Worker`, and `Login`.
*Required*: Yes
*Type*: String
*Allowed values*: `Controller | Login | Compute`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PartitionNames`  <a name="cfn-sagemaker-cluster-clusterslurmconfig-partitionnames"></a>
The list of Slurm partition names that the instance group belongs to.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 0`
*Maximum*: `1024 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
