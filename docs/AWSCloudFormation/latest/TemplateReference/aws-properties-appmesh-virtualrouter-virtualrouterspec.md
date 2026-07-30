---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualrouter-virtualrouterspec.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualRouter VirtualRouterSpec
<a name="aws-properties-appmesh-virtualrouter-virtualrouterspec"></a>

An object that represents the specification of a virtual router.

## Syntax
<a name="aws-properties-appmesh-virtualrouter-virtualrouterspec-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualrouter-virtualrouterspec-syntax.json"></a>

```
{
  "[Listeners](#cfn-appmesh-virtualrouter-virtualrouterspec-listeners)" : {{[ VirtualRouterListener, ... ]}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualrouter-virtualrouterspec-syntax.yaml"></a>

```
  [Listeners](#cfn-appmesh-virtualrouter-virtualrouterspec-listeners): {{
    - VirtualRouterListener}}
```

## Properties
<a name="aws-properties-appmesh-virtualrouter-virtualrouterspec-properties"></a>

`Listeners`  <a name="cfn-appmesh-virtualrouter-virtualrouterspec-listeners"></a>
The listeners that the virtual router is expected to receive inbound traffic from.
*Required*: Yes
*Type*: Array of [VirtualRouterListener](aws-properties-appmesh-virtualrouter-virtualrouterlistener.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
