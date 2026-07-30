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
