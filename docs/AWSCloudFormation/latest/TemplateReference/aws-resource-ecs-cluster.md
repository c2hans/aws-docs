---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-cluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Cluster
<a name="aws-resource-ecs-cluster"></a>

The `AWS::ECS::Cluster` resource creates an Amazon Elastic Container Service (Amazon ECS) cluster.

## Syntax
<a name="aws-resource-ecs-cluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ecs-cluster-syntax.json"></a>

```
{
  "Type" : "AWS::ECS::Cluster",
  "Properties" : {
      "[CapacityProviders](#cfn-ecs-cluster-capacityproviders)" : {{[ String, ... ]}},
      "[ClusterName](#cfn-ecs-cluster-clustername)" : {{String}},
      "[ClusterSettings](#cfn-ecs-cluster-clustersettings)" : {{[ ClusterSettings, ... ]}},
      "[Configuration](#cfn-ecs-cluster-configuration)" : {{ClusterConfiguration}},
      "[DefaultCapacityProviderStrategy](#cfn-ecs-cluster-defaultcapacityproviderstrategy)" : {{[ CapacityProviderStrategyItem, ... ]}},
      "[ServiceConnectDefaults](#cfn-ecs-cluster-serviceconnectdefaults)" : {{ServiceConnectDefaults}},
      "[Tags](#cfn-ecs-cluster-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ecs-cluster-syntax.yaml"></a>

```
Type: AWS::ECS::Cluster
Properties:
  [CapacityProviders](#cfn-ecs-cluster-capacityproviders): {{
    - String}}
  [ClusterName](#cfn-ecs-cluster-clustername): {{String}}
  [ClusterSettings](#cfn-ecs-cluster-clustersettings): {{
    - ClusterSettings}}
  [Configuration](#cfn-ecs-cluster-configuration): {{
    ClusterConfiguration}}
  [DefaultCapacityProviderStrategy](#cfn-ecs-cluster-defaultcapacityproviderstrategy): {{
    - CapacityProviderStrategyItem}}
  [ServiceConnectDefaults](#cfn-ecs-cluster-serviceconnectdefaults): {{
    ServiceConnectDefaults}}
  [Tags](#cfn-ecs-cluster-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ecs-cluster-properties"></a>

`CapacityProviders`  <a name="cfn-ecs-cluster-capacityproviders"></a>
The short name of one or more capacity providers to associate with the cluster. A capacity provider must be associated with a cluster before it can be included as part of the default capacity provider strategy of the cluster or used in a capacity provider strategy when calling the [CreateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html) or [RunTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html) actions.
If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must be created but not associated with another cluster. New Auto Scaling group capacity providers can be created with the [CreateCapacityProvider](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html) API operation.
To use a AWS Fargate capacity provider, specify either the `FARGATE` or `FARGATE_SPOT` capacity providers. The AWS Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.
The [PutCapacityProvider](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutCapacityProvider.html) API operation is used to update the list of available capacity providers for a cluster after the cluster is created.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClusterName`  <a name="cfn-ecs-cluster-clustername"></a>
A user-generated string that you use to identify your cluster. If you don't specify a name, AWS CloudFormation generates a unique physical ID for the name.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClusterSettings`  <a name="cfn-ecs-cluster-clustersettings"></a>
The settings to use when creating a cluster. This parameter is used to turn on CloudWatch Container Insights with enhanced observability or CloudWatch Container Insights for a cluster.
Container Insights with enhanced observability provides all the Container Insights metrics, plus additional task and container metrics. This version supports enhanced observability for Amazon ECS clusters using the Amazon EC2 and Fargate launch types. After you configure Container Insights with enhanced observability on Amazon ECS, Container Insights auto-collects detailed infrastructure telemetry from the cluster level down to the container level in your environment and displays these critical performance data in curated dashboards removing the heavy lifting in observability set-up.
For more information, see [Monitor Amazon ECS containers using Container Insights with enhanced observability](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-container-insights.html) in the *Amazon Elastic Container Service Developer Guide*.
*Required*: No
*Type*: [Array](aws-properties-ecs-cluster-clustersettings.md) of [ClusterSettings](aws-properties-ecs-cluster-clustersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Configuration`  <a name="cfn-ecs-cluster-configuration"></a>
The execute command and managed storage configuration for the cluster.
*Required*: No
*Type*: [ClusterConfiguration](aws-properties-ecs-cluster-clusterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultCapacityProviderStrategy`  <a name="cfn-ecs-cluster-defaultcapacityproviderstrategy"></a>
The default capacity provider strategy for the cluster. When services or tasks are run in the cluster with no launch type or capacity provider strategy specified, the default capacity provider strategy is used.
*Required*: No
*Type*: Array of [CapacityProviderStrategyItem](aws-properties-ecs-cluster-capacityproviderstrategyitem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceConnectDefaults`  <a name="cfn-ecs-cluster-serviceconnectdefaults"></a>
Use this parameter to set a default Service Connect namespace. After you set a default Service Connect namespace, any new services with Service Connect turned on that are created in the cluster are added as client services in the namespace. This setting only applies to new services that set the `enabled` parameter to `true` in the `ServiceConnectConfiguration`. You can set the namespace of each service individually in the `ServiceConnectConfiguration` to override this default parameter.
Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide*.
*Required*: No
*Type*: [ServiceConnectDefaults](aws-properties-ecs-cluster-serviceconnectdefaults.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ecs-cluster-tags"></a>
The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8
+ Maximum value length - 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.
*Required*: No
*Type*: Array of [Tag](aws-properties-ecs-cluster-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ecs-cluster-return-values"></a>

### Ref
<a name="aws-resource-ecs-cluster-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

In the following example, the `Ref` function returns the name of the `MyECSCluster` cluster, such as `MyStack-MyECSCluster-NT5EUXTNTXXD`.

 `{ "Ref": "MyECSCluster" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ecs-cluster-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ecs-cluster-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Amazon ECS cluster, such as `arn:aws:ecs:us-east-2:123456789012:cluster/MyECSCluster`.

## Examples
<a name="aws-resource-ecs-cluster--examples"></a>

**Topics**
+ [Create a cluster with Fargate capacity providers and a default capacity provider strategy](#aws-resource-ecs-cluster--examples--Create_a_cluster_with_Fargate_capacity_providers_and_a_default_capacity_provider_strategy)
+ [Create a cluster with the Amazon Linux 2023 ECS-Optimized-AMI](#aws-resource-ecs-cluster--examples--Create_a_cluster_with_the_Amazon_Linux_2023_ECS-Optimized-AMI)
+ [Create an empty cluster with CloudWatch Container Insights enabled and defined tags](#aws-resource-ecs-cluster--examples--Create_an_empty_cluster_with_CloudWatch_Container_Insights_enabled_and_defined_tags)

### Create a cluster with Fargate capacity providers and a default capacity provider strategy
<a name="aws-resource-ecs-cluster--examples--Create_a_cluster_with_Fargate_capacity_providers_and_a_default_capacity_provider_strategy"></a>

The following example creates a cluster named `MyFargateCluster` with the `FARGATE` and `FARGATE_SPOT` capacity providers. A default capacity provider strategy is also created where tasks launched will be split evenly between the `FARGATE` and `FARGATE_SPOT` capacity providers. The template also enables ECS Exec using the default logging configuration. For more information, see [Monitor Amazon ECS containers with ECS Exec](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html) in the *Amazon ECS Developer Guide*.

#### JSON
<a name="aws-resource-ecs-cluster--examples--Create_a_cluster_with_Fargate_capacity_providers_and_a_default_capacity_provider_strategy--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "ECSCluster": {
      "Type": "AWS::ECS::Cluster",
      "Properties": {
        "ClusterName": "MyFargateCluster",
        "CapacityProviders": ["FARGATE", "FARGATE_SPOT"],
        "DefaultCapacityProviderStrategy": [
          {
            "CapacityProvider": "FARGATE",
            "Weight": 1
          },
          {
            "CapacityProvider": "FARGATE_SPOT",
            "Weight": 1
          }
        ],
        "Configuration": {
          "ExecuteCommandConfiguration": {
            "Logging": "DEFAULT"
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-ecs-cluster--examples--Create_a_cluster_with_Fargate_capacity_providers_and_a_default_capacity_provider_strategy--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  ECSCluster:
    Type: AWS::ECS::Cluster
    Properties:
      ClusterName: MyFargateCluster
      CapacityProviders:
        - FARGATE
        - FARGATE_SPOT
      DefaultCapacityProviderStrategy:
        - CapacityProvider: FARGATE
          Weight: 1
        - CapacityProvider: FARGATE_SPOT
          Weight: 1
      Configuration:
        ExecuteCommandConfiguration:
          Logging: DEFAULT
```

### Create a cluster with the Amazon Linux 2023 ECS-Optimized-AMI
<a name="aws-resource-ecs-cluster--examples--Create_a_cluster_with_the_Amazon_Linux_2023_ECS-Optimized-AMI"></a>

The following example creates a cluster named `MyCluster` with a capacity provider that launches Amazon Linux 2023 t2.medium instances. Replace parameters with your own information.

#### JSON
<a name="aws-resource-ecs-cluster--examples--Create_a_cluster_with_the_Amazon_Linux_2023_ECS-Optimized-AMI--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "EC2 ECS cluster that starts out empty, with no EC2 instances yet. An ECS capacity provider automatically launches more EC2 instances as required on the fly when you request ECS to launch services or standalone tasks.",
  "Parameters": {
      "InstanceType": {
          "Type": "String",
          "Description": "EC2 instance type",
          "Default": "t2.medium",
          "AllowedValues": [
              "t1.micro",
              "t2.2xlarge",
              "t2.large",
              "t2.medium",
              "t2.micro",
              "t2.nano",
              "t2.small",
              "t2.xlarge",
              "t3.2xlarge",
              "t3.large",
              "t3.medium",
              "t3.micro",
              "t3.nano",
              "t3.small",
              "t3.xlarge"
          ]
      },
      "DesiredCapacity": {
          "Type": "Number",
          "Default": "0",
          "Description": "Number of EC2 instances to launch in your ECS cluster."
      },
      "MaxSize": {
          "Type": "Number",
          "Default": "100",
          "Description": "Maximum number of EC2 instances that can be launched in your ECS cluster."
      },
      "ECSAMI": {
          "Description": "The Amazon Machine Image ID used for the cluster",
          "Type": "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>",
          "Default": "/aws/service/ecs/optimized-ami/amazon-linux-2023/recommended/image_id"
      },
      "VpcId": {
          "Type": "AWS::EC2::VPC::Id",
          "Description": "VPC ID where the ECS cluster is launched",
          "Default": "vpc-1234567890abcdef0"
      },
      "SubnetIds": {
          "Type": "List<AWS::EC2::Subnet::Id>",
          "Description": "List of subnet IDs where the EC2 instances will be launched",
          "Default": "subnet-021345abcdef67890"
      }
  },
  "Resources": {
      "ECSCluster": {
          "Type": "AWS::ECS::Cluster",
          "Properties": {
              "ClusterSettings": [
                  {
                      "Name": "containerInsights",
                      "Value": "enabled"
                  }
              ]
          }
      },
      "ECSAutoScalingGroup": {
          "Type": "AWS::AutoScaling::AutoScalingGroup",
          "DependsOn": [
              "ECSCluster",
              "EC2Role"
          ],
          "Properties": {
              "VPCZoneIdentifier": {
                  "Ref": "SubnetIds"
              },
              "LaunchTemplate": {
                  "LaunchTemplateId": {
                      "Ref": "ContainerInstances"
                  },
                  "Version": {
                      "Fn::GetAtt": [
                          "ContainerInstances",
                          "LatestVersionNumber"
                      ]
                  }
              },
              "MinSize": 0,
              "MaxSize": {
                  "Ref": "MaxSize"
              },
              "DesiredCapacity": {
                  "Ref": "DesiredCapacity"
              },
              "NewInstancesProtectedFromScaleIn": true
          },
          "UpdatePolicy": {
              "AutoScalingReplacingUpdate": {
                  "WillReplace": "true"
              }
          }
      },
      "ContainerInstances": {
          "Type": "AWS::EC2::LaunchTemplate",
          "Properties": {
              "LaunchTemplateName": "asg-launch-template",
              "LaunchTemplateData": {
                  "ImageId": {
                      "Ref": "ECSAMI"
                  },
                  "InstanceType": {
                      "Ref": "InstanceType"
                  },
                  "IamInstanceProfile": {
                      "Name": {
                          "Ref": "EC2InstanceProfile"
                      }
                  },
                  "SecurityGroupIds": [
                      {
                          "Ref": "ContainerHostSecurityGroup"
                      }
                  ],
                  "UserData": {
                      "Fn::Base64": {
                          "Fn::Sub": "#!/bin/bash -xe\n echo ECS_CLUSTER=${ECSCluster} >> /etc/ecs/ecs.config\n yum install -y aws-cfn-bootstrap\n /opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource ContainerInstances --configsets full_install --region ${AWS::Region} &\n"
                      }
                  },
                  "MetadataOptions": {
                      "HttpEndpoint": "enabled",
                      "HttpTokens": "required"
                  }
              }
          }
      },
      "EC2InstanceProfile": {
          "Type": "AWS::IAM::InstanceProfile",
          "Properties": {
              "Path": "/",
              "Roles": [
                  {
                      "Ref": "EC2Role"
                  }
              ]
          }
      },
      "CapacityProvider": {
          "Type": "AWS::ECS::CapacityProvider",
          "Properties": {
              "AutoScalingGroupProvider": {
                  "AutoScalingGroupArn": {
                      "Ref": "ECSAutoScalingGroup"
                  },
                  "ManagedScaling": {
                      "InstanceWarmupPeriod": 60,
                      "MinimumScalingStepSize": 1,
                      "MaximumScalingStepSize": 100,
                      "Status": "ENABLED",
                      "TargetCapacity": 100
                  },
                  "ManagedTerminationProtection": "ENABLED"
              }
          }
      },
      "CapacityProviderAssociation": {
          "Type": "AWS::ECS::ClusterCapacityProviderAssociations",
          "Properties": {
              "CapacityProviders": [
                  {
                      "Ref": "CapacityProvider"
                  }
              ],
              "Cluster": {
                  "Ref": "ECSCluster"
              },
              "DefaultCapacityProviderStrategy": [
                  {
                      "Base": 0,
                      "CapacityProvider": {
                          "Ref": "CapacityProvider"
                      },
                      "Weight": 1
                  }
              ]
          }
      },
      "ContainerHostSecurityGroup": {
          "Type": "AWS::EC2::SecurityGroup",
          "Properties": {
              "GroupDescription": "Access to the EC2 hosts that run containers",
              "VpcId": {
                  "Ref": "VpcId"
              }
          }
      },
      "EC2Role": {
          "Type": "AWS::IAM::Role",
          "Properties": {
              "AssumeRolePolicyDocument": {
                  "Statement": [
                      {
                          "Effect": "Allow",
                          "Principal": {
                              "Service": [
                                  "ec2.amazonaws.com"
                              ]
                          },
                          "Action": [
                              "sts:AssumeRole"
                          ]
                      }
                  ]
              },
              "Path": "/",
              "ManagedPolicyArns": [
                  "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role",
                  "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
              ]
          }
      },
      "ECSTaskExecutionRole": {
          "Type": "AWS::IAM::Role",
          "Properties": {
              "AssumeRolePolicyDocument": {
                  "Statement": [
                      {
                          "Effect": "Allow",
                          "Principal": {
                              "Service": [
                                  "ecs-tasks.amazonaws.com"
                              ]
                          },
                          "Action": [
                              "sts:AssumeRole"
                          ],
                          "Condition": {
                              "ArnLike": {
                                  "aws:SourceArn": {
                                      "Fn::Sub": "arn:${AWS::Partition}:ecs:${AWS::Region}:${AWS::AccountId}:*"
                                  }
                              },
                              "StringEquals": {
                                  "aws:SourceAccount": {
                                        "Fn::Sub": "${AWS::AccountId}"
                                    }
                              }
                          }
                      }
                  ]
              },
              "Path": "/",
              "ManagedPolicyArns": [
                  "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
              ]
          }
      }
  },
  "Outputs": {
      "ClusterName": {
          "Description": "The ECS cluster into which to launch resources",
          "Value": "ECSCluster"
      },
      "ECSTaskExecutionRole": {
          "Description": "The role used to start up a task",
          "Value": "ECSTaskExecutionRole"
      },
      "CapacityProvider": {
          "Description": "The cluster capacity provider that the service should use to request capacity when it wants to start up a task",
          "Value": "CapacityProvider"
      }
  }
}
```

#### YAML
<a name="aws-resource-ecs-cluster--examples--Create_a_cluster_with_the_Amazon_Linux_2023_ECS-Optimized-AMI--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: EC2 ECS cluster that starts out empty, with no EC2 instances yet.
  An ECS capacity provider automatically launches more EC2 instances as required
  on the fly when you request ECS to launch services or standalone tasks.
Parameters:
  InstanceType:
    Type: String
    Description: EC2 instance type
    Default: "t2.medium"
    AllowedValues:
      - t1.micro
      - t2.2xlarge
      - t2.large
      - t2.medium
      - t2.micro
      - t2.nano
      - t2.small
      - t2.xlarge
      - t3.2xlarge
      - t3.large
      - t3.medium
      - t3.micro
      - t3.nano
      - t3.small
      - t3.xlarge
  DesiredCapacity:
    Type: Number
    Default: "0"
    Description: Number of EC2 instances to launch in your ECS cluster.
  MaxSize:
    Type: Number
    Default: "100"
    Description: Maximum number of EC2 instances that can be launched in your ECS cluster.
  ECSAMI:
    Description: The Amazon Machine Image ID used for the cluster
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ecs/optimized-ami/amazon-linux-2023/recommended/image_id
  VpcId:
    Type: AWS::EC2::VPC::Id
    Description: VPC ID where the ECS cluster is launched
    Default: vpc-1234567890abcdef0
  SubnetIds:
    Type: List<AWS::EC2::Subnet::Id>
    Description: List of subnet IDs where the EC2 instances will be launched
    Default: "subnet-021345abcdef67890"
Resources:
# This is authorizes ECS to manage resources on your
  # account on your behalf. This role is likely already created on your account
  # ECSRole:
  #  Type: AWS::IAM::ServiceLinkedRole
  #  Properties:
  #    AWSServiceName: 'ecs.amazonaws.com'

   # ECS Resources
  ECSCluster:
    Type: AWS::ECS::Cluster
    Properties:
      ClusterSettings:
        - Name: containerInsights
          Value: enabled

  # Autoscaling group. This launches the actual EC2 instances that will register
  # themselves as members of the cluster, and run the docker containers.
  ECSAutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    DependsOn:
      # This is to ensure that the ASG gets deleted first before these
    # resources, when it comes to stack teardown.
      - ECSCluster
      - EC2Role
    Properties:
      VPCZoneIdentifier:
        Ref: SubnetIds
      LaunchTemplate:
        LaunchTemplateId: !Ref ContainerInstances
        Version: !GetAtt ContainerInstances.LatestVersionNumber
      MinSize: 0
      MaxSize:
        Ref: MaxSize
      DesiredCapacity:
        Ref: DesiredCapacity
      NewInstancesProtectedFromScaleIn: true
    UpdatePolicy:
      AutoScalingReplacingUpdate:
        WillReplace: "true"
  # The config for each instance that is added to the cluster
  ContainerInstances:
    Type: AWS::EC2::LaunchTemplate
    Properties:
      LaunchTemplateName: "asg-launch-template"
      LaunchTemplateData:
        ImageId:
          Ref: ECSAMI
        InstanceType:
          Ref: InstanceType
        IamInstanceProfile:
          Name: !Ref EC2InstanceProfile
        SecurityGroupIds:
          - !Ref ContainerHostSecurityGroup
        # This injected configuration file is how the EC2 instance
      # knows which ECS cluster on your AWS account it should be joining
        UserData:
          Fn::Base64: !Sub |
           #!/bin/bash -xe
            echo ECS_CLUSTER=${ECSCluster} >> /etc/ecs/ecs.config
            yum install -y aws-cfn-bootstrap
            /opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource ContainerInstances --configsets full_install --region ${AWS::Region} &
         # Disable IMDSv1, and require IMDSv2
        MetadataOptions:
          HttpEndpoint: enabled
          HttpTokens: required
  EC2InstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: /
      Roles:
      - !Ref EC2Role
  # Create an ECS capacity provider to attach the ASG to the ECS cluster
  # so that it autoscales as we launch more containers
  CapacityProvider:
    Type: AWS::ECS::CapacityProvider
    Properties:
      AutoScalingGroupProvider:
        AutoScalingGroupArn: !Ref ECSAutoScalingGroup
        ManagedScaling:
          InstanceWarmupPeriod: 60
          MinimumScalingStepSize: 1
          MaximumScalingStepSize: 100
          Status: ENABLED
          # Percentage of cluster reservation to try to maintain
          TargetCapacity: 100
        ManagedTerminationProtection: ENABLED
   # Create a cluster capacity provider assocation so that the cluster
  # will use the capacity provider
  CapacityProviderAssociation:
    Type: AWS::ECS::ClusterCapacityProviderAssociations
    Properties:
      CapacityProviders:
        - !Ref CapacityProvider
      Cluster: !Ref ECSCluster
      DefaultCapacityProviderStrategy:
        - Base: 0
          CapacityProvider: !Ref CapacityProvider
          Weight: 1
  # A security group for the EC2 hosts that will run the containers.
  # This can be used to limit incoming traffic to or outgoing traffic
  # from the container's host EC2 instance.
  ContainerHostSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Access to the EC2 hosts that run containers
      VpcId:
        Ref: VpcId
  # Role for the EC2 hosts. This allows the ECS agent on the EC2 hosts
  # to communciate with the ECS control plane, as well as download the docker
  # images from ECR to run on your host.
  EC2Role:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
            Action:
              - sts:AssumeRole
      Path: /
      ManagedPolicyArns:
      # See reference: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonEC2ContainerServiceforEC2Role
        - arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role
      # This managed policy allows us to connect to the instance using SSM
        - arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
  # This is a role which is used within Fargate to allow the Fargate agent
  # to download images, and upload logs.
  ECSTaskExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ecs-tasks.amazonaws.com
            Action:
              - sts:AssumeRole
            Condition:
              ArnLike:
                aws:SourceArn: !Sub arn:${AWS::Partition}:ecs:${AWS::Region}:${AWS::AccountId}:*
              StringEquals:
                aws:SourceAccount: !Sub ${AWS::AccountId}
      Path: /
      # This role enables all features of ECS. See reference:
    # https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonECSTaskExecutionRolePolicy
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy
Outputs:
  ClusterName:
    Description: The ECS cluster into which to launch resources
    Value: ECSCluster
  ECSTaskExecutionRole:
    Description: The role used to start up a task
    Value: ECSTaskExecutionRole
  CapacityProvider:
    Description: The cluster capacity provider that the service should use to
      request capacity when it wants to start up a task
    Value: CapacityProvider
```

### Create an empty cluster with CloudWatch Container Insights enabled and defined tags
<a name="aws-resource-ecs-cluster--examples--Create_an_empty_cluster_with_CloudWatch_Container_Insights_enabled_and_defined_tags"></a>

The following example creates an empty cluster named `MyCluster` that has CloudWatch Container Insights enabled and is tagged with the key `environment` and the value `production`.

#### JSON
<a name="aws-resource-ecs-cluster--examples--Create_an_empty_cluster_with_CloudWatch_Container_Insights_enabled_and_defined_tags--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "ECSCluster": {
        "Type": "AWS::ECS::Cluster",
        "Properties": {
            "ClusterName": "MyCluster",
            "ClusterSettings": [
                {
                    "Name": "containerInsights",
                    "Value": "enabled"
                }
            ],
            "Tags": [
                {
                    "Key": "environment",
                    "Value": "production"
                }
            ]
        }
    }
  }
}
```

#### YAML
<a name="aws-resource-ecs-cluster--examples--Create_an_empty_cluster_with_CloudWatch_Container_Insights_enabled_and_defined_tags--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  ECSCluster:
    Type: AWS::ECS::Cluster
    Properties:
      ClusterName: MyCluster
      ClusterSettings:
        - Name: containerInsights
          Value: enabled
      Tags:
        - Key: environment
          Value: production
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
