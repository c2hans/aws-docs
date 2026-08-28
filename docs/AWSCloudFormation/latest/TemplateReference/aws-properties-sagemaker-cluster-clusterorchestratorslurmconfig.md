---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusterorchestratorslurmconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterOrchestratorSlurmConfig
<a name="aws-properties-sagemaker-cluster-clusterorchestratorslurmconfig"></a>

The configuration settings for the Slurm orchestrator used with the SageMaker HyperPod cluster.

## Syntax
<a name="aws-properties-sagemaker-cluster-clusterorchestratorslurmconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusterorchestratorslurmconfig-syntax.json"></a>

```
{
  "[SlurmConfigStrategy](#cfn-sagemaker-cluster-clusterorchestratorslurmconfig-slurmconfigstrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusterorchestratorslurmconfig-syntax.yaml"></a>

```
  [SlurmConfigStrategy](#cfn-sagemaker-cluster-clusterorchestratorslurmconfig-slurmconfigstrategy): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusterorchestratorslurmconfig-properties"></a>

`SlurmConfigStrategy`  <a name="cfn-sagemaker-cluster-clusterorchestratorslurmconfig-slurmconfigstrategy"></a>
The strategy for managing partitions for the Slurm configuration. Valid values are `Managed`, `Overwrite`, and `Merge`.
*Required*: No
*Type*: String
*Allowed values*: `Overwrite | Managed | Merge`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
