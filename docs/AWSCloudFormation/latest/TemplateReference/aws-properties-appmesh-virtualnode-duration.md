---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-duration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode Duration
<a name="aws-properties-appmesh-virtualnode-duration"></a>

An object that represents a duration of time.

## Syntax
<a name="aws-properties-appmesh-virtualnode-duration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-duration-syntax.json"></a>

```
{
  "[Unit](#cfn-appmesh-virtualnode-duration-unit)" : {{String}},
  "[Value](#cfn-appmesh-virtualnode-duration-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-duration-syntax.yaml"></a>

```
  [Unit](#cfn-appmesh-virtualnode-duration-unit): {{String}}
  [Value](#cfn-appmesh-virtualnode-duration-value): {{Integer}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-duration-properties"></a>

`Unit`  <a name="cfn-appmesh-virtualnode-duration-unit"></a>
A unit of time.
*Required*: Yes
*Type*: String
*Allowed values*: `s | ms`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appmesh-virtualnode-duration-value"></a>
A number of time units.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
