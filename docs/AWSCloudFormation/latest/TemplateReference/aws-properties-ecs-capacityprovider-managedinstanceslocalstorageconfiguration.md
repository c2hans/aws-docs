---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-managedinstanceslocalstorageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider ManagedInstancesLocalStorageConfiguration
<a name="aws-properties-ecs-capacityprovider-managedinstanceslocalstorageconfiguration"></a>

The local storage configuration for Amazon ECS Managed Instances. This defines how ECS uses and configures instance store volumes available on container instance.

## Syntax
<a name="aws-properties-ecs-capacityprovider-managedinstanceslocalstorageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-managedinstanceslocalstorageconfiguration-syntax.json"></a>

```
{
  "[UseLocalStorage](#cfn-ecs-capacityprovider-managedinstanceslocalstorageconfiguration-uselocalstorage)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-managedinstanceslocalstorageconfiguration-syntax.yaml"></a>

```
  [UseLocalStorage](#cfn-ecs-capacityprovider-managedinstanceslocalstorageconfiguration-uselocalstorage): {{Boolean}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-managedinstanceslocalstorageconfiguration-properties"></a>

`UseLocalStorage`  <a name="cfn-ecs-capacityprovider-managedinstanceslocalstorageconfiguration-uselocalstorage"></a>
Use instance store volumes for data storage when available. EBS volumes are not provisioned for data storage. If the container instance has multiple instance store volumes, a single data volume is created. Consider defining instance store requirements using the `localStorage`, `localStorageTypes` and `totalLocalStorageGB` properties.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
