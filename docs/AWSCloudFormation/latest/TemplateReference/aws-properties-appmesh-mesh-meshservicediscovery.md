---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-mesh-meshservicediscovery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::Mesh MeshServiceDiscovery
<a name="aws-properties-appmesh-mesh-meshservicediscovery"></a>

An object that represents the service discovery information for a service mesh.

## Syntax
<a name="aws-properties-appmesh-mesh-meshservicediscovery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-mesh-meshservicediscovery-syntax.json"></a>

```
{
  "[IpPreference](#cfn-appmesh-mesh-meshservicediscovery-ippreference)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-mesh-meshservicediscovery-syntax.yaml"></a>

```
  [IpPreference](#cfn-appmesh-mesh-meshservicediscovery-ippreference): {{String}}
```

## Properties
<a name="aws-properties-appmesh-mesh-meshservicediscovery-properties"></a>

`IpPreference`  <a name="cfn-appmesh-mesh-meshservicediscovery-ippreference"></a>
The IP version to use to control traffic within the mesh.
*Required*: No
*Type*: String
*Allowed values*: `IPv6_PREFERRED | IPv4_PREFERRED | IPv4_ONLY | IPv6_ONLY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
