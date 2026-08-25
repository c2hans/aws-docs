---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-taskexecution-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::TaskExecution Tag
<a name="aws-properties-datasync-taskexecution-tag"></a>

<a name="aws-properties-datasync-taskexecution-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::DataSync::TaskExecution](aws-resource-datasync-taskexecution.md).

## Syntax
<a name="aws-properties-datasync-taskexecution-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-taskexecution-tag-syntax.json"></a>

```
{
  "[Key](#cfn-datasync-taskexecution-tag-key)" : {{String}},
  "[Value](#cfn-datasync-taskexecution-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-taskexecution-tag-syntax.yaml"></a>

```
  [Key](#cfn-datasync-taskexecution-tag-key): {{String}}
  [Value](#cfn-datasync-taskexecution-tag-value): {{String}}
```

## Properties
<a name="aws-properties-datasync-taskexecution-tag-properties"></a>

`Key`  <a name="cfn-datasync-taskexecution-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s+=._:/-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-datasync-taskexecution-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s+=._:@/-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
