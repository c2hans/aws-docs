---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html
---

# CreateService
<a name="API_CreateService"></a>

Runs and maintains your desired number of tasks from a specified task definition. If the number of tasks running in a service drops below the `desiredCount`, Amazon ECS runs another copy of the task in the specified cluster. To update an existing service, use [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html).

**Note**
On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.

**Note**
Amazon Elastic Inference (EI) is no longer available to customers.

In addition to maintaining the desired count of tasks in your service, you can optionally run your service behind one or more load balancers. The load balancers distribute traffic across the tasks that are associated with the service. For more information, see [Service load balancing](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html) in the *Amazon Elastic Container Service Developer Guide*.

You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. `volumeConfigurations` is only supported for REPLICA service and not DAEMON service. For more information, see [Amazon EBS volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types) in the *Amazon Elastic Container Service Developer Guide*.

Tasks for services that don't use a load balancer are considered healthy if they're in the `RUNNING` state. Tasks for services that use a load balancer are considered healthy if they're in the `RUNNING` state and are reported as healthy by the load balancer.

There are two service scheduler strategies available:
+  `REPLICA` - The replica scheduling strategy places and maintains your desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. For more information, see [Service scheduler concepts](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) in the *Amazon Elastic Container Service Developer Guide*.
+  `DAEMON` - The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks. It also stops tasks that don't meet the placement constraints. When using this strategy, you don't need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies. For more information, see [Amazon ECS services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) in the *Amazon Elastic Container Service Developer Guide*.

The deployment controller is the mechanism that determines how tasks are deployed for your service. The valid options are:
+ ECS

   When you create a service which uses the `ECS` deployment controller, you can choose between the following deployment strategies (which you can set in the “`strategy`” field in “`deploymentConfiguration`”): :
  +  `ROLLING`: When you create a service which uses the *rolling update* (`ROLLING`) deployment strategy, the Amazon ECS service scheduler replaces the currently running tasks with new tasks. The number of tasks that Amazon ECS adds or removes from the service during a rolling update is controlled by the service deployment configuration. For more information, see [Deploy Amazon ECS services by replacing tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html) in the *Amazon Elastic Container Service Developer Guide*.

    Rolling update deployments are best suited for the following scenarios:
    + Gradual service updates: You need to update your service incrementally without taking the entire service offline at once.
    + Limited resource requirements: You want to avoid the additional resource costs of running two complete environments simultaneously (as required by blue/green deployments).
    + Acceptable deployment time: Your application can tolerate a longer deployment process, as rolling updates replace tasks one by one.
    + No need for instant roll back: Your service can tolerate a rollback process that takes minutes rather than seconds.
    + Simple deployment process: You prefer a straightforward deployment approach without the complexity of managing multiple environments, target groups, and listeners.
    + No load balancer requirement: Your service doesn't use or require a load balancer, Application Load Balancer, Network Load Balancer, or Service Connect (which are required for blue/green deployments).
    + Stateful applications: Your application maintains state that makes it difficult to run two parallel environments.
    + Cost sensitivity: You want to minimize deployment costs by not running duplicate environments during deployment.

    Rolling updates are the default deployment strategy for services and provide a balance between deployment safety and resource efficiency for many common application scenarios.
  +  `BLUE_GREEN`: A *blue/green* deployment strategy (`BLUE_GREEN`) is a release methodology that reduces downtime and risk by running two identical production environments called blue and green. With Amazon ECS blue/green deployments, you can validate new service revisions before directing production traffic to them. This approach provides a safer way to deploy changes with the ability to quickly roll back if needed. For more information, see [Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html) in the *Amazon Elastic Container Service Developer Guide*.

    Amazon ECS blue/green deployments are best suited for the following scenarios:
    + Service validation: When you need to validate new service revisions before directing production traffic to them
    + Zero downtime: When your service requires zero-downtime deployments
    + Instant roll back: When you need the ability to quickly roll back if issues are detected
    + Load balancer requirement: When your service uses Application Load Balancer, Network Load Balancer, or Service Connect
  +  `LINEAR`: A *linear* deployment strategy (`LINEAR`) gradually shifts traffic from the current production environment to a new environment in equal percentage increments. With Amazon ECS linear deployments, you can control the pace of traffic shifting and validate new service revisions with increasing amounts of production traffic.

    Linear deployments are best suited for the following scenarios:
    + Gradual validation: When you want to gradually validate your new service version with increasing traffic
    + Performance monitoring: When you need time to monitor metrics and performance during the deployment
    + Risk minimization: When you want to minimize risk by exposing the new version to production traffic incrementally
    + Load balancer requirement: When your service uses Application Load Balancer or Service Connect
  +  `CANARY`: A *canary* deployment strategy (`CANARY`) shifts a small percentage of traffic to the new service revision first, then shifts the remaining traffic all at once after a specified time period. This allows you to test the new version with a subset of users before full deployment.

    Canary deployments are best suited for the following scenarios:
    + Feature testing: When you want to test new features with a small subset of users before full rollout
    + Production validation: When you need to validate performance and functionality with real production traffic
    + Blast radius control: When you want to minimize blast radius if issues are discovered in the new version
    + Load balancer requirement: When your service uses Application Load Balancer or Service Connect
