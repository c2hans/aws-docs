---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html
---

# UpdateService
<a name="API_UpdateService"></a>

Modifies the parameters of a service.

**Note**
On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.

For services using the rolling update (`ECS`) you can update the desired count, deployment configuration, network configuration, load balancers, service registries, enable ECS managed tags option, propagate tags option, task placement constraints and strategies, and task definition. When you update any of these parameters, Amazon ECS starts new tasks with the new configuration.

You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when starting or running a task, or when creating or updating a service. For more information, see [Amazon EBS volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types) in the *Amazon Elastic Container Service Developer Guide*. You can update your volume configurations and trigger a new deployment. `volumeConfigurations` is only supported for REPLICA service and not DAEMON service. If you leave `volumeConfigurations` `null`, it doesn't trigger a new deployment. For more information on volumes, see [Amazon EBS volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types) in the *Amazon Elastic Container Service Developer Guide*.

For services using the blue/green (`CODE_DEPLOY`) deployment controller, only the desired count, deployment configuration, health check grace period, task placement constraints and strategies, enable ECS managed tags option, and propagate tags can be updated using this API. If the network configuration, platform version, task definition, or load balancer need to be updated, create a new AWS CodeDeploy deployment. For more information, see [CreateDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html) in the * AWS CodeDeploy API Reference*.

For services using an external deployment controller, you can update only the desired count, task placement constraints and strategies, health check grace period, enable ECS managed tags option, and propagate tags option, using this API. If the launch type, load balancer, network configuration, platform version, or task definition need to be updated, create a new task set For more information, see [CreateTaskSet](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html).

You can add to or subtract from the number of instantiations of a task definition in a service by specifying the cluster that the service is running in and a new `desiredCount` parameter.

You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when starting or running a task, or when creating or updating a service. For more information, see [Amazon EBS volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types) in the *Amazon Elastic Container Service Developer Guide*.

If you have updated the container image of your application, you can create a new task definition with that image and deploy it to your service. The service scheduler uses the minimum healthy percent and maximum percent parameters (in the service's deployment configuration) to determine the deployment strategy.

**Note**
If your updated Docker image uses the same tag as what is in the existing task definition for your service (for example, `my_image:latest`), you don't need to create a new revision of your task definition. You can update the service using the `forceNewDeployment` option. The new tasks launched by the deployment pull the current image/tag combination from your repository when they start.

You can also update the deployment configuration of a service. When a deployment is triggered by updating the task definition of a service, the service scheduler uses the deployment configuration parameters, `minimumHealthyPercent` and `maximumPercent`, to determine the deployment strategy.
+ If `minimumHealthyPercent` is below 100%, the scheduler can ignore `desiredCount` temporarily during a deployment. For example, if `desiredCount` is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. Tasks for services that don't use a load balancer are considered healthy if they're in the `RUNNING` state. Tasks for services that use a load balancer are considered healthy if they're in the `RUNNING` state and are reported as healthy by the load balancer.
+ The `maximumPercent` parameter represents an upper limit on the number of running tasks during a deployment. You can use it to define the deployment batch size. For example, if `desiredCount` is four tasks, a maximum of 200% starts four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available).

When [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) stops a task during a deployment, the equivalent of `docker stop` is issued to the containers running in the task. This results in a `SIGTERM` and a 30-second timeout. After this, `SIGKILL` is sent and the containers are forcibly stopped. If the container handles the `SIGTERM` gracefully and exits within 30 seconds from receiving it, no `SIGKILL` is sent.

When the service scheduler launches new tasks, it determines task placement in your cluster with the following logic.
+ Determine which of the container instances in your cluster can support your service's task definition. For example, they have the required CPU, memory, ports, and container instance attributes.
+ By default, the service scheduler attempts to balance tasks across Availability Zones in this manner even though you can choose a different placement strategy.
  + Sort the valid container instances by the fewest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have zero, valid container instances in either zone B or C are considered optimal for placement.
  + Place the new service task on a valid container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the fewest number of running tasks for this service.

When the service scheduler stops running tasks, it attempts to maintain balance across the Availability Zones in your cluster using the following logic:
+ Sort the container instances by the largest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have two, container instances in either zone B or C are considered optimal for termination.
+ Stop the task on a container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the largest number of running tasks for this service.

