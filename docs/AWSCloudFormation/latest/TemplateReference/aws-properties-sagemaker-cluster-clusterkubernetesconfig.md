---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusterkubernetesconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterKubernetesConfig
<a name="aws-properties-sagemaker-cluster-clusterkubernetesconfig"></a>

Kubernetes configuration that specifies labels and taints to be applied to cluster nodes in an instance group.

## Syntax
<a name="aws-properties-sagemaker-cluster-clusterkubernetesconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusterkubernetesconfig-syntax.json"></a>

```
{
  "[Labels](#cfn-sagemaker-cluster-clusterkubernetesconfig-labels)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Taints](#cfn-sagemaker-cluster-clusterkubernetesconfig-taints)" : {{[ ClusterKubernetesTaint, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusterkubernetesconfig-syntax.yaml"></a>

```
  [Labels](#cfn-sagemaker-cluster-clusterkubernetesconfig-labels): {{
    {{Key}}: {{Value}}}}
  [Taints](#cfn-sagemaker-cluster-clusterkubernetesconfig-taints): {{
    - ClusterKubernetesTaint}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusterkubernetesconfig-properties"></a>

`Labels`  <a name="cfn-sagemaker-cluster-clusterkubernetesconfig-labels"></a>
Key-value pairs of labels to be applied to cluster nodes.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Taints`  <a name="cfn-sagemaker-cluster-clusterkubernetesconfig-taints"></a>
List of taints to be applied to cluster nodes.
*Required*: No
*Type*: Array of [ClusterKubernetesTaint](aws-properties-sagemaker-cluster-clusterkubernetestaint.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
