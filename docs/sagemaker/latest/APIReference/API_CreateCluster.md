---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCluster.html
---

# CreateCluster
<a name="API_CreateCluster"></a>

Creates an Amazon SageMaker HyperPod cluster. SageMaker HyperPod is a capability of SageMaker for creating and managing persistent clusters for developing large machine learning models, such as large language models (LLMs) and diffusion models. To learn more, see [Amazon SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) in the *Amazon SageMaker Developer Guide*.

## Request Syntax
<a name="API_CreateCluster_RequestSyntax"></a>

```
{
   "AutoScaling": {
      "AutoScalerType": "{{string}}",
      "Mode": "{{string}}"
   },
   "ClusterName": "{{string}}",
   "ClusterRole": "{{string}}",
   "InstanceGroups": [
      {
         "AutoPatchConfig": {
            "DeploymentConfig": {
               "AutoRollbackConfiguration": [
                  {
                     "AlarmName": "{{string}}"
                  }
               ],
               "RollingUpdatePolicy": {
                  "MaximumBatchSize": {
                     "Type": "{{string}}",
                     "Value": {{number}}
                  },
                  "RollbackMaximumBatchSize": {
                     "Type": "{{string}}",
                     "Value": {{number}}
                  }
               },
               "WaitIntervalInSeconds": {{number}}
            },
            "PatchingStrategy": "{{string}}",
            "PatchSchedule": {
               "NextPatchDate": {{number}}
            }
         },
         "CapacityRequirements": {
            "OnDemand": {
            },
            "Spot": {
            }
         },
         "ExecutionRole": "{{string}}",
         "ImageId": "{{string}}",
         "ImageReleaseVersion": "{{string}}",
         "InstanceCount": {{number}},
         "InstanceGroupName": "{{string}}",
         "InstanceRequirements": {
            "InstanceTypes": [ "{{string}}" ]
         },
         "InstanceStorageConfigs": [
            { ... }
         ],
         "InstanceType": "{{string}}",
         "KubernetesConfig": {
            "Labels": {
               "{{string}}" : "{{string}}"
            },
            "Taints": [
               {
                  "Effect": "{{string}}",
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         },
         "LifeCycleConfig": {
            "OnCreate": "{{string}}",
            "OnInitComplete": "{{string}}",
            "SourceS3Uri": "{{string}}"
         },
         "MinInstanceCount": {{number}},
         "NetworkInterface": {
            "InterfaceType": "{{string}}"
         },
         "OnStartDeepHealthChecks": [ "{{string}}" ],
         "OverrideVpcConfig": {
            "SecurityGroupIds": [ "{{string}}" ],
            "Subnets": [ "{{string}}" ]
         },
         "ScheduledUpdateConfig": {
            "DeploymentConfig": {
               "AutoRollbackConfiguration": [
                  {
                     "AlarmName": "{{string}}"
                  }
               ],
               "RollingUpdatePolicy": {
                  "MaximumBatchSize": {
                     "Type": "{{string}}",
                     "Value": {{number}}
                  },
                  "RollbackMaximumBatchSize": {
                     "Type": "{{string}}",
                     "Value": {{number}}
                  }
               },
               "WaitIntervalInSeconds": {{number}}
            },
            "ScheduleExpression": "{{string}}"
         },
         "SlurmConfig": {
            "NodeType": "{{string}}",
            "PartitionNames": [ "{{string}}" ]
         },
         "ThreadsPerCore": {{number}},
         "TrainingPlanArn": "{{string}}"
      }
   ],
   "NodeProvisioningMode": "{{string}}",
   "NodeRecovery": "{{string}}",
   "Orchestrator": {
      "Eks": {
         "ClusterArn": "{{string}}"
      },
      "Slurm": {
         "SlurmConfigStrategy": "{{string}}"
      }
   },
   "RestrictedInstanceGroups": [
      {
         "EnvironmentConfig": {
            "FSxLustreConfig": {
               "PerUnitStorageThroughput": {{number}},
               "SizeInGiB": {{number}}
            }
         },
         "ExecutionRole": "{{string}}",
         "InstanceCount": {{number}},
         "InstanceGroupName": "{{string}}",
         "InstanceStorageConfigs": [
            { ... }
         ],
         "InstanceType": "{{string}}",
         "OnStartDeepHealthChecks": [ "{{string}}" ],
         "OverrideVpcConfig": {
            "SecurityGroupIds": [ "{{string}}" ],
            "Subnets": [ "{{string}}" ]
         },
         "ScheduledUpdateConfig": {
            "DeploymentConfig": {
               "AutoRollbackConfiguration": [
                  {
                     "AlarmName": "{{string}}"
                  }
               ],
               "RollingUpdatePolicy": {
                  "MaximumBatchSize": {
                     "Type": "{{string}}",
                     "Value": {{number}}
                  },
                  "RollbackMaximumBatchSize": {
                     "Type": "{{string}}",
                     "Value": {{number}}
                  }
               },
               "WaitIntervalInSeconds": {{number}}
            },
            "ScheduleExpression": "{{string}}"
         },
         "ThreadsPerCore": {{number}},
         "TrainingPlanArn": "{{string}}"
      }
   ],
   "RestrictedInstanceGroupsConfig": {
      "SharedEnvironmentConfig": {
         "FSxLustreConfig": {
            "PerUnitStorageThroughput": {{number}},
            "SizeInGiB": {{number}}
         },
         "FSxLustreDeletionPolicy": "{{string}}"
      }
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TieredStorageConfig": {
      "InstanceMemoryAllocationPercentage": {{number}},
      "Mode": "{{string}}"
   },
   "VpcConfig": {
      "SecurityGroupIds": [ "{{string}}" ],
      "Subnets": [ "{{string}}" ]
   }
}
```

