---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-subjectalternativenamematchers.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode SubjectAlternativeNameMatchers
<a name="aws-properties-appmesh-virtualnode-subjectalternativenamematchers"></a>

An object that represents the methods by which a subject alternative name on a peer Transport Layer Security (TLS) certificate can be matched.

## Syntax
<a name="aws-properties-appmesh-virtualnode-subjectalternativenamematchers-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-subjectalternativenamematchers-syntax.json"></a>

```
{
  "[Exact](#cfn-appmesh-virtualnode-subjectalternativenamematchers-exact)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-subjectalternativenamematchers-syntax.yaml"></a>

```
  [Exact](#cfn-appmesh-virtualnode-subjectalternativenamematchers-exact): {{
    - String}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-subjectalternativenamematchers-properties"></a>

`Exact`  <a name="cfn-appmesh-virtualnode-subjectalternativenamematchers-exact"></a>
The values sent must match the specified values exactly.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
