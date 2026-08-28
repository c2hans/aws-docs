---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-backenddefaults.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode BackendDefaults
<a name="aws-properties-appmesh-virtualnode-backenddefaults"></a>

An object that represents the default properties for a backend.

## Syntax
<a name="aws-properties-appmesh-virtualnode-backenddefaults-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-backenddefaults-syntax.json"></a>

```
{
  "[ClientPolicy](#cfn-appmesh-virtualnode-backenddefaults-clientpolicy)" : {{ClientPolicy}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-backenddefaults-syntax.yaml"></a>

```
  [ClientPolicy](#cfn-appmesh-virtualnode-backenddefaults-clientpolicy): {{
    ClientPolicy}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-backenddefaults-properties"></a>

`ClientPolicy`  <a name="cfn-appmesh-virtualnode-backenddefaults-clientpolicy"></a>
A reference to an object that represents a client policy.
*Required*: No
*Type*: [ClientPolicy](aws-properties-appmesh-virtualnode-clientpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
