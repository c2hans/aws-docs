---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-neptunegraph-graph-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NeptuneGraph::Graph Tag
<a name="aws-properties-neptunegraph-graph-tag"></a>

A key-value pair to associate with the Neptune Analytics graph.

## Syntax
<a name="aws-properties-neptunegraph-graph-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-neptunegraph-graph-tag-syntax.json"></a>

```
{
  "[Key](#cfn-neptunegraph-graph-tag-key)" : {{String}},
  "[Value](#cfn-neptunegraph-graph-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-neptunegraph-graph-tag-syntax.yaml"></a>

```
  [Key](#cfn-neptunegraph-graph-tag-key): {{String}}
  [Value](#cfn-neptunegraph-graph-tag-value): {{String}}
```

## Properties
<a name="aws-properties-neptunegraph-graph-tag-properties"></a>

`Key`  <a name="cfn-neptunegraph-graph-tag-key"></a>
**Key** (string)   –   A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length. It can't be prefixed with `AWS:` and can only contain the set of Unicode characters specified by this Java regular expression: `"^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$")`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-neptunegraph-graph-tag-value"></a>
**Value** (string)   –   A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length. It can't be prefixed with `AWS:` and can only contain the set of Unicode characters specified by this Java regular expression: `"^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$")`.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
