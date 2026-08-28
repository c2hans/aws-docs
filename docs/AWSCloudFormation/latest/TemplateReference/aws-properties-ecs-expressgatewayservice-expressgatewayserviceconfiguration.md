---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-expressgatewayserviceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ExpressGatewayService ExpressGatewayServiceConfiguration
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayserviceconfiguration"></a>

Represents a specific configuration revision of an Express service, containing all the settings and parameters for that revision.

## Syntax
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayserviceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayserviceconfiguration-syntax.json"></a>

```
{
  "[Cpu](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-cpu)" : {{String}},
  "[CreatedAt](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-createdat)" : {{String}},
  "[ExecutionRoleArn](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-executionrolearn)" : {{String}},
  "[HealthCheckPath](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-healthcheckpath)" : {{String}},
  "[IngressPaths](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-ingresspaths)" : {{[ IngressPathSummary, ... ]}},
  "[Memory](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-memory)" : {{String}},
  "[NetworkConfiguration](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-networkconfiguration)" : {{ExpressGatewayServiceNetworkConfiguration}},
  "[PrimaryContainer](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-primarycontainer)" : {{ExpressGatewayContainer}},
  "[ScalingTarget](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-scalingtarget)" : {{ExpressGatewayScalingTarget}},
  "[ServiceRevisionArn](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-servicerevisionarn)" : {{String}},
  "[TaskDefinitionArn](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-taskdefinitionarn)" : {{String}},
  "[TaskRoleArn](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-taskrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayserviceconfiguration-syntax.yaml"></a>

```
  [Cpu](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-cpu): {{String}}
  [CreatedAt](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-createdat): {{String}}
  [ExecutionRoleArn](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-executionrolearn): {{String}}
  [HealthCheckPath](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-healthcheckpath): {{String}}
  [IngressPaths](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-ingresspaths): {{
    - IngressPathSummary}}
  [Memory](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-memory): {{String}}
  [NetworkConfiguration](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-networkconfiguration): {{
    ExpressGatewayServiceNetworkConfiguration}}
  [PrimaryContainer](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-primarycontainer): {{
    ExpressGatewayContainer}}
  [ScalingTarget](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-scalingtarget): {{
    ExpressGatewayScalingTarget}}
  [ServiceRevisionArn](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-servicerevisionarn): {{String}}
  [TaskDefinitionArn](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-taskdefinitionarn): {{String}}
  [TaskRoleArn](#cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-taskrolearn): {{String}}
```

## Properties
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayserviceconfiguration-properties"></a>

`Cpu`  <a name="cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-cpu"></a>
The CPU allocation for tasks in this service revision.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreatedAt`  <a name="cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-createdat"></a>
The Unix timestamp for when this service revision was created.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleArn`  <a name="cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-executionrolearn"></a>
The ARN of the task execution role for the service revision.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheckPath`  <a name="cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-healthcheckpath"></a>
The health check path for this service revision.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IngressPaths`  <a name="cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-ingresspaths"></a>
The entry point into this service revision.
*Required*: No
*Type*: Array of [IngressPathSummary](aws-properties-ecs-expressgatewayservice-ingresspathsummary.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Memory`  <a name="cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-memory"></a>
The memory allocation for tasks in this service revision.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkConfiguration`  <a name="cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-networkconfiguration"></a>
The network configuration for tasks in this service revision.
*Required*: No
*Type*: [ExpressGatewayServiceNetworkConfiguration](aws-properties-ecs-expressgatewayservice-expressgatewayservicenetworkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryContainer`  <a name="cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-primarycontainer"></a>
The primary container configuration for this service revision.
*Required*: No
*Type*: [ExpressGatewayContainer](aws-properties-ecs-expressgatewayservice-expressgatewaycontainer.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingTarget`  <a name="cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-scalingtarget"></a>
The auto-scaling configuration for this service revision.
*Required*: No
*Type*: [ExpressGatewayScalingTarget](aws-properties-ecs-expressgatewayservice-expressgatewayscalingtarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceRevisionArn`  <a name="cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-servicerevisionarn"></a>
The ARN of the service revision.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskDefinitionArn`  <a name="cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-taskdefinitionarn"></a>
The ARN of the task definition used by this service revision. This is present for all Express services and reflects the task definition in use, whether managed by Amazon ECS or provided by the customer.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskRoleArn`  <a name="cfn-ecs-expressgatewayservice-expressgatewayserviceconfiguration-taskrolearn"></a>
The ARN of the task role for the service revision.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
