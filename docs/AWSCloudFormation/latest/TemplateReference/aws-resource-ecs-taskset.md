---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskSet
<a name="aws-resource-ecs-taskset"></a>

Create a task set in the specified cluster and service. This is used when a service uses the `EXTERNAL` deployment controller type. For more information, see [Amazon ECS deployment types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html) in the *Amazon Elastic Container Service Developer Guide*.

**Note**
On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.

For information about the maximum number of task sets and other quotas, see [Amazon ECS service quotas](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html) in the *Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-resource-ecs-taskset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ecs-taskset-syntax.json"></a>

```
{
  "Type" : "AWS::ECS::TaskSet",
  "Properties" : {
      "[CapacityProviderStrategy](#cfn-ecs-taskset-capacityproviderstrategy)" : {{[ CapacityProviderStrategyItem, ... ]}},
      "[Cluster](#cfn-ecs-taskset-cluster)" : {{String}},
      "[ExternalId](#cfn-ecs-taskset-externalid)" : {{String}},
      "[LaunchType](#cfn-ecs-taskset-launchtype)" : {{String}},
      "[LoadBalancers](#cfn-ecs-taskset-loadbalancers)" : {{[ LoadBalancer, ... ]}},
      "[NetworkConfiguration](#cfn-ecs-taskset-networkconfiguration)" : {{NetworkConfiguration}},
      "[PlatformVersion](#cfn-ecs-taskset-platformversion)" : {{String}},
      "[Scale](#cfn-ecs-taskset-scale)" : {{Scale}},
      "[Service](#cfn-ecs-taskset-service)" : {{String}},
      "[ServiceRegistries](#cfn-ecs-taskset-serviceregistries)" : {{[ ServiceRegistry, ... ]}},
      "[Tags](#cfn-ecs-taskset-tags)" : {{[ Tag, ... ]}},
      "[TaskDefinition](#cfn-ecs-taskset-taskdefinition)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ecs-taskset-syntax.yaml"></a>

```
Type: AWS::ECS::TaskSet
Properties:
  [CapacityProviderStrategy](#cfn-ecs-taskset-capacityproviderstrategy): {{
    - CapacityProviderStrategyItem}}
  [Cluster](#cfn-ecs-taskset-cluster): {{String}}
  [ExternalId](#cfn-ecs-taskset-externalid): {{String}}
  [LaunchType](#cfn-ecs-taskset-launchtype): {{String}}
  [LoadBalancers](#cfn-ecs-taskset-loadbalancers): {{
    - LoadBalancer}}
  [NetworkConfiguration](#cfn-ecs-taskset-networkconfiguration): {{
    NetworkConfiguration}}
  [PlatformVersion](#cfn-ecs-taskset-platformversion): {{String}}
  [Scale](#cfn-ecs-taskset-scale): {{
    Scale}}
  [Service](#cfn-ecs-taskset-service): {{String}}
  [ServiceRegistries](#cfn-ecs-taskset-serviceregistries): {{
    - ServiceRegistry}}
  [Tags](#cfn-ecs-taskset-tags): {{
    - Tag}}
  [TaskDefinition](#cfn-ecs-taskset-taskdefinition): {{String}}
```

## Properties
<a name="aws-resource-ecs-taskset-properties"></a>

`CapacityProviderStrategy`  <a name="cfn-ecs-taskset-capacityproviderstrategy"></a>
The capacity provider strategy that are associated with the task set.
*Required*: No
*Type*: Array of [CapacityProviderStrategyItem](aws-properties-ecs-taskset-capacityproviderstrategyitem.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Cluster`  <a name="cfn-ecs-taskset-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExternalId`  <a name="cfn-ecs-taskset-externalid"></a>
An optional non-unique tag that identifies this task set in external systems. If the task set is associated with a service discovery registry, the tasks in this task set will have the `ECS_TASK_SET_EXTERNAL_ID`AWS Cloud Map attribute set to the provided value.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LaunchType`  <a name="cfn-ecs-taskset-launchtype"></a>
The launch type that new tasks in the task set uses. For more information, see [Amazon ECS launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide*.
If a `launchType` is specified, the `capacityProviderStrategy` parameter must be omitted.
*Required*: No
*Type*: String
*Allowed values*: `EC2 | FARGATE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LoadBalancers`  <a name="cfn-ecs-taskset-loadbalancers"></a>
A load balancer object representing the load balancer to use with the task set. The supported load balancer types are either an Application Load Balancer or a Network Load Balancer.
*Required*: No
*Type*: Array of [LoadBalancer](aws-properties-ecs-taskset-loadbalancer.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkConfiguration`  <a name="cfn-ecs-taskset-networkconfiguration"></a>
The network configuration for the task set.
*Required*: No
*Type*: [NetworkConfiguration](aws-properties-ecs-taskset-networkconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PlatformVersion`  <a name="cfn-ecs-taskset-platformversion"></a>
The platform version that the tasks in the task set uses. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the `LATEST` platform version is used.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Scale`  <a name="cfn-ecs-taskset-scale"></a>
A floating-point percentage of your desired number of tasks to place and keep running in the task set.
*Required*: No
*Type*: [Scale](aws-properties-ecs-taskset-scale.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Service`  <a name="cfn-ecs-taskset-service"></a>
The short name or full Amazon Resource Name (ARN) of the service to create the task set in.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceRegistries`  <a name="cfn-ecs-taskset-serviceregistries"></a>
The details of the service discovery registries to assign to this task set. For more information, see [Service discovery](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html).
*Required*: No
*Type*: Array of [ServiceRegistry](aws-properties-ecs-taskset-serviceregistry.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ecs-taskset-tags"></a>
The metadata that you apply to the task set to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8
+ Maximum value length - 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.
*Required*: No
*Type*: Array of [Tag](aws-properties-ecs-taskset-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskDefinition`  <a name="cfn-ecs-taskset-taskdefinition"></a>
The task definition for the tasks in the task set to use. If a revision isn't specified, the latest `ACTIVE` revision is used.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ecs-taskset-return-values"></a>

### Ref
<a name="aws-resource-ecs-taskset-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ecs-taskset-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ecs-taskset-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The ID of the task set.

## Examples
<a name="aws-resource-ecs-taskset--examples"></a>

### Create an Amazon ECS task set
<a name="aws-resource-ecs-taskset--examples--Create_an_task_set"></a>

This template defines a task definition, a cluster, a service, and a task set. The task set uses the specified task definition and is created in the specified cluster and service. Replace the `ExecutionRoleArn`, `SecurityGroups`, and `Subnets` with your own information.

#### JSON
<a name="aws-resource-ecs-taskset--examples--Create_an_task_set--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "ECSCluster": {
      "Type": "AWS::ECS::Cluster",
      "Properties": {
        "ClusterName": "deployment-cluster"
      }
    },
    "ECSService": {
      "Type": "AWS::ECS::Service",
      "Properties": {
        "ServiceName": "deployment-service",
        "Cluster": {
          "Ref": "ECSCluster"
        },
        "DesiredCount": 2,
        "DeploymentController": {
          "Type": "EXTERNAL"
        }
      }
    },
    "ECSTaskDefinition": {
      "Type": "AWS::ECS::TaskDefinition",
      "Properties": {
        "ContainerDefinitions": [
          {
            "Command": [
             "/bin/sh -c \"echo '<html> <head> <title>Amazon
              ECS Sample App</title> <style>body {margin-top: 40px;
              background-color: #333;} </style> </head><body>
              <div style=color:white;text-align:center> <h1>Amazon
              ECS Sample App</h1> <h2>Congratulations!</h2>
              <p>Your application is now running on a container in Amazon
              ECS.</p> </div></body></html>'
              >  /usr/local/apache2/htdocs/index.html &&
              httpd-foreground\""
            ],
            "EntryPoint": ["sh", "-c"],
            "Essential": true,
            "Image": "public.ecr.aws/docker/library/httpd:2.4",
            "LogConfiguration": {
              "LogDriver": "awslogs",
              "Options": {
                "awslogs-group": "/ecs/deployment",
                "awslogs-region": "us-east-1",
                "awslogs-stream-prefix": "ecs"
              }
            },
            "Name": "sample-fargate-app",
            "PortMappings": [
              {
                "ContainerPort": 80,
                "HostPort": 80,
                "Protocol": "tcp"
              }
            ]
          }
        ],
        "Cpu": 256,
        "ExecutionRoleArn": "arn:aws:iam::111122223333:role/ecsTaskExecutionRole",
        "Family": "deployment-task",
        "Memory": 512,
        "NetworkMode": "awsvpc",
        "RequiresCompatibilities": ["FARGATE"],
        "RuntimePlatform": {
          "OperatingSystemFamily": "LINUX"
        }
      }
    },
    "ECSTaskSet": {
      "Type": "AWS::ECS::TaskSet",
      "Properties": {
        "Cluster": {
          "Ref": "ECSCluster"
        },
        "LaunchType": "FARGATE",
        "NetworkConfiguration": {
          "AwsVpcConfiguration": {
            "AssignPublicIp": "ENABLED",
            "SecurityGroups": ["sg-abcdef01234567890"],
            "Subnets": ["subnet-021345abcdef67890"]
          }
        },
        "PlatformVersion": "1.4.0",
        "Scale": {
          "Unit": "PERCENT",
          "Value": 100
        },
        "Service": {
          "Ref": "ECSService"
        },
        "TaskDefinition": {
          "Ref": "ECSTaskDefinition"
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-ecs-taskset--examples--Create_an_task_set--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  ECSCluster:
    Type: AWS::ECS::Cluster
    Properties:
      ClusterName: deployment-cluster
  ECSService:
    Type: AWS::ECS::Service
    Properties:
      ServiceName: deployment-service
      Cluster:
        Ref: ECSCluster
      DesiredCount: 2
      DeploymentController:
        Type: EXTERNAL
  ECSTaskDefinition:
    Type: AWS::ECS::TaskDefinition
    Properties:
      ContainerDefinitions:
        - Command:
            - "/bin/sh -c \"echo '<html> <head> <title>Amazon
              ECS Sample App</title> <style>body {margin-top: 40px;
              background-color: #333;} </style> </head><body>
              <div style=color:white;text-align:center> <h1>Amazon
              ECS Sample App</h1> <h2>Congratulations!</h2>
              <p>Your application is now running on a container in Amazon
              ECS.</p> </div></body></html>'
              >  /usr/local/apache2/htdocs/index.html &&
              httpd-foreground\""
          EntryPoint:
            - sh
            - -c
          Essential: true
          Image: 'public.ecr.aws/docker/library/httpd:2.4'
          LogConfiguration:
            LogDriver: awslogs
            Options:
              awslogs-group: /ecs/deployment
              awslogs-region: us-east-1
              awslogs-stream-prefix: ecs
          Name: sample-fargate-app
          PortMappings:
            - ContainerPort: 80
              HostPort: 80
              Protocol: tcp
      Cpu: 256
      ExecutionRoleArn: arn:aws:iam::111122223333:role/ecsTaskExecutionRole
      Family: deployment-task
      Memory: 512
      NetworkMode: awsvpc
      RequiresCompatibilities:
        - FARGATE
      RuntimePlatform:
        OperatingSystemFamily: LINUX
  ECSTaskSet:
    Type: AWS::ECS::TaskSet
    Properties:
      Cluster:
        Ref: ECSCluster
      LaunchType: FARGATE
      NetworkConfiguration:
        AwsVpcConfiguration:
          AssignPublicIp: ENABLED
          SecurityGroups:
            - sg-abcdef01234567890
          Subnets:
            - subnet-abcdef01234567890
      PlatformVersion: 1.4.0
      Scale:
        Unit: PERCENT
        Value: 50
      Service:
        Ref: ECSService
      TaskDefinition:
        Ref: ECSTaskDefinition
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
