---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationsmb-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationSMB Tag
<a name="aws-properties-datasync-locationsmb-tag"></a>

<a name="aws-properties-datasync-locationsmb-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::DataSync::LocationSMB](aws-resource-datasync-locationsmb.md).

## Syntax
<a name="aws-properties-datasync-locationsmb-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationsmb-tag-syntax.json"></a>

```
{
  "[Key](#cfn-datasync-locationsmb-tag-key)" : {{String}},
  "[Value](#cfn-datasync-locationsmb-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-locationsmb-tag-syntax.yaml"></a>

```
  [Key](#cfn-datasync-locationsmb-tag-key): {{String}}
  [Value](#cfn-datasync-locationsmb-tag-value): {{String}}
```

## Properties
<a name="aws-properties-datasync-locationsmb-tag-properties"></a>

`Key`  <a name="cfn-datasync-locationsmb-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s+=._:/-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-datasync-locationsmb-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s+=._:@/-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
