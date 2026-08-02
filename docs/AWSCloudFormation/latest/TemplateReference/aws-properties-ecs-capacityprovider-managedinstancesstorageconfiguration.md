---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-managedinstancesstorageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider ManagedInstancesStorageConfiguration
<a name="aws-properties-ecs-capacityprovider-managedinstancesstorageconfiguration"></a>

The storage configuration for Amazon ECS Managed Instances. This defines the data volume configuration for the instances.

## Syntax
<a name="aws-properties-ecs-capacityprovider-managedinstancesstorageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-managedinstancesstorageconfiguration-syntax.json"></a>

```
{
  "[StorageSizeGiB](#cfn-ecs-capacityprovider-managedinstancesstorageconfiguration-storagesizegib)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-managedinstancesstorageconfiguration-syntax.yaml"></a>

```
  [StorageSizeGiB](#cfn-ecs-capacityprovider-managedinstancesstorageconfiguration-storagesizegib): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-managedinstancesstorageconfiguration-properties"></a>

`StorageSizeGiB`  <a name="cfn-ecs-capacityprovider-managedinstancesstorageconfiguration-storagesizegib"></a>
The size of the data volume.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