## Request Parameters
<a name="API_CreateCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoScaling](#API_CreateCluster_RequestSyntax) **   <a name="sagemaker-CreateCluster-request-AutoScaling"></a>
The autoscaling configuration for the cluster. Enables automatic scaling of cluster nodes based on workload demand using a Karpenter-based system.
Type: [ClusterAutoScalingConfig](API_ClusterAutoScalingConfig.md) object
Required: No

 ** [ClusterName](#API_CreateCluster_RequestSyntax) **   <a name="sagemaker-CreateCluster-request-ClusterName"></a>
The name for the new SageMaker HyperPod cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** [ClusterRole](#API_CreateCluster_RequestSyntax) **   <a name="sagemaker-CreateCluster-request-ClusterRole"></a>
The Amazon Resource Name (ARN) of the IAM role that HyperPod assumes to perform cluster autoscaling operations. This role must have permissions for `sagemaker:BatchAddClusterNodes` and `sagemaker:BatchDeleteClusterNodes`. This is only required when autoscaling is enabled and when HyperPod is performing autoscaling operations.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** [InstanceGroups](#API_CreateCluster_RequestSyntax) **   <a name="sagemaker-CreateCluster-request-InstanceGroups"></a>
The instance groups to be created in the SageMaker HyperPod cluster.
Type: Array of [ClusterInstanceGroupSpecification](API_ClusterInstanceGroupSpecification.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [NodeProvisioningMode](#API_CreateCluster_RequestSyntax) **   <a name="sagemaker-CreateCluster-request-NodeProvisioningMode"></a>
The mode for provisioning nodes in the cluster. You can specify the following modes:
+  **Continuous**: Scaling behavior that enables 1) concurrent operation execution within instance groups, 2) continuous retry mechanisms for failed operations, 3) enhanced customer visibility into cluster events through detailed event streams, 4) partial provisioning capabilities. Your clusters and instance groups remain `InService` while scaling. This mode is only supported for EKS orchestrated clusters.
Type: String
Valid Values: `Continuous`
Required: No

 ** [NodeRecovery](#API_CreateCluster_RequestSyntax) **   <a name="sagemaker-CreateCluster-request-NodeRecovery"></a>
The node recovery mode for the SageMaker HyperPod cluster. When set to `Automatic`, SageMaker HyperPod will automatically reboot or replace faulty nodes when issues are detected. When set to `None`, cluster administrators will need to manually manage any faulty cluster instances.
Type: String
Valid Values: `Automatic | None`
Required: No

 ** [Orchestrator](#API_CreateCluster_RequestSyntax) **   <a name="sagemaker-CreateCluster-request-Orchestrator"></a>
The type of orchestrator to use for the SageMaker HyperPod cluster. Currently, supported values are `"Eks"` and `"Slurm"`, which is to use an Amazon Elastic Kubernetes Service or Slurm cluster as the orchestrator.
If you specify the `Orchestrator` field, you must provide exactly one orchestrator configuration: either `Eks` or `Slurm`. Specifying both or providing an empty configuration returns a validation error.
Type: [ClusterOrchestrator](API_ClusterOrchestrator.md) object
Required: No

 ** [RestrictedInstanceGroups](#API_CreateCluster_RequestSyntax) **   <a name="sagemaker-CreateCluster-request-RestrictedInstanceGroups"></a>
The specialized instance groups for training models like Amazon Nova to be created in the SageMaker HyperPod cluster.
Type: Array of [ClusterRestrictedInstanceGroupSpecification](API_ClusterRestrictedInstanceGroupSpecification.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [RestrictedInstanceGroupsConfig](#API_CreateCluster_RequestSyntax) **   <a name="sagemaker-CreateCluster-request-RestrictedInstanceGroupsConfig"></a>
The configuration for the restricted instance groups (RIG) in the SageMaker HyperPod cluster.
Type: [ClusterRestrictedInstanceGroupsConfig](API_ClusterRestrictedInstanceGroupsConfig.md) object
Required: No

 ** [Tags](#API_CreateCluster_RequestSyntax) **   <a name="sagemaker-CreateCluster-request-Tags"></a>
Custom tags for managing the SageMaker HyperPod cluster as an AWS resource. You can add tags to your cluster in the same way you add them in other AWS services that support tagging. To learn more about tagging AWS resources in general, see [Tagging AWS Resources User Guide](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TieredStorageConfig](#API_CreateCluster_RequestSyntax) **   <a name="sagemaker-CreateCluster-request-TieredStorageConfig"></a>
The configuration for managed tier checkpointing on the HyperPod cluster. When enabled, this feature uses a multi-tier storage approach for storing model checkpoints, providing faster checkpoint operations and improved fault tolerance across cluster nodes.
Type: [ClusterTieredStorageConfig](API_ClusterTieredStorageConfig.md) object
Required: No

 ** [VpcConfig](#API_CreateCluster_RequestSyntax) **   <a name="sagemaker-CreateCluster-request-VpcConfig"></a>
Specifies the Amazon Virtual Private Cloud (VPC) that is associated with the Amazon SageMaker HyperPod cluster. You can control access to and from your resources by configuring your VPC. For more information, see [Give SageMaker access to resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).
When your Amazon VPC and subnets support IPv6, network communications differ based on the cluster orchestration platform:
+ Slurm-orchestrated clusters automatically configure nodes with dual IPv6 and IPv4 addresses, allowing immediate IPv6 network communications.
+ In Amazon EKS-orchestrated clusters, nodes receive dual-stack addressing, but pods can only use IPv6 when the Amazon EKS cluster is explicitly IPv6-enabled. For information about deploying an IPv6 Amazon EKS cluster, see [Amazon EKS IPv6 Cluster Deployment](https://docs.aws.amazon.com/eks/latest/userguide/deploy-ipv6-cluster.html#_deploy_an_ipv6_cluster_with_eksctl).
Additional resources for IPv6 configuration:
+ For information about adding IPv6 support to your VPC, see to [IPv6 Support for VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html).
+ For information about creating a new IPv6-compatible VPC, see [Amazon VPC Creation Guide](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html).
+ To configure SageMaker HyperPod with a custom Amazon VPC, see [Custom Amazon VPC Setup for SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html#sagemaker-hyperpod-prerequisites-optional-vpc).
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateCluster_ResponseSyntax"></a>

```
{
   "ClusterArn": "string"
}
```

## Response Elements
<a name="API_CreateCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterArn](#API_CreateCluster_ResponseSyntax) **   <a name="sagemaker-CreateCluster-response-ClusterArn"></a>
The Amazon Resource Name (ARN) of the cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`

## Errors
<a name="API_CreateCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateCluster)
