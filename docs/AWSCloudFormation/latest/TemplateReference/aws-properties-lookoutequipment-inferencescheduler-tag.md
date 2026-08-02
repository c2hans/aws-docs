---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lookoutequipment-inferencescheduler-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LookoutEquipment::InferenceScheduler Tag
<a name="aws-properties-lookoutequipment-inferencescheduler-tag"></a>

A tag is a key-value pair that can be added to a resource as metadata.

## Syntax
<a name="aws-properties-lookoutequipment-inferencescheduler-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lookoutequipment-inferencescheduler-tag-syntax.json"></a>

```
{
  "[Key](#cfn-lookoutequipment-inferencescheduler-tag-key)" : {{String}},
  "[Value](#cfn-lookoutequipment-inferencescheduler-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-lookoutequipment-inferencescheduler-tag-syntax.yaml"></a>

```
  [Key](#cfn-lookoutequipment-inferencescheduler-tag-key): {{String}}
  [Value](#cfn-lookoutequipment-inferencescheduler-tag-value): {{String}}
```

## Properties
<a name="aws-properties-lookoutequipment-inferencescheduler-tag-properties"></a>

`Key`  <a name="cfn-lookoutequipment-inferencescheduler-tag-key"></a>
The key for the specified tag.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-lookoutequipment-inferencescheduler-tag-value"></a>
The value for the specified tag.
*Required*: Yes
*Type*: String
*Pattern*: `[\s\w+-=\.:/@]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
