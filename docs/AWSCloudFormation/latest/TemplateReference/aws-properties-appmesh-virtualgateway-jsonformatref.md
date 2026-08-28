---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-jsonformatref.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway JsonFormatRef
<a name="aws-properties-appmesh-virtualgateway-jsonformatref"></a>

An object that represents the key value pairs for the JSON.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-jsonformatref-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-jsonformatref-syntax.json"></a>

```
{
  "[Key](#cfn-appmesh-virtualgateway-jsonformatref-key)" : {{String}},
  "[Value](#cfn-appmesh-virtualgateway-jsonformatref-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-jsonformatref-syntax.yaml"></a>

```
  [Key](#cfn-appmesh-virtualgateway-jsonformatref-key): {{String}}
  [Value](#cfn-appmesh-virtualgateway-jsonformatref-value): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-jsonformatref-properties"></a>

`Key`  <a name="cfn-appmesh-virtualgateway-jsonformatref-key"></a>
The specified key for the JSON.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appmesh-virtualgateway-jsonformatref-value"></a>
The specified value for the JSON.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
