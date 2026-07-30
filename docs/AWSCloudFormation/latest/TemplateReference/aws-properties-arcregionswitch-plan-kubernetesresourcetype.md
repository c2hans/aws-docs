---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-kubernetesresourcetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan KubernetesResourceType
<a name="aws-properties-arcregionswitch-plan-kubernetesresourcetype"></a>

Defines the type of Kubernetes resource to scale in an Amazon EKS cluster.

## Syntax
<a name="aws-properties-arcregionswitch-plan-kubernetesresourcetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-kubernetesresourcetype-syntax.json"></a>

```
{
  "[ApiVersion](#cfn-arcregionswitch-plan-kubernetesresourcetype-apiversion)" : {{String}},
  "[Kind](#cfn-arcregionswitch-plan-kubernetesresourcetype-kind)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-kubernetesresourcetype-syntax.yaml"></a>

```
  [ApiVersion](#cfn-arcregionswitch-plan-kubernetesresourcetype-apiversion): {{String}}
  [Kind](#cfn-arcregionswitch-plan-kubernetesresourcetype-kind): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-kubernetesresourcetype-properties"></a>

`ApiVersion`  <a name="cfn-arcregionswitch-plan-kubernetesresourcetype-apiversion"></a>
The API version type for the Kubernetes resource.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Kind`  <a name="cfn-arcregionswitch-plan-kubernetesresourcetype-kind"></a>
The kind for the Kubernetes resource.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
