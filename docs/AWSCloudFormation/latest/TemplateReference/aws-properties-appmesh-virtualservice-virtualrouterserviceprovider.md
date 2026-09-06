---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualservice-virtualrouterserviceprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualService VirtualRouterServiceProvider
<a name="aws-properties-appmesh-virtualservice-virtualrouterserviceprovider"></a>

An object that represents a virtual node service provider.

## Syntax
<a name="aws-properties-appmesh-virtualservice-virtualrouterserviceprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualservice-virtualrouterserviceprovider-syntax.json"></a>

```
{
  "[VirtualRouterName](#cfn-appmesh-virtualservice-virtualrouterserviceprovider-virtualroutername)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualservice-virtualrouterserviceprovider-syntax.yaml"></a>

```
  [VirtualRouterName](#cfn-appmesh-virtualservice-virtualrouterserviceprovider-virtualroutername): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualservice-virtualrouterserviceprovider-properties"></a>

`VirtualRouterName`  <a name="cfn-appmesh-virtualservice-virtualrouterserviceprovider-virtualroutername"></a>
The name of the virtual router that is acting as a service provider.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
