---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cassandra-table-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Table Tag
<a name="aws-properties-cassandra-table-tag"></a>

Describes a tag. A tag is a key-value pair. You can add up to 50 tags to a single Amazon Keyspaces resource.

AWS-assigned tag names and values are automatically assigned the `aws:` prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix `user:` in the Cost Allocation Report. You cannot backdate the application of a tag.

For more information, see [Adding tags and labels to Amazon Keyspaces resources](https://docs.aws.amazon.com/keyspaces/latest/devguide/tagging-keyspaces.html) in the *Amazon Keyspaces Developer Guide*.

## Syntax
<a name="aws-properties-cassandra-table-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cassandra-table-tag-syntax.json"></a>

```
{
  "[Key](#cfn-cassandra-table-tag-key)" : {{String}},
  "[Value](#cfn-cassandra-table-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cassandra-table-tag-syntax.yaml"></a>

```
  [Key](#cfn-cassandra-table-tag-key): {{String}}
  [Value](#cfn-cassandra-table-tag-value): {{String}}
```

## Properties
<a name="aws-properties-cassandra-table-tag-properties"></a>

`Key`  <a name="cfn-cassandra-table-tag-key"></a>
The key of the tag. Tag keys are case sensitive. Each Amazon Keyspaces resource can only have up to one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cassandra-table-tag-value"></a>
The value of the tag. Tag values are case-sensitive and can be null.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