+ External

  Use a third-party deployment controller.
+ Blue/green deployment (powered by AWS CodeDeploy)

   AWS CodeDeploy installs an updated version of the application as a new replacement task set and reroutes production traffic from the original application task set to the replacement task set. The original task set is terminated after a successful deployment. Use this deployment controller to verify a new deployment of a service before sending production traffic to it.

When creating a service that uses the `EXTERNAL` deployment controller, you can specify only parameters that aren't controlled at the task set level. The only required parameter is the service name. You control your services using the [CreateTaskSet](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html). For more information, see [Amazon ECS deployment types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html) in the *Amazon Elastic Container Service Developer Guide*.

When the service scheduler launches new tasks, it determines task placement. For information about task placement and task placement strategies, see [Amazon ECS task placement](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement.html) in the *Amazon Elastic Container Service Developer Guide*

## Request Syntax
<a name="API_CreateService_RequestSyntax"></a>

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
   "clientToken": "{{string}}",
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
   "healthCheckGracePeriodSeconds": {{number}},
   "launchType": "{{string}}",
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
   "role": "{{string}}",
   "schedulingStrategy": "{{string}}",
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
   "serviceName": "{{string}}",
   "serviceRegistries": [
      {
         "containerName": "{{string}}",
         "containerPort": {{number}},
         "port": {{number}},
         "registryArn": "{{string}}"
      }
   ],
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
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
<a name="API_CreateService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [availabilityZoneRebalancing](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-availabilityZoneRebalancing"></a>
Indicates whether to use Availability Zone rebalancing for the service.
For more information, see [Balancing an Amazon ECS service across Availability Zones](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html) in the * *Amazon Elastic Container Service Developer Guide* *.
The default behavior of `AvailabilityZoneRebalancing` differs between create and update requests:
+ For create service requests, when no value is specified for `AvailabilityZoneRebalancing`, Amazon ECS defaults the value to `ENABLED`.
+ For update service requests, when no value is specified for `AvailabilityZoneRebalancing`, Amazon ECS defaults to the existing service’s `AvailabilityZoneRebalancing` value. If the service never had an `AvailabilityZoneRebalancing` value set, Amazon ECS treats this as `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [capacityProviderStrategy](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-capacityProviderStrategy"></a>
The capacity provider strategy to use for the service.
If you want to use Amazon ECS Managed Instances, you must use the `capacityProviderStrategy` request parameter and omit the `launchType` request parameter.
If a `capacityProviderStrategy` is specified, the `launchType` parameter must be omitted. If no `capacityProviderStrategy` or `launchType` is specified, the `defaultCapacityProviderStrategy` for the cluster is used.
A capacity provider strategy can contain a maximum of 20 capacity providers.
Type: Array of [CapacityProviderStrategyItem](API_CapacityProviderStrategyItem.md) objects
Required: No

 ** [clientToken](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-clientToken"></a>
An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed.
Type: String
Required: No

 ** [cluster](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster that you run your service on. If you do not specify a cluster, the default cluster is assumed.
Type: String
Required: No

 ** [deploymentConfiguration](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-deploymentConfiguration"></a>
Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.
Type: [DeploymentConfiguration](API_DeploymentConfiguration.md) object
Required: No

 ** [deploymentController](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-deploymentController"></a>
The deployment controller to use for the service. If no deployment controller is specified, the default value of `ECS` is used.
Type: [DeploymentController](API_DeploymentController.md) object
Required: No

 ** [desiredCount](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-desiredCount"></a>
The number of instantiations of the specified task definition to place and keep running in your service.
This is required if `schedulingStrategy` is `REPLICA` or isn't specified. If `schedulingStrategy` is `DAEMON` then this isn't required.
Type: Integer
Required: No

 ** [enableECSManagedTags](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-enableECSManagedTags"></a>
Specifies whether to turn on Amazon ECS managed tags for the tasks within the service. For more information, see [Tagging your Amazon ECS resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon Elastic Container Service Developer Guide*.
When you use Amazon ECS managed tags, you must set the `propagateTags` request parameter.
Type: Boolean
Required: No

 ** [enableExecuteCommand](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-enableExecuteCommand"></a>
Determines whether the execute command functionality is turned on for the service. If `true`, this enables execute command functionality on all containers in the service tasks.
Type: Boolean
Required: No

 ** [healthCheckGracePeriodSeconds](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-healthCheckGracePeriodSeconds"></a>
The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you do not specify a health check grace period value, the default value of 0 is used. If you do not use any of the health checks, then `healthCheckGracePeriodSeconds` is unused.
If your service has more running tasks than desired, unhealthy tasks in the grace period might be stopped to reach the desired count.
Type: Integer
Required: No

 ** [launchType](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-launchType"></a>
The infrastructure that you run your service on. For more information, see [Amazon ECS launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide*.
If you want to use Amazon ECS Managed Instances, you must use the `capacityProviderStrategy` request parameter and omit the `launchType` request parameter.
The `FARGATE` launch type runs your tasks on AWS Fargate On-Demand infrastructure.
Fargate Spot infrastructure is available for use but a capacity provider strategy must be used. For more information, see [AWS Fargate capacity providers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html) in the *Amazon ECS Developer Guide*.
The `EC2` launch type runs your tasks on Amazon EC2 instances registered to your cluster.
The `EXTERNAL` launch type runs your tasks on your on-premises server or virtual machine (VM) capacity registered to your cluster.
A service can use either a launch type or a capacity provider strategy. If a `launchType` is specified, the `capacityProviderStrategy` parameter must be omitted.
Type: String
Valid Values: `EC2 | FARGATE | EXTERNAL | MANAGED_INSTANCES`
Required: No

 ** [loadBalancers](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-loadBalancers"></a>
A load balancer object representing the load balancers to use with your service. For more information, see [Service load balancing](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html) in the *Amazon Elastic Container Service Developer Guide*.
If the service uses the `ECS` deployment controller and using either an Application Load Balancer or Network Load Balancer, you must specify one or more target group ARNs to attach to the service. The service-linked role is required for services that use multiple target groups. For more information, see [Using service-linked roles for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html) in the *Amazon Elastic Container Service Developer Guide*.
If the service uses the `CODE_DEPLOY` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a `targetGroupPair`). During a deployment, AWS CodeDeploy determines which task set in your service has the status `PRIMARY`, and it associates one target group with it. Then, it also associates the other target group with the replacement task set. The load balancer can also have up to two listeners: a required listener for production traffic and an optional listener that you can use to perform validation tests with Lambda functions before routing production traffic to it.
If you use the `CODE_DEPLOY` deployment controller, these values can be changed when updating the service.
For Application Load Balancers and Network Load Balancers, this object must contain the load balancer target group ARN, the container name, and the container port to access from the load balancer. The container name must be as it appears in a container definition. The load balancer name parameter must be omitted. When a task from this service is placed on a container instance, the container instance and port combination is registered as a target in the target group that's specified here.
For Classic Load Balancers, this object must contain the load balancer name, the container name , and the container port to access from the load balancer. The container name must be as it appears in a container definition. The target group ARN parameter must be omitted. When a task from this service is placed on a container instance, the container instance is registered with the load balancer that's specified here.
Services with tasks that use the `awsvpc` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers aren't supported. Also, when you create any target groups for these services, you must choose `ip` as the target type, not `instance`. This is because tasks that use the `awsvpc` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
Type: Array of [LoadBalancer](API_LoadBalancer.md) objects
Required: No

 ** [monitoring](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-monitoring"></a>
The optional monitoring configuration for the service, which defines the resolution for the service-level `CPUUtilization` and `MemoryUtilization` Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of `60` seconds.
Type: [MonitoringConfiguration](API_MonitoringConfiguration.md) object
Required: No

 ** [networkConfiguration](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-networkConfiguration"></a>
The network configuration for the service. This parameter is required for task definitions that use the `awsvpc` network mode to receive their own elastic network interface, and it isn't supported for other network modes. For more information, see [Task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** [placementConstraints](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-placementConstraints"></a>
An array of placement constraint objects to use for tasks in your service. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.
Type: Array of [PlacementConstraint](API_PlacementConstraint.md) objects
Required: No

 ** [placementStrategy](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-placementStrategy"></a>
The placement strategy objects to use for tasks in your service. You can specify a maximum of 5 strategy rules for each service.
Type: Array of [PlacementStrategy](API_PlacementStrategy.md) objects
Required: No

 ** [platformVersion](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-platformVersion"></a>
The platform version that your tasks in the service are running on. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the `LATEST` platform version is used. For more information, see [AWS Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** [propagateTags](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-propagateTags"></a>
Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the [TagResource](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html) API action.
You must set this to a value other than `NONE` when you use Cost Explorer. For more information, see [Amazon ECS usage reports](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/usage-reports.html) in the *Amazon Elastic Container Service Developer Guide*.
The default is `NONE`.
Type: String
Valid Values: `TASK_DEFINITION | SERVICE | NONE`
Required: No

 ** [role](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-role"></a>
The name or full Amazon Resource Name (ARN) of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is only permitted if you are using a load balancer with your service and your task definition doesn't use the `awsvpc` network mode. If you specify the `role` parameter, you must also specify a load balancer object with the `loadBalancers` parameter.
If your account has already created the Amazon ECS service-linked role, that role is used for your service unless you specify a role here. The service-linked role is required if your task definition uses the `awsvpc` network mode or if the service is configured to use service discovery, an external deployment controller, multiple target groups, or Elastic Inference accelerators in which case you don't specify a role here. For more information, see [Using service-linked roles for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html) in the *Amazon Elastic Container Service Developer Guide*.
If your specified role has a path other than `/`, then you must either specify the full role ARN (this is recommended) or prefix the role name with the path. For example, if a role with the name `bar` has a path of `/foo/` then you would specify `/foo/bar` as the role name. For more information, see [Friendly names and paths](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names) in the *IAM User Guide*.
Type: String
Required: No

 ** [schedulingStrategy](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-schedulingStrategy"></a>
The scheduling strategy to use for the service. For more information, see [Services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html).
There are two service scheduler strategies available:
+  `REPLICA`-The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. This scheduler strategy is required if the service uses the `CODE_DEPLOY` or `EXTERNAL` deployment controller types.
+  `DAEMON`-The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks and will stop tasks that don't meet the placement constraints. When you're using this strategy, you don't need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies.
**Note**
Tasks using the Fargate launch type or the `CODE_DEPLOY` or `EXTERNAL` deployment controller types don't support the `DAEMON` scheduling strategy.
Type: String
Valid Values: `REPLICA | DAEMON`
Required: No

 ** [serviceConnectConfiguration](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-serviceConnectConfiguration"></a>
The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.
Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: [ServiceConnectConfiguration](API_ServiceConnectConfiguration.md) object
Required: No

 ** [serviceName](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-serviceName"></a>
The name of your service. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.
Type: String
Required: Yes

 ** [serviceRegistries](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-serviceRegistries"></a>
The details of the service discovery registry to associate with this service. For more information, see [Service discovery](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html).
Each service may be associated with one service registry. Multiple service registries for each service isn't supported.
Type: Array of [ServiceRegistry](API_ServiceRegistry.md) objects
Required: No

 ** [tags](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-tags"></a>
The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. When a service is deleted, the tags are deleted as well.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8
+ Maximum value length - 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [taskDefinition](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-taskDefinition"></a>
The `family` and `revision` (`family:revision`) or full ARN of the task definition to run in your service. If a `revision` isn't specified, the latest `ACTIVE` revision is used.
A task definition must be specified if the service uses either the `ECS` or `CODE_DEPLOY` deployment controllers.
For more information about deployment types, see [Amazon ECS deployment types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html).
Type: String
Required: No

 ** [volumeConfigurations](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-volumeConfigurations"></a>
The configuration for a volume specified in the task definition as a volume that is configured at launch time. Currently, the only supported volume type is an Amazon EBS volume.
Type: Array of [ServiceVolumeConfiguration](API_ServiceVolumeConfiguration.md) objects
Required: No

 ** [vpcLatticeConfigurations](#API_CreateService_RequestSyntax) **   <a name="ECS-CreateService-request-vpcLatticeConfigurations"></a>
The VPC Lattice configuration for the service being created.
Type: Array of [VpcLatticeConfiguration](API_VpcLatticeConfiguration.md) objects
Required: No

## Response Syntax
<a name="API_CreateService_ResponseSyntax"></a>

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
<a name="API_CreateService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [service](#API_CreateService_ResponseSyntax) **   <a name="ECS-CreateService-response-service"></a>
The full description of your service following the create call.
A service will return either a `capacityProviderStrategy` or `launchType` parameter, but not both, depending where one was specified when it was created.
If a service is using the `ECS` deployment controller, the `deploymentController` and `taskSets` parameters will not be returned.
if the service uses the `CODE_DEPLOY` deployment controller, the `deploymentController`, `taskSets` and `deployments` parameters will be returned, however the `deployments` parameter will be an empty list.
The response includes a `lifecycleHookDetails` field, which is an empty array when the service is created or updated. The values are populated when a lifecycle hook executes and are available as part of the service deployment details ([DescribeServiceDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html)).
Type: [Service](API_Service.md) object

## Errors
<a name="API_CreateService_Errors"></a>

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

 ** UnsupportedFeatureException **
The specified task isn't supported in this Region.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## Examples
<a name="API_CreateService_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example 1
<a name="API_CreateService_Example_1"></a>

This example API request creates a service in your default Region called `ecs-simple-service`. The service uses the `ecs-demo` task definition and it maintains 10 instantiations of that task. It uses both the `FARGATE` and `FARGATE_SPOT` capacity providers.

#### Sample Request
<a name="API_CreateService_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 87
X-Amz-Target: AmazonEC2ContainerServiceV20141113.CreateService
X-Amz-Date: 20150429T170125Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "serviceName": "ecs-simple-service",
  "taskDefinition": "ecs-demo",
  "desiredCount": 10,
   "capacityProviderStrategy": [
      {
         "base": number,
         "capacityProvider": "FARGATE_SPOT",
         "weight": 1
      }
   ]
}
```

