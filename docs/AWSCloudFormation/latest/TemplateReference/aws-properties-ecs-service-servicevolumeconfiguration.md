---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-servicevolumeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service ServiceVolumeConfiguration
<a name="aws-properties-ecs-service-servicevolumeconfiguration"></a>

The configuration for a volume specified in the task definition as a volume that is configured at launch time. Currently, the only supported volume type is an Amazon EBS volume.

## Syntax
<a name="aws-properties-ecs-service-servicevolumeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-servicevolumeconfiguration-syntax.json"></a>

```
{
  "[ManagedEBSVolume](#cfn-ecs-service-servicevolumeconfiguration-managedebsvolume)" : {{ServiceManagedEBSVolumeConfiguration}},
  "[Name](#cfn-ecs-service-servicevolumeconfiguration-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-service-servicevolumeconfiguration-syntax.yaml"></a>

```
  [ManagedEBSVolume](#cfn-ecs-service-servicevolumeconfiguration-managedebsvolume): {{
    ServiceManagedEBSVolumeConfiguration}}
  [Name](#cfn-ecs-service-servicevolumeconfiguration-name): {{String}}
```

## Properties
<a name="aws-properties-ecs-service-servicevolumeconfiguration-properties"></a>

`ManagedEBSVolume`  <a name="cfn-ecs-service-servicevolumeconfiguration-managedebsvolume"></a>
The configuration for the Amazon EBS volume that Amazon ECS creates and manages on your behalf. These settings are used to create each Amazon EBS volume, with one volume created for each task in the service. The Amazon EBS volumes are visible in your account in the Amazon EC2 console once they are created.
*Required*: No
*Type*: [ServiceManagedEBSVolumeConfiguration](aws-properties-ecs-service-servicemanagedebsvolumeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ecs-service-servicevolumeconfiguration-name"></a>
The name of the volume. This value must match the volume name from the `Volume` object in the task definition.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
