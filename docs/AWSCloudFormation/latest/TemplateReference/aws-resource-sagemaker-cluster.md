---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-cluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster
<a name="aws-resource-sagemaker-cluster"></a>

Creates an Amazon SageMaker HyperPod cluster. SageMaker HyperPod is a capability of SageMaker for creating and managing persistent clusters for developing large machine learning models, such as large language models (LLMs) and diffusion models. To learn more, see [Amazon SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) in the *Amazon SageMaker Developer Guide*.

## Syntax
<a name="aws-resource-sagemaker-cluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-cluster-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::Cluster",
  "Properties" : {
      "[AutoScaling](#cfn-sagemaker-cluster-autoscaling)" : {{ClusterAutoScalingConfig}},
      "[ClusterName](#cfn-sagemaker-cluster-clustername)" : {{String}},
      "[ClusterRole](#cfn-sagemaker-cluster-clusterrole)" : {{String}},
      "[InstanceGroups](#cfn-sagemaker-cluster-instancegroups)" : {{[ ClusterInstanceGroup, ... ]}},
      "[NodeProvisioningMode](#cfn-sagemaker-cluster-nodeprovisioningmode)" : {{String}},
      "[NodeRecovery](#cfn-sagemaker-cluster-noderecovery)" : {{String}},
      "[Orchestrator](#cfn-sagemaker-cluster-orchestrator)" : {{Orchestrator}},
      "[RestrictedInstanceGroups](#cfn-sagemaker-cluster-restrictedinstancegroups)" : {{[ ClusterRestrictedInstanceGroup, ... ]}},
      "[RestrictedInstanceGroupsConfig](#cfn-sagemaker-cluster-restrictedinstancegroupsconfig)" : {{RestrictedInstanceGroupsConfig}},
      "[Tags](#cfn-sagemaker-cluster-tags)" : {{[ Tag, ... ]}},
      "[TieredStorageConfig](#cfn-sagemaker-cluster-tieredstorageconfig)" : {{TieredStorageConfig}},
      "[VpcConfig](#cfn-sagemaker-cluster-vpcconfig)" : {{VpcConfig}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-cluster-syntax.yaml"></a>

```
Type: AWS::SageMaker::Cluster
Properties:
  [AutoScaling](#cfn-sagemaker-cluster-autoscaling): {{
    ClusterAutoScalingConfig}}
  [ClusterName](#cfn-sagemaker-cluster-clustername): {{String}}
  [ClusterRole](#cfn-sagemaker-cluster-clusterrole): {{String}}
  [InstanceGroups](#cfn-sagemaker-cluster-instancegroups): {{
    - ClusterInstanceGroup}}
  [NodeProvisioningMode](#cfn-sagemaker-cluster-nodeprovisioningmode): {{String}}
  [NodeRecovery](#cfn-sagemaker-cluster-noderecovery): {{String}}
  [Orchestrator](#cfn-sagemaker-cluster-orchestrator): {{
    Orchestrator}}
  [RestrictedInstanceGroups](#cfn-sagemaker-cluster-restrictedinstancegroups): {{
    - ClusterRestrictedInstanceGroup}}
  [RestrictedInstanceGroupsConfig](#cfn-sagemaker-cluster-restrictedinstancegroupsconfig): {{
    RestrictedInstanceGroupsConfig}}
  [Tags](#cfn-sagemaker-cluster-tags): {{
    - Tag}}
  [TieredStorageConfig](#cfn-sagemaker-cluster-tieredstorageconfig): {{
    TieredStorageConfig}}
  [VpcConfig](#cfn-sagemaker-cluster-vpcconfig): {{
    VpcConfig}}
```

## Properties
<a name="aws-resource-sagemaker-cluster-properties"></a>

`AutoScaling`  <a name="cfn-sagemaker-cluster-autoscaling"></a>
The autoscaling configuration for the cluster. Enables automatic scaling of cluster nodes based on workload demand using a Karpenter-based system.
*Required*: No
*Type*: [ClusterAutoScalingConfig](aws-properties-sagemaker-cluster-clusterautoscalingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClusterName`  <a name="cfn-sagemaker-cluster-clustername"></a>
The name of the SageMaker HyperPod cluster.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClusterRole`  <a name="cfn-sagemaker-cluster-clusterrole"></a>
The Amazon Resource Name (ARN) of the IAM role that HyperPod assumes to perform cluster autoscaling operations. This role must have permissions for `sagemaker:BatchAddClusterNodes` and `sagemaker:BatchDeleteClusterNodes`. This is only required when autoscaling is enabled and when HyperPod is performing autoscaling operations.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceGroups`  <a name="cfn-sagemaker-cluster-instancegroups"></a>
The instance groups of the SageMaker HyperPod cluster. To delete an instance group, remove it from the array.
*Required*: No
*Type*: Array of [ClusterInstanceGroup](aws-properties-sagemaker-cluster-clusterinstancegroup.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodeProvisioningMode`  <a name="cfn-sagemaker-cluster-nodeprovisioningmode"></a>
The mode for provisioning nodes in the cluster. You can specify the following modes:
+ **Continuous**: Scaling behavior that enables 1) concurrent operation execution within instance groups, 2) continuous retry mechanisms for failed operations, 3) enhanced customer visibility into cluster events through detailed event streams, 4) partial provisioning capabilities. Your clusters and instance groups remain `InService` while scaling. This mode is only supported for EKS orchestrated clusters.
*Required*: No
*Type*: String
*Allowed values*: `Continuous`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodeRecovery`  <a name="cfn-sagemaker-cluster-noderecovery"></a>
Specifies whether to enable or disable the automatic node recovery feature of SageMaker HyperPod. Available values are `Automatic` for enabling and `None` for disabling.
*Required*: No
*Type*: String
*Allowed values*: `Automatic | None`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Orchestrator`  <a name="cfn-sagemaker-cluster-orchestrator"></a>
The orchestrator type for the SageMaker HyperPod cluster. Currently, `'eks'` is the only available option.
*Required*: No
*Type*: [Orchestrator](aws-properties-sagemaker-cluster-orchestrator.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestrictedInstanceGroups`  <a name="cfn-sagemaker-cluster-restrictedinstancegroups"></a>
The specialized instance groups for training models like Amazon Nova to be created in the SageMaker HyperPod cluster.
*Required*: No
*Type*: Array of [ClusterRestrictedInstanceGroup](aws-properties-sagemaker-cluster-clusterrestrictedinstancegroup.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestrictedInstanceGroupsConfig`  <a name="cfn-sagemaker-cluster-restrictedinstancegroupsconfig"></a>
Property description not available.
*Required*: No
*Type*: [RestrictedInstanceGroupsConfig](aws-properties-sagemaker-cluster-restrictedinstancegroupsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-cluster-tags"></a>
A tag object that consists of a key and an optional value, used to manage metadata for SageMaker AWS resources.
You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html).
For more information on adding metadata to your AWS resources with tagging, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html). For advice on best practices for managing AWS resources with tagging, see [Tagging Best Practices: Implement an Effective AWS Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf).
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-cluster-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TieredStorageConfig`  <a name="cfn-sagemaker-cluster-tieredstorageconfig"></a>
The configuration for managed tier checkpointing on the HyperPod cluster. When enabled, this feature uses a multi-tier storage approach for storing model checkpoints, providing faster checkpoint operations and improved fault tolerance across cluster nodes.
*Required*: No
*Type*: [TieredStorageConfig](aws-properties-sagemaker-cluster-tieredstorageconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcConfig`  <a name="cfn-sagemaker-cluster-vpcconfig"></a>
Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).
*Required*: No
*Type*: [VpcConfig](aws-properties-sagemaker-cluster-vpcconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-cluster-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-cluster-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-cluster-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-cluster-return-values-fn--getatt-fn--getatt"></a>

`ClusterArn`  <a name="ClusterArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster.

`ClusterStatus`  <a name="ClusterStatus-fn::getatt"></a>
The status of the SageMaker HyperPod cluster.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time when the SageMaker HyperPod cluster is created.

`FailureMessage`  <a name="FailureMessage-fn::getatt"></a>
The failure message of the SageMaker HyperPod cluster.
