---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-clientpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode ClientPolicy
<a name="aws-properties-appmesh-virtualnode-clientpolicy"></a>

An object that represents a client policy.

## Syntax
<a name="aws-properties-appmesh-virtualnode-clientpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-clientpolicy-syntax.json"></a>

```
{
  "[TLS](#cfn-appmesh-virtualnode-clientpolicy-tls)" : {{ClientPolicyTls}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-clientpolicy-syntax.yaml"></a>

```
  [TLS](#cfn-appmesh-virtualnode-clientpolicy-tls): {{
    ClientPolicyTls}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-clientpolicy-properties"></a>

`TLS`  <a name="cfn-appmesh-virtualnode-clientpolicy-tls"></a>
A reference to an object that represents a Transport Layer Security (TLS) client policy.
*Required*: No
*Type*: [ClientPolicyTls](aws-properties-appmesh-virtualnode-clientpolicytls.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