## Request Syntax
<a name="API_UpdateService_RequestSyntax"></a>

```
{
   "availabilityZoneRebalancing": "{{string}}",
   "capacityProviderStrategy": [
      {
         "base": {{number}},
         "capacityProvider": "{{string}}",
         "weight": {{number}}
      }
   ],
   "cluster": "{{string}}",
   "deploymentConfiguration": {
      "alarms": {
         "alarmNames": [ "{{string}}" ],
         "enable": {{boolean}},
         "rollback": {{boolean}}
      },
      "bakeTimeInMinutes": {{number}},
      "canaryConfiguration": {
         "canaryBakeTimeInMinutes": {{number}},
         "canaryPercent": {{number}}
      },
      "deploymentCircuitBreaker": {
         "enable": {{boolean}},
         "resetOnHealthyTask": {{boolean}},
         "rollback": {{boolean}},
         "thresholdConfiguration": {
            "type": "{{string}}",
            "value": {{number}}
         }
      },
      "earlySuccessCriteria": {
         "enable": {{boolean}},
         "healthyPercent": {{number}},
         "sourceServiceRevisionCleanup": "{{string}}"
      },
      "lifecycleHooks": [
         {
            "hookDetails": {{JSON value}},
            "hookTargetArn": "{{string}}",
            "lifecycleStages": [ "{{string}}" ],
            "roleArn": "{{string}}",
            "targetType": "{{string}}",
            "timeoutConfiguration": {
               "action": "{{string}}",
               "timeoutInMinutes": {{number}}
            }
         }
      ],
      "linearConfiguration": {
         "stepBakeTimeInMinutes": {{number}},
         "stepPercent": {{number}}
      },
      "maximumPercent": {{number}},
      "minimumHealthyPercent": {{number}},
      "strategy": "{{string}}"
   },
   "deploymentController": {
      "type": "{{string}}"
   },
   "desiredCount": {{number}},
   "enableECSManagedTags": {{boolean}},
   "enableExecuteCommand": {{boolean}},
   "forceNewDeployment": {{boolean}},
   "healthCheckGracePeriodSeconds": {{number}},
   "loadBalancers": [
      {
         "advancedConfiguration": {
            "alternateTargetGroupArn": "{{string}}",
            "productionListenerRule": "{{string}}",
            "roleArn": "{{string}}",
            "testListenerRule": "{{string}}"
         },
         "containerName": "{{string}}",
         "containerPort": {{number}},
         "loadBalancerName": "{{string}}",
         "targetGroupArn": "{{string}}"
      }
   ],
   "monitoring": {
      "metricConfigurations": [
         {
            "metricNames": [ "{{string}}" ],
            "resolutionSeconds": {{number}}
         }
      ]
   },
   "networkConfiguration": {
      "awsvpcConfiguration": {
         "assignPublicIp": "{{string}}",
         "securityGroups": [ "{{string}}" ],
         "subnets": [ "{{string}}" ]
      }
   },
   "placementConstraints": [
      {
         "expression": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "placementStrategy": [
      {
         "field": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "platformVersion": "{{string}}",
   "propagateTags": "{{string}}",
   "service": "{{string}}",
   "serviceConnectConfiguration": {
      "accessLogConfiguration": {
         "format": "{{string}}",
         "includeQueryParameters": "{{string}}"
      },
      "enabled": {{boolean}},
      "logConfiguration": {
         "logDriver": "{{string}}",
         "options": {
            "{{string}}" : "{{string}}"
         },
         "secretOptions": [
            {
               "name": "{{string}}",
               "valueFrom": "{{string}}"
            }
         ]
      },
      "namespace": "{{string}}",
      "services": [
         {
            "clientAliases": [
               {
                  "dnsName": "{{string}}",
                  "port": {{number}},
                  "testTrafficRules": {
                     "header": {
                        "name": "{{string}}",
                        "value": {
                           "exact": "{{string}}"
                        }
                     }
                  }
               }
            ],
            "discoveryName": "{{string}}",
            "ingressPortOverride": {{number}},
            "portName": "{{string}}",
            "timeout": {
               "idleTimeoutSeconds": {{number}},
               "perRequestTimeoutSeconds": {{number}}
            },
            "tls": {
               "issuerCertificateAuthority": {
                  "awsPcaAuthorityArn": "{{string}}"
               },
               "kmsKey": "{{string}}",
               "roleArn": "{{string}}"
            }
         }
      ]
   },
   "serviceRegistries": [
      {
         "containerName": "{{string}}",
         "containerPort": {{number}},
         "port": {{number}},
         "registryArn": "{{string}}"
      }
   ],
   "taskDefinition": "{{string}}",
   "volumeConfigurations": [
      {
         "managedEBSVolume": {
            "encrypted": {{boolean}},
            "filesystemType": "{{string}}",
            "iops": {{number}},
            "kmsKeyId": "{{string}}",
            "roleArn": "{{string}}",
            "sizeInGiB": {{number}},
            "snapshotId": "{{string}}",
            "tagSpecifications": [
               {
                  "propagateTags": "{{string}}",
                  "resourceType": "{{string}}",
                  "tags": [
                     {
                        "key": "{{string}}",
                        "value": "{{string}}"
                     }
                  ]
               }
            ],
            "throughput": {{number}},
            "volumeInitializationRate": {{number}},
            "volumeType": "{{string}}"
         },
         "name": "{{string}}"
      }
   ],
   "vpcLatticeConfigurations": [
      {
         "portName": "{{string}}",
         "roleArn": "{{string}}",
         "targetGroupArn": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [availabilityZoneRebalancing](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-availabilityZoneRebalancing"></a>
Indicates whether to use Availability Zone rebalancing for the service.
For more information, see [Balancing an Amazon ECS service across Availability Zones](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html) in the * *Amazon Elastic Container Service Developer Guide* *.
The default behavior of `AvailabilityZoneRebalancing` differs between create and update requests:
+ For create service requests, when no value is specified for `AvailabilityZoneRebalancing`, Amazon ECS defaults the value to `ENABLED`.
+ For update service requests, when no value is specified for `AvailabilityZoneRebalancing`, Amazon ECS defaults to the existing service’s `AvailabilityZoneRebalancing` value. If the service never had an `AvailabilityZoneRebalancing` value set, Amazon ECS treats this as `DISABLED`.
This parameter doesn't trigger a new service deployment.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [capacityProviderStrategy](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-capacityProviderStrategy"></a>
The details of a capacity provider strategy. You can set a capacity provider when you create a cluster, run a task, or update a service.
If you want to use Amazon ECS Managed Instances, you must use the `capacityProviderStrategy` request parameter.
When you use Fargate, the capacity providers are `FARGATE` or `FARGATE_SPOT`.
When you use Amazon EC2, the capacity providers are Auto Scaling groups.
You can change capacity providers for rolling deployments and blue/green deployments.
The following list provides the valid transitions:
+ Update the Fargate launch type to an Auto Scaling group capacity provider.
+ Update the Amazon EC2 launch type to a Fargate capacity provider.
+ Update the Fargate capacity provider to an Auto Scaling group capacity provider.
+ Update the Amazon EC2 capacity provider to a Fargate capacity provider.
+ Update the Auto Scaling group or Fargate capacity provider back to the launch type.

  Pass an empty list in the `capacityProviderStrategy` parameter.
For information about AWS CDK considerations, see [AWS CDK considerations](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-parameters.html).
This parameter doesn't trigger a new service deployment.
Type: Array of [CapacityProviderStrategyItem](API_CapacityProviderStrategyItem.md) objects
Required: No

 ** [cluster](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster that your service runs on. If you do not specify a cluster, the default cluster is assumed.
You can't change the cluster name.
Type: String
Required: No

 ** [deploymentConfiguration](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-deploymentConfiguration"></a>
Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.
This parameter doesn't trigger a new service deployment.
Type: [DeploymentConfiguration](API_DeploymentConfiguration.md) object
Required: No

 ** [deploymentController](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-deploymentController"></a>
The deployment controller to use for the service.
Type: [DeploymentController](API_DeploymentController.md) object
Required: No

 ** [desiredCount](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-desiredCount"></a>
The number of instantiations of the task to place and keep running in your service.
This parameter doesn't trigger a new service deployment.
Type: Integer
Required: No

 ** [enableECSManagedTags](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-enableECSManagedTags"></a>
Determines whether to turn on Amazon ECS managed tags for the tasks in the service. For more information, see [Tagging Your Amazon ECS Resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon Elastic Container Service Developer Guide*.
Only tasks launched after the update will reflect the update. To update the tags on all tasks, set `forceNewDeployment` to `true`, so that Amazon ECS starts new tasks with the updated tags.
This parameter doesn't trigger a new service deployment.
Type: Boolean
Required: No

 ** [enableExecuteCommand](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-enableExecuteCommand"></a>
If `true`, this enables execute command functionality on all task containers.
If you do not want to override the value that was set when the service was created, you can set this to `null` when performing this action.
This parameter doesn't trigger a new service deployment.
Type: Boolean
Required: No

 ** [forceNewDeployment](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-forceNewDeployment"></a>
Determines whether to force a new deployment of the service. By default, deployments aren't forced. You can use this option to start a new deployment with no service definition changes. For example, you can update a service's tasks to use a newer Docker image with the same image/tag combination (`my_image:latest`) or to roll Fargate tasks onto a newer platform version.
Type: Boolean
Required: No

 ** [healthCheckGracePeriodSeconds](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-healthCheckGracePeriodSeconds"></a>
The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you don't specify a health check grace period value, the default value of `0` is used. If you don't use any of the health checks, then `healthCheckGracePeriodSeconds` is unused.
If your service's tasks take a while to start and respond to health checks, you can specify a health check grace period of up to 2,147,483,647 seconds (about 69 years). During that time, the Amazon ECS service scheduler ignores health check status. This grace period can prevent the service scheduler from marking tasks as unhealthy and stopping them before they have time to come up.
If your service has more running tasks than desired, unhealthy tasks in the grace period might be stopped to reach the desired count.
This parameter doesn't trigger a new service deployment.
Type: Integer
Required: No

 ** [loadBalancers](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-loadBalancers"></a>
You must have a service-linked role when you update this property
A list of Elastic Load Balancing load balancer objects. It contains the load balancer name, the container name, and the container port to access from the load balancer. The container name is as it appears in a container definition.
When you add, update, or remove a load balancer configuration, Amazon ECS starts new tasks with the updated Elastic Load Balancing configuration, and then stops the old tasks when the new tasks are running.
For services that use rolling updates, you can add, update, or remove Elastic Load Balancing target groups. You can update from a single target group to multiple target groups and from multiple target groups to a single target group.
For services that use blue/green deployments, you can update Elastic Load Balancing target groups by using ` [CreateDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html) ` through AWS CodeDeploy. Note that multiple target groups are not supported for blue/green deployments. For more information see [Register multiple target groups with a service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html) in the *Amazon Elastic Container Service Developer Guide*.
For services that use the external deployment controller, you can add, update, or remove load balancers by using [CreateTaskSet](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html). Note that multiple target groups are not supported for external deployments. For more information see [Register multiple target groups with a service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html) in the *Amazon Elastic Container Service Developer Guide*.
You can remove existing `loadBalancers` by passing an empty list.
This parameter triggers a new service deployment.
Type: Array of [LoadBalancer](API_LoadBalancer.md) objects
Required: No

 ** [monitoring](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-monitoring"></a>
The optional monitoring configuration for the service, which defines the resolution for the service-level `CPUUtilization` and `MemoryUtilization` Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of `60` seconds.
Type: [MonitoringConfiguration](API_MonitoringConfiguration.md) object
Required: No

 ** [networkConfiguration](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-networkConfiguration"></a>
An object representing the network configuration for the service.
This parameter triggers a new service deployment.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** [placementConstraints](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-placementConstraints"></a>
An array of task placement constraint objects to update the service to use. If no value is specified, the existing placement constraints for the service will remain unchanged. If this value is specified, it will override any existing placement constraints defined for the service. To remove all existing placement constraints, specify an empty array.
You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.
This parameter doesn't trigger a new service deployment.
Type: Array of [PlacementConstraint](API_PlacementConstraint.md) objects
Required: No

 ** [placementStrategy](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-placementStrategy"></a>
The task placement strategy objects to update the service to use. If no value is specified, the existing placement strategy for the service will remain unchanged. If this value is specified, it will override the existing placement strategy defined for the service. To remove an existing placement strategy, specify an empty object.
You can specify a maximum of five strategy rules for each service.
This parameter doesn't trigger a new service deployment.
Type: Array of [PlacementStrategy](API_PlacementStrategy.md) objects
Required: No

 ** [platformVersion](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-platformVersion"></a>
The platform version that your tasks in the service run on. A platform version is only specified for tasks using the Fargate launch type. If a platform version is not specified, the `LATEST` platform version is used. For more information, see [AWS Fargate Platform Versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide*.
This parameter triggers a new service deployment.
Type: String
Required: No

 ** [propagateTags](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-propagateTags"></a>
Determines whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags aren't propagated.
Only tasks launched after the update will reflect the update. To update the tags on all tasks, set `forceNewDeployment` to `true`, so that Amazon ECS starts new tasks with the updated tags.
This parameter doesn't trigger a new service deployment.
Type: String
Valid Values: `TASK_DEFINITION | SERVICE | NONE`
Required: No

 ** [service](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-service"></a>
The name of the service to update.
Type: String
Required: Yes

 ** [serviceConnectConfiguration](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-serviceConnectConfiguration"></a>
The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.
Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide*.
This parameter triggers a new service deployment.
Type: [ServiceConnectConfiguration](API_ServiceConnectConfiguration.md) object
Required: No

 ** [serviceRegistries](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-serviceRegistries"></a>
You must have a service-linked role when you update this property.
For more information about the role see the `CreateService` request parameter [`role`](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html#ECS-CreateService-request-role).
The details for the service discovery registries to assign to this service. For more information, see [Service Discovery](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html).
When you add, update, or remove the service registries configuration, Amazon ECS starts new tasks with the updated service registries configuration, and then stops the old tasks when the new tasks are running.
You can remove existing `serviceRegistries` by passing an empty list.
This parameter triggers a new service deployment.
Type: Array of [ServiceRegistry](API_ServiceRegistry.md) objects
Required: No

 ** [taskDefinition](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-taskDefinition"></a>
The `family` and `revision` (`family:revision`) or full ARN of the task definition to run in your service. If a `revision` is not specified, the latest `ACTIVE` revision is used. If you modify the task definition with `UpdateService`, Amazon ECS spawns a task with the new version of the task definition and then stops an old task after the new version is running.
This parameter triggers a new service deployment.
Type: String
Required: No

 ** [volumeConfigurations](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-volumeConfigurations"></a>
The details of the volume that was `configuredAtLaunch`. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in [ServiceManagedEBSVolumeConfiguration](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceManagedEBSVolumeConfiguration.html). The `name` of the volume must match the `name` from the task definition. If set to null, no new deployment is triggered. Otherwise, if this configuration differs from the existing one, it triggers a new deployment.
This parameter triggers a new service deployment.
Type: Array of [ServiceVolumeConfiguration](API_ServiceVolumeConfiguration.md) objects
Required: No

 ** [vpcLatticeConfigurations](#API_UpdateService_RequestSyntax) **   <a name="ECS-UpdateService-request-vpcLatticeConfigurations"></a>
An object representing the VPC Lattice configuration for the service being updated.
This parameter triggers a new service deployment.
Type: Array of [VpcLatticeConfiguration](API_VpcLatticeConfiguration.md) objects
Required: No

## Response Syntax
<a name="API_UpdateService_ResponseSyntax"></a>

```
{
   "service": {
      "availabilityZoneRebalancing": "string",
      "capacityProviderStrategy": [
         {
            "base": number,
            "capacityProvider": "string",
            "weight": number
         }
      ],
      "clusterArn": "string",
      "createdAt": number,
      "createdBy": "string",
      "currentServiceDeployment": "string",
      "currentServiceRevisions": [
         {
            "arn": "string",
            "pendingTaskCount": number,
            "requestedTaskCount": number,
            "runningTaskCount": number
         }
      ],
      "deploymentConfiguration": {
         "alarms": {
            "alarmNames": [ "string" ],
            "enable": boolean,
            "rollback": boolean
         },
         "bakeTimeInMinutes": number,
         "canaryConfiguration": {
            "canaryBakeTimeInMinutes": number,
            "canaryPercent": number
         },
         "deploymentCircuitBreaker": {
            "enable": boolean,
            "resetOnHealthyTask": boolean,
            "rollback": boolean,
            "thresholdConfiguration": {
               "type": "string",
               "value": number
            }
         },
         "earlySuccessCriteria": {
            "enable": boolean,
            "healthyPercent": number,
            "sourceServiceRevisionCleanup": "string"
         },
         "lifecycleHooks": [
            {
               "hookDetails": JSON value,
               "hookTargetArn": "string",
               "lifecycleStages": [ "string" ],
               "roleArn": "string",
               "targetType": "string",
               "timeoutConfiguration": {
                  "action": "string",
                  "timeoutInMinutes": number
               }
            }
         ],
         "linearConfiguration": {
            "stepBakeTimeInMinutes": number,
            "stepPercent": number
         },
         "maximumPercent": number,
         "minimumHealthyPercent": number,
         "strategy": "string"
      },
      "deploymentController": {
         "type": "string"
      },
      "deployments": [
         {
            "capacityProviderStrategy": [
               {
                  "base": number,
                  "capacityProvider": "string",
                  "weight": number
               }
            ],
            "createdAt": number,
            "desiredCount": number,
            "failedTasks": number,
            "fargateEphemeralStorage": {
               "kmsKeyId": "string"
            },
            "id": "string",
            "launchType": "string",
            "networkConfiguration": {
               "awsvpcConfiguration": {
                  "assignPublicIp": "string",
                  "securityGroups": [ "string" ],
                  "subnets": [ "string" ]
               }
            },
            "pendingCount": number,
            "platformFamily": "string",
            "platformVersion": "string",
            "rolloutState": "string",
            "rolloutStateReason": "string",
            "runningCount": number,
            "serviceConnectConfiguration": {
               "accessLogConfiguration": {
                  "format": "string",
                  "includeQueryParameters": "string"
               },
               "enabled": boolean,
               "logConfiguration": {
                  "logDriver": "string",
                  "options": {
                     "string" : "string"
                  },
                  "secretOptions": [
                     {
                        "name": "string",
                        "valueFrom": "string"
                     }
                  ]
               },
               "namespace": "string",
               "services": [
                  {
                     "clientAliases": [
                        {
                           "dnsName": "string",
                           "port": number,
                           "testTrafficRules": {
                              "header": {
                                 "name": "string",
                                 "value": {
                                    "exact": "string"
                                 }
                              }
                           }
                        }
                     ],
                     "discoveryName": "string",
                     "ingressPortOverride": number,
                     "portName": "string",
                     "timeout": {
                        "idleTimeoutSeconds": number,
                        "perRequestTimeoutSeconds": number
                     },
                     "tls": {
                        "issuerCertificateAuthority": {
                           "awsPcaAuthorityArn": "string"
                        },
                        "kmsKey": "string",
                        "roleArn": "string"
                     }
                  }
               ]
            },
            "serviceConnectResources": [
               {
                  "discoveryArn": "string",
                  "discoveryName": "string"
               }
            ],
            "status": "string",
            "taskDefinition": "string",
            "updatedAt": number,
            "volumeConfigurations": [
               {
                  "managedEBSVolume": {
                     "encrypted": boolean,
                     "filesystemType": "string",
                     "iops": number,
                     "kmsKeyId": "string",
                     "roleArn": "string",
                     "sizeInGiB": number,
                     "snapshotId": "string",
                     "tagSpecifications": [
                        {
                           "propagateTags": "string",
                           "resourceType": "string",
                           "tags": [
                              {
                                 "key": "string",
                                 "value": "string"
                              }
                           ]
                        }
                     ],
                     "throughput": number,
                     "volumeInitializationRate": number,
                     "volumeType": "string"
                  },
                  "name": "string"
               }
            ],
            "vpcLatticeConfigurations": [
               {
                  "portName": "string",
                  "roleArn": "string",
                  "targetGroupArn": "string"
               }
            ]
         }
      ],
      "desiredCount": number,
      "enableECSManagedTags": boolean,
      "enableExecuteCommand": boolean,
      "events": [
         {
            "createdAt": number,
            "id": "string",
            "message": "string"
         }
      ],
      "healthCheckGracePeriodSeconds": number,
      "launchType": "string",
      "loadBalancers": [
         {
            "advancedConfiguration": {
               "alternateTargetGroupArn": "string",
               "productionListenerRule": "string",
               "roleArn": "string",
               "testListenerRule": "string"
            },
            "containerName": "string",
            "containerPort": number,
            "loadBalancerName": "string",
            "targetGroupArn": "string"
         }
      ],
      "networkConfiguration": {
         "awsvpcConfiguration": {
            "assignPublicIp": "string",
            "securityGroups": [ "string" ],
            "subnets": [ "string" ]
         }
      },
      "pendingCount": number,
      "placementConstraints": [
         {
            "expression": "string",
            "type": "string"
         }
      ],
      "placementStrategy": [
         {
            "field": "string",
            "type": "string"
         }
      ],
      "platformFamily": "string",
      "platformVersion": "string",
      "propagateTags": "string",
      "resourceManagementType": "string",
      "roleArn": "string",
      "runningCount": number,
      "schedulingStrategy": "string",
      "serviceArn": "string",
      "serviceName": "string",
      "serviceRegistries": [
         {
            "containerName": "string",
            "containerPort": number,
            "port": number,
            "registryArn": "string"
         }
      ],
      "status": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ],
      "taskDefinition": "string",
      "taskSets": [
         {
            "capacityProviderStrategy": [
               {
                  "base": number,
                  "capacityProvider": "string",
                  "weight": number
               }
            ],
            "clusterArn": "string",
            "computedDesiredCount": number,
            "createdAt": number,
            "externalId": "string",
            "fargateEphemeralStorage": {
               "kmsKeyId": "string"
            },
            "id": "string",
            "launchType": "string",
            "loadBalancers": [
               {
                  "advancedConfiguration": {
                     "alternateTargetGroupArn": "string",
                     "productionListenerRule": "string",
                     "roleArn": "string",
                     "testListenerRule": "string"
                  },
                  "containerName": "string",
                  "containerPort": number,
                  "loadBalancerName": "string",
                  "targetGroupArn": "string"
               }
            ],
            "networkConfiguration": {
               "awsvpcConfiguration": {
                  "assignPublicIp": "string",
                  "securityGroups": [ "string" ],
                  "subnets": [ "string" ]
               }
            },
            "pendingCount": number,
            "platformFamily": "string",
            "platformVersion": "string",
            "runningCount": number,
            "scale": {
               "unit": "string",
               "value": number
            },
            "serviceArn": "string",
            "serviceRegistries": [
               {
                  "containerName": "string",
                  "containerPort": number,
                  "port": number,
                  "registryArn": "string"
               }
            ],
            "stabilityStatus": "string",
            "stabilityStatusAt": number,
            "startedBy": "string",
            "status": "string",
            "tags": [
               {
                  "key": "string",
                  "value": "string"
               }
            ],
            "taskDefinition": "string",
            "taskSetArn": "string",
            "updatedAt": number
         }
      ]
   }
}
```

## Response Elements
<a name="API_UpdateService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [service](#API_UpdateService_ResponseSyntax) **   <a name="ECS-UpdateService-response-service"></a>
The full description of your service following the update call.
The response includes a `lifecycleHookDetails` field, which is an empty array when the service is created or updated. The values are populated when a lifecycle hook executes and are available as part of the service deployment details ([DescribeServiceDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html)).
Type: [Service](API_Service.md) object

## Errors
<a name="API_UpdateService_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have authorization to perform the requested action.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClientException **
These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClusterNotFoundException **
The specified cluster wasn't found. You can view your available clusters with [ListClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html). Amazon ECS clusters are Region specific.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** NamespaceNotFoundException **
The specified namespace wasn't found.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** PlatformTaskDefinitionIncompatibilityException **
The specified platform version doesn't satisfy the required capabilities of the task definition.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** PlatformUnknownException **
The specified platform version doesn't exist.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

 ** ServiceNotActiveException **
The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with [CreateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServiceNotFoundException **
The specified service wasn't found. You can view your available services with [ListServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html). Amazon ECS services are cluster specific and Region specific.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** UnsupportedFeatureException **
The specified task isn't supported in this Region.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## Examples
<a name="API_UpdateService_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_UpdateService_Example_1"></a>

This example request updates the `hello_world` service to a desired count of 3.

#### Sample Request
<a name="API_UpdateService_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 45
X-Amz-Target: AmazonEC2ContainerServiceV20141113.UpdateService
X-Amz-Date: 20150429T194543Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "service": "hello_world",
  "desiredCount": 3
}
```