#### Sample Response
<a name="API_CreateService_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 29 Apr 2015 17:01:27 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 636
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
        "createdAt": 1430326887.362,
        "desiredCount": 10,
        "id": "ecs-svc/9223370606527888445",
        "pendingCount": 0,
        "runningCount": 0,
        "status": "PRIMARY",
        "taskDefinition": "arn:aws:ecs:us-east-1:012345678910:task-definition/ecs-demo:1",
        "updatedAt": 1430326887.362
      }
    ],
    "capacityProviderStrategy": [
      {
        "capacityProvider": "FARGATE",
        "weight": 1,
        "base": 0
      },
      {
        "capacityProvider": "FARGATE_SPOT",
        "weight": 1,
        "base": 0
      }
    ],
    "desiredCount": 10,
    "events": [],
    "loadBalancers": [],
    "pendingCount": 0,
    "runningCount": 0,
    "serviceArn": "arn:aws:ecs:us-east-1:012345678910:service/default/ecs-simple-service",
    "serviceName": "ecs-simple-service",
    "status": "ACTIVE",
    "taskDefinition": "arn:aws:ecs:us-east-1:012345678910:task-definition/ecs-demo:1"
  }
}
```

### Example 2
<a name="API_CreateService_Example_2"></a>

This example API request creates a service with multiple load balancer target groups.

#### Sample Request
<a name="API_CreateService_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonEC2ContainerServiceV20141113.CreateService
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.16.190 Python/3.6.1 Darwin/16.7.0 botocore/1.12.180
X-Amz-Date: 20190723T001203Z
Authorization: AUTHPARAMS
Content-Length: 453

{
   "serviceName":"ecs-multiplealb-service",
   "taskDefinition":"ecs-multiplealb-demo",
   "loadBalancers":[
      {
         "targetGroupArn":"arn:aws:elasticloadbalancing:us-east-1:012345678910:targetgroup/tg1/18ce32cc074018ed",
         "containerName":"simple-app",
         "containerPort":80
      },
      {
         "targetGroupArn":"arn:aws:elasticloadbalancing:us-east-1:012345678910:targetgroup/tg2/737bead11d516e2a",
         "containerName":"simple-app",
         "containerPort":8080
      }
   ],
   "desiredCount":10
}
```

