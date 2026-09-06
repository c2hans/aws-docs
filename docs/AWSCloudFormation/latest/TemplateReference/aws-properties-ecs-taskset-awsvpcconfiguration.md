---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskset-awsvpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskSet AwsVpcConfiguration
<a name="aws-properties-ecs-taskset-awsvpcconfiguration"></a>

An object representing the networking details for a task or service. For example `awsVpcConfiguration={subnets=["subnet-12344321"],securityGroups=["sg-12344321"]}`.

## Syntax
<a name="aws-properties-ecs-taskset-awsvpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskset-awsvpcconfiguration-syntax.json"></a>

```
{
  "[AssignPublicIp](#cfn-ecs-taskset-awsvpcconfiguration-assignpublicip)" : {{String}},
  "[SecurityGroups](#cfn-ecs-taskset-awsvpcconfiguration-securitygroups)" : {{[ String, ... ]}},
  "[Subnets](#cfn-ecs-taskset-awsvpcconfiguration-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ecs-taskset-awsvpcconfiguration-syntax.yaml"></a>

```
  [AssignPublicIp](#cfn-ecs-taskset-awsvpcconfiguration-assignpublicip): {{String}}
  [SecurityGroups](#cfn-ecs-taskset-awsvpcconfiguration-securitygroups): {{
    - String}}
  [Subnets](#cfn-ecs-taskset-awsvpcconfiguration-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-ecs-taskset-awsvpcconfiguration-properties"></a>

`AssignPublicIp`  <a name="cfn-ecs-taskset-awsvpcconfiguration-assignpublicip"></a>
Whether the task's elastic network interface receives a public IP address.
Consider the following when you set this value:
+ When you use `create-service` or `update-service`, the default is `DISABLED`.
+ When the service `deploymentController` is `ECS`, the value must be `DISABLED`.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroups`  <a name="cfn-ecs-taskset-awsvpcconfiguration-securitygroups"></a>
The IDs of the security groups associated with the task or service. If you don't specify a security group, the default security group for the VPC is used. There's a limit of 5 security groups that can be specified.
All specified security groups must be from the same VPC.
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Subnets`  <a name="cfn-ecs-taskset-awsvpcconfiguration-subnets"></a>
The IDs of the subnets associated with the task or service. There's a limit of 16 subnets that can be specified.
All specified subnets must be from the same VPC.
*Required*: Yes
*Type*: Array of String
*Maximum*: `16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
