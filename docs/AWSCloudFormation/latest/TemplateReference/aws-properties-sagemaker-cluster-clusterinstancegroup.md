---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusterinstancegroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterInstanceGroup
<a name="aws-properties-sagemaker-cluster-clusterinstancegroup"></a>

The configuration information of the instance group within the HyperPod cluster.

## Syntax
<a name="aws-properties-sagemaker-cluster-clusterinstancegroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusterinstancegroup-syntax.json"></a>

```
{
  "[AutoPatchConfig](#cfn-sagemaker-cluster-clusterinstancegroup-autopatchconfig)" : {{AutoPatchConfig}},
  "[CapacityRequirements](#cfn-sagemaker-cluster-clusterinstancegroup-capacityrequirements)" : {{ClusterCapacityRequirements}},
  "[CurrentCount](#cfn-sagemaker-cluster-clusterinstancegroup-currentcount)" : {{Integer}},
  "[ExecutionRole](#cfn-sagemaker-cluster-clusterinstancegroup-executionrole)" : {{String}},
  "[ImageId](#cfn-sagemaker-cluster-clusterinstancegroup-imageid)" : {{String}},
  "[InstanceCount](#cfn-sagemaker-cluster-clusterinstancegroup-instancecount)" : {{Integer}},
  "[InstanceGroupName](#cfn-sagemaker-cluster-clusterinstancegroup-instancegroupname)" : {{String}},
  "[InstanceRequirements](#cfn-sagemaker-cluster-clusterinstancegroup-instancerequirements)" : {{InstanceRequirements}},
  "[InstanceStorageConfigs](#cfn-sagemaker-cluster-clusterinstancegroup-instancestorageconfigs)" : {{[ ClusterInstanceStorageConfig, ... ]}},
  "[InstanceType](#cfn-sagemaker-cluster-clusterinstancegroup-instancetype)" : {{String}},
  "[KubernetesConfig](#cfn-sagemaker-cluster-clusterinstancegroup-kubernetesconfig)" : {{ClusterKubernetesConfig}},
  "[LifeCycleConfig](#cfn-sagemaker-cluster-clusterinstancegroup-lifecycleconfig)" : {{ClusterLifeCycleConfig}},
  "[MinInstanceCount](#cfn-sagemaker-cluster-clusterinstancegroup-mininstancecount)" : {{Integer}},
  "[NetworkInterface](#cfn-sagemaker-cluster-clusterinstancegroup-networkinterface)" : {{ClusterNetworkInterface}},
  "[OnStartDeepHealthChecks](#cfn-sagemaker-cluster-clusterinstancegroup-onstartdeephealthchecks)" : {{[ String, ... ]}},
  "[OverrideVpcConfig](#cfn-sagemaker-cluster-clusterinstancegroup-overridevpcconfig)" : {{VpcConfig}},
  "[ScheduledUpdateConfig](#cfn-sagemaker-cluster-clusterinstancegroup-scheduledupdateconfig)" : {{ScheduledUpdateConfig}},
  "[SlurmConfig](#cfn-sagemaker-cluster-clusterinstancegroup-slurmconfig)" : {{ClusterSlurmConfig}},
  "[ThreadsPerCore](#cfn-sagemaker-cluster-clusterinstancegroup-threadspercore)" : {{Integer}},
  "[TrainingPlanArn](#cfn-sagemaker-cluster-clusterinstancegroup-trainingplanarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusterinstancegroup-syntax.yaml"></a>

```
  [AutoPatchConfig](#cfn-sagemaker-cluster-clusterinstancegroup-autopatchconfig): {{
    AutoPatchConfig}}
  [CapacityRequirements](#cfn-sagemaker-cluster-clusterinstancegroup-capacityrequirements): {{
    ClusterCapacityRequirements}}
  [CurrentCount](#cfn-sagemaker-cluster-clusterinstancegroup-currentcount): {{Integer}}
  [ExecutionRole](#cfn-sagemaker-cluster-clusterinstancegroup-executionrole): {{String}}
  [ImageId](#cfn-sagemaker-cluster-clusterinstancegroup-imageid): {{String}}
  [InstanceCount](#cfn-sagemaker-cluster-clusterinstancegroup-instancecount): {{Integer}}
  [InstanceGroupName](#cfn-sagemaker-cluster-clusterinstancegroup-instancegroupname): {{String}}
  [InstanceRequirements](#cfn-sagemaker-cluster-clusterinstancegroup-instancerequirements): {{
    InstanceRequirements}}
  [InstanceStorageConfigs](#cfn-sagemaker-cluster-clusterinstancegroup-instancestorageconfigs): {{
    - ClusterInstanceStorageConfig}}
  [InstanceType](#cfn-sagemaker-cluster-clusterinstancegroup-instancetype): {{String}}
  [KubernetesConfig](#cfn-sagemaker-cluster-clusterinstancegroup-kubernetesconfig): {{
    ClusterKubernetesConfig}}
  [LifeCycleConfig](#cfn-sagemaker-cluster-clusterinstancegroup-lifecycleconfig): {{
    ClusterLifeCycleConfig}}
  [MinInstanceCount](#cfn-sagemaker-cluster-clusterinstancegroup-mininstancecount): {{Integer}}
  [NetworkInterface](#cfn-sagemaker-cluster-clusterinstancegroup-networkinterface): {{
    ClusterNetworkInterface}}
  [OnStartDeepHealthChecks](#cfn-sagemaker-cluster-clusterinstancegroup-onstartdeephealthchecks): {{
    - String}}
  [OverrideVpcConfig](#cfn-sagemaker-cluster-clusterinstancegroup-overridevpcconfig): {{
    VpcConfig}}
  [ScheduledUpdateConfig](#cfn-sagemaker-cluster-clusterinstancegroup-scheduledupdateconfig): {{
    ScheduledUpdateConfig}}
  [SlurmConfig](#cfn-sagemaker-cluster-clusterinstancegroup-slurmconfig): {{
    ClusterSlurmConfig}}
  [ThreadsPerCore](#cfn-sagemaker-cluster-clusterinstancegroup-threadspercore): {{Integer}}
  [TrainingPlanArn](#cfn-sagemaker-cluster-clusterinstancegroup-trainingplanarn): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusterinstancegroup-properties"></a>

`AutoPatchConfig`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-autopatchconfig"></a>
Property description not available.
*Required*: No
*Type*: [AutoPatchConfig](aws-properties-sagemaker-cluster-autopatchconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapacityRequirements`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-capacityrequirements"></a>
The capacity requirements for the instance group, specifying on-demand and spot instance configurations.
*Required*: No
*Type*: [ClusterCapacityRequirements](aws-properties-sagemaker-cluster-clustercapacityrequirements.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CurrentCount`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-currentcount"></a>
The number of instances that are currently in the instance group of a SageMaker HyperPod cluster.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRole`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-executionrole"></a>
The execution role for the instance group to assume.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageId`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-imageid"></a>
The ID of the Amazon Machine Image (AMI) to use for the instances in the group.
*Required*: No
*Type*: String
*Pattern*: `^ami-[0-9a-fA-F]{8,17}|default$`
*Minimum*: `7`
*Maximum*: `21`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceCount`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-instancecount"></a>
The number of instances in an instance group of the SageMaker HyperPod cluster.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceGroupName`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-instancegroupname"></a>
The name of the instance group of a SageMaker HyperPod cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceRequirements`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-instancerequirements"></a>
Property description not available.
*Required*: No
*Type*: [InstanceRequirements](aws-properties-sagemaker-cluster-instancerequirements.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceStorageConfigs`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-instancestorageconfigs"></a>
The configurations of additional storage specified to the instance group where the instance (node) is launched.
*Required*: No
*Type*: Array of [ClusterInstanceStorageConfig](aws-properties-sagemaker-cluster-clusterinstancestorageconfig.md)
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceType`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-instancetype"></a>
The instance type of the instance group of a SageMaker HyperPod cluster.
*Required*: No
*Type*: String
*Allowed values*: `ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p5.4xlarge | ml.p6e-gb200.36xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.c5.large | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.12xlarge | ml.c5.18xlarge | ml.c5.24xlarge | ml.c5n.large | ml.c5n.2xlarge | ml.c5n.4xlarge | ml.c5n.9xlarge | ml.c5n.18xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.8xlarge | ml.m5.12xlarge | ml.m5.16xlarge | ml.m5.24xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.16xlarge | ml.g6.12xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.gr6.4xlarge | ml.gr6.8xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.16xlarge | ml.g6e.12xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.p6-b200.48xlarge | ml.trn2.3xlarge | ml.trn2.48xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.i3en.large | ml.i3en.xlarge | ml.i3en.2xlarge | ml.i3en.3xlarge | ml.i3en.6xlarge | ml.i3en.12xlarge | ml.i3en.24xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.r5d.16xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.p6-b300.48xlarge`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KubernetesConfig`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-kubernetesconfig"></a>
The Kubernetes configuration for the instance group, including labels and taints.
*Required*: No
*Type*: [ClusterKubernetesConfig](aws-properties-sagemaker-cluster-clusterkubernetesconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifeCycleConfig`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-lifecycleconfig"></a>
The lifecycle configuration for a SageMaker HyperPod cluster.
*Required*: No
*Type*: [ClusterLifeCycleConfig](aws-properties-sagemaker-cluster-clusterlifecycleconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinInstanceCount`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-mininstancecount"></a>
The minimum number of instances to maintain in the instance group.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkInterface`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-networkinterface"></a>
Property description not available.
*Required*: No
*Type*: [ClusterNetworkInterface](aws-properties-sagemaker-cluster-clusternetworkinterface.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnStartDeepHealthChecks`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-onstartdeephealthchecks"></a>
A flag indicating whether deep health checks should be performed when the HyperPod cluster instance group is created or updated. Deep health checks are comprehensive, invasive tests that validate the health of the underlying hardware and infrastructure components.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OverrideVpcConfig`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-overridevpcconfig"></a>
The customized Amazon VPC configuration at the instance group level that overrides the default Amazon VPC configuration of the SageMaker HyperPod cluster.
*Required*: No
*Type*: [VpcConfig](aws-properties-sagemaker-cluster-vpcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduledUpdateConfig`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-scheduledupdateconfig"></a>
Configuration for scheduled updates to the instance group.
*Required*: No
*Type*: [ScheduledUpdateConfig](aws-properties-sagemaker-cluster-scheduledupdateconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlurmConfig`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-slurmconfig"></a>
The Slurm workload manager configuration for the instance group.
*Required*: No
*Type*: [ClusterSlurmConfig](aws-properties-sagemaker-cluster-clusterslurmconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThreadsPerCore`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-threadspercore"></a>
The number of threads per CPU core you specified under `CreateCluster`.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrainingPlanArn`  <a name="cfn-sagemaker-cluster-clusterinstancegroup-trainingplanarn"></a>
The Amazon Resource Name (ARN) of the training plan associated with the instance group.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*$`
*Minimum*: `50`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