#### Sample Response
<a name="API_UpdateService_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 29 Apr 2015 19:45:43 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 13376
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "service": {
    "clusterArn": "arn:aws:ecs:us-east-1:012345678910:cluster/default",
    "deploymentConfiguration": {
        "maximumPercent": 200,
        "minimumHealthyPercent": 100
    },
    "deployments": [
      {
        "createdAt": 1430333711.033,
        "desiredCount": 3,
        "id": "ecs-svc/9223370606521064774",
        "pendingCount": 0,
        "runningCount": 0,
        "status": "PRIMARY",
        "taskDefinition": "arn:aws:ecs:us-east-1:012345678910:task-definition/hello_world:10",
        "updatedAt": 1430336267.173
      }
    ],
    "desiredCount": 3,
    "events": [],
    "loadBalancers": [],
    "pendingCount": 0,
    "runningCount": 0,
    "serviceArn": "arn:aws:ecs:us-east-1:012345678910:service/default/hello_world",
    "serviceName": "hello_world",
    "status": "ACTIVE",
    "taskDefinition": "arn:aws:ecs:us-east-1:012345678910:task-definition/hello_world:10"
  }
}
```

### Example 2
<a name="API_UpdateService_Example_2"></a>

This example updates an existing service to add a pause lifecycle hook at the POST\_PRODUCTION\_TRAFFIC\_SHIFT stage of a blue/green deployment.

#### Sample Request
<a name="API_UpdateService_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 300
X-Amz-Target: AmazonEC2ContainerServiceV20141113.UpdateService
X-Amz-Date: 20260506T160000Z
User-Agent: aws-cli/2.26 Python/3.12.6 Darwin/14.3.0
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "service": "my-service",
  "cluster": "my-cluster",
  "deploymentConfiguration": {
    "strategy": "BLUE_GREEN",
    "lifecycleHooks": [
      {
        "targetType": "PAUSE",
        "lifecycleStages": ["POST_PRODUCTION_TRAFFIC_SHIFT"],
        "timeoutConfiguration": {
          "timeoutInMinutes": 60,
          "action": "ROLLBACK"
        }
      }
    ]
  }
}
```

