---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-managedinstancesnetworkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider ManagedInstancesNetworkConfiguration
<a name="aws-properties-ecs-capacityprovider-managedinstancesnetworkconfiguration"></a>

The network configuration for Amazon ECS Managed Instances. This specifies the VPC subnets and security groups that instances use for network connectivity. Amazon ECS Managed Instances support multiple network modes including `awsvpc` (instances receive ENIs for task isolation), `host` (instances share network namespace with tasks), and `none` (no external network connectivity), ensuring backward compatibility for migrating workloads from Fargate or Amazon EC2.

## Syntax
<a name="aws-properties-ecs-capacityprovider-managedinstancesnetworkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-managedinstancesnetworkconfiguration-syntax.json"></a>

```
{
  "[SecurityGroups](#cfn-ecs-capacityprovider-managedinstancesnetworkconfiguration-securitygroups)" : {{[ String, ... ]}},
  "[Subnets](#cfn-ecs-capacityprovider-managedinstancesnetworkconfiguration-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-managedinstancesnetworkconfiguration-syntax.yaml"></a>

```
  [SecurityGroups](#cfn-ecs-capacityprovider-managedinstancesnetworkconfiguration-securitygroups): {{
    - String}}
  [Subnets](#cfn-ecs-capacityprovider-managedinstancesnetworkconfiguration-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-managedinstancesnetworkconfiguration-properties"></a>

`SecurityGroups`  <a name="cfn-ecs-capacityprovider-managedinstancesnetworkconfiguration-securitygroups"></a>
The list of security group IDs to apply to Amazon ECS Managed Instances. These security groups control the network traffic allowed to and from the instances.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subnets`  <a name="cfn-ecs-capacityprovider-managedinstancesnetworkconfiguration-subnets"></a>
The list of subnet IDs where Amazon ECS can launch Amazon ECS Managed Instances. Instances are distributed across the specified subnets for high availability. All subnets must be in the same VPC.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