#### Sample Response
<a name="API_CreateService_Example_2_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f
Content-Type: application/x-amz-json-1.1
Content-Length: 1440
Date: Tue, 23 Jul 2019 00:12:03 GMT
Connection: keep-alive

{
    "service": {
        "serviceArn": "arn:aws:ecs:us-east-1:012345678910:service/default/ecs-multiplealb-service",
        "serviceName": "ecs-multiplealb-service",
        "clusterArn": "arn:aws:ecs:us-east-1:012345678910:cluster/default",
        "loadBalancers": [
            {
                "targetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:012345678910:targetgroup/tg1/18ce32cc074018ed",
                "containerName": "simple-app",
                "containerPort": 80
            },
            {
                "targetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:012345678910:targetgroup/tg2/737bead11d516e2a",
                "containerName": "simple-app",
                "containerPort": 8080
            }
        ],
        "serviceRegistries": [],
        "status": "ACTIVE",
        "desiredCount": 10,
        "runningCount": 0,
        "pendingCount": 0,
        "launchType": "EC2",
        "taskDefinition": "arn:aws:ecs:us-east-1:012345678910:task-definition/ecs-multiplealb-demo",
        "deploymentConfiguration": {
            "maximumPercent": 200,
            "minimumHealthyPercent": 100
        },
        "deployments": [
            {
                "id": "ecs-svc/9223370473014051517",
                "status": "PRIMARY",
                "taskDefinition": "arn:aws:ecs:us-east-1:012345678910:task-definition/ecs-multiplealb-demo",
                "desiredCount": 10,
                "pendingCount": 0,
                "runningCount": 0,
                "createdAt": 1563840724.29,
                "updatedAt": 1563840724.29,
                "launchType": "EC2"
            }
        ],
        "roleArn": "arn:aws:iam::012345678910:role/aws-service-role/ecs.amazonaws.com/AWSServiceRoleForECS",
        "events": [],
        "createdAt": 1563840724.29,
        "placementConstraints": [],
        "placementStrategy": [],
        "healthCheckGracePeriodSeconds": 0,
        "schedulingStrategy": "REPLICA",
        "enableECSManagedTags": false,
        "propagateTags": "NONE"
    }
}
```

### Example 3
<a name="API_CreateService_Example_3"></a>

This example API request creates a service with a strategy that distributes tasks evenly across Availability Zones and then bin packs tasks based on memory within each Availability Zone.

#### Sample Request
<a name="API_CreateService_Example_3_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonEC2ContainerServiceV20141113.CreateService
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.16.190 Python/3.6.1 Darwin/16.7.0 botocore/1.12.180
X-Amz-Date: 20190723T001203Z
Authorization: AUTHPARAMS
Content-Length: 453

{
   "serviceName":"example-placement1",
   "taskDefinition":"windows-simple-iis",
   "placementStrategy": [
        {
            "field": "attribute:ecs.availability-zone",
            "type": "spread"
        },
        {
            "field": "memory",
            "type": "binpack"
        }
   ]
   "desiredCount":3
}
```

