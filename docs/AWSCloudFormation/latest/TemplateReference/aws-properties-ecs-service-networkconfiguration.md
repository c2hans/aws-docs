---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-networkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service NetworkConfiguration
<a name="aws-properties-ecs-service-networkconfiguration"></a>

The network configuration for a task or service.

## Syntax
<a name="aws-properties-ecs-service-networkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-networkconfiguration-syntax.json"></a>

```
{
  "[AwsvpcConfiguration](#cfn-ecs-service-networkconfiguration-awsvpcconfiguration)" : {{AwsVpcConfiguration}}
}
```

### YAML
<a name="aws-properties-ecs-service-networkconfiguration-syntax.yaml"></a>

```
  [AwsvpcConfiguration](#cfn-ecs-service-networkconfiguration-awsvpcconfiguration): {{
    AwsVpcConfiguration}}
```

## Properties
<a name="aws-properties-ecs-service-networkconfiguration-properties"></a>

`AwsvpcConfiguration`  <a name="cfn-ecs-service-networkconfiguration-awsvpcconfiguration"></a>
The VPC subnets and security groups that are associated with a task.
All specified subnets and security groups must be from the same VPC.
*Required*: No
*Type*: [AwsVpcConfiguration](aws-properties-ecs-service-awsvpcconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ecs-service-networkconfiguration--seealso"></a>
+  [Associate an Application Load Balancer with a service](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#aws-resource-ecs-service--examples--Associate_an_Application_Load_Balancer_with_a_service)
