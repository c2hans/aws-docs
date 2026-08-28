---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualservice-virtualserviceprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualService VirtualServiceProvider
<a name="aws-properties-appmesh-virtualservice-virtualserviceprovider"></a>

An object that represents the provider for a virtual service.

## Syntax
<a name="aws-properties-appmesh-virtualservice-virtualserviceprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualservice-virtualserviceprovider-syntax.json"></a>

```
{
  "[VirtualNode](#cfn-appmesh-virtualservice-virtualserviceprovider-virtualnode)" : {{VirtualNodeServiceProvider}},
  "[VirtualRouter](#cfn-appmesh-virtualservice-virtualserviceprovider-virtualrouter)" : {{VirtualRouterServiceProvider}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualservice-virtualserviceprovider-syntax.yaml"></a>

```
  [VirtualNode](#cfn-appmesh-virtualservice-virtualserviceprovider-virtualnode): {{
    VirtualNodeServiceProvider}}
  [VirtualRouter](#cfn-appmesh-virtualservice-virtualserviceprovider-virtualrouter): {{
    VirtualRouterServiceProvider}}
```

## Properties
<a name="aws-properties-appmesh-virtualservice-virtualserviceprovider-properties"></a>

`VirtualNode`  <a name="cfn-appmesh-virtualservice-virtualserviceprovider-virtualnode"></a>
The virtual node associated with a virtual service.
*Required*: No
*Type*: [VirtualNodeServiceProvider](aws-properties-appmesh-virtualservice-virtualnodeserviceprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VirtualRouter`  <a name="cfn-appmesh-virtualservice-virtualserviceprovider-virtualrouter"></a>
The virtual router associated with a virtual service.
*Required*: No
*Type*: [VirtualRouterServiceProvider](aws-properties-appmesh-virtualservice-virtualrouterserviceprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
