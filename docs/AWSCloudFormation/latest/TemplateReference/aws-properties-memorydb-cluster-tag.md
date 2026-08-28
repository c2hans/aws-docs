---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-memorydb-cluster-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MemoryDB::Cluster Tag
<a name="aws-properties-memorydb-cluster-tag"></a>

A tag that can be added to an MemoryDB resource. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your MemoryDB resources. When you add or remove tags on clusters, those actions will be replicated to all nodes in the cluster. A tag with a null Value is permitted. For more information, see [Tagging your MemoryDB resources](https://docs.aws.amazon.com/MemoryDB/latest/devguide/tagging-resources.html)

## Syntax
<a name="aws-properties-memorydb-cluster-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-memorydb-cluster-tag-syntax.json"></a>

```
{
  "[Key](#cfn-memorydb-cluster-tag-key)" : {{String}},
  "[Value](#cfn-memorydb-cluster-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-memorydb-cluster-tag-syntax.yaml"></a>

```
  [Key](#cfn-memorydb-cluster-tag-key): {{String}}
  [Value](#cfn-memorydb-cluster-tag-value): {{String}}
```

## Properties
<a name="aws-properties-memorydb-cluster-tag-properties"></a>

`Key`  <a name="cfn-memorydb-cluster-tag-key"></a>
The key for the tag. May not be null.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)(?!memorydb:)[a-zA-Z0-9 _\.\/=+:\-@]{1,128}$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-memorydb-cluster-tag-value"></a>
The tag's value. May be null.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)(?!memorydb:)[a-zA-Z0-9 _\.\/=+:\-@]{1,256}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
