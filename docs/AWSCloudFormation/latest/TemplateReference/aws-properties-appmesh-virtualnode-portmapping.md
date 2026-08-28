---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-portmapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode PortMapping
<a name="aws-properties-appmesh-virtualnode-portmapping"></a>

An object representing a virtual node or virtual router listener port mapping.

## Syntax
<a name="aws-properties-appmesh-virtualnode-portmapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-portmapping-syntax.json"></a>

```
{
  "[Port](#cfn-appmesh-virtualnode-portmapping-port)" : {{Integer}},
  "[Protocol](#cfn-appmesh-virtualnode-portmapping-protocol)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-portmapping-syntax.yaml"></a>

```
  [Port](#cfn-appmesh-virtualnode-portmapping-port): {{Integer}}
  [Protocol](#cfn-appmesh-virtualnode-portmapping-protocol): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-portmapping-properties"></a>

`Port`  <a name="cfn-appmesh-virtualnode-portmapping-port"></a>
The port used for the port mapping.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-appmesh-virtualnode-portmapping-protocol"></a>
The protocol used for the port mapping. Specify `http`, `http2`, `grpc`, or `tcp`.
*Required*: Yes
*Type*: String
*Allowed values*: `http | tcp | http2 | grpc`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
