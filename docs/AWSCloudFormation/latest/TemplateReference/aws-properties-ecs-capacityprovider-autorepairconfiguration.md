---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-autorepairconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider AutoRepairConfiguration
<a name="aws-properties-ecs-capacityprovider-autorepairconfiguration"></a>

The auto repair configuration for an Amazon ECS Managed Instances capacity provider. When enabled, Amazon ECS automatically replaces container instances that are detected as unhealthy based on container instance health checks, including accelerated compute device and daemon health checks.

## Syntax
<a name="aws-properties-ecs-capacityprovider-autorepairconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-autorepairconfiguration-syntax.json"></a>

```
{
  "[ActionsStatus](#cfn-ecs-capacityprovider-autorepairconfiguration-actionsstatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-autorepairconfiguration-syntax.yaml"></a>

```
  [ActionsStatus](#cfn-ecs-capacityprovider-autorepairconfiguration-actionsstatus): {{String}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-autorepairconfiguration-properties"></a>

`ActionsStatus`  <a name="cfn-ecs-capacityprovider-autorepairconfiguration-actionsstatus"></a>
The status of auto repair actions for the capacity provider. When set to `ENABLED`, Amazon ECS automatically replaces container instances with an `IMPAIRED` health status. When set to `DISABLED`, Amazon ECS still monitors container instance health but does not automatically replace impaired instances.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
