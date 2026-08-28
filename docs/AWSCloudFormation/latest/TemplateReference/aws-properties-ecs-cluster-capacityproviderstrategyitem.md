---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-cluster-capacityproviderstrategyitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Cluster CapacityProviderStrategyItem
<a name="aws-properties-ecs-cluster-capacityproviderstrategyitem"></a>

The `CapacityProviderStrategyItem` property specifies the details of the default capacity provider strategy for the cluster. When services or tasks are run in the cluster with no launch type or capacity provider strategy specified, the default capacity provider strategy is used.

## Syntax
<a name="aws-properties-ecs-cluster-capacityproviderstrategyitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-cluster-capacityproviderstrategyitem-syntax.json"></a>

```
{
  "[Base](#cfn-ecs-cluster-capacityproviderstrategyitem-base)" : {{Integer}},
  "[CapacityProvider](#cfn-ecs-cluster-capacityproviderstrategyitem-capacityprovider)" : {{String}},
  "[Weight](#cfn-ecs-cluster-capacityproviderstrategyitem-weight)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-cluster-capacityproviderstrategyitem-syntax.yaml"></a>

```
  [Base](#cfn-ecs-cluster-capacityproviderstrategyitem-base): {{Integer}}
  [CapacityProvider](#cfn-ecs-cluster-capacityproviderstrategyitem-capacityprovider): {{String}}
  [Weight](#cfn-ecs-cluster-capacityproviderstrategyitem-weight): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-cluster-capacityproviderstrategyitem-properties"></a>

`Base`  <a name="cfn-ecs-cluster-capacityproviderstrategyitem-base"></a>
The *base* value designates how many tasks, at a minimum, to run on the specified capacity provider for each service. Only one capacity provider in a capacity provider strategy can have a *base* defined. If no value is specified, the default value of `0` is used.
Base value characteristics:
+ Only one capacity provider in a strategy can have a base defined
+ The default value is `0` if not specified
+ The valid range is 0 to 100,000
+ Base requirements are satisfied first before weight distribution
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapacityProvider`  <a name="cfn-ecs-cluster-capacityproviderstrategyitem-capacityprovider"></a>
The short name of the capacity provider. This can be either an AWS managed capacity provider (`FARGATE` or `FARGATE_SPOT`) or the name of a custom capacity provider that you created.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-ecs-cluster-capacityproviderstrategyitem-weight"></a>
The *weight* value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider. The `weight` value is taken into consideration after the `base` value, if defined, is satisfied.
If no `weight` value is specified, the default value of `0` is used. When multiple capacity providers are specified within a capacity provider strategy, at least one of the capacity providers must have a weight value greater than zero and any capacity providers with a weight of `0` can't be used to place tasks. If you specify multiple capacity providers in a strategy that all have a weight of `0`, any `RunTask` or `CreateService` actions using the capacity provider strategy will fail.
Weight value characteristics:
+ Weight is considered after the base value is satisfied
+ The default value is `0` if not specified
+ The valid range is 0 to 1,000
+ At least one capacity provider must have a weight greater than zero
+ Capacity providers with weight of `0` cannot place tasks
Task distribution logic:

1. Base satisfaction: The minimum number of tasks specified by the base value are placed on that capacity provider

1. Weight distribution: After base requirements are met, additional tasks are distributed according to weight ratios
Examples:
Equal Distribution: Two capacity providers both with weight `1` will split tasks evenly after base requirements are met.
Weighted Distribution: If capacityProviderA has weight `1` and capacityProviderB has weight `4`, then for every 1 task on A, 4 tasks will run on B.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ecs-cluster-capacityproviderstrategyitem--seealso"></a>
+  [ Define a cluster with the AWS Fargate capacity providers and a default capacity provider strategy defined](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#aws-resource-ecs-cluster--examples--Define_a_cluster_with_the__capacity_providers_and_a_default_capacity_provider_strategy_defined)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
