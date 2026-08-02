---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusterkubernetestaint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterKubernetesTaint
<a name="aws-properties-sagemaker-cluster-clusterkubernetestaint"></a>

A Kubernetes taint that can be applied to cluster nodes.

## Syntax
<a name="aws-properties-sagemaker-cluster-clusterkubernetestaint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusterkubernetestaint-syntax.json"></a>

```
{
  "[Effect](#cfn-sagemaker-cluster-clusterkubernetestaint-effect)" : {{String}},
  "[Key](#cfn-sagemaker-cluster-clusterkubernetestaint-key)" : {{String}},
  "[Value](#cfn-sagemaker-cluster-clusterkubernetestaint-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusterkubernetestaint-syntax.yaml"></a>

```
  [Effect](#cfn-sagemaker-cluster-clusterkubernetestaint-effect): {{String}}
  [Key](#cfn-sagemaker-cluster-clusterkubernetestaint-key): {{String}}
  [Value](#cfn-sagemaker-cluster-clusterkubernetestaint-value): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusterkubernetestaint-properties"></a>

`Effect`  <a name="cfn-sagemaker-cluster-clusterkubernetestaint-effect"></a>
The effect of the taint. Valid values are `NoSchedule`, `PreferNoSchedule`, and `NoExecute`.
*Required*: Yes
*Type*: String
*Allowed values*: `NoSchedule | PreferNoSchedule | NoExecute`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-sagemaker-cluster-clusterkubernetestaint-key"></a>
The key of the taint.
*Required*: Yes
*Type*: String
*Pattern*: `([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?[A-Za-z0-9]([-A-Za-z0-9_.]*[A-Za-z0-9])?`
*Minimum*: `1`
*Maximum*: `317`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-sagemaker-cluster-clusterkubernetestaint-value"></a>
The value of the taint.
*Required*: No
*Type*: String
*Pattern*: `(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])?`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