#### Sample Response
<a name="API_UpdateService_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Tue May 6, 2026 16:00:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 950
Connection: keep-alive
RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
  "service": {
    "serviceArn": "arn:aws:ecs:us-east-1:012345678910:service/my-cluster/my-service",
    "serviceName": "my-service",
    "clusterArn": "arn:aws:ecs:us-east-1:012345678910:cluster/my-cluster",
    "deploymentConfiguration": {
        "maximumPercent": 200,
        "minimumHealthyPercent": 100,
        "strategy": "BLUE_GREEN",
        "lifecycleHooks": [
            {
                "targetType": "PAUSE",
                "lifecycleStages": ["POST_PRODUCTION_TRAFFIC_SHIFT"],
                "timeoutConfiguration": {
                    "timeoutInMinutes": 60,
                    "action": "ROLLBACK"
                }
            }
        ]
    },
    "deployments": [
      {
        "id": "ecs-svc/9223370606521064774",
        "status": "PRIMARY",
        "taskDefinition": "arn:aws:ecs:us-east-1:012345678910:task-definition/ecs-demo:2",
        "desiredCount": 2,
        "pendingCount": 0,
        "runningCount": 2,
        "createdAt": 1746547200.000,
        "updatedAt": 1746547200.000
      }
    ],
    "desiredCount": 2,
    "events": [],
    "loadBalancers": [],
    "pendingCount": 0,
    "runningCount": 2,
    "status": "ACTIVE",
    "taskDefinition": "arn:aws:ecs:us-east-1:012345678910:task-definition/ecs-demo:2"
  }
}
```

## See Also
<a name="API_UpdateService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/UpdateService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/UpdateService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/UpdateService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/UpdateService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/UpdateService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/UpdateService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/UpdateService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/UpdateService)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/UpdateService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/UpdateService)
