---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusterrestrictedinstancegroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterRestrictedInstanceGroup
<a name="aws-properties-sagemaker-cluster-clusterrestrictedinstancegroup"></a>

Specialized instance groups for training models like Amazon Nova in the SageMaker HyperPod cluster.

## Syntax
<a name="aws-properties-sagemaker-cluster-clusterrestrictedinstancegroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusterrestrictedinstancegroup-syntax.json"></a>

```
{
  "[CurrentCount](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-currentcount)" : {{Integer}},
  "[EnvironmentConfig](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-environmentconfig)" : {{EnvironmentConfig}},
  "[ExecutionRole](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-executionrole)" : {{String}},
  "[InstanceCount](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-instancecount)" : {{Integer}},
  "[InstanceGroupName](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-instancegroupname)" : {{String}},
  "[InstanceStorageConfigs](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-instancestorageconfigs)" : {{[ ClusterInstanceStorageConfig, ... ]}},
  "[InstanceType](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-instancetype)" : {{String}},
  "[OnStartDeepHealthChecks](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-onstartdeephealthchecks)" : {{[ String, ... ]}},
  "[OverrideVpcConfig](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-overridevpcconfig)" : {{VpcConfig}},
  "[ThreadsPerCore](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-threadspercore)" : {{Integer}},
  "[TrainingPlanArn](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-trainingplanarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusterrestrictedinstancegroup-syntax.yaml"></a>

```
  [CurrentCount](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-currentcount): {{Integer}}
  [EnvironmentConfig](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-environmentconfig): {{
    EnvironmentConfig}}
  [ExecutionRole](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-executionrole): {{String}}
  [InstanceCount](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-instancecount): {{Integer}}
  [InstanceGroupName](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-instancegroupname): {{String}}
  [InstanceStorageConfigs](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-instancestorageconfigs): {{
    - ClusterInstanceStorageConfig}}
  [InstanceType](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-instancetype): {{String}}
  [OnStartDeepHealthChecks](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-onstartdeephealthchecks): {{
    - String}}
  [OverrideVpcConfig](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-overridevpcconfig): {{
    VpcConfig}}
  [ThreadsPerCore](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-threadspercore): {{Integer}}
  [TrainingPlanArn](#cfn-sagemaker-cluster-clusterrestrictedinstancegroup-trainingplanarn): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusterrestrictedinstancegroup-properties"></a>

`CurrentCount`  <a name="cfn-sagemaker-cluster-clusterrestrictedinstancegroup-currentcount"></a>
The current number of instances in the restricted instance group.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentConfig`  <a name="cfn-sagemaker-cluster-clusterrestrictedinstancegroup-environmentconfig"></a>
Environment configuration for the restricted instance group, including FSx Lustre settings.
*Required*: No
*Type*: [EnvironmentConfig](aws-properties-sagemaker-cluster-environmentconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRole`  <a name="cfn-sagemaker-cluster-clusterrestrictedinstancegroup-executionrole"></a>
The Amazon Resource Name (ARN) of the IAM execution role for the restricted instance group.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceCount`  <a name="cfn-sagemaker-cluster-clusterrestrictedinstancegroup-instancecount"></a>
The number of instances in the restricted instance group.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceGroupName`  <a name="cfn-sagemaker-cluster-clusterrestrictedinstancegroup-instancegroupname"></a>
The name of the restricted instance group.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceStorageConfigs`  <a name="cfn-sagemaker-cluster-clusterrestrictedinstancegroup-instancestorageconfigs"></a>
Storage configurations for instances in the restricted instance group.
*Required*: No
*Type*: Array of [ClusterInstanceStorageConfig](aws-properties-sagemaker-cluster-clusterinstancestorageconfig.md)
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceType`  <a name="cfn-sagemaker-cluster-clusterrestrictedinstancegroup-instancetype"></a>
The EC2 instance type for the restricted instance group.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnStartDeepHealthChecks`  <a name="cfn-sagemaker-cluster-clusterrestrictedinstancegroup-onstartdeephealthchecks"></a>
Deep health checks to run when instances start in the restricted instance group.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverrideVpcConfig`  <a name="cfn-sagemaker-cluster-clusterrestrictedinstancegroup-overridevpcconfig"></a>
VPC configuration override for the restricted instance group.
*Required*: No
*Type*: [VpcConfig](aws-properties-sagemaker-cluster-vpcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThreadsPerCore`  <a name="cfn-sagemaker-cluster-clusterrestrictedinstancegroup-threadspercore"></a>
The number of threads per CPU core for instances in the restricted instance group.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrainingPlanArn`  <a name="cfn-sagemaker-cluster-clusterrestrictedinstancegroup-trainingplanarn"></a>
The Amazon Resource Name (ARN) of the training plan for the restricted instance group.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*$`
*Minimum*: `50`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
