---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualservice-virtualservicespec.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualService VirtualServiceSpec
<a name="aws-properties-appmesh-virtualservice-virtualservicespec"></a>

An object that represents the specification of a virtual service.

## Syntax
<a name="aws-properties-appmesh-virtualservice-virtualservicespec-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualservice-virtualservicespec-syntax.json"></a>

```
{
  "[Provider](#cfn-appmesh-virtualservice-virtualservicespec-provider)" : {{VirtualServiceProvider}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualservice-virtualservicespec-syntax.yaml"></a>

```
  [Provider](#cfn-appmesh-virtualservice-virtualservicespec-provider): {{
    VirtualServiceProvider}}
```

## Properties
<a name="aws-properties-appmesh-virtualservice-virtualservicespec-properties"></a>

`Provider`  <a name="cfn-appmesh-virtualservice-virtualservicespec-provider"></a>
The App Mesh object that is acting as the provider for a virtual service. You can specify a single virtual node or virtual router.
*Required*: No
*Type*: [VirtualServiceProvider](aws-properties-appmesh-virtualservice-virtualserviceprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
