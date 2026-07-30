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
