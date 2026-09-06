---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-mesh-meshspec.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::Mesh MeshSpec
<a name="aws-properties-appmesh-mesh-meshspec"></a>

An object that represents the specification of a service mesh.

## Syntax
<a name="aws-properties-appmesh-mesh-meshspec-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-mesh-meshspec-syntax.json"></a>

```
{
  "[EgressFilter](#cfn-appmesh-mesh-meshspec-egressfilter)" : {{EgressFilter}},
  "[ServiceDiscovery](#cfn-appmesh-mesh-meshspec-servicediscovery)" : {{MeshServiceDiscovery}}
}
```

### YAML
<a name="aws-properties-appmesh-mesh-meshspec-syntax.yaml"></a>

```
  [EgressFilter](#cfn-appmesh-mesh-meshspec-egressfilter): {{
    EgressFilter}}
  [ServiceDiscovery](#cfn-appmesh-mesh-meshspec-servicediscovery): {{
    MeshServiceDiscovery}}
```

## Properties
<a name="aws-properties-appmesh-mesh-meshspec-properties"></a>

`EgressFilter`  <a name="cfn-appmesh-mesh-meshspec-egressfilter"></a>
The egress filter rules for the service mesh.
*Required*: No
*Type*: [EgressFilter](aws-properties-appmesh-mesh-egressfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceDiscovery`  <a name="cfn-appmesh-mesh-meshspec-servicediscovery"></a>
An object that represents the service discovery information for a service mesh.
*Required*: No
*Type*: [MeshServiceDiscovery](aws-properties-appmesh-mesh-meshservicediscovery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
