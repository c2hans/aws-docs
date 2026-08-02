---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-awsvpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service AwsVpcConfiguration
<a name="aws-properties-ecs-service-awsvpcconfiguration"></a>

An object representing the networking details for a task or service. For example `awsVpcConfiguration={subnets=["subnet-12344321"],securityGroups=["sg-12344321"]}`.

## Syntax
<a name="aws-properties-ecs-service-awsvpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-awsvpcconfiguration-syntax.json"></a>

```
{
  "[AssignPublicIp](#cfn-ecs-service-awsvpcconfiguration-assignpublicip)" : {{String}},
  "[SecurityGroups](#cfn-ecs-service-awsvpcconfiguration-securitygroups)" : {{[ String, ... ]}},
  "[Subnets](#cfn-ecs-service-awsvpcconfiguration-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ecs-service-awsvpcconfiguration-syntax.yaml"></a>

```
  [AssignPublicIp](#cfn-ecs-service-awsvpcconfiguration-assignpublicip): {{String}}
  [SecurityGroups](#cfn-ecs-service-awsvpcconfiguration-securitygroups): {{
    - String}}
  [Subnets](#cfn-ecs-service-awsvpcconfiguration-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-ecs-service-awsvpcconfiguration-properties"></a>

`AssignPublicIp`  <a name="cfn-ecs-service-awsvpcconfiguration-assignpublicip"></a>
Whether the task's elastic network interface receives a public IP address.
Consider the following when you set this value:
+ When you use `create-service` or `update-service`, the default is `DISABLED`.
+ When the service `deploymentController` is `ECS`, the value must be `DISABLED`.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroups`  <a name="cfn-ecs-service-awsvpcconfiguration-securitygroups"></a>
The IDs of the security groups associated with the task or service. If you don't specify a security group, the default security group for the VPC is used. There's a limit of 5 security groups that can be specified.
All specified security groups must be from the same VPC.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subnets`  <a name="cfn-ecs-service-awsvpcconfiguration-subnets"></a>
The IDs of the subnets associated with the task or service. There's a limit of 16 subnets that can be specified.
All specified subnets must be from the same VPC.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ecs-service-awsvpcconfiguration--seealso"></a>
+  [Creating a cluster capacity provider association using an Auto Scaling group capacity provider](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-clustercapacityproviderassociations.html#aws-resource-ecs-clustercapacityproviderassociations--examples--Creating_a_cluster_capacity_provider_association_using_an_Auto_Scaling_group_capacity_provider.)
