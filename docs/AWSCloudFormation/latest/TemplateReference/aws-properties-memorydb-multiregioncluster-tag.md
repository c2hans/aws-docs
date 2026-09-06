---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-memorydb-multiregioncluster-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MemoryDB::MultiRegionCluster Tag
<a name="aws-properties-memorydb-multiregioncluster-tag"></a>

A tag that can be added to an MemoryDB resource. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your MemoryDB resources. When you add or remove tags on clusters, those actions will be replicated to all nodes in the cluster. A tag with a null Value is permitted. For more information, see [Tagging your MemoryDB resources](https://docs.aws.amazon.com/MemoryDB/latest/devguide/tagging-resources.html)

## Syntax
<a name="aws-properties-memorydb-multiregioncluster-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-memorydb-multiregioncluster-tag-syntax.json"></a>

```
{
  "[Key](#cfn-memorydb-multiregioncluster-tag-key)" : {{String}},
  "[Value](#cfn-memorydb-multiregioncluster-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-memorydb-multiregioncluster-tag-syntax.yaml"></a>

```
  [Key](#cfn-memorydb-multiregioncluster-tag-key): {{String}}
  [Value](#cfn-memorydb-multiregioncluster-tag-value): {{String}}
```

## Properties
<a name="aws-properties-memorydb-multiregioncluster-tag-properties"></a>

`Key`  <a name="cfn-memorydb-multiregioncluster-tag-key"></a>
The key for the tag. May not be null.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)(?!memorydb:)[a-zA-Z0-9 _\.\/=+:\-@]{1,128}$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-memorydb-multiregioncluster-tag-value"></a>
The tag's value. May be null.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)(?!memorydb:)[a-zA-Z0-9 _\.\/=+:\-@]{1,256}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
