---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusterautoscalingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterAutoScalingConfig
<a name="aws-properties-sagemaker-cluster-clusterautoscalingconfig"></a>

Specifies the autoscaling configuration for a HyperPod cluster.

## Syntax
<a name="aws-properties-sagemaker-cluster-clusterautoscalingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusterautoscalingconfig-syntax.json"></a>

```
{
  "[AutoScalerType](#cfn-sagemaker-cluster-clusterautoscalingconfig-autoscalertype)" : {{String}},
  "[Mode](#cfn-sagemaker-cluster-clusterautoscalingconfig-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusterautoscalingconfig-syntax.yaml"></a>

```
  [AutoScalerType](#cfn-sagemaker-cluster-clusterautoscalingconfig-autoscalertype): {{String}}
  [Mode](#cfn-sagemaker-cluster-clusterautoscalingconfig-mode): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusterautoscalingconfig-properties"></a>

`AutoScalerType`  <a name="cfn-sagemaker-cluster-clusterautoscalingconfig-autoscalertype"></a>
The type of autoscaler to use. Currently supported value is `Karpenter`.
*Required*: No
*Type*: String
*Allowed values*: `Karpenter`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-sagemaker-cluster-clusterautoscalingconfig-mode"></a>
Describes whether autoscaling is enabled or disabled for the cluster. Valid values are `Enable` and `Disable`.
*Required*: Yes
*Type*: String
*Allowed values*: `Enable | Disable`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
