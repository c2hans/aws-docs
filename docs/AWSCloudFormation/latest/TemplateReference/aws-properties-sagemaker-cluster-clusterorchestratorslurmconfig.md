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
  "[AccountingDatabase](#cfn-sagemaker-cluster-clusterorchestratorslurmconfig-accountingdatabase)" : {{ClusterAccountingDatabase}},
  "[SlurmConfigStrategy](#cfn-sagemaker-cluster-clusterorchestratorslurmconfig-slurmconfigstrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusterorchestratorslurmconfig-syntax.yaml"></a>

```
  [AccountingDatabase](#cfn-sagemaker-cluster-clusterorchestratorslurmconfig-accountingdatabase): {{
    ClusterAccountingDatabase}}
  [SlurmConfigStrategy](#cfn-sagemaker-cluster-clusterorchestratorslurmconfig-slurmconfigstrategy): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusterorchestratorslurmconfig-properties"></a>

`AccountingDatabase`  <a name="cfn-sagemaker-cluster-clusterorchestratorslurmconfig-accountingdatabase"></a>
Property description not available.
*Required*: No
*Type*: [ClusterAccountingDatabase](aws-properties-sagemaker-cluster-clusteraccountingdatabase.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlurmConfigStrategy`  <a name="cfn-sagemaker-cluster-clusterorchestratorslurmconfig-slurmconfigstrategy"></a>
The strategy for managing partitions for the Slurm configuration. Valid values are `Managed`, `Overwrite`, and `Merge`.
*Required*: No
*Type*: String
*Allowed values*: `Overwrite | Managed | Merge`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
