---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-clustercapacityproviderassociations.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ClusterCapacityProviderAssociations
<a name="aws-resource-ecs-clustercapacityproviderassociations"></a>

The `AWS::ECS::ClusterCapacityProviderAssociations` resource associates one or more capacity providers and a default capacity provider strategy with a cluster.

## Syntax
<a name="aws-resource-ecs-clustercapacityproviderassociations-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ecs-clustercapacityproviderassociations-syntax.json"></a>

```
{
  "Type" : "AWS::ECS::ClusterCapacityProviderAssociations",
  "Properties" : {
      "[CapacityProviders](#cfn-ecs-clustercapacityproviderassociations-capacityproviders)" : {{[ String, ... ]}},
      "[Cluster](#cfn-ecs-clustercapacityproviderassociations-cluster)" : {{String}},
      "[DefaultCapacityProviderStrategy](#cfn-ecs-clustercapacityproviderassociations-defaultcapacityproviderstrategy)" : {{[ CapacityProviderStrategy, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ecs-clustercapacityproviderassociations-syntax.yaml"></a>

```
Type: AWS::ECS::ClusterCapacityProviderAssociations
Properties:
  [CapacityProviders](#cfn-ecs-clustercapacityproviderassociations-capacityproviders): {{
    - String}}
  [Cluster](#cfn-ecs-clustercapacityproviderassociations-cluster): {{String}}
  [DefaultCapacityProviderStrategy](#cfn-ecs-clustercapacityproviderassociations-defaultcapacityproviderstrategy): {{
    - CapacityProviderStrategy}}
```

## Properties
<a name="aws-resource-ecs-clustercapacityproviderassociations-properties"></a>

`CapacityProviders`  <a name="cfn-ecs-clustercapacityproviderassociations-capacityproviders"></a>
The capacity providers to associate with the cluster.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Cluster`  <a name="cfn-ecs-clustercapacityproviderassociations-cluster"></a>
The cluster the capacity provider association is the target of.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefaultCapacityProviderStrategy`  <a name="cfn-ecs-clustercapacityproviderassociations-defaultcapacityproviderstrategy"></a>
The default capacity provider strategy to associate with the cluster.
*Required*: Yes
*Type*: Array of [CapacityProviderStrategy](aws-properties-ecs-clustercapacityproviderassociations-capacityproviderstrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ecs-clustercapacityproviderassociations-return-values"></a>

### Ref
<a name="aws-resource-ecs-clustercapacityproviderassociations-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the cluster name.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