#### Sample Response
<a name="API_CreateService_Example_3_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f
Content-Type: application/x-amz-json-1.1
Content-Length: 1440
Date: Tue, 23 Jul 2019 00:12:03 GMT
Connection: keep-alive

{
    "service": {
        "serviceArn": "arn:aws:ecs:us-east-1:123456789012:service/windows-ec2/default/example-placement1",
        "serviceName": "example-placement1",
        "clusterArn": "arn:aws:ecs:us-east-1:123456789012:cluster/windows-ec2",
        "loadBalancers": [],
        "serviceRegistries": [],
        "status": "ACTIVE",
        "desiredCount": 3,
        "runningCount": 0,
        "pendingCount": 0,
        "launchType": "EC2",
        "taskDefinition": "arn:aws:ecs:us-east-1:123456789012:task-definition/windows-simple-iis:2",
        "deploymentConfiguration": {
            "deploymentCircuitBreaker": {
                "enable": false,
                "rollback": false
            },
            "maximumPercent": 200,
            "minimumHealthyPercent": 100
        },
        "deployments": [
            {
                "id": "ecs-svc/409552086333EXAMPLE",
                "status": "PRIMARY",
                "taskDefinition": "arn:aws:ecs:us-east-1:123456789012:task-definition/windows-simple-iis:2",
                "desiredCount": 3,
                "pendingCount": 0,
                "runningCount": 0,
                "failedTasks": 0,
                "createdAt": "2022-07-21T15:06:08.787000-04:00",
                "updatedAt": "2022-07-21T15:06:08.787000-04:00",
                "launchType": "EC2",
                "rolloutState": "IN_PROGRESS",
                "rolloutStateReason": "ECS deployment ecs-svc/409552086333EXAMPLE in progress."
            }
        ],
        "events": [],
        "createdAt": "2022-07-21T15:06:08.787000-04:00",
        "placementConstraints": [],
        "placementStrategy": [
            {
                "type": "spread",
                "field": "attribute:ecs.availability-zone"
            },
            {
                "type": "binpack",
                "field": "MEMORY"
            }
        ],
        "schedulingStrategy": "REPLICA",
        "createdBy": "arn:aws:iam::123456789012:user/johndoe",
        "enableECSManagedTags": false,
        "propagateTags": "NONE",
        "enableExecuteCommand": false
    }
}
```

### Example 4
<a name="API_CreateService_Example_4"></a>

This example creates a service with a blue/green deployment strategy that includes a pause lifecycle hook at the POST\_PRODUCTION\_TRAFFIC\_SHIFT stage. The deployment pauses at that stage until you explicitly continue or roll back using the ContinueServiceDeployment API, or until the 60-minute timeout expires and triggers a rollback.

#### Sample Request
<a name="API_CreateService_Example_4_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 350
X-Amz-Target: AmazonEC2ContainerServiceV20141113.CreateService
X-Amz-Date: 20260506T160000Z
User-Agent: aws-cli/2.26 Python/3.12.6 Darwin/14.3.0
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "serviceName": "ecs-service-with-pause-hook",
  "taskDefinition": "ecs-demo",
  "desiredCount": 2,
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
<a name="API_CreateService_Example_4_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Tue May 6, 2026 16:00:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 822
Connection: keep-alive
RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
    "service": {
        "serviceArn": "arn:aws:ecs:us-east-1:012345678910:service/default/ecs-service-with-pause-hook",
        "serviceName": "ecs-service-with-pause-hook",
        "clusterArn": "arn:aws:ecs:us-east-1:012345678910:cluster/default",
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
            "id": "ecs-svc/9223370606527888445",
            "status": "PRIMARY",
            "taskDefinition": "arn:aws:ecs:us-east-1:012345678910:task-definition/ecs-demo:1",
            "desiredCount": 2,
            "pendingCount": 0,
            "runningCount": 0,
            "createdAt": 1746547200.000,
            "updatedAt": 1746547200.000
          }
        ],
        "desiredCount": 2,
        "events": [],
        "loadBalancers": [],
        "pendingCount": 0,
        "runningCount": 0,
        "status": "ACTIVE",
        "taskDefinition": "arn:aws:ecs:us-east-1:012345678910:task-definition/ecs-demo:1"
    }
}
```

## See Also
<a name="API_CreateService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/CreateService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/CreateService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/CreateService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/CreateService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/CreateService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/CreateService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/CreateService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/CreateService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/CreateService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/CreateService)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
