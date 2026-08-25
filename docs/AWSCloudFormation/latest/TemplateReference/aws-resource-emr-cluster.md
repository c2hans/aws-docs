---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-cluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster
<a name="aws-resource-emr-cluster"></a>

The `AWS::EMR::Cluster` resource specifies an Amazon EMR cluster. This cluster is a collection of Amazon EC2 instances that run open source big data frameworks and applications to process and analyze vast amounts of data. For more information, see the [Amazon EMR Management Guide](https://docs.aws.amazon.com/emr/latest/ManagementGuide/).

Amazon EMR now supports launching task instance groups and task instance fleets as part of the `AWS::EMR::Cluster` resource. This can be done by using the `JobFlowInstancesConfig` property type's `TaskInstanceGroups` and `TaskInstanceFleets` subproperties. Using these subproperties reduces delays in provisioning task nodes compared to specifying task nodes with the `AWS::EMR::InstanceGroupConfig` and `AWS::EMR::InstanceFleetConfig` resources. Please refer to the examples at the bottom of this page to learn how to use these subproperties.

## Syntax
<a name="aws-resource-emr-cluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-emr-cluster-syntax.json"></a>

```
{
  "Type" : "AWS::EMR::Cluster",
  "Properties" : {
      "[AdditionalInfo](#cfn-emr-cluster-additionalinfo)" : {{Json}},
      "[Applications](#cfn-emr-cluster-applications)" : {{[ Application, ... ]}},
      "[AutoScalingRole](#cfn-emr-cluster-autoscalingrole)" : {{String}},
      "[AutoTerminationPolicy](#cfn-emr-cluster-autoterminationpolicy)" : {{AutoTerminationPolicy}},
      "[BootstrapActions](#cfn-emr-cluster-bootstrapactions)" : {{[ BootstrapActionConfig, ... ]}},
      "[Configurations](#cfn-emr-cluster-configurations)" : {{[ Configuration, ... ]}},
      "[CustomAmiId](#cfn-emr-cluster-customamiid)" : {{String}},
      "[EbsRootVolumeIops](#cfn-emr-cluster-ebsrootvolumeiops)" : {{Integer}},
      "[EbsRootVolumeSize](#cfn-emr-cluster-ebsrootvolumesize)" : {{Integer}},
      "[EbsRootVolumeThroughput](#cfn-emr-cluster-ebsrootvolumethroughput)" : {{Integer}},
      "[Instances](#cfn-emr-cluster-instances)" : {{JobFlowInstancesConfig}},
      "[JobFlowRole](#cfn-emr-cluster-jobflowrole)" : {{String}},
      "[KerberosAttributes](#cfn-emr-cluster-kerberosattributes)" : {{KerberosAttributes}},
      "[LogEncryptionKmsKeyId](#cfn-emr-cluster-logencryptionkmskeyid)" : {{String}},
      "[LogUri](#cfn-emr-cluster-loguri)" : {{String}},
      "[ManagedScalingPolicy](#cfn-emr-cluster-managedscalingpolicy)" : {{ManagedScalingPolicy}},
      "[Name](#cfn-emr-cluster-name)" : {{String}},
      "[OSReleaseLabel](#cfn-emr-cluster-osreleaselabel)" : {{String}},
      "[PlacementGroupConfigs](#cfn-emr-cluster-placementgroupconfigs)" : {{[ PlacementGroupConfig, ... ]}},
      "[ReleaseLabel](#cfn-emr-cluster-releaselabel)" : {{String}},
      "[ScaleDownBehavior](#cfn-emr-cluster-scaledownbehavior)" : {{String}},
      "[SecurityConfiguration](#cfn-emr-cluster-securityconfiguration)" : {{String}},
      "[ServiceRole](#cfn-emr-cluster-servicerole)" : {{String}},
      "[StepConcurrencyLevel](#cfn-emr-cluster-stepconcurrencylevel)" : {{Integer}},
      "[Steps](#cfn-emr-cluster-steps)" : {{[ StepConfig, ... ]}},
      "[Tags](#cfn-emr-cluster-tags)" : {{[ Tag, ... ]}},
      "[VisibleToAllUsers](#cfn-emr-cluster-visibletoallusers)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-emr-cluster-syntax.yaml"></a>

```
Type: AWS::EMR::Cluster
Properties:
  [AdditionalInfo](#cfn-emr-cluster-additionalinfo): {{Json}}
  [Applications](#cfn-emr-cluster-applications): {{
    - Application}}
  [AutoScalingRole](#cfn-emr-cluster-autoscalingrole): {{String}}
  [AutoTerminationPolicy](#cfn-emr-cluster-autoterminationpolicy): {{
    AutoTerminationPolicy}}
  [BootstrapActions](#cfn-emr-cluster-bootstrapactions): {{
    - BootstrapActionConfig}}
  [Configurations](#cfn-emr-cluster-configurations): {{
    - Configuration}}
  [CustomAmiId](#cfn-emr-cluster-customamiid): {{String}}
  [EbsRootVolumeIops](#cfn-emr-cluster-ebsrootvolumeiops): {{Integer}}
  [EbsRootVolumeSize](#cfn-emr-cluster-ebsrootvolumesize): {{Integer}}
  [EbsRootVolumeThroughput](#cfn-emr-cluster-ebsrootvolumethroughput): {{Integer}}
  [Instances](#cfn-emr-cluster-instances): {{
    JobFlowInstancesConfig}}
  [JobFlowRole](#cfn-emr-cluster-jobflowrole): {{String}}
  [KerberosAttributes](#cfn-emr-cluster-kerberosattributes): {{
    KerberosAttributes}}
  [LogEncryptionKmsKeyId](#cfn-emr-cluster-logencryptionkmskeyid): {{String}}
  [LogUri](#cfn-emr-cluster-loguri): {{String}}
  [ManagedScalingPolicy](#cfn-emr-cluster-managedscalingpolicy): {{
    ManagedScalingPolicy}}
  [Name](#cfn-emr-cluster-name): {{String}}
  [OSReleaseLabel](#cfn-emr-cluster-osreleaselabel): {{String}}
  [PlacementGroupConfigs](#cfn-emr-cluster-placementgroupconfigs): {{
    - PlacementGroupConfig}}
  [ReleaseLabel](#cfn-emr-cluster-releaselabel): {{String}}
  [ScaleDownBehavior](#cfn-emr-cluster-scaledownbehavior): {{String}}
  [SecurityConfiguration](#cfn-emr-cluster-securityconfiguration): {{String}}
  [ServiceRole](#cfn-emr-cluster-servicerole): {{String}}
  [StepConcurrencyLevel](#cfn-emr-cluster-stepconcurrencylevel): {{Integer}}
  [Steps](#cfn-emr-cluster-steps): {{
    - StepConfig}}
  [Tags](#cfn-emr-cluster-tags): {{
    - Tag}}
  [VisibleToAllUsers](#cfn-emr-cluster-visibletoallusers): {{Boolean}}
```

## Properties
<a name="aws-resource-emr-cluster-properties"></a>

`AdditionalInfo`  <a name="cfn-emr-cluster-additionalinfo"></a>
A JSON string for selecting additional features.
*Required*: No
*Type*: Json
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Applications`  <a name="cfn-emr-cluster-applications"></a>
The applications to install on this cluster, for example, Spark, Flink, Oozie, Zeppelin, and so on.
*Required*: No
*Type*: Array of [Application](aws-properties-emr-cluster-application.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AutoScalingRole`  <a name="cfn-emr-cluster-autoscalingrole"></a>
An IAM role for automatic scaling policies. The default role is `EMR_AutoScaling_DefaultRole`. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate Amazon EC2 instances in an instance group.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AutoTerminationPolicy`  <a name="cfn-emr-cluster-autoterminationpolicy"></a>
An auto-termination policy for an Amazon EMR cluster. An auto-termination policy defines the amount of idle time in seconds after which a cluster automatically terminates. For alternative cluster termination options, see [Control cluster termination](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html).
*Required*: No
*Type*: [AutoTerminationPolicy](aws-properties-emr-cluster-autoterminationpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BootstrapActions`  <a name="cfn-emr-cluster-bootstrapactions"></a>
A list of bootstrap actions to run before Hadoop starts on the cluster nodes.
*Required*: No
*Type*: Array of [BootstrapActionConfig](aws-properties-emr-cluster-bootstrapactionconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configurations`  <a name="cfn-emr-cluster-configurations"></a>
Applies only to Amazon EMR releases 4.x and later. The list of configurations that are supplied to the Amazon EMR cluster.
*Required*: No
*Type*: Array of [Configuration](aws-properties-emr-cluster-configuration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomAmiId`  <a name="cfn-emr-cluster-customamiid"></a>
Available only in Amazon EMR releases 5.7.0 and later. The ID of a custom Amazon EBS-backed Linux AMI if the cluster uses a custom AMI.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EbsRootVolumeIops`  <a name="cfn-emr-cluster-ebsrootvolumeiops"></a>
The IOPS, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EbsRootVolumeSize`  <a name="cfn-emr-cluster-ebsrootvolumesize"></a>
The size, in GiB, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 4.x and later.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EbsRootVolumeThroughput`  <a name="cfn-emr-cluster-ebsrootvolumethroughput"></a>
The throughput, in MiB/s, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Instances`  <a name="cfn-emr-cluster-instances"></a>
A specification of the number and type of Amazon EC2 instances.
*Required*: Yes
*Type*: [JobFlowInstancesConfig](aws-properties-emr-cluster-jobflowinstancesconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobFlowRole`  <a name="cfn-emr-cluster-jobflowrole"></a>
Also called instance profile and Amazon EC2 role. An IAM role for an Amazon EMR cluster. The Amazon EC2 instances of the cluster assume this role. The default role is `EMR_EC2_DefaultRole`. In order to use the default role, you must have already created it using the AWS CLI or console.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KerberosAttributes`  <a name="cfn-emr-cluster-kerberosattributes"></a>
Attributes for Kerberos configuration when Kerberos authentication is enabled using a security configuration. For more information see [Use Kerberos Authentication](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html) in the *Amazon EMR Management Guide*.
*Required*: No
*Type*: [KerberosAttributes](aws-properties-emr-cluster-kerberosattributes.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogEncryptionKmsKeyId`  <a name="cfn-emr-cluster-logencryptionkmskeyid"></a>
 The AWS KMS key used for encrypting log files. This attribute is only available with Amazon EMR 5.30.0 and later, excluding Amazon EMR 6.0.0.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogUri`  <a name="cfn-emr-cluster-loguri"></a>
The path to the Amazon S3 location where logs for this cluster are stored.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ManagedScalingPolicy`  <a name="cfn-emr-cluster-managedscalingpolicy"></a>
Creates or updates a managed scaling policy for an Amazon EMR cluster. The managed scaling policy defines the limits for resources, such as Amazon EC2 instances that can be added or terminated from a cluster. The policy only applies to the core and task nodes. The master node cannot be scaled after initial configuration.
*Required*: No
*Type*: [ManagedScalingPolicy](aws-properties-emr-cluster-managedscalingpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-emr-cluster-name"></a>
The name of the cluster. This parameter can't contain the characters <, >, $, \|, or ` (backtick).
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OSReleaseLabel`  <a name="cfn-emr-cluster-osreleaselabel"></a>
The Amazon Linux release specified in a cluster launch RunJobFlow request. If no Amazon Linux release was specified, the default Amazon Linux release is shown in the response.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PlacementGroupConfigs`  <a name="cfn-emr-cluster-placementgroupconfigs"></a>
Property description not available.
*Required*: No
*Type*: Array of [PlacementGroupConfig](aws-properties-emr-cluster-placementgroupconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReleaseLabel`  <a name="cfn-emr-cluster-releaselabel"></a>
The Amazon EMR release label, which determines the version of open-source application packages installed on the cluster. Release labels are in the form `emr-x.x.x`, where x.x.x is an Amazon EMR release version such as `emr-5.14.0`. For more information about Amazon EMR release versions and included application versions and features, see [https://docs.aws.amazon.com/emr/latest/ReleaseGuide/](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/). The release label applies only to Amazon EMR releases version 4.0 and later. Earlier versions use `AmiVersion`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScaleDownBehavior`  <a name="cfn-emr-cluster-scaledownbehavior"></a>
The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized. `TERMINATE_AT_INSTANCE_HOUR` indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. `TERMINATE_AT_TASK_COMPLETION` indicates that Amazon EMR adds nodes to a deny list and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. `TERMINATE_AT_TASK_COMPLETION` is available only in Amazon EMR releases 4.1.0 and later, and is the default for versions of Amazon EMR earlier than 5.1.0.
*Required*: No
*Type*: String
*Allowed values*: `TERMINATE_AT_INSTANCE_HOUR | TERMINATE_AT_TASK_COMPLETION`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityConfiguration`  <a name="cfn-emr-cluster-securityconfiguration"></a>
The name of the security configuration applied to the cluster.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `10280`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceRole`  <a name="cfn-emr-cluster-servicerole"></a>
The IAM role that Amazon EMR assumes in order to access AWS resources on your behalf.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StepConcurrencyLevel`  <a name="cfn-emr-cluster-stepconcurrencylevel"></a>
Specifies the number of steps that can be executed concurrently. The default value is `1`. The maximum value is `256`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Steps`  <a name="cfn-emr-cluster-steps"></a>
A list of steps to run.
*Required*: No
*Type*: Array of [StepConfig](aws-properties-emr-cluster-stepconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-emr-cluster-tags"></a>
A list of tags associated with a cluster.
*Required*: No
*Type*: Array of [Tag](aws-properties-emr-cluster-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisibleToAllUsers`  <a name="cfn-emr-cluster-visibletoallusers"></a>
Indicates whether the cluster is visible to all IAM users of the AWS account associated with the cluster. If this value is set to `true`, all IAM users of that AWS account can view and manage the cluster if they have the proper policy permissions set. If this value is `false`, only the IAM user that created the cluster can view and manage it. This value can be changed using the SetVisibleToAllUsers action.
When you create clusters directly through the EMR console or API, this value is set to `true` by default. However, for `AWS::EMR::Cluster` resources in CloudFormation, the default is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-emr-cluster-return-values"></a>

### Ref
<a name="aws-resource-emr-cluster-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns returns the cluster ID, such as j-1ABCD123AB1A.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-emr-cluster-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-emr-cluster-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier for the cluster.

`MasterPublicDNS`  <a name="MasterPublicDNS-fn::getatt"></a>
The public DNS name of the master node (instance), such as `ec2-12-123-123-123.us-west-2.compute.amazonaws.com`.

## Examples
<a name="aws-resource-emr-cluster--examples"></a>

Create cluster examples.

**Topics**
+ [Create a cluster using a custom AMI for EC2 instances](#aws-resource-emr-cluster--examples--Create_a_cluster_using_a_custom_AMI_for_EC2_instances)
+ [Create a cluster and specify the root volume size of EC2 instances](#aws-resource-emr-cluster--examples--Create_a_cluster_and_specify_the_root_volume_size_of_EC2_instances)
+ [Create a cluster with Kerberos authentication](#aws-resource-emr-cluster--examples--Create_a_cluster_with_Kerberos_authentication)
+ [Create a cluster with a managed scaling policy](#aws-resource-emr-cluster--examples--Create_a_cluster_with_a_managed_scaling_policy)
+ [Create a cluster with task instance groups](#aws-resource-emr-cluster--examples--Create_a_cluster_with_task_instance_groups)
+ [Create a cluster with a task instance fleet](#aws-resource-emr-cluster--examples--Create_a_cluster_with_a_task_instance_fleet)

### Create a cluster using a custom AMI for EC2 instances
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_using_a_custom_AMI_for_EC2_instances"></a>

The following example template specifies a cluster using a custom Amazon Linux AMI for the EC2 instances in the cluster.

#### JSON
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_using_a_custom_AMI_for_EC2_instances--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters" : {
    "CustomAmiId" : {
      "Type" : "String"
    },
    "InstanceType" : {
      "Type" : "String"
    },
    "ReleaseLabel" : {
      "Type" : "String"
    },
    "SubnetId" : {
      "Type" : "String"
    },
    "TerminationProtected" : {
      "Type" : "String",
      "Default" : "false"
    },
    "ElasticMapReducePrincipal" : {
      "Type" : "String"
    },
    "Ec2Principal" : {
      "Type" : "String"
    }
  },
  "Resources": {
    "cluster": {
      "Type": "AWS::EMR::Cluster",
      "Properties": {
        "CustomAmiId" : {"Ref" : "CustomAmiId"},
        "Instances": {
          "MasterInstanceGroup": {
            "InstanceCount": 1,
            "InstanceType": {"Ref" : "InstanceType"},
            "Market": "ON_DEMAND",
            "Name": "cfnMaster"
          },
          "CoreInstanceGroup": {
            "InstanceCount": 1,
            "InstanceType": {"Ref" : "InstanceType"},
            "Market": "ON_DEMAND",
            "Name": "cfnCore"
          },
          "TaskInstanceGroups": [
            {
              "InstanceCount": 1,
              "InstanceType": {"Ref" : "InstanceType"},
              "Market": "ON_DEMAND",
              "Name": "cfnTask-1"
            },
            {
              "InstanceCount": 1,
              "InstanceType": {"Ref" : "InstanceType"},
              "Market": "ON_DEMAND",
              "Name": "cfnTask-2"
            }
          ],
          "TerminationProtected" : {"Ref" : "TerminationProtected"},
          "Ec2SubnetId" : {"Ref" : "SubnetId"}
        },
        "Name": "CFNtest",
        "JobFlowRole" : {"Ref": "emrEc2InstanceProfile"},
        "ServiceRole" : {"Ref": "emrRole"},
        "ReleaseLabel" : {"Ref" : "ReleaseLabel"},
        "VisibleToAllUsers" : true,
        "Tags": [
          {
            "Key": "key1",
            "Value": "value1"
          }
        ]
      }
    },
    "emrRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17"		 	 	 ,
          "Statement": [
            {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                "Service": {"Ref" : "ElasticMapReducePrincipal"}
              },
              "Action": "sts:AssumeRole"
            }
          ]
        },
        "Path": "/",
        "ManagedPolicyArns": ["arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole"]
      }
    },
    "emrEc2Role": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17"		 	 	 ,
          "Statement": [
            {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                "Service": {"Ref" : "Ec2Principal"}
              },
              "Action": "sts:AssumeRole"
            }
          ]
        },
        "Path": "/",
        "ManagedPolicyArns": ["arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role"]
      }
    },
    "emrEc2InstanceProfile": {
      "Type": "AWS::IAM::InstanceProfile",
      "Properties": {
        "Path": "/",
        "Roles": [ {
          "Ref": "emrEc2Role"
        } ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_using_a_custom_AMI_for_EC2_instances--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  CustomAmiId:
    Type: String
  InstanceType:
    Type: String
  ReleaseLabel:
    Type: String
  SubnetId:
    Type: String
  TerminationProtected:
    Type: String
    Default: 'false'
  ElasticMapReducePrincipal:
    Type: String
  Ec2Principal:
    Type: String
Resources:
  cluster:
    Type: AWS::EMR::Cluster
    Properties:
      CustomAmiId: !Ref CustomAmiId
      Instances:
        MasterInstanceGroup:
          InstanceCount: 1
          InstanceType: !Ref InstanceType
          Market: ON_DEMAND
          Name: cfnMaster
        CoreInstanceGroup:
          InstanceCount: 1
          InstanceType: !Ref InstanceType
          Market: ON_DEMAND
          Name: cfnCore
        TaskInstanceGroups:
          - InstanceCount: 1
            InstanceType: !Ref InstanceType
            Market: ON_DEMAND
            Name: cfnTask-1
          - InstanceCount: 1
            InstanceType: !Ref InstanceType
            Market: ON_DEMAND
            Name: cfnTask-2
        TerminationProtected: !Ref TerminationProtected
        Ec2SubnetId: !Ref SubnetId
      Name: CFNtest
      JobFlowRole: !Ref emrEc2InstanceProfile
      ServiceRole: !Ref emrRole
      ReleaseLabel: !Ref ReleaseLabel
      VisibleToAllUsers: true
      Tags:
        - Key: key1
          Value: value1
  emrRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2008-10-17
        Statement:
          - Sid: ''
            Effect: Allow
            Principal:
              Service: !Ref ElasticMapReducePrincipal
            Action: 'sts:AssumeRole'
      Path: /
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole'
  emrEc2Role:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2008-10-17
        Statement:
          - Sid: ''
            Effect: Allow
            Principal:
              Service: !Ref Ec2Principal
            Action: 'sts:AssumeRole'
      Path: /
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role'
  emrEc2InstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: /
      Roles:
        - !Ref emrEc2Role
```

### Create a cluster and specify the root volume size of EC2 instances
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_and_specify_the_root_volume_size_of_EC2_instances"></a>

The following example template enables you to specify the size of the EBS root volume for cluster instances.

#### JSON
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_and_specify_the_root_volume_size_of_EC2_instances--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters" : {
    "InstanceType" : {
      "Type" : "String"
    },
    "ReleaseLabel" : {
      "Type" : "String"
    },
    "SubnetId" : {
      "Type" : "String"
    },
    "TerminationProtected" : {
      "Type" : "String",
      "Default" : "false"
    },
    "EbsRootVolumeSize" : {
      "Type" : "String"
    }
  },
  "Resources": {
    "cluster": {
      "Type": "AWS::EMR::Cluster",
      "Properties": {
        "EbsRootVolumeSize" : {"Ref" : "EbsRootVolumeSize"},
        "Instances": {
          "MasterInstanceGroup": {
            "InstanceCount": 1,
            "InstanceType": {"Ref" : "InstanceType"},
            "Market": "ON_DEMAND",
            "Name": "cfnMaster"
          },
          "CoreInstanceGroup": {
            "InstanceCount": 1,
            "InstanceType": {"Ref" : "InstanceType"},
            "Market": "ON_DEMAND",
            "Name": "cfnCore"
          },
          "TaskInstanceGroups": [
            {
              "InstanceCount": 1,
              "InstanceType": {"Ref" : "InstanceType"},
              "Market": "ON_DEMAND",
              "Name": "cfnTask-1"
            },
            {
              "InstanceCount": 1,
              "InstanceType": {"Ref" : "InstanceType"},
              "Market": "ON_DEMAND",
              "Name": "cfnTask-2"
            }
          ],
          "TerminationProtected" : {"Ref" : "TerminationProtected"},
          "Ec2SubnetId" : {"Ref" : "SubnetId"}
        },
        "Name": "CFNtest",
        "JobFlowRole" : {"Ref": "emrEc2InstanceProfile"},
        "ServiceRole" : {"Ref": "emrRole"},
        "ReleaseLabel" : {"Ref" : "ReleaseLabel"},
        "VisibleToAllUsers" : true,
        "Tags": [
          {
            "Key": "key1",
            "Value": "value1"
          }
        ]
      }
    },
    "emrRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17"		 	 	 ,
          "Statement": [
            {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                "Service": "elasticmapreduce.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
            }
          ]
        },
        "Path": "/",
        "ManagedPolicyArns": ["arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole"]
      }
    },
    "emrEc2Role": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17"		 	 	 ,
          "Statement": [
            {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                "Service": "ec2.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
            }
          ]
        },
        "Path": "/",
        "ManagedPolicyArns": ["arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role"]
      }
    },
    "emrEc2InstanceProfile": {
      "Type": "AWS::IAM::InstanceProfile",
      "Properties": {
        "Path": "/",
        "Roles": [ {
          "Ref": "emrEc2Role"
        } ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_and_specify_the_root_volume_size_of_EC2_instances--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  InstanceType:
    Type: String
  ReleaseLabel:
    Type: String
  SubnetId:
    Type: String
  TerminationProtected:
    Type: String
    Default: 'false'
  EbsRootVolumeSize:
    Type: String
Resources:
  cluster:
    Type: AWS::EMR::Cluster
    Properties:
      EbsRootVolumeSize: !Ref EbsRootVolumeSize
      Instances:
        MasterInstanceGroup:
          InstanceCount: 1
          InstanceType: !Ref InstanceType
          Market: ON_DEMAND
          Name: cfnMaster
        CoreInstanceGroup:
          InstanceCount: 1
          InstanceType: !Ref InstanceType
          Market: ON_DEMAND
          Name: cfnCore
        TaskInstanceGroups:
          - InstanceCount: 1
            InstanceType: !Ref InstanceType
            Market: ON_DEMAND
            Name: cfnTask-1
          - InstanceCount: 1
            InstanceType: !Ref InstanceType
            Market: ON_DEMAND
            Name: cfnTask-2
        TerminationProtected: !Ref TerminationProtected
        Ec2SubnetId: !Ref SubnetId
      Name: CFNtest
      JobFlowRole: !Ref emrEc2InstanceProfile
      ServiceRole: !Ref emrRole
      ReleaseLabel: !Ref ReleaseLabel
      VisibleToAllUsers: true
      Tags:
        - Key: key1
          Value: value1
  emrRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2008-10-17
        Statement:
          - Sid: ''
            Effect: Allow
            Principal:
              Service: elasticmapreduce.amazonaws.com
            Action: 'sts:AssumeRole'
      Path: /
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole'
  emrEc2Role:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2008-10-17
        Statement:
          - Sid: ''
            Effect: Allow
            Principal:
              Service: ec2.amazonaws.com
            Action: 'sts:AssumeRole'
      Path: /
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role'
  emrEc2InstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: /
      Roles:
        - !Ref emrEc2Role
```

### Create a cluster with Kerberos authentication
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_with_Kerberos_authentication"></a>

The following example template enables you to specify the Kerberos authentication configuration for an EMR cluster.

#### JSON
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_with_Kerberos_authentication--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters" : {
    "CrossRealmTrustPrincipalPassword" : {
      "Type" : "String"
    },
    "KdcAdminPassword" : {
      "Type" : "String"
    },
    "Realm" : {
      "Type" : "String"
    },
    "InstanceType" : {
      "Type" : "String"
    },
    "ReleaseLabel" : {
      "Type" : "String"
    },
    "SubnetId" : {
      "Type" : "String"
    }
  },
  "Resources": {
    "cluster": {
      "Type": "AWS::EMR::Cluster",
      "Properties": {
        "Instances": {
          "MasterInstanceGroup": {
            "InstanceCount": 1,
            "InstanceType": {"Ref" : "InstanceType"},
            "Market": "ON_DEMAND",
            "Name": "cfnMaster"
          },
          "CoreInstanceGroup": {
            "InstanceCount": 1,
            "InstanceType": {"Ref" : "InstanceType"},
            "Market": "ON_DEMAND",
            "Name": "cfnCore"
          },
          "TaskInstanceGroups": [
            {
              "InstanceCount": 1,
              "InstanceType": {"Ref" : "InstanceType"},
              "Market": "ON_DEMAND",
              "Name": "cfnTask-1"
            },
            {
              "InstanceCount": 1,
              "InstanceType": {"Ref" : "InstanceType"},
              "Market": "ON_DEMAND",
              "Name": "cfnTask-2"
            }
          ],
          "Ec2SubnetId" : {"Ref" : "SubnetId"}
        },
        "Name": "CFNtest2",
        "JobFlowRole" : {"Ref": "emrEc2InstanceProfile"},
        "KerberosAttributes" : {
          "CrossRealmTrustPrincipalPassword" : "CfnIntegrationTest-1",
          "KdcAdminPassword" : "CfnIntegrationTest-1",
          "Realm": "EC2.INTERNAL"
        },
        "ServiceRole" : {"Ref": "emrRole"},
        "ReleaseLabel" : {"Ref" : "ReleaseLabel"},
        "SecurityConfiguration" : {"Ref" : "securityConfiguration"},
        "VisibleToAllUsers" : true,
        "Tags": [
          {
            "Key": "key1",
            "Value": "value1"
          }
        ]
      }
    },
    "key" : {
      "Type" : "AWS::KMS::Key",
      "Properties" : {
        "KeyPolicy" : {
          "Version": "2012-10-17"		 	 	 ,
          "Id": "key-default-1",
          "Statement": [
            {
              "Sid": "Enable IAM User Permissions",
              "Effect": "Allow",
              "Principal": {
                "AWS": { "Fn::GetAtt" : ["emrEc2Role", "Arn"]}
              },
              "Action": "kms:*",
              "Resource": "*"
            },
            {
              "Sid": "Enable IAM User Permissions",
              "Effect": "Allow",
              "Principal": {
                "AWS": { "Fn::Join" : ["" , ["arn:aws:iam::", {"Ref" : "AWS::AccountId"} ,":root" ]] }
              },
              "Action": "kms:*",
              "Resource": "*"
            }
          ]
        }
      }
    },
    "securityConfiguration": {
      "Type" : "AWS::EMR::SecurityConfiguration",
      "Properties" : {
        "SecurityConfiguration" : {
          "AuthenticationConfiguration": {
            "KerberosConfiguration": {
              "Provider": "ClusterDedicatedKdc",
              "ClusterDedicatedKdcConfiguration": {
                "TicketLifetimeInHours": 24,
                "CrossRealmTrustConfiguration": {
                  "Realm": "AD.DOMAIN.COM",
                  "Domain": "ad.domain.com",
                  "AdminServer": "ad.domain.com",
                  "KdcServer": "ad.domain.com"
                }
              }
            }
          }
        }
      }
    },
    "emrRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17"		 	 	 ,
          "Statement": [
            {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                "Service": "elasticmapreduce.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
            }
          ]
        },
        "Path": "/",
        "ManagedPolicyArns": ["arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole"]
      }
    },
    "emrEc2Role": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17"		 	 	 ,
          "Statement": [
            {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                "Service": "ec2.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
            }
          ]
        },
        "Path": "/",
        "ManagedPolicyArns": ["arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role"]
      }
    },
    "emrEc2InstanceProfile": {
      "Type": "AWS::IAM::InstanceProfile",
      "Properties": {
        "Path": "/",
        "Roles": [ {
          "Ref": "emrEc2Role"
        } ]
      }
    }
  },
  "Outputs" : {
    "keyArn" : {
      "Value" : {"Fn::GetAtt" : ["key", "Arn"]}
    }
  }
}
```

#### YAML
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_with_Kerberos_authentication--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  CrossRealmTrustPrincipalPassword:
    Type: String
  KdcAdminPassword:
    Type: String
  Realm:
    Type: String
  InstanceType:
    Type: String
  ReleaseLabel:
    Type: String
  SubnetId:
    Type: String
Resources:
  cluster:
    Type: 'AWS::EMR::Cluster'
    Properties:
      Instances:
        MasterInstanceGroup:
          InstanceCount: 1
          InstanceType: !Ref InstanceType
          Market: ON_DEMAND
          Name: cfnMaster
        CoreInstanceGroup:
          InstanceCount: 1
          InstanceType: !Ref InstanceType
          Market: ON_DEMAND
          Name: cfnCore
        TaskInstanceGroups:
          - InstanceCount: 1
            InstanceType: !Ref InstanceType
            Market: ON_DEMAND
            Name: cfnTask-1
          - InstanceCount: 1
            InstanceType: !Ref InstanceType
            Market: ON_DEMAND
            Name: cfnTask-2
        Ec2SubnetId: !Ref SubnetId
      Name: CFNtest2
      JobFlowRole: !Ref emrEc2InstanceProfile
      KerberosAttributes:
        CrossRealmTrustPrincipalPassword: CfnIntegrationTest-1
        KdcAdminPassword: CfnIntegrationTest-1
        Realm: EC2.INTERNAL
      ServiceRole: !Ref emrRole
      ReleaseLabel: !Ref ReleaseLabel
      SecurityConfiguration: !Ref securityConfiguration
      VisibleToAllUsers: true
      Tags:
        - Key: key1
          Value: value1
  key:
    Type: 'AWS::KMS::Key'
    Properties:
      KeyPolicy:
        Version: 2012-10-17
        Id: key-default-1
        Statement:
          - Sid: Enable IAM User Permissions
            Effect: Allow
            Principal:
              AWS: !GetAtt
                - emrEc2Role
                - Arn
            Action: 'kms:*'
            Resource: '*'
          - Sid: Enable IAM User Permissions
            Effect: Allow
            Principal:
              AWS: !Join
                - ''
                - - 'arn:aws:iam::'
                  - !Ref 'AWS::AccountId'
                  - ':root'
            Action: 'kms:*'
            Resource: '*'
  securityConfiguration:
    Type: 'AWS::EMR::SecurityConfiguration'
    Properties:
      SecurityConfiguration:
        AuthenticationConfiguration:
          KerberosConfiguration:
            Provider: ClusterDedicatedKdc
            ClusterDedicatedKdcConfiguration:
              TicketLifetimeInHours: 24
              CrossRealmTrustConfiguration:
                Realm: AD.DOMAIN.COM
                Domain: ad.domain.com
                AdminServer: ad.domain.com
                KdcServer: ad.domain.com
  emrRole:
    Type: 'AWS::IAM::Role'
    Properties:
      AssumeRolePolicyDocument:
        Version: 2008-10-17
        Statement:
          - Sid: ''
            Effect: Allow
            Principal:
              Service: elasticmapreduce.amazonaws.com
            Action: 'sts:AssumeRole'
      Path: /
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole'
  emrEc2Role:
    Type: 'AWS::IAM::Role'
    Properties:
      AssumeRolePolicyDocument:
        Version: 2008-10-17
        Statement:
          - Sid: ''
            Effect: Allow
            Principal:
              Service: ec2.amazonaws.com
            Action: 'sts:AssumeRole'
      Path: /
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role'
  emrEc2InstanceProfile:
    Type: 'AWS::IAM::InstanceProfile'
    Properties:
      Path: /
      Roles:
        - !Ref emrEc2Role
Outputs:
  keyArn:
    Value: !GetAtt
      - key
      - Arn
```

### Create a cluster with a managed scaling policy
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_with_a_managed_scaling_policy"></a>

The following example template enables you to specify the managed scaling policy for an EMR cluster.

#### JSON
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_with_a_managed_scaling_policy--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters" : {
    "InstanceType" : {
      "Type" : "String"
    },
    "ReleaseLabel" : {
      "Type" : "String"
    },
    "SubnetId" : {
      "Type" : "String"
    },
    "MinimumCapacityUnits" : {
      "Type" : "String"
    },
    "MaximumCapacityUnits" : {
      "Type" : "String"
    },
    "MaximumCoreCapacityUnits" : {
      "Type" : "String"
    },
    "MaximumOnDemandCapacityUnits" : {
      "Type" : "String"
    },
    "UnitType" : {
      "Type" : "String"
    }
  },
  "Resources": {
    "cluster": {
      "Type": "AWS::EMR::Cluster",
      "Properties": {
        "Instances": {
          "MasterInstanceGroup": {
            "InstanceCount": 1,
            "InstanceType": {"Ref" : "InstanceType"},
            "Market": "ON_DEMAND",
            "Name": "primary"
          },
          "CoreInstanceGroup": {
            "InstanceCount": 1,
            "InstanceType": {"Ref" : "InstanceType"},
            "Market": "ON_DEMAND",
            "Name": "core"
          },
          "TaskInstanceGroups": [
            {
              "InstanceCount": 1,
              "InstanceType": {"Ref" : "InstanceType"},
              "Market": "ON_DEMAND",
              "Name": "cfnTask-1"
            },
            {
              "InstanceCount": 1,
              "InstanceType": {"Ref" : "InstanceType"},
              "Market": "ON_DEMAND",
              "Name": "cfnTask-2"
            }
          ],
          "Ec2SubnetId" : {"Ref" : "SubnetId"}
        },
        "Name": "ManagedScalingExample",
        "JobFlowRole" : "EMR_EC2_DefaultRole",
        "ServiceRole" : "EMR_DefaultRole",
        "ReleaseLabel" : {"Ref" : "ReleaseLabel"},
        "ManagedScalingPolicy" : {
          "ComputeLimits" : {
            "MinimumCapacityUnits" : {"Ref": "MinimumCapacityUnits"},
            "MaximumCapacityUnits" : {"Ref": "MaximumCapacityUnits"},
            "MaximumCoreCapacityUnits" : {"Ref": "MaximumCoreCapacityUnits"},
            "MaximumOnDemandCapacityUnits" : {"Ref": "MaximumOnDemandCapacityUnits"},
            "UnitType" : {"Ref": "UnitType"}
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_with_a_managed_scaling_policy--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  InstanceType:
    Type: String
  ReleaseLabel:
    Type: String
  SubnetId:
    Type: String
  MinimumCapacityUnits:
    Type: String
  MaximumCapacityUnits:
    Type: String
  MaximumCoreCapacityUnits:
    Type: String
  MaximumOnDemandCapacityUnits:
    Type: String
  UnitType:
    Type: String
Resources:
  cluster:
    Type: 'AWS::EMR::Cluster'
    Properties:
      Instances:
        MasterInstanceGroup:
          InstanceCount: 1
          InstanceType: !Ref InstanceType
          Market: ON_DEMAND
          Name: primary
        CoreInstanceGroup:
          InstanceCount: 1
          InstanceType: !Ref InstanceType
          Market: ON_DEMAND
          Name: core
        TaskInstanceGroups:
          - InstanceCount: 1
            InstanceType: !Ref InstanceType
            Market: ON_DEMAND
            Name: cfnTask-1
          - InstanceCount: 1
            InstanceType: !Ref InstanceType
            Market: ON_DEMAND
            Name: cfnTask-2
        Ec2SubnetId: !Ref SubnetId
      Name: ManagedScalingExample
      JobFlowRole: EMR_EC2_DefaultRole
      ServiceRole: EMR_DefaultRole
      ReleaseLabel: !Ref ReleaseLabel
      ManagedScalingPolicy:
        ComputeLimits:
          MinimumCapacityUnits: !Ref MinimumCapacityUnits
          MaximumCapacityUnits: !Ref MaximumCapacityUnits
          MaximumCoreCapacityUnits: !Ref MaximumCoreCapacityUnits
          MaximumOnDemandCapacityUnits: !Ref MaximumOnDemandCapacityUnits
          UnitType: !Ref UnitType
```

### Create a cluster with task instance groups
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_with_task_instance_groups"></a>

The following example template enables you to create task instance groups for an EMR cluster.

#### JSON
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_with_task_instance_groups--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters" : {
    "InstanceType" : {
      "Type" : "String"
    },
    "ReleaseLabel" : {
      "Type" : "String"
    },
    "SubnetId" : {
      "Type" : "String"
    },
    "TerminationProtected" : {
      "Type" : "String",
      "Default" : "false"
    },
    "ElasticMapReducePrincipal" : {
      "Type" : "String"
    },
    "Ec2Principal" : {
      "Type" : "String"
    }
  },
  "Resources": {
    "cluster": {
      "Type": "AWS::EMR::Cluster",
      "Properties": {
        "Instances": {
          "MasterInstanceGroup": {
            "InstanceCount": 1,
            "InstanceType": {"Ref" : "InstanceType"},
            "Market": "ON_DEMAND",
            "Name": "cfnMaster"
          },
          "CoreInstanceGroup": {
            "InstanceCount": 1,
            "InstanceType": {"Ref" : "InstanceType"},
            "Market": "ON_DEMAND",
            "Name": "cfnCore"
          },
          "TaskInstanceGroups": [
            {
              "InstanceCount": 1,
              "InstanceType": {"Ref" : "InstanceType"},
              "Market": "ON_DEMAND",
              "Name": "cfnTask-1"
            },
            {
              "InstanceCount": 1,
              "InstanceType": {"Ref" : "InstanceType"},
              "Market": "ON_DEMAND",
              "Name": "cfnTask-2"
            }
          ],
          "TerminationProtected" : {"Ref" : "TerminationProtected"},
          "Ec2SubnetId" : {"Ref" : "SubnetId"}
        },
        "Name": "CFNtest",
        "JobFlowRole" : {"Ref": "emrEc2InstanceProfile"},
        "ServiceRole" : {"Ref": "emrRole"},
        "ReleaseLabel" : {"Ref" : "ReleaseLabel"},

        "VisibleToAllUsers" : true,
        "Tags": [
          {
            "Key": "key1",
            "Value": "value1"
          }
        ]
      }
    },
    "emrRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17"		 	 	 ,
          "Statement": [
            {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                "Service": {"Ref" : "ElasticMapReducePrincipal"}
              },
              "Action": "sts:AssumeRole"
            }
          ]
        },
        "Path": "/",
        "ManagedPolicyArns": ["arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole"]
      }
    },
    "emrEc2Role": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17"		 	 	 ,
          "Statement": [
            {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                "Service": {"Ref" : "Ec2Principal"}
              },
              "Action": "sts:AssumeRole"
            }
          ]
        },
        "Path": "/",
        "ManagedPolicyArns": ["arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role"]
      }
    },
    "emrEc2InstanceProfile": {
      "Type": "AWS::IAM::InstanceProfile",
      "Properties": {
        "Path": "/",
        "Roles": [ {
          "Ref": "emrEc2Role"
        } ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_with_task_instance_groups--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  InstanceType:
    Type: String
  ReleaseLabel:
    Type: String
  SubnetId:
    Type: String
  TerminationProtected:
    Type: String
    Default: 'false'
  ElasticMapReducePrincipal:
    Type: String
  Ec2Principal:
    Type: String
Resources:
  cluster:
    Type: AWS::EMR::Cluster
    Properties:
      Instances:
        MasterInstanceGroup:
          InstanceCount: 1
          InstanceType: !Ref InstanceType
          Market: ON_DEMAND
          Name: cfnMaster
        CoreInstanceGroup:
          InstanceCount: 1
          InstanceType: !Ref InstanceType
          Market: ON_DEMAND
          Name: cfnCore
        TaskInstanceGroups:
          - InstanceCount: 1
            InstanceType: !Ref InstanceType
            Market: ON_DEMAND
            Name: cfnTask-1
          - InstanceCount: 1
            InstanceType: !Ref InstanceType
            Market: ON_DEMAND
            Name: cfnTask-2
        TerminationProtected: !Ref TerminationProtected
        Ec2SubnetId: !Ref SubnetId
      Name: CFNtest
      JobFlowRole: !Ref emrEc2InstanceProfile
      ServiceRole: !Ref emrRole
      ReleaseLabel: !Ref ReleaseLabel
      VisibleToAllUsers: true
      Tags:
        - Key: key1
          Value: value1
  emrRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2008-10-17
        Statement:
          - Sid: ''
            Effect: Allow
            Principal:
              Service: !Ref ElasticMapReducePrincipal
            Action: 'sts:AssumeRole'
      Path: /
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole'
  emrEc2Role:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2008-10-17
        Statement:
          - Sid: ''
            Effect: Allow
            Principal:
              Service: !Ref Ec2Principal
            Action: 'sts:AssumeRole'
      Path: /
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role'
  emrEc2InstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: /
      Roles:
        - !Ref emrEc2Role
```

### Create a cluster with a task instance fleet
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_with_a_task_instance_fleet"></a>

The following example template enables you to create a task instance fleet for an EMR cluster.

#### JSON
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_with_a_task_instance_fleet--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters" : {
    "InstanceType" : {
      "Type" : "String"
    },
    "ReleaseLabel" : {
      "Type" : "String"
    },
    "SubnetId" : {
      "Type" : "String"
    },
    "TerminationProtected" : {
      "Type" : "String",
      "Default" : "false"
    },
    "ElasticMapReducePrincipal" : {
      "Type" : "String"
    },
    "Ec2Principal" : {
      "Type" : "String"
    }
  },
  "Resources": {
    "cluster": {
      "Type": "AWS::EMR::Cluster",
      "Properties": {
        "Instances": {
          "MasterInstanceFleet": {
            "Name": "cfnMaster",
            "TargetOnDemandCapacity": 1,
            "TargetSpotCapacity": 0,
            "InstanceTypeConfigs": [
              {
                "InstanceType": {"Ref" : "InstanceType"},
                "WeightedCapacity": 1
              }
            ]
          },
          "CoreInstanceFleet": {
            "Name": "cfnCore",
            "TargetOnDemandCapacity": 1,
            "TargetSpotCapacity": 0,
            "InstanceTypeConfigs": [
              {
                "InstanceType": {"Ref" : "InstanceType"},
                "WeightedCapacity": 1
              }
            ]
          },
          "TaskInstanceFleets": [
            {
              "Name": "cfnTask",
              "TargetOnDemandCapacity": 1,
              "TargetSpotCapacity": 0,
              "InstanceTypeConfigs": [
                {
                  "InstanceType": {"Ref" : "InstanceType"},
                  "WeightedCapacity": 1
                }
              ]
            }
          ],
          "TerminationProtected" : {"Ref" : "TerminationProtected"},
          "Ec2SubnetIds" : [
            {"Ref" : "SubnetId"}
          ]
        },
        "Name": "CFNtest",
        "JobFlowRole" : {"Ref": "emrEc2InstanceProfile"},
        "ServiceRole" : {"Ref": "emrRole"},
        "ReleaseLabel" : {"Ref" : "ReleaseLabel"},
        "VisibleToAllUsers" : true,
        "Tags": [
          {
            "Key": "key1",
            "Value": "value1"
          }
        ]
      }
    },
    "emrRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17"		 	 	 ,
          "Statement": [
            {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                "Service": {"Ref" : "ElasticMapReducePrincipal"}
              },
              "Action": "sts:AssumeRole"
            }
          ]
        },
        "Path": "/",
        "ManagedPolicyArns": ["arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole"]
      }
    },
    "emrEc2Role": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17"		 	 	 ,
          "Statement": [
            {
              "Sid": "",

              "Effect": "Allow",
              "Principal": {
                "Service": {"Ref" : "Ec2Principal"}
              },
              "Action": "sts:AssumeRole"
            }
          ]
        },
        "Path": "/",
        "ManagedPolicyArns": ["arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role"]
      }
    },
    "emrEc2InstanceProfile": {
      "Type": "AWS::IAM::InstanceProfile",
      "Properties": {
        "Path": "/",
        "Roles": [ {
          "Ref": "emrEc2Role"
        } ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-emr-cluster--examples--Create_a_cluster_with_a_task_instance_fleet--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  InstanceType:
    Type: String
  ReleaseLabel:
    Type: String
  SubnetId:
    Type: String
  TerminationProtected:
    Type: String
    Default: 'false'
  ElasticMapReducePrincipal:
    Type: String
  Ec2Principal:
    Type: String
Resources:
  cluster:
    Type: AWS::EMR::Cluster
    Properties:
      Instances:
        MasterInstanceFleet:
          Name: cfnMaster
          TargetOnDemandCapacity: 1
          TargetSpotCapacity: 0
          InstanceTypeConfigs:
            - InstanceType: !Ref InstanceType
              WeightedCapacity: 1
        CoreInstanceFleet:
          Name: cfnCore
          TargetOnDemandCapacity: 1
          TargetSpotCapacity: 0
          InstanceTypeConfigs:
            - InstanceType: !Ref InstanceType
              WeightedCapacity: 1
        TaskInstanceFleets:
          - Name: cfnTask
            TargetOnDemandCapacity: 1
            TargetSpotCapacity: 0
            InstanceTypeConfigs:
              - InstanceType: !Ref InstanceType
                WeightedCapacity: 1
        TerminationProtected: !Ref TerminationProtected
        Ec2SubnetIds:
          - !Ref SubnetId
      Name: CFNtest
      JobFlowRole: !Ref emrEc2InstanceProfile
      ServiceRole: !Ref emrRole
      ReleaseLabel: !Ref ReleaseLabel
      VisibleToAllUsers: true
      Tags:
        - Key: key1
          Value: value1
  emrRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2008-10-17
        Statement:
          - Sid: ''
            Effect: Allow
            Principal:
              Service: !Ref ElasticMapReducePrincipal
            Action: 'sts:AssumeRole'
      Path: /
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole'
  emrEc2Role:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2008-10-17
        Statement:
          - Sid: ''
            Effect: Allow
            Principal:
              Service: !Ref Ec2Principal
            Action: 'sts:AssumeRole'
      Path: /
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role'
  emrEc2InstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: /
      Roles:
        - !Ref emrEc2Role
```
