---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-backend.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode Backend
<a name="aws-properties-appmesh-virtualnode-backend"></a>

An object that represents the backends that a virtual node is expected to send outbound traffic to.

## Syntax
<a name="aws-properties-appmesh-virtualnode-backend-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-backend-syntax.json"></a>

```
{
  "[VirtualService](#cfn-appmesh-virtualnode-backend-virtualservice)" : {{VirtualServiceBackend}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-backend-syntax.yaml"></a>

```
  [VirtualService](#cfn-appmesh-virtualnode-backend-virtualservice): {{
    VirtualServiceBackend}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-backend-properties"></a>

`VirtualService`  <a name="cfn-appmesh-virtualnode-backend-virtualservice"></a>
Specifies a virtual service to use as a backend.
*Required*: No
*Type*: [VirtualServiceBackend](aws-properties-appmesh-virtualnode-virtualservicebackend.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
