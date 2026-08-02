---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-docdb-globalcluster-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DocDB::GlobalCluster Tag
<a name="aws-properties-docdb-globalcluster-tag"></a>

Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

## Syntax
<a name="aws-properties-docdb-globalcluster-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-docdb-globalcluster-tag-syntax.json"></a>

```
{
  "[Key](#cfn-docdb-globalcluster-tag-key)" : {{String}},
  "[Value](#cfn-docdb-globalcluster-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-docdb-globalcluster-tag-syntax.yaml"></a>

```
  [Key](#cfn-docdb-globalcluster-tag-key): {{String}}
  [Value](#cfn-docdb-globalcluster-tag-value): {{String}}
```

## Properties
<a name="aws-properties-docdb-globalcluster-tag-properties"></a>

`Key`  <a name="cfn-docdb-globalcluster-tag-key"></a>
The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with "`aws:`" or "`rds:`". The string can contain only the set of Unicode letters, digits, white space, '\_', '.', '/', '=', '\+', '-' (Java regex: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-]\*)$").
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-docdb-globalcluster-tag-value"></a>
The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with "`aws:`" or "`rds:`". The string can contain only the set of Unicode letters, digits, white space, '\_', '.', '/', '=', '\+', '-' (Java regex: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-]\*)$").
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
