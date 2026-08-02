---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-optiongroup-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::OptionGroup Tag
<a name="aws-properties-rds-optiongroup-tag"></a>

Metadata assigned to an Amazon RDS resource consisting of a key-value pair.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.

## Syntax
<a name="aws-properties-rds-optiongroup-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rds-optiongroup-tag-syntax.json"></a>

```
{
  "[Key](#cfn-rds-optiongroup-tag-key)" : {{String}},
  "[Value](#cfn-rds-optiongroup-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-rds-optiongroup-tag-syntax.yaml"></a>

```
  [Key](#cfn-rds-optiongroup-tag-key): {{String}}
  [Value](#cfn-rds-optiongroup-tag-value): {{String}}
```

## Properties
<a name="aws-properties-rds-optiongroup-tag-properties"></a>

`Key`  <a name="cfn-rds-optiongroup-tag-key"></a>
A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with `aws:` or `rds:`. The string can only contain only the set of Unicode letters, digits, white-space, '\_', '.', ':', '/', '=', '\+', '-', '@' (Java regex: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-@]\*)$").
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-rds-optiongroup-tag-value"></a>
A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with `aws:` or `rds:`. The string can only contain only the set of Unicode letters, digits, white-space, '\_', '.', ':', '/', '=', '\+', '-', '@' (Java regex: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-@]\*)$").
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-rds-optiongroup-tag--examples"></a>

The following example specifies a tag for an option group.

###
<a name="aws-properties-rds-optiongroup-tag--examples--"></a>

#### JSON
<a name="aws-properties-rds-optiongroup-tag--examples----json"></a>

```
"Tags" : [
   {
      "Key" : "keyname1",
      "Value" : "value1"
   },
   {
      "Key" : "keyname2",
      "Value" : "value2"
   }
]
```

#### YAML
<a name="aws-properties-rds-optiongroup-tag--examples----yaml"></a>

```
Tags:
  - Key: keyname1
    Value: value1
  - Key: keyname2
    Value: value2
```
