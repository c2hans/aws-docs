---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusterorchestratoreksconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterOrchestratorEksConfig
<a name="aws-properties-sagemaker-cluster-clusterorchestratoreksconfig"></a>

The configuration for the Amazon EKS cluster that is used as the orchestrator for the SageMaker HyperPod cluster. This includes the Amazon Resource Name (ARN) of the EKS cluster

## Syntax
<a name="aws-properties-sagemaker-cluster-clusterorchestratoreksconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusterorchestratoreksconfig-syntax.json"></a>

```
{
  "[ClusterArn](#cfn-sagemaker-cluster-clusterorchestratoreksconfig-clusterarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusterorchestratoreksconfig-syntax.yaml"></a>

```
  [ClusterArn](#cfn-sagemaker-cluster-clusterorchestratoreksconfig-clusterarn): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusterorchestratoreksconfig-properties"></a>

`ClusterArn`  <a name="cfn-sagemaker-cluster-clusterorchestratoreksconfig-clusterarn"></a>
The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
