---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-forcenewdeployment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service ForceNewDeployment
<a name="aws-properties-ecs-service-forcenewdeployment"></a>

Determines whether to force a new deployment of the service. By default, deployments aren't forced. You can use this option to start a new deployment with no service definition changes. For example, you can update a service's tasks to use a newer Docker image with the same image/tag combination (`my_image:latest`) or to roll Fargate tasks onto a newer platform version.

## Syntax
<a name="aws-properties-ecs-service-forcenewdeployment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-forcenewdeployment-syntax.json"></a>

```
{
  "[EnableForceNewDeployment](#cfn-ecs-service-forcenewdeployment-enableforcenewdeployment)" : {{Boolean}},
  "[ForceNewDeploymentNonce](#cfn-ecs-service-forcenewdeployment-forcenewdeploymentnonce)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-service-forcenewdeployment-syntax.yaml"></a>

```
  [EnableForceNewDeployment](#cfn-ecs-service-forcenewdeployment-enableforcenewdeployment): {{Boolean}}
  [ForceNewDeploymentNonce](#cfn-ecs-service-forcenewdeployment-forcenewdeploymentnonce): {{String}}
```

## Properties
<a name="aws-properties-ecs-service-forcenewdeployment-properties"></a>

`EnableForceNewDeployment`  <a name="cfn-ecs-service-forcenewdeployment-enableforcenewdeployment"></a>
Determines whether to force a new deployment of the service. By default, deployments aren't forced. You can use this option to start a new deployment with no service definition changes. For example, you can update a service's tasks to use a newer Docker image with the same image/tag combination (`my_image:latest`) or to roll Fargate tasks onto a newer platform version.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForceNewDeploymentNonce`  <a name="cfn-ecs-service-forcenewdeployment-forcenewdeploymentnonce"></a>
When you change the` ForceNewDeploymentNonce` value in your template, it signals Amazon ECS to start a new deployment even though no other service parameters have changed. The value must be a unique, time- varying value like a timestamp, random string, or sequence number. Use this property when you want to ensure your tasks pick up the latest version of a Docker image that uses the same tag but has been updated in the registry.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
