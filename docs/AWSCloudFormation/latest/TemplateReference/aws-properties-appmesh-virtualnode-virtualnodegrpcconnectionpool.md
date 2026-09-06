---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-virtualnodegrpcconnectionpool.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode VirtualNodeGrpcConnectionPool
<a name="aws-properties-appmesh-virtualnode-virtualnodegrpcconnectionpool"></a>

An object that represents a type of connection pool.

## Syntax
<a name="aws-properties-appmesh-virtualnode-virtualnodegrpcconnectionpool-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-virtualnodegrpcconnectionpool-syntax.json"></a>

```
{
  "[MaxRequests](#cfn-appmesh-virtualnode-virtualnodegrpcconnectionpool-maxrequests)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-virtualnodegrpcconnectionpool-syntax.yaml"></a>

```
  [MaxRequests](#cfn-appmesh-virtualnode-virtualnodegrpcconnectionpool-maxrequests): {{Integer}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-virtualnodegrpcconnectionpool-properties"></a>

`MaxRequests`  <a name="cfn-appmesh-virtualnode-virtualnodegrpcconnectionpool-maxrequests"></a>
Maximum number of inflight requests Envoy can concurrently support across hosts in upstream cluster.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
