---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeCluster.html
---

# DescribeCluster
<a name="API_DescribeCluster"></a>

Retrieves information of a SageMaker HyperPod cluster.

## Request Syntax
<a name="API_DescribeCluster_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_DescribeCluster_RequestSyntax) **   <a name="sagemaker-DescribeCluster-request-ClusterName"></a>
The string name or the Amazon Resource Name (ARN) of the SageMaker HyperPod cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

## Response Syntax
<a name="API_DescribeCluster_ResponseSyntax"></a>

```
{
   "AutoScaling": {
      "AutoScalerType": "string",
      "FailureMessage": "string",
      "Mode": "string",
      "Status": "string"
   },
   "ClusterArn": "string",
   "ClusterName": "string",
   "ClusterRole": "string",
   "ClusterStatus": "string",
   "CreationTime": number,
   "FailureMessage": "string",
   "InstanceGroups": [
      {
         "ActiveOperations": {
            "string" : number
         },
         "ActiveSoftwareUpdateConfig": {
            "AutoRollbackConfiguration": [
               {
                  "AlarmName": "string"
               }
            ],
            "RollingUpdatePolicy": {
               "MaximumBatchSize": {
                  "Type": "string",
                  "Value": number
               },
               "RollbackMaximumBatchSize": {
                  "Type": "string",
                  "Value": number
               }
            },
            "WaitIntervalInSeconds": number
         },
         "AutoPatchConfig": {
            "CurrentPatchSchedule": {
               "NextPatchDate": number
            },
            "DeploymentConfig": {
               "AutoRollbackConfiguration": [
                  {
                     "AlarmName": "string"
                  }
               ],
               "RollingUpdatePolicy": {
                  "MaximumBatchSize": {
                     "Type": "string",
                     "Value": number
                  },
                  "RollbackMaximumBatchSize": {
                     "Type": "string",
                     "Value": number
                  }
               },
               "WaitIntervalInSeconds": number
            },
            "DesiredPatchSchedule": {
               "NextPatchDate": number
            },
            "PatchingStrategy": "string"
         },
         "CapacityRequirements": {
            "OnDemand": {
            },
            "Spot": {
            }
         },
         "CurrentCount": number,
         "CurrentImageId": "string",
         "CurrentImageReleaseVersion": "string",
         "DesiredImageId": "string",
         "DesiredImageReleaseVersion": "string",
         "ExecutionRole": "string",
         "ImageVersionStatus": "string",
         "InstanceGroupName": "string",
         "InstanceRequirements": {
            "CurrentInstanceTypes": [ "string" ],
            "DesiredInstanceTypes": [ "string" ]
         },
         "InstanceStorageConfigs": [
            { ... }
         ],
         "InstanceType": "string",
         "InstanceTypeDetails": [
            {
               "CurrentCount": number,
               "InstanceType": "string",
               "ThreadsPerCore": number
            }
         ],
         "KubernetesConfig": {
            "CurrentLabels": {
               "string" : "string"
            },
            "CurrentTaints": [
               {
                  "Effect": "string",
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "DesiredLabels": {
               "string" : "string"
            },
            "DesiredTaints": [
               {
                  "Effect": "string",
                  "Key": "string",
                  "Value": "string"
               }
            ]
         },
         "LifeCycleConfig": {
            "OnCreate": "string",
            "OnInitComplete": "string",
            "SourceS3Uri": "string"
         },
         "MinCount": number,
         "NetworkInterface": {
            "InterfaceType": "string"
         },
         "OnStartDeepHealthChecks": [ "string" ],
         "OverrideVpcConfig": {
            "SecurityGroupIds": [ "string" ],
            "Subnets": [ "string" ]
         },
         "ScheduledUpdateConfig": {
            "DeploymentConfig": {
               "AutoRollbackConfiguration": [
                  {
                     "AlarmName": "string"
                  }
               ],
               "RollingUpdatePolicy": {
                  "MaximumBatchSize": {
                     "Type": "string",
                     "Value": number
                  },
                  "RollbackMaximumBatchSize": {
                     "Type": "string",
                     "Value": number
                  }
               },
               "WaitIntervalInSeconds": number
            },
            "ScheduleExpression": "string"
         },
         "SlurmConfig": {
            "NodeType": "string",
            "PartitionNames": [ "string" ]
         },
         "SoftwareUpdateStatus": "string",
         "Status": "string",
         "TargetCount": number,
         "TargetStateCount": number,
         "ThreadsPerCore": number,
         "TrainingPlanArn": "string",
         "TrainingPlanStatus": "string"
      }
   ],
   "NodeProvisioningMode": "string",
   "NodeRecovery": "string",
   "Orchestrator": {
      "Eks": {
         "ClusterArn": "string"
      },
      "Slurm": {
         "SlurmConfigStrategy": "string"
      }
   },
   "RestrictedInstanceGroups": [
      {
         "CurrentCount": number,
         "EnvironmentConfig": {
            "FSxLustreConfig": {
               "PerUnitStorageThroughput": number,
               "SizeInGiB": number
            },
            "S3OutputPath": "string"
         },
         "ExecutionRole": "string",
         "InstanceGroupName": "string",
         "InstanceStorageConfigs": [
            { ... }
         ],
         "InstanceType": "string",
         "OnStartDeepHealthChecks": [ "string" ],
         "OverrideVpcConfig": {
            "SecurityGroupIds": [ "string" ],
            "Subnets": [ "string" ]
         },
         "ScheduledUpdateConfig": {
            "DeploymentConfig": {
               "AutoRollbackConfiguration": [
                  {
                     "AlarmName": "string"
                  }
               ],
               "RollingUpdatePolicy": {
                  "MaximumBatchSize": {
                     "Type": "string",
                     "Value": number
                  },
                  "RollbackMaximumBatchSize": {
                     "Type": "string",
                     "Value": number
                  }
               },
               "WaitIntervalInSeconds": number
            },
            "ScheduleExpression": "string"
         },
         "Status": "string",
         "TargetCount": number,
         "ThreadsPerCore": number,
         "TrainingPlanArn": "string",
         "TrainingPlanStatus": "string"
      }
   ],
   "RestrictedInstanceGroupsConfig": {
      "SharedEnvironmentConfig": {
         "CurrentFSxLustreConfig": {
            "PerUnitStorageThroughput": number,
            "SizeInGiB": number
         },
         "CurrentFSxLustreDeletionPolicy": "string",
         "DesiredFSxLustreConfig": {
            "PerUnitStorageThroughput": number,
            "SizeInGiB": number
         },
         "DesiredFSxLustreDeletionPolicy": "string"
      }
   },
   "TieredStorageConfig": {
      "InstanceMemoryAllocationPercentage": number,
      "Mode": "string"
   },
   "VpcConfig": {
      "SecurityGroupIds": [ "string" ],
      "Subnets": [ "string" ]
   }
}
```

