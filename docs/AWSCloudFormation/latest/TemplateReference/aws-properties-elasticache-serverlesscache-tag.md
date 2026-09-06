---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-serverlesscache-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::ServerlessCache Tag
<a name="aws-properties-elasticache-serverlesscache-tag"></a>

A tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your ElastiCache resources. When you add or remove tags on replication groups, those actions will be replicated to all nodes in the replication group. A tag with a null Value is permitted.

## Syntax
<a name="aws-properties-elasticache-serverlesscache-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-serverlesscache-tag-syntax.json"></a>

```
{
  "[Key](#cfn-elasticache-serverlesscache-tag-key)" : {{String}},
  "[Value](#cfn-elasticache-serverlesscache-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticache-serverlesscache-tag-syntax.yaml"></a>

```
  [Key](#cfn-elasticache-serverlesscache-tag-key): {{String}}
  [Value](#cfn-elasticache-serverlesscache-tag-value): {{String}}
```

## Properties
<a name="aws-properties-elasticache-serverlesscache-tag-properties"></a>

`Key`  <a name="cfn-elasticache-serverlesscache-tag-key"></a>
The key for the tag. May not be null.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z0-9 _\.\/=+:\-@]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-elasticache-serverlesscache-tag-value"></a>
The tag's value. May be null.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9 _\.\/=+:\-@]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
