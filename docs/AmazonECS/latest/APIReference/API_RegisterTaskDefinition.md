---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RegisterTaskDefinition.html
---

# RegisterTaskDefinition
<a name="API_RegisterTaskDefinition"></a>

Registers a new task definition from the supplied `family` and `containerDefinitions`. Optionally, you can add data volumes to your containers with the `volumes` parameter. For more information about task definition parameters and defaults, see [Amazon ECS Task Definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html) in the *Amazon Elastic Container Service Developer Guide*.

You can specify a role for your task with the `taskRoleArn` parameter. When you specify a role for a task, its containers can then use the latest versions of the AWS CLI or SDKs to make API requests to the AWS services that are specified in the policy that's associated with the role. For more information, see [IAM Roles for Tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.

You can specify a Docker networking mode for the containers in your task definition with the `networkMode` parameter. If you specify the `awsvpc` network mode, the task is allocated an elastic network interface, and you must specify a [NetworkConfiguration](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkConfiguration.html) when you create a service or run a task with the task definition. For more information, see [Task Networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide*.

## Request Syntax
<a name="API_RegisterTaskDefinition_RequestSyntax"></a>

```
{
   "containerDefinitions": [
      {
         "command": [ "{{string}}" ],
         "cpu": {{number}},
         "credentialSpecs": [ "{{string}}" ],
         "dependsOn": [
            {
               "condition": "{{string}}",
               "containerName": "{{string}}"
            }
         ],
         "disableNetworking": {{boolean}},
         "dnsSearchDomains": [ "{{string}}" ],
         "dnsServers": [ "{{string}}" ],
         "dockerLabels": {
            "{{string}}" : "{{string}}"
         },
         "dockerSecurityOptions": [ "{{string}}" ],
         "entryPoint": [ "{{string}}" ],
         "environment": [
            {
               "name": "{{string}}",
               "value": "{{string}}"
            }
         ],
         "environmentFiles": [
            {
               "type": "{{string}}",
               "value": "{{string}}"
            }
         ],
         "essential": {{boolean}},
         "extraHosts": [
            {
               "hostname": "{{string}}",
               "ipAddress": "{{string}}"
            }
         ],
         "firelensConfiguration": {
            "options": {
               "{{string}}" : "{{string}}"
            },
            "type": "{{string}}"
         },
         "healthCheck": {
            "command": [ "{{string}}" ],
            "interval": {{number}},
            "retries": {{number}},
            "startPeriod": {{number}},
            "timeout": {{number}}
         },
         "hostname": "{{string}}",
         "image": "{{string}}",
         "interactive": {{boolean}},
         "links": [ "{{string}}" ],
         "linuxParameters": {
            "capabilities": {
               "add": [ "{{string}}" ],
               "drop": [ "{{string}}" ]
            },
            "devices": [
               {
                  "containerPath": "{{string}}",
                  "hostPath": "{{string}}",
                  "permissions": [ "{{string}}" ]
               }
            ],
            "initProcessEnabled": {{boolean}},
            "maxSwap": {{number}},
            "sharedMemorySize": {{number}},
            "swappiness": {{number}},
            "tmpfs": [
               {
                  "containerPath": "{{string}}",
                  "mountOptions": [ "{{string}}" ],
                  "size": {{number}}
               }
            ]
         },
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
         "memory": {{number}},
         "memoryReservation": {{number}},
         "mountPoints": [
            {
               "containerPath": "{{string}}",
               "readOnly": {{boolean}},
               "sourceVolume": "{{string}}"
            }
         ],
         "name": "{{string}}",
         "portMappings": [
            {
               "appProtocol": "{{string}}",
               "containerPort": {{number}},
               "containerPortRange": "{{string}}",
               "hostPort": {{number}},
               "name": "{{string}}",
               "protocol": "{{string}}"
            }
         ],
         "privileged": {{boolean}},
         "pseudoTerminal": {{boolean}},
         "readonlyRootFilesystem": {{boolean}},
         "repositoryCredentials": {
            "credentialsParameter": "{{string}}"
         },
         "resourceRequirements": [
            {
               "type": "{{string}}",
               "value": "{{string}}"
            }
         ],
         "restartPolicy": {
            "enabled": {{boolean}},
            "ignoredExitCodes": [ {{number}} ],
            "restartAttemptPeriod": {{number}}
         },
         "secrets": [
            {
               "name": "{{string}}",
               "valueFrom": "{{string}}"
            }
         ],
         "startTimeout": {{number}},
         "stopTimeout": {{number}},
         "systemControls": [
            {
               "namespace": "{{string}}",
               "value": "{{string}}"
            }
         ],
         "ulimits": [
            {
               "hardLimit": {{number}},
               "name": "{{string}}",
               "softLimit": {{number}}
            }
         ],
         "user": "{{string}}",
         "versionConsistency": "{{string}}",
         "volumesFrom": [
            {
               "readOnly": {{boolean}},
               "sourceContainer": "{{string}}"
            }
         ],
         "workingDirectory": "{{string}}"
      }
   ],
   "cpu": "{{string}}",
   "enableFaultInjection": {{boolean}},
   "ephemeralStorage": {
      "sizeInGiB": {{number}}
   },
   "executionRoleArn": "{{string}}",
   "family": "{{string}}",
   "inferenceAccelerators": [
      {
         "deviceName": "{{string}}",
         "deviceType": "{{string}}"
      }
   ],
   "ipcMode": "{{string}}",
   "memory": "{{string}}",
   "networkMode": "{{string}}",
   "pidMode": "{{string}}",
   "placementConstraints": [
      {
         "expression": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "proxyConfiguration": {
      "containerName": "{{string}}",
      "properties": [
         {
            "name": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "type": "{{string}}"
   },
   "requiresCompatibilities": [ "{{string}}" ],
   "runtimePlatform": {
      "cpuArchitecture": "{{string}}",
      "operatingSystemFamily": "{{string}}"
   },
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "taskRoleArn": "{{string}}",
   "volumes": [
      {
         "configuredAtLaunch": {{boolean}},
         "dockerVolumeConfiguration": {
            "autoprovision": {{boolean}},
            "driver": "{{string}}",
            "driverOpts": {
               "{{string}}" : "{{string}}"
            },
            "labels": {
               "{{string}}" : "{{string}}"
            },
            "scope": "{{string}}"
         },
         "efsVolumeConfiguration": {
            "authorizationConfig": {
               "accessPointId": "{{string}}",
               "iam": "{{string}}"
            },
            "fileSystemId": "{{string}}",
            "rootDirectory": "{{string}}",
            "transitEncryption": "{{string}}",
            "transitEncryptionPort": {{number}}
         },
         "fsxWindowsFileServerVolumeConfiguration": {
            "authorizationConfig": {
               "credentialsParameter": "{{string}}",
               "domain": "{{string}}"
            },
            "fileSystemId": "{{string}}",
            "rootDirectory": "{{string}}"
         },
         "host": {
            "sourcePath": "{{string}}"
         },
         "name": "{{string}}",
         "s3filesVolumeConfiguration": {
            "accessPointArn": "{{string}}",
            "fileSystemArn": "{{string}}",
            "rootDirectory": "{{string}}",
            "transitEncryptionPort": {{number}}
         }
      }
   ]
}
```

## Request Parameters
<a name="API_RegisterTaskDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [containerDefinitions](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-containerDefinitions"></a>
A list of container definitions in JSON format that describe the different containers that make up your task.
Type: Array of [ContainerDefinition](API_ContainerDefinition.md) objects
Required: Yes

 ** [cpu](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-cpu"></a>
The number of CPU units used by the task. It can be expressed as an integer using CPU units (for example, `1024`) or as a string using vCPUs (for example, `1 vCPU` or `1 vcpu`) in a task definition. String values are converted to an integer indicating the CPU units when the task definition is registered.
Task-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.
If you're using the EC2 launch type or external launch type, this field is optional. Supported values are between `128` CPU units (`0.125` vCPUs) and `196608` CPU units (`192` vCPUs). If you do not specify a value, the parameter is ignored.
This field is required for Fargate. For information about the valid values, see [Task size](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_size) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** [enableFaultInjection](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-enableFaultInjection"></a>
Enables fault injection when you register your task definition and allows for fault injection requests to be accepted from the task's containers. The default value is `false`.
Type: Boolean
Required: No

 ** [ephemeralStorage](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-ephemeralStorage"></a>
The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on AWS Fargate. For more information, see [Using data volumes in tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html) in the *Amazon ECS Developer Guide*.
For tasks using the Fargate launch type, the task requires the following platforms:
+ Linux platform version `1.4.0` or later.
+ Windows platform version `1.0.0` or later.
Type: [EphemeralStorage](API_EphemeralStorage.md) object
Required: No

 ** [executionRoleArn](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make AWS API calls on your behalf. For informationabout the required IAM roles for Amazon ECS, see [IAM roles for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-ecs-iam-role-overview.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** [family](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-family"></a>
You must specify a `family` for a task definition. You can use it track multiple versions of the same task definition. The `family` is used as a name for your task definition. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.
Type: String
Required: Yes

 ** [inferenceAccelerators](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-inferenceAccelerators"></a>
 *This parameter has been deprecated.*
The Elastic Inference accelerators to use for the containers in the task.
Type: Array of [InferenceAccelerator](API_InferenceAccelerator.md) objects
Required: No

 ** [ipcMode](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-ipcMode"></a>
The IPC resource namespace to use for the containers in the task. The valid values are `host`, `task`, or `none`. If `host` is specified, then all containers within the tasks that specified the `host` IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If `task` is specified, all containers within the specified task share the same IPC resources. If `none` is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance.
If the `host` IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose.
If you are setting namespaced kernel parameters using `systemControls` for the containers in the task, the following will apply to your IPC resource namespace. For more information, see [System Controls](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) in the *Amazon Elastic Container Service Developer Guide*.
+ For tasks that use the `host` IPC mode, IPC namespace related `systemControls` are not supported.
+ For tasks that use the `task` IPC mode, IPC namespace related `systemControls` will apply to all containers within a task.
This parameter is not supported for Windows containers or tasks run on AWS Fargate.
Type: String
Valid Values: `host | task | none`
Required: No

 ** [memory](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-memory"></a>
The amount of memory (in MiB) used by the task. It can be expressed as an integer using MiB (for example ,`1024`) or as a string using GB (for example, `1GB` or `1 GB`) in a task definition. String values are converted to an integer indicating the MiB when the task definition is registered.
Task-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.
If using the EC2 launch type, this field is optional.
If using the Fargate launch type, this field is required and you must use one of the following values. This determines your range of supported values for the `cpu` parameter.
The CPU units cannot be less than 1 vCPU when you use Windows containers on Fargate.
+ 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available `cpu` values: 256 (.25 vCPU)
+ 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available `cpu` values: 512 (.5 vCPU)
+ 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available `cpu` values: 1024 (1 vCPU)
+ Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available `cpu` values: 2048 (2 vCPU)
+ Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available `cpu` values: 4096 (4 vCPU)
+ Between 16 GB and 60 GB in 4 GB increments - Available `cpu` values: 8192 (8 vCPU)

  This option requires Linux platform `1.4.0` or later.
+ Between 32GB and 120 GB in 8 GB increments - Available `cpu` values: 16384 (16 vCPU)

  This option requires Linux platform `1.4.0` or later.
Type: String
Required: No

 ** [networkMode](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-networkMode"></a>
The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`. If no network mode is specified, the default is `bridge`.
For Amazon ECS tasks on Fargate, the `awsvpc` network mode is required. For Amazon ECS tasks on Amazon EC2 Linux instances, any network mode can be used. For Amazon ECS tasks on Amazon EC2 Windows instances, `<default>` or `awsvpc` can be used. If the network mode is set to `none`, you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The `host` and `awsvpc` network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the `bridge` mode.
With the `host` and `awsvpc` network modes, exposed container ports are mapped directly to the corresponding host port (for the `host` network mode) or the attached elastic network interface port (for the `awsvpc` network mode), so you cannot take advantage of dynamic host port mappings.
When using the `host` network mode, you should not run containers using the root user (UID 0). It is considered best practice to use a non-root user.
If the network mode is `awsvpc`, the task is allocated an elastic network interface, and you must specify a [NetworkConfiguration](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkConfiguration.html) value when you create a service or run a task with the task definition. For more information, see [Task Networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide*.
If the network mode is `host`, you cannot run multiple instantiations of the same task on a single container instance when port mappings are used.
Type: String
Valid Values: `bridge | host | awsvpc | none`
Required: No

 ** [pidMode](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-pidMode"></a>
The process namespace to use for the containers in the task. The valid values are `host` or `task`. On Fargate for Linux containers, the only valid value is `task`. For example, monitoring sidecars might need `pidMode` to access information about other containers running in the same task.
If `host` is specified, all containers within the tasks that specified the `host` PID mode on the same container instance share the same process namespace with the host Amazon EC2 instance.
If `task` is specified, all containers within the specified task share the same process namespace.
If no value is specified, the The default is a private namespace for each container.
If the `host` PID mode is used, there's a heightened risk of undesired process namespace exposure.
This parameter is not supported for Windows containers.
This parameter is only supported for tasks that are hosted on AWS Fargate if the tasks are using platform version `1.4.0` or later (Linux). This isn't supported for Windows containers on Fargate.
Type: String
Valid Values: `host | task`
Required: No

 ** [placementConstraints](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-placementConstraints"></a>
An array of placement constraint objects to use for the task. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.
Type: Array of [TaskDefinitionPlacementConstraint](API_TaskDefinitionPlacementConstraint.md) objects
Required: No

 ** [proxyConfiguration](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-proxyConfiguration"></a>
The configuration details for the App Mesh proxy.
For tasks hosted on Amazon EC2 instances, the container instances require at least version `1.26.0` of the container agent and at least version `1.26.0-1` of the `ecs-init` package to use a proxy configuration. If your container instances are launched from the Amazon ECS-optimized AMI version `20190301` or later, then they contain the required versions of the container agent and `ecs-init`. For more information, see [Amazon ECS-optimized AMI versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-ami-versions.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: [ProxyConfiguration](API_ProxyConfiguration.md) object
Required: No

 ** [requiresCompatibilities](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-requiresCompatibilities"></a>
The task launch type that Amazon ECS validates the task definition against. A client exception is returned if the task definition doesn't validate against the compatibilities specified. If no value is specified, the parameter is omitted from the response.
Type: Array of strings
Valid Values: `EC2 | FARGATE | EXTERNAL | MANAGED_INSTANCES`
Required: No

 ** [runtimePlatform](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-runtimePlatform"></a>
The operating system that your tasks definitions run on.
Type: [RuntimePlatform](API_RuntimePlatform.md) object
Required: No

 ** [tags](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-tags"></a>
The metadata that you apply to the task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.
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

 ** [taskRoleArn](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-taskRoleArn"></a>
The short name or full Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see [IAM Roles for Tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** [volumes](#API_RegisterTaskDefinition_RequestSyntax) **   <a name="ECS-RegisterTaskDefinition-request-volumes"></a>
A list of volume definitions in JSON format that containers in your task might use.
Type: Array of [Volume](API_Volume.md) objects
Required: No

## Response Syntax
<a name="API_RegisterTaskDefinition_ResponseSyntax"></a>

```
{
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ],
   "taskDefinition": {
      "compatibilities": [ "string" ],
      "containerDefinitions": [
         {
            "command": [ "string" ],
            "cpu": number,
            "credentialSpecs": [ "string" ],
            "dependsOn": [
               {
                  "condition": "string",
                  "containerName": "string"
               }
            ],
            "disableNetworking": boolean,
            "dnsSearchDomains": [ "string" ],
            "dnsServers": [ "string" ],
            "dockerLabels": {
               "string" : "string"
            },
            "dockerSecurityOptions": [ "string" ],
            "entryPoint": [ "string" ],
            "environment": [
               {
                  "name": "string",
                  "value": "string"
               }
            ],
            "environmentFiles": [
               {
                  "type": "string",
                  "value": "string"
               }
            ],
            "essential": boolean,
            "extraHosts": [
               {
                  "hostname": "string",
                  "ipAddress": "string"
               }
            ],
            "firelensConfiguration": {
               "options": {
                  "string" : "string"
               },
               "type": "string"
            },
            "healthCheck": {
               "command": [ "string" ],
               "interval": number,
               "retries": number,
               "startPeriod": number,
               "timeout": number
            },
            "hostname": "string",
            "image": "string",
            "interactive": boolean,
            "links": [ "string" ],
            "linuxParameters": {
               "capabilities": {
                  "add": [ "string" ],
                  "drop": [ "string" ]
               },
               "devices": [
                  {
                     "containerPath": "string",
                     "hostPath": "string",
                     "permissions": [ "string" ]
                  }
               ],
               "initProcessEnabled": boolean,
               "maxSwap": number,
               "sharedMemorySize": number,
               "swappiness": number,
               "tmpfs": [
                  {
                     "containerPath": "string",
                     "mountOptions": [ "string" ],
                     "size": number
                  }
               ]
            },
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
            "memory": number,
            "memoryReservation": number,
            "mountPoints": [
               {
                  "containerPath": "string",
                  "readOnly": boolean,
                  "sourceVolume": "string"
               }
            ],
            "name": "string",
            "portMappings": [
               {
                  "appProtocol": "string",
                  "containerPort": number,
                  "containerPortRange": "string",
                  "hostPort": number,
                  "name": "string",
                  "protocol": "string"
               }
            ],
            "privileged": boolean,
            "pseudoTerminal": boolean,
            "readonlyRootFilesystem": boolean,
            "repositoryCredentials": {
               "credentialsParameter": "string"
            },
            "resourceRequirements": [
               {
                  "type": "string",
                  "value": "string"
               }
            ],
            "restartPolicy": {
               "enabled": boolean,
               "ignoredExitCodes": [ number ],
               "restartAttemptPeriod": number
            },
            "secrets": [
               {
                  "name": "string",
                  "valueFrom": "string"
               }
            ],
            "startTimeout": number,
            "stopTimeout": number,
            "systemControls": [
               {
                  "namespace": "string",
                  "value": "string"
               }
            ],
            "ulimits": [
               {
                  "hardLimit": number,
                  "name": "string",
                  "softLimit": number
               }
            ],
            "user": "string",
            "versionConsistency": "string",
            "volumesFrom": [
               {
                  "readOnly": boolean,
                  "sourceContainer": "string"
               }
            ],
            "workingDirectory": "string"
         }
      ],
      "cpu": "string",
      "deleteRequestedAt": number,
      "deregisteredAt": number,
      "enableFaultInjection": boolean,
      "ephemeralStorage": {
         "sizeInGiB": number
      },
      "executionRoleArn": "string",
      "family": "string",
      "inferenceAccelerators": [
         {
            "deviceName": "string",
            "deviceType": "string"
         }
      ],
      "ipcMode": "string",
      "memory": "string",
      "networkMode": "string",
      "pidMode": "string",
      "placementConstraints": [
         {
            "expression": "string",
            "type": "string"
         }
      ],
      "proxyConfiguration": {
         "containerName": "string",
         "properties": [
            {
               "name": "string",
               "value": "string"
            }
         ],
         "type": "string"
      },
      "registeredAt": number,
      "registeredBy": "string",
      "requiresAttributes": [
         {
            "name": "string",
            "targetId": "string",
            "targetType": "string",
            "value": "string"
         }
      ],
      "requiresCompatibilities": [ "string" ],
      "revision": number,
      "runtimePlatform": {
         "cpuArchitecture": "string",
         "operatingSystemFamily": "string"
      },
      "status": "string",
      "taskDefinitionArn": "string",
      "taskRoleArn": "string",
      "volumes": [
         {
            "configuredAtLaunch": boolean,
            "dockerVolumeConfiguration": {
               "autoprovision": boolean,
               "driver": "string",
               "driverOpts": {
                  "string" : "string"
               },
               "labels": {
                  "string" : "string"
               },
               "scope": "string"
            },
            "efsVolumeConfiguration": {
               "authorizationConfig": {
                  "accessPointId": "string",
                  "iam": "string"
               },
               "fileSystemId": "string",
               "rootDirectory": "string",
               "transitEncryption": "string",
               "transitEncryptionPort": number
            },
            "fsxWindowsFileServerVolumeConfiguration": {
               "authorizationConfig": {
                  "credentialsParameter": "string",
                  "domain": "string"
               },
               "fileSystemId": "string",
               "rootDirectory": "string"
            },
            "host": {
               "sourcePath": "string"
            },
            "name": "string",
            "s3filesVolumeConfiguration": {
               "accessPointArn": "string",
               "fileSystemArn": "string",
               "rootDirectory": "string",
               "transitEncryptionPort": number
            }
         }
      ]
   }
}
```

## Response Elements
<a name="API_RegisterTaskDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_RegisterTaskDefinition_ResponseSyntax) **   <a name="ECS-RegisterTaskDefinition-response-tags"></a>
The list of tags associated with the task definition.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [taskDefinition](#API_RegisterTaskDefinition_ResponseSyntax) **   <a name="ECS-RegisterTaskDefinition-response-taskDefinition"></a>
The full description of the registered task definition.
Type: [TaskDefinition](API_TaskDefinition.md) object

## Errors
<a name="API_RegisterTaskDefinition_Errors"></a>

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

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The limit for the resource was exceeded.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

## Examples
<a name="API_RegisterTaskDefinition_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the [AWS Command Line Interface](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.

### Example
<a name="API_RegisterTaskDefinition_Example_1"></a>

This example request registers a task definition in the `hello_world` family with the `host` networking mode.

#### Sample Request
<a name="API_RegisterTaskDefinition_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecs.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 486
X-Amz-Target: AmazonEC2ContainerServiceV20141113.RegisterTaskDefinition
X-Amz-Date: 20150429T193109Z
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "networkMode": "host",
  "containerDefinitions": [
    {
      "name": "wordpress",
      "links": [
        "mysql"
      ],
      "image": "public.ecr.aws/docker/library/wordpress:latest",
      "essential": true,
      "portMappings": [
        {
          "containerPort": 80,
          "hostPort": 80
        }
      ],
      "memory": 500,
      "cpu": 10
    },
    {
      "name": "mysql",
      "image": "public.ecr.aws/docker/library/mysql:latest",
      "cpu": 10,
      "environment": [
        {
          "name": "MYSQL_ROOT_PASSWORD",
          "value": "password"
        }
      ],
      "memory": 500,
      "healthCheck": {
          "retries": 3,
          "command": [
              "CMD-SHELL",
              "curl -f http://localhost:8080/ || exit 1"
          ],
          "timeout": 5,
          "interval": 30,
      },
      "essential": true
    }
  ],
  "family": "hello_world"
}
```

#### Sample Response
<a name="API_RegisterTaskDefinition_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 12 Aug 2016 22:17:20 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 714
Connection: keep-alive
x-amzn-RequestId: 896d7e0f-60da-11e6-8e21-55c97a4b6423

{
  "taskDefinition": {
    "containerDefinitions": [
      {
        "cpu": 10,
        "environment": [],
        "healthCheck": {
              "retries": 3,
              "command": [
                  "CMD-SHELL",
                  "curl -f http://localhost:8080/ || exit 1"
              ],
              "timeout": 5,
              "interval": 30,
              "startPeriod": null
        },
        "essential": true,
        "image": "public.ecr.aws/docker/library/wordpress:latest",
        "links": [
          "mysql"
        ],
        "memory": 500,
        "mountPoints": [],
        "name": "wordpress",
        "portMappings": [
          {
            "containerPort": 80,
            "hostPort": 80,
            "protocol": "tcp"
          }
        ],
        "volumesFrom": []
      },
      {
        "cpu": 10,
        "environment": [
          {
            "name": "MYSQL_ROOT_PASSWORD",
            "value": "password"
          }
        ],
        "essential": true,
        "image": "public.ecr.aws/docker/library/mysql:latest",
        "memory": 500,
        "mountPoints": [],
        "name": "mysql",
        "portMappings": [],
        "volumesFrom": []
      }
    ],
    "family": "hello_world",
    "networkMode": "host",
    "runtimePlatform":LINUX
    "requiresAttributes": [
      {
        "name": "com.amazonaws.ecs.capability.docker-remote-api.1.18"
      }
    ],
    "revision": 4,
    "status": "ACTIVE",
    "taskDefinitionArn": "arn:aws:ecs:us-east-1:012345678910:task-definition/hello_world:4",
    "volumes": []
  }
}
```

## See Also
<a name="API_RegisterTaskDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/RegisterTaskDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/RegisterTaskDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/RegisterTaskDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/RegisterTaskDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/RegisterTaskDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/RegisterTaskDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/RegisterTaskDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/RegisterTaskDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/RegisterTaskDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/RegisterTaskDefinition)