## Response Elements
<a name="API_DescribeCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoScaling](#API_DescribeCluster_ResponseSyntax) **   <a name="sagemaker-DescribeCluster-response-AutoScaling"></a>
The current autoscaling configuration and status for the autoscaler.
Type: [ClusterAutoScalingConfigOutput](API_ClusterAutoScalingConfigOutput.md) object

 ** [ClusterArn](#API_DescribeCluster_ResponseSyntax) **   <a name="sagemaker-DescribeCluster-response-ClusterArn"></a>
The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`

 ** [ClusterName](#API_DescribeCluster_ResponseSyntax) **   <a name="sagemaker-DescribeCluster-response-ClusterName"></a>
The name of the SageMaker HyperPod cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`

 ** [ClusterRole](#API_DescribeCluster_ResponseSyntax) **   <a name="sagemaker-DescribeCluster-response-ClusterRole"></a>
The Amazon Resource Name (ARN) of the IAM role that HyperPod uses for cluster autoscaling operations.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [ClusterStatus](#API_DescribeCluster_ResponseSyntax) **   <a name="sagemaker-DescribeCluster-response-ClusterStatus"></a>
The status of the SageMaker HyperPod cluster.
Type: String
Valid Values: `Creating | Deleting | Failed | InService | RollingBack | SystemUpdating | Updating`

 ** [CreationTime](#API_DescribeCluster_ResponseSyntax) **   <a name="sagemaker-DescribeCluster-response-CreationTime"></a>
The time when the SageMaker Cluster is created.
Type: Timestamp

 ** [FailureMessage](#API_DescribeCluster_ResponseSyntax) **   <a name="sagemaker-DescribeCluster-response-FailureMessage"></a>
The failure message of the SageMaker HyperPod cluster.
Type: String

 ** [InstanceGroups](#API_DescribeCluster_ResponseSyntax) **   <a name="sagemaker-DescribeCluster-response-InstanceGroups"></a>
The instance groups of the SageMaker HyperPod cluster.
Type: Array of [ClusterInstanceGroupDetails](API_ClusterInstanceGroupDetails.md) objects

 ** [NodeProvisioningMode](#API_DescribeCluster_ResponseSyntax) **   <a name="sagemaker-DescribeCluster-response-NodeProvisioningMode"></a>
The mode used for provisioning nodes in the cluster.
Type: String
Valid Values: `Continuous`

 ** [NodeRecovery](#API_DescribeCluster_ResponseSyntax) **   <a name="sagemaker-DescribeCluster-response-NodeRecovery"></a>
The node recovery mode configured for the SageMaker HyperPod cluster.
Type: String
Valid Values: `Automatic | None`

 ** [Orchestrator](#API_DescribeCluster_ResponseSyntax) **   <a name="sagemaker-DescribeCluster-response-Orchestrator"></a>
The type of orchestrator used for the SageMaker HyperPod cluster.
Type: [ClusterOrchestrator](API_ClusterOrchestrator.md) object

 ** [RestrictedInstanceGroups](#API_DescribeCluster_ResponseSyntax) **   <a name="sagemaker-DescribeCluster-response-RestrictedInstanceGroups"></a>
The specialized instance groups for training models like Amazon Nova to be created in the SageMaker HyperPod cluster.
Type: Array of [ClusterRestrictedInstanceGroupDetails](API_ClusterRestrictedInstanceGroupDetails.md) objects

 ** [RestrictedInstanceGroupsConfig](#API_DescribeCluster_ResponseSyntax) **   <a name="sagemaker-DescribeCluster-response-RestrictedInstanceGroupsConfig"></a>
The configuration for the restricted instance groups (RIG) in the SageMaker HyperPod cluster.
Type: [ClusterRestrictedInstanceGroupsConfigOutput](API_ClusterRestrictedInstanceGroupsConfigOutput.md) object

 ** [TieredStorageConfig](#API_DescribeCluster_ResponseSyntax) **   <a name="sagemaker-DescribeCluster-response-TieredStorageConfig"></a>
The current configuration for managed tier checkpointing on the HyperPod cluster. For example, this shows whether the feature is enabled and the percentage of cluster memory allocated for checkpoint storage.
Type: [ClusterTieredStorageConfig](API_ClusterTieredStorageConfig.md) object

 ** [VpcConfig](#API_DescribeCluster_ResponseSyntax) **   <a name="sagemaker-DescribeCluster-response-VpcConfig"></a>
Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).
Type: [VpcConfig](API_VpcConfig.md) object

## Errors
<a name="API_DescribeCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
