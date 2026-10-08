---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-mesh-egressfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::Mesh EgressFilter
<a name="aws-properties-appmesh-mesh-egressfilter"></a>

An object that represents the egress filter rules for a service mesh.

## Syntax
<a name="aws-properties-appmesh-mesh-egressfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-mesh-egressfilter-syntax.json"></a>

```
{
  "[Type](#cfn-appmesh-mesh-egressfilter-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-mesh-egressfilter-syntax.yaml"></a>

```
  [Type](#cfn-appmesh-mesh-egressfilter-type): {{String}}
```

## Properties
<a name="aws-properties-appmesh-mesh-egressfilter-properties"></a>

`Type`  <a name="cfn-appmesh-mesh-egressfilter-type"></a>
The egress filter type. By default, the type is `DROP_ALL`, which allows egress only from virtual nodes to other defined resources in the service mesh (and any traffic to `*.amazonaws.com` for AWS API calls). You can set the egress filter type to `ALLOW_ALL` to allow egress to any endpoint inside or outside of the service mesh.
When using `DROP_ALL`, the egress filter is a traffic-routing control, not a security boundary. The `*.amazonaws.com` allowance is based on the TLS Server Name Indication (SNI) that the client presents, and isn't verified against the destination IP address. To restrict the destinations that your workloads can reach, use security groups or network ACLs.
If you specify any backends on a virtual node when using `ALLOW_ALL`, you must specifiy all egress for that virtual node as backends. Otherwise, `ALLOW_ALL` will no longer work for that virtual node.
*Required*: Yes
*Type*: String
*Allowed values*: `ALLOW_ALL | DROP_ALL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
