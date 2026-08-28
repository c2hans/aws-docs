---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-expressgatewayservicenetworkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ExpressGatewayService ExpressGatewayServiceNetworkConfiguration
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayservicenetworkconfiguration"></a>

The network configuration for an Express service. By default, an Express service utilizes subnets and security groups associated with the default VPC.

## Syntax
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayservicenetworkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayservicenetworkconfiguration-syntax.json"></a>

```
{
  "[SecurityGroups](#cfn-ecs-expressgatewayservice-expressgatewayservicenetworkconfiguration-securitygroups)" : {{[ String, ... ]}},
  "[Subnets](#cfn-ecs-expressgatewayservice-expressgatewayservicenetworkconfiguration-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayservicenetworkconfiguration-syntax.yaml"></a>

```
  [SecurityGroups](#cfn-ecs-expressgatewayservice-expressgatewayservicenetworkconfiguration-securitygroups): {{
    - String}}
  [Subnets](#cfn-ecs-expressgatewayservice-expressgatewayservicenetworkconfiguration-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-ecs-expressgatewayservice-expressgatewayservicenetworkconfiguration-properties"></a>

`SecurityGroups`  <a name="cfn-ecs-expressgatewayservice-expressgatewayservicenetworkconfiguration-securitygroups"></a>
The IDs of the security groups associated with the Express service.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subnets`  <a name="cfn-ecs-expressgatewayservice-expressgatewayservicenetworkconfiguration-subnets"></a>
The IDs of the subnets associated with the Express service.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
