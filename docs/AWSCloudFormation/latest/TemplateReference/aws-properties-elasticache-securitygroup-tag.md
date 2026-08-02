---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-securitygroup-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::SecurityGroup Tag
<a name="aws-properties-elasticache-securitygroup-tag"></a>

A tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your ElastiCache resources, with the exception of global replication group. When you add or remove tags on replication groups, those actions will be replicated to all nodes in the replication group. A tag with a null Value is permitted.

## Syntax
<a name="aws-properties-elasticache-securitygroup-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-securitygroup-tag-syntax.json"></a>

```
{
  "[Key](#cfn-elasticache-securitygroup-tag-key)" : {{String}},
  "[Value](#cfn-elasticache-securitygroup-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticache-securitygroup-tag-syntax.yaml"></a>

```
  [Key](#cfn-elasticache-securitygroup-tag-key): {{String}}
  [Value](#cfn-elasticache-securitygroup-tag-value): {{String}}
```

## Properties
<a name="aws-properties-elasticache-securitygroup-tag-properties"></a>

`Key`  <a name="cfn-elasticache-securitygroup-tag-key"></a>
The key for the tag. May not be null.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-elasticache-securitygroup-tag-value"></a>
The tag's value. May be null.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
