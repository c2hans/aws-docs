---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-orchestrator.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster Orchestrator
<a name="aws-properties-sagemaker-cluster-orchestrator"></a>

The orchestrator for a SageMaker HyperPod cluster.

## Syntax
<a name="aws-properties-sagemaker-cluster-orchestrator-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-orchestrator-syntax.json"></a>

```
{
  "[Eks](#cfn-sagemaker-cluster-orchestrator-eks)" : {{ClusterOrchestratorEksConfig}},
  "[Slurm](#cfn-sagemaker-cluster-orchestrator-slurm)" : {{ClusterOrchestratorSlurmConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-orchestrator-syntax.yaml"></a>

```
  [Eks](#cfn-sagemaker-cluster-orchestrator-eks): {{
    ClusterOrchestratorEksConfig}}
  [Slurm](#cfn-sagemaker-cluster-orchestrator-slurm): {{
    ClusterOrchestratorSlurmConfig}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-orchestrator-properties"></a>

`Eks`  <a name="cfn-sagemaker-cluster-orchestrator-eks"></a>
The configuration of the Amazon EKS orchestrator cluster for the SageMaker HyperPod cluster.
*Required*: No
*Type*: [ClusterOrchestratorEksConfig](aws-properties-sagemaker-cluster-clusterorchestratoreksconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Slurm`  <a name="cfn-sagemaker-cluster-orchestrator-slurm"></a>
Configuration for using Slurm as the cluster orchestrator.
*Required*: No
*Type*: [ClusterOrchestratorSlurmConfig](aws-properties-sagemaker-cluster-clusterorchestratorslurmconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
