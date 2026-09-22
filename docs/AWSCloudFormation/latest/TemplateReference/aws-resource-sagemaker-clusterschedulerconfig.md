---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-clusterschedulerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ClusterSchedulerConfig
<a name="aws-resource-sagemaker-clusterschedulerconfig"></a>

Create cluster policy configuration. This policy is used for task prioritization and fair-share allocation of idle compute. This helps prioritize critical workloads and distributes idle compute across entities.

## Syntax
<a name="aws-resource-sagemaker-clusterschedulerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-clusterschedulerconfig-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::ClusterSchedulerConfig",
  "Properties" : {
      "[ClusterArn](#cfn-sagemaker-clusterschedulerconfig-clusterarn)" : {{String}},
      "[Description](#cfn-sagemaker-clusterschedulerconfig-description)" : {{String}},
      "[Name](#cfn-sagemaker-clusterschedulerconfig-name)" : {{String}},
      "[SchedulerConfig](#cfn-sagemaker-clusterschedulerconfig-schedulerconfig)" : {{SchedulerConfig}},
      "[Tags](#cfn-sagemaker-clusterschedulerconfig-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-clusterschedulerconfig-syntax.yaml"></a>

```
Type: AWS::SageMaker::ClusterSchedulerConfig
Properties:
  [ClusterArn](#cfn-sagemaker-clusterschedulerconfig-clusterarn): {{String}}
  [Description](#cfn-sagemaker-clusterschedulerconfig-description): {{String}}
  [Name](#cfn-sagemaker-clusterschedulerconfig-name): {{String}}
  [SchedulerConfig](#cfn-sagemaker-clusterschedulerconfig-schedulerconfig): {{
    SchedulerConfig}}
  [Tags](#cfn-sagemaker-clusterschedulerconfig-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-clusterschedulerconfig-properties"></a>

`ClusterArn`  <a name="cfn-sagemaker-clusterschedulerconfig-clusterarn"></a>
ARN of the cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}$`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-sagemaker-clusterschedulerconfig-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-sagemaker-clusterschedulerconfig-name"></a>
Name of the cluster policy.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SchedulerConfig`  <a name="cfn-sagemaker-clusterschedulerconfig-schedulerconfig"></a>
Cluster policy configuration. This policy is used for task prioritization and fair-share allocation. This helps prioritize critical workloads and distributes idle compute across entities.
*Required*: Yes
*Type*: [SchedulerConfig](aws-properties-sagemaker-clusterschedulerconfig-schedulerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-clusterschedulerconfig-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-clusterschedulerconfig-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-clusterschedulerconfig-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-clusterschedulerconfig-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-clusterschedulerconfig-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-clusterschedulerconfig-return-values-fn--getatt-fn--getatt"></a>

`ClusterSchedulerConfigArn`  <a name="ClusterSchedulerConfigArn-fn::getatt"></a>
ARN of the cluster policy.

`ClusterSchedulerConfigId`  <a name="ClusterSchedulerConfigId-fn::getatt"></a>
ID of the cluster policy.

`ClusterSchedulerConfigVersion`  <a name="ClusterSchedulerConfigVersion-fn::getatt"></a>
Version of the cluster policy.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Creation time of the cluster policy.

`Status`  <a name="Status-fn::getatt"></a>
Status of the cluster policy.
