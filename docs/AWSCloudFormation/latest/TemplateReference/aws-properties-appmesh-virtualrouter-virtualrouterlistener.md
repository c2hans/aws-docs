---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualrouter-virtualrouterlistener.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualRouter VirtualRouterListener
<a name="aws-properties-appmesh-virtualrouter-virtualrouterlistener"></a>

An object that represents a virtual router listener.

## Syntax
<a name="aws-properties-appmesh-virtualrouter-virtualrouterlistener-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualrouter-virtualrouterlistener-syntax.json"></a>

```
{
  "[PortMapping](#cfn-appmesh-virtualrouter-virtualrouterlistener-portmapping)" : {{PortMapping}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualrouter-virtualrouterlistener-syntax.yaml"></a>

```
  [PortMapping](#cfn-appmesh-virtualrouter-virtualrouterlistener-portmapping): {{
    PortMapping}}
```

## Properties
<a name="aws-properties-appmesh-virtualrouter-virtualrouterlistener-properties"></a>

`PortMapping`  <a name="cfn-appmesh-virtualrouter-virtualrouterlistener-portmapping"></a>
The port mapping information for the listener.
*Required*: Yes
*Type*: [PortMapping](aws-properties-appmesh-virtualrouter-portmapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
