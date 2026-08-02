---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-healthlake-fhirdatastore-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::HealthLake::FHIRDatastore Tag
<a name="aws-properties-healthlake-fhirdatastore-tag"></a>

A label consisting of a user-defined key and value. The form for tags is {"Key", "Value"}

## Syntax
<a name="aws-properties-healthlake-fhirdatastore-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-healthlake-fhirdatastore-tag-syntax.json"></a>

```
{
  "[Key](#cfn-healthlake-fhirdatastore-tag-key)" : {{String}},
  "[Value](#cfn-healthlake-fhirdatastore-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-healthlake-fhirdatastore-tag-syntax.yaml"></a>

```
  [Key](#cfn-healthlake-fhirdatastore-tag-key): {{String}}
  [Value](#cfn-healthlake-fhirdatastore-tag-value): {{String}}
```

## Properties
<a name="aws-properties-healthlake-fhirdatastore-tag-properties"></a>

`Key`  <a name="cfn-healthlake-fhirdatastore-tag-key"></a>
The key portion of a tag. Tag keys are case sensitive.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-healthlake-fhirdatastore-tag-value"></a>
 The value portion of a tag. Tag values are case-sensitive.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
