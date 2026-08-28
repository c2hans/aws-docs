---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html
---

# UpdateCluster
<a name="API_UpdateCluster"></a>

Updates a SageMaker HyperPod cluster.

## Request Syntax
<a name="API_UpdateCluster_RequestSyntax"></a>

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
   "InstanceGroupsToDelete": [ "{{string}}" ],
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
   "TieredStorageConfig": {
      "InstanceMemoryAllocationPercentage": {{number}},
      "Mode": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoScaling](#API_UpdateCluster_RequestSyntax) **   <a name="sagemaker-UpdateCluster-request-AutoScaling"></a>
Updates the autoscaling configuration for the cluster. Use to enable or disable automatic node scaling.
Type: [ClusterAutoScalingConfig](API_ClusterAutoScalingConfig.md) object
Required: No

 ** [ClusterName](#API_UpdateCluster_RequestSyntax) **   <a name="sagemaker-UpdateCluster-request-ClusterName"></a>
Specify the name of the SageMaker HyperPod cluster you want to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [ClusterRole](#API_UpdateCluster_RequestSyntax) **   <a name="sagemaker-UpdateCluster-request-ClusterRole"></a>
The Amazon Resource Name (ARN) of the IAM role that HyperPod assumes for cluster autoscaling operations. Cannot be updated while autoscaling is enabled.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** [InstanceGroups](#API_UpdateCluster_RequestSyntax) **   <a name="sagemaker-UpdateCluster-request-InstanceGroups"></a>
Specify the instance groups to update.
Type: Array of [ClusterInstanceGroupSpecification](API_ClusterInstanceGroupSpecification.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [InstanceGroupsToDelete](#API_UpdateCluster_RequestSyntax) **   <a name="sagemaker-UpdateCluster-request-InstanceGroupsToDelete"></a>
Specify the names of the instance groups to delete. Use a single `,` as the separator between multiple names.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** [NodeProvisioningMode](#API_UpdateCluster_RequestSyntax) **   <a name="sagemaker-UpdateCluster-request-NodeProvisioningMode"></a>
Determines how instance provisioning is handled during cluster operations. In `Continuous` mode, the cluster provisions available instances incrementally and retries until the target count is reached. The cluster becomes operational once cluster-level resources are ready. Use `CurrentCount` and `TargetCount` in `DescribeCluster` to track provisioning progress.
Type: String
Valid Values: `Continuous`
Required: No

 ** [NodeRecovery](#API_UpdateCluster_RequestSyntax) **   <a name="sagemaker-UpdateCluster-request-NodeRecovery"></a>
The node recovery mode to be applied to the SageMaker HyperPod cluster.
Type: String
Valid Values: `Automatic | None`
Required: No

 ** [Orchestrator](#API_UpdateCluster_RequestSyntax) **   <a name="sagemaker-UpdateCluster-request-Orchestrator"></a>
The type of orchestrator used for the SageMaker HyperPod cluster.
Type: [ClusterOrchestrator](API_ClusterOrchestrator.md) object
Required: No

 ** [RestrictedInstanceGroups](#API_UpdateCluster_RequestSyntax) **   <a name="sagemaker-UpdateCluster-request-RestrictedInstanceGroups"></a>
The specialized instance groups for training models like Amazon Nova to be created in the SageMaker HyperPod cluster.
Type: Array of [ClusterRestrictedInstanceGroupSpecification](API_ClusterRestrictedInstanceGroupSpecification.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [RestrictedInstanceGroupsConfig](#API_UpdateCluster_RequestSyntax) **   <a name="sagemaker-UpdateCluster-request-RestrictedInstanceGroupsConfig"></a>
The configuration for the restricted instance groups (RIG) in the SageMaker HyperPod cluster.
Type: [ClusterRestrictedInstanceGroupsConfig](API_ClusterRestrictedInstanceGroupsConfig.md) object
Required: No

 ** [TieredStorageConfig](#API_UpdateCluster_RequestSyntax) **   <a name="sagemaker-UpdateCluster-request-TieredStorageConfig"></a>
Updates the configuration for managed tier checkpointing on the HyperPod cluster. For example, you can enable or disable the feature and modify the percentage of cluster memory allocated for checkpoint storage.
Type: [ClusterTieredStorageConfig](API_ClusterTieredStorageConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateCluster_ResponseSyntax"></a>

```
{
   "ClusterArn": "string"
}
```

## Response Elements
<a name="API_UpdateCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterArn](#API_UpdateCluster_ResponseSyntax) **   <a name="sagemaker-UpdateCluster-response-ClusterArn"></a>
The Amazon Resource Name (ARN) of the updated SageMaker HyperPod cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`

## Errors
<a name="API_UpdateCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
