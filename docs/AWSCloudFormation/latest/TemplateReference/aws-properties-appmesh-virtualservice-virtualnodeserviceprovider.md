---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualservice-virtualnodeserviceprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualService VirtualNodeServiceProvider
<a name="aws-properties-appmesh-virtualservice-virtualnodeserviceprovider"></a>

An object that represents a virtual node service provider.

## Syntax
<a name="aws-properties-appmesh-virtualservice-virtualnodeserviceprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualservice-virtualnodeserviceprovider-syntax.json"></a>

```
{
  "[VirtualNodeName](#cfn-appmesh-virtualservice-virtualnodeserviceprovider-virtualnodename)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualservice-virtualnodeserviceprovider-syntax.yaml"></a>

```
  [VirtualNodeName](#cfn-appmesh-virtualservice-virtualnodeserviceprovider-virtualnodename): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualservice-virtualnodeserviceprovider-properties"></a>

`VirtualNodeName`  <a name="cfn-appmesh-virtualservice-virtualnodeserviceprovider-virtualnodename"></a>
The name of the virtual node that is acting as a service provider.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
