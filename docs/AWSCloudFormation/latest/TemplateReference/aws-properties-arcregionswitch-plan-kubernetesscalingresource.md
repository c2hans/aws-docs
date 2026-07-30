---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-kubernetesscalingresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan KubernetesScalingResource
<a name="aws-properties-arcregionswitch-plan-kubernetesscalingresource"></a>

Defines a Kubernetes resource to scale in an Amazon EKS cluster.

## Syntax
<a name="aws-properties-arcregionswitch-plan-kubernetesscalingresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-kubernetesscalingresource-syntax.json"></a>

```
{
  "[HpaName](#cfn-arcregionswitch-plan-kubernetesscalingresource-hpaname)" : {{String}},
  "[Name](#cfn-arcregionswitch-plan-kubernetesscalingresource-name)" : {{String}},
  "[Namespace](#cfn-arcregionswitch-plan-kubernetesscalingresource-namespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-kubernetesscalingresource-syntax.yaml"></a>

```
  [HpaName](#cfn-arcregionswitch-plan-kubernetesscalingresource-hpaname): {{String}}
  [Name](#cfn-arcregionswitch-plan-kubernetesscalingresource-name): {{String}}
  [Namespace](#cfn-arcregionswitch-plan-kubernetesscalingresource-namespace): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-kubernetesscalingresource-properties"></a>

`HpaName`  <a name="cfn-arcregionswitch-plan-kubernetesscalingresource-hpaname"></a>
The hpaname for the Kubernetes resource.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-arcregionswitch-plan-kubernetesscalingresource-name"></a>
The name for the Kubernetes resource.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-arcregionswitch-plan-kubernetesscalingresource-namespace"></a>
The namespace for the Kubernetes resource.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
