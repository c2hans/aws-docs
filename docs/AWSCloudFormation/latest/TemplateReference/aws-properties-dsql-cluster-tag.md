---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dsql-cluster-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DSQL::Cluster Tag
<a name="aws-properties-dsql-cluster-tag"></a>

Defines a tag for an cluster.

## Syntax
<a name="aws-properties-dsql-cluster-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dsql-cluster-tag-syntax.json"></a>

```
{
  "[Key](#cfn-dsql-cluster-tag-key)" : {{String}},
  "[Value](#cfn-dsql-cluster-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-dsql-cluster-tag-syntax.yaml"></a>

```
  [Key](#cfn-dsql-cluster-tag-key): {{String}}
  [Value](#cfn-dsql-cluster-tag-value): {{String}}
```

## Properties
<a name="aws-properties-dsql-cluster-tag-properties"></a>

`Key`  <a name="cfn-dsql-cluster-tag-key"></a>
Unique tag key, maximum 128 Unicode characters in UTF-8.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-dsql-cluster-tag-value"></a>
Tag value, maximum 256 Unicode characters in UTF-8.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
