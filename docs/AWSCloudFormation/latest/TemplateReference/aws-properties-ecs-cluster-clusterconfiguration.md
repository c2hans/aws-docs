---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-cluster-clusterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Cluster ClusterConfiguration
<a name="aws-properties-ecs-cluster-clusterconfiguration"></a>

The execute command and managed storage configuration for the cluster.

## Syntax
<a name="aws-properties-ecs-cluster-clusterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-cluster-clusterconfiguration-syntax.json"></a>

```
{
  "[ExecuteCommandConfiguration](#cfn-ecs-cluster-clusterconfiguration-executecommandconfiguration)" : {{ExecuteCommandConfiguration}},
  "[ManagedStorageConfiguration](#cfn-ecs-cluster-clusterconfiguration-managedstorageconfiguration)" : {{ManagedStorageConfiguration}}
}
```

### YAML
<a name="aws-properties-ecs-cluster-clusterconfiguration-syntax.yaml"></a>

```
  [ExecuteCommandConfiguration](#cfn-ecs-cluster-clusterconfiguration-executecommandconfiguration): {{
    ExecuteCommandConfiguration}}
  [ManagedStorageConfiguration](#cfn-ecs-cluster-clusterconfiguration-managedstorageconfiguration): {{
    ManagedStorageConfiguration}}
```

## Properties
<a name="aws-properties-ecs-cluster-clusterconfiguration-properties"></a>

`ExecuteCommandConfiguration`  <a name="cfn-ecs-cluster-clusterconfiguration-executecommandconfiguration"></a>
The details of the execute command configuration.
*Required*: No
*Type*: [ExecuteCommandConfiguration](aws-properties-ecs-cluster-executecommandconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedStorageConfiguration`  <a name="cfn-ecs-cluster-clusterconfiguration-managedstorageconfiguration"></a>
The details of the managed storage configuration.
*Required*: No
*Type*: [ManagedStorageConfiguration](aws-properties-ecs-cluster-managedstorageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ecs-cluster-clusterconfiguration--seealso"></a>
+  [ Define a cluster with the AWS Fargate capacity providers and a default capacity provider strategy defined](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#aws-resource-ecs-cluster--examples--Define_a_cluster_with_the__capacity_providers_and_a_default_capacity_provider_strategy_defined)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
