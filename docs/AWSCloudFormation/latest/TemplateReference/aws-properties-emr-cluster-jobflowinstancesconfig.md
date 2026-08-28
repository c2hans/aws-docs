---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-jobflowinstancesconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster JobFlowInstancesConfig
<a name="aws-properties-emr-cluster-jobflowinstancesconfig"></a>

`JobFlowInstancesConfig` is a property of the `AWS::EMR::Cluster` resource. `JobFlowInstancesConfig` defines the instance groups or instance fleets that comprise the cluster. `JobFlowInstancesConfig` must contain either `InstanceFleetConfig` or `InstanceGroupConfig`. They cannot be used together.

You can now define task instance groups or task instance fleets using the `TaskInstanceGroups` and `TaskInstanceFleets` subproperties. Using these subproperties reduces delays in provisioning task nodes compared to specifying task nodes with the `InstanceFleetConfig` and `InstanceGroupConfig` resources.

## Syntax
<a name="aws-properties-emr-cluster-jobflowinstancesconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-jobflowinstancesconfig-syntax.json"></a>

```
{
  "[AdditionalMasterSecurityGroups](#cfn-emr-cluster-jobflowinstancesconfig-additionalmastersecuritygroups)" : {{[ String, ... ]}},
  "[AdditionalSlaveSecurityGroups](#cfn-emr-cluster-jobflowinstancesconfig-additionalslavesecuritygroups)" : {{[ String, ... ]}},
  "[CoreInstanceFleet](#cfn-emr-cluster-jobflowinstancesconfig-coreinstancefleet)" : {{InstanceFleetConfig}},
  "[CoreInstanceGroup](#cfn-emr-cluster-jobflowinstancesconfig-coreinstancegroup)" : {{InstanceGroupConfig}},
  "[Ec2KeyName](#cfn-emr-cluster-jobflowinstancesconfig-ec2keyname)" : {{String}},
  "[Ec2SubnetId](#cfn-emr-cluster-jobflowinstancesconfig-ec2subnetid)" : {{String}},
  "[Ec2SubnetIds](#cfn-emr-cluster-jobflowinstancesconfig-ec2subnetids)" : {{[ String, ... ]}},
  "[EmrManagedMasterSecurityGroup](#cfn-emr-cluster-jobflowinstancesconfig-emrmanagedmastersecuritygroup)" : {{String}},
  "[EmrManagedSlaveSecurityGroup](#cfn-emr-cluster-jobflowinstancesconfig-emrmanagedslavesecuritygroup)" : {{String}},
  "[HadoopVersion](#cfn-emr-cluster-jobflowinstancesconfig-hadoopversion)" : {{String}},
  "[KeepJobFlowAliveWhenNoSteps](#cfn-emr-cluster-jobflowinstancesconfig-keepjobflowalivewhennosteps)" : {{Boolean}},
  "[MasterInstanceFleet](#cfn-emr-cluster-jobflowinstancesconfig-masterinstancefleet)" : {{InstanceFleetConfig}},
  "[MasterInstanceGroup](#cfn-emr-cluster-jobflowinstancesconfig-masterinstancegroup)" : {{InstanceGroupConfig}},
  "[Placement](#cfn-emr-cluster-jobflowinstancesconfig-placement)" : {{PlacementType}},
  "[ServiceAccessSecurityGroup](#cfn-emr-cluster-jobflowinstancesconfig-serviceaccesssecuritygroup)" : {{String}},
  "[TaskInstanceFleets](#cfn-emr-cluster-jobflowinstancesconfig-taskinstancefleets)" : {{[ InstanceFleetConfig, ... ]}},
  "[TaskInstanceGroups](#cfn-emr-cluster-jobflowinstancesconfig-taskinstancegroups)" : {{[ InstanceGroupConfig, ... ]}},
  "[TerminationProtected](#cfn-emr-cluster-jobflowinstancesconfig-terminationprotected)" : {{Boolean}},
  "[UnhealthyNodeReplacement](#cfn-emr-cluster-jobflowinstancesconfig-unhealthynodereplacement)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-emr-cluster-jobflowinstancesconfig-syntax.yaml"></a>

```
  [AdditionalMasterSecurityGroups](#cfn-emr-cluster-jobflowinstancesconfig-additionalmastersecuritygroups): {{
    - String}}
  [AdditionalSlaveSecurityGroups](#cfn-emr-cluster-jobflowinstancesconfig-additionalslavesecuritygroups): {{
    - String}}
  [CoreInstanceFleet](#cfn-emr-cluster-jobflowinstancesconfig-coreinstancefleet): {{
    InstanceFleetConfig}}
  [CoreInstanceGroup](#cfn-emr-cluster-jobflowinstancesconfig-coreinstancegroup): {{
    InstanceGroupConfig}}
  [Ec2KeyName](#cfn-emr-cluster-jobflowinstancesconfig-ec2keyname): {{String}}
  [Ec2SubnetId](#cfn-emr-cluster-jobflowinstancesconfig-ec2subnetid): {{String}}
  [Ec2SubnetIds](#cfn-emr-cluster-jobflowinstancesconfig-ec2subnetids): {{
    - String}}
  [EmrManagedMasterSecurityGroup](#cfn-emr-cluster-jobflowinstancesconfig-emrmanagedmastersecuritygroup): {{String}}
  [EmrManagedSlaveSecurityGroup](#cfn-emr-cluster-jobflowinstancesconfig-emrmanagedslavesecuritygroup): {{String}}
  [HadoopVersion](#cfn-emr-cluster-jobflowinstancesconfig-hadoopversion): {{String}}
  [KeepJobFlowAliveWhenNoSteps](#cfn-emr-cluster-jobflowinstancesconfig-keepjobflowalivewhennosteps): {{Boolean}}
  [MasterInstanceFleet](#cfn-emr-cluster-jobflowinstancesconfig-masterinstancefleet): {{
    InstanceFleetConfig}}
  [MasterInstanceGroup](#cfn-emr-cluster-jobflowinstancesconfig-masterinstancegroup): {{
    InstanceGroupConfig}}
  [Placement](#cfn-emr-cluster-jobflowinstancesconfig-placement): {{
    PlacementType}}
  [ServiceAccessSecurityGroup](#cfn-emr-cluster-jobflowinstancesconfig-serviceaccesssecuritygroup): {{String}}
  [TaskInstanceFleets](#cfn-emr-cluster-jobflowinstancesconfig-taskinstancefleets): {{
    - InstanceFleetConfig}}
  [TaskInstanceGroups](#cfn-emr-cluster-jobflowinstancesconfig-taskinstancegroups): {{
    - InstanceGroupConfig}}
  [TerminationProtected](#cfn-emr-cluster-jobflowinstancesconfig-terminationprotected): {{Boolean}}
  [UnhealthyNodeReplacement](#cfn-emr-cluster-jobflowinstancesconfig-unhealthynodereplacement): {{Boolean}}
```

## Properties
<a name="aws-properties-emr-cluster-jobflowinstancesconfig-properties"></a>

`AdditionalMasterSecurityGroups`  <a name="cfn-emr-cluster-jobflowinstancesconfig-additionalmastersecuritygroups"></a>
A list of additional Amazon EC2 security group IDs for the master node.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdditionalSlaveSecurityGroups`  <a name="cfn-emr-cluster-jobflowinstancesconfig-additionalslavesecuritygroups"></a>
A list of additional Amazon EC2 security group IDs for the core and task nodes.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CoreInstanceFleet`  <a name="cfn-emr-cluster-jobflowinstancesconfig-coreinstancefleet"></a>
Describes the EC2 instances and instance configurations for the core instance fleet when using clusters with the instance fleet configuration.
*Required*: No
*Type*: [InstanceFleetConfig](aws-properties-emr-cluster-instancefleetconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CoreInstanceGroup`  <a name="cfn-emr-cluster-jobflowinstancesconfig-coreinstancegroup"></a>
Describes the EC2 instances and instance configurations for core instance groups when using clusters with the uniform instance group configuration.
*Required*: No
*Type*: [InstanceGroupConfig](aws-properties-emr-cluster-instancegroupconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ec2KeyName`  <a name="cfn-emr-cluster-jobflowinstancesconfig-ec2keyname"></a>
The name of the Amazon EC2 key pair that can be used to connect to the master node using SSH as the user called "hadoop."
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ec2SubnetId`  <a name="cfn-emr-cluster-jobflowinstancesconfig-ec2subnetid"></a>
Applies to clusters that use the uniform instance group configuration. To launch the cluster in Amazon Virtual Private Cloud (Amazon VPC), set this parameter to the identifier of the Amazon VPC subnet where you want the cluster to launch. If you do not specify this value and your account supports EC2-Classic, the cluster launches in EC2-Classic.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ec2SubnetIds`  <a name="cfn-emr-cluster-jobflowinstancesconfig-ec2subnetids"></a>
Applies to clusters that use the instance fleet configuration. When multiple Amazon EC2 subnet IDs are specified, Amazon EMR evaluates them and launches instances in the optimal subnet.
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmrManagedMasterSecurityGroup`  <a name="cfn-emr-cluster-jobflowinstancesconfig-emrmanagedmastersecuritygroup"></a>
The identifier of the Amazon EC2 security group for the master node. If you specify `EmrManagedMasterSecurityGroup`, you must also specify `EmrManagedSlaveSecurityGroup`.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmrManagedSlaveSecurityGroup`  <a name="cfn-emr-cluster-jobflowinstancesconfig-emrmanagedslavesecuritygroup"></a>
The identifier of the Amazon EC2 security group for the core and task nodes. If you specify `EmrManagedSlaveSecurityGroup`, you must also specify `EmrManagedMasterSecurityGroup`.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HadoopVersion`  <a name="cfn-emr-cluster-jobflowinstancesconfig-hadoopversion"></a>
Applies only to Amazon EMR release versions earlier than 4.0. The Hadoop version for the cluster. Valid inputs are "0.18" (no longer maintained), "0.20" (no longer maintained), "0.20.205" (no longer maintained), "1.0.3", "2.2.0", or "2.4.0". If you do not set this value, the default of 0.18 is used, unless the `AmiVersion` parameter is set in the RunJobFlow call, in which case the default version of Hadoop for that AMI version is used.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeepJobFlowAliveWhenNoSteps`  <a name="cfn-emr-cluster-jobflowinstancesconfig-keepjobflowalivewhennosteps"></a>
Specifies whether the cluster should remain available after completing all steps. Defaults to `false`. For more information about configuring cluster termination, see [Control Cluster Termination](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html) in the *EMR Management Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MasterInstanceFleet`  <a name="cfn-emr-cluster-jobflowinstancesconfig-masterinstancefleet"></a>
Describes the EC2 instances and instance configurations for the master instance fleet when using clusters with the instance fleet configuration.
*Required*: No
*Type*: [InstanceFleetConfig](aws-properties-emr-cluster-instancefleetconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MasterInstanceGroup`  <a name="cfn-emr-cluster-jobflowinstancesconfig-masterinstancegroup"></a>
Describes the EC2 instances and instance configurations for the master instance group when using clusters with the uniform instance group configuration.
*Required*: No
*Type*: [InstanceGroupConfig](aws-properties-emr-cluster-instancegroupconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Placement`  <a name="cfn-emr-cluster-jobflowinstancesconfig-placement"></a>
The Availability Zone in which the cluster runs.
*Required*: No
*Type*: [PlacementType](aws-properties-emr-cluster-placementtype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceAccessSecurityGroup`  <a name="cfn-emr-cluster-jobflowinstancesconfig-serviceaccesssecuritygroup"></a>
The identifier of the Amazon EC2 security group for the Amazon EMR service to access clusters in VPC private subnets.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskInstanceFleets`  <a name="cfn-emr-cluster-jobflowinstancesconfig-taskinstancefleets"></a>
Describes the EC2 instances and instance configurations for the task instance fleets when using clusters with the instance fleet configuration. These task instance fleets are added to the cluster as part of the cluster launch. Each task instance fleet must have a unique name specified so that CloudFormation can differentiate between the task instance fleets.
You can currently specify only one task instance fleet for a cluster. After creating the cluster, you can only modify the mutable properties of `InstanceFleetConfig`, which are `TargetOnDemandCapacity` and `TargetSpotCapacity`. Modifying any other property results in cluster replacement.
To allow a maximum of 30 Amazon EC2 instance types per fleet, include `TaskInstanceFleets` when you create your cluster. If you create your cluster without `TaskInstanceFleets`, Amazon EMR uses its default allocation strategy, which allows for a maximum of five Amazon EC2 instance types.
*Required*: No
*Type*: Array of [InstanceFleetConfig](aws-properties-emr-cluster-instancefleetconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskInstanceGroups`  <a name="cfn-emr-cluster-jobflowinstancesconfig-taskinstancegroups"></a>
Describes the EC2 instances and instance configurations for task instance groups when using clusters with the uniform instance group configuration. These task instance groups are added to the cluster as part of the cluster launch. Each task instance group must have a unique name specified so that CloudFormation can differentiate between the task instance groups.
After creating the cluster, you can only modify the mutable properties of `InstanceGroupConfig`, which are `AutoScalingPolicy` and `InstanceCount`. Modifying any other property results in cluster replacement.
*Required*: No
*Type*: Array of [InstanceGroupConfig](aws-properties-emr-cluster-instancegroupconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TerminationProtected`  <a name="cfn-emr-cluster-jobflowinstancesconfig-terminationprotected"></a>
Specifies whether to lock the cluster to prevent the Amazon EC2 instances from being terminated by API call, user intervention, or in the event of a job-flow error.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnhealthyNodeReplacement`  <a name="cfn-emr-cluster-jobflowinstancesconfig-unhealthynodereplacement"></a>
Indicates whether Amazon EMR should gracefully replace core nodes that have degraded within the cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
