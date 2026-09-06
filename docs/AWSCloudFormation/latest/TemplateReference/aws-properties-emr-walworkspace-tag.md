---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-walworkspace-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::WALWorkspace Tag
<a name="aws-properties-emr-walworkspace-tag"></a>

A key-value pair containing user-defined metadata that you can associate with an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see [Tag Clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html).

## Syntax
<a name="aws-properties-emr-walworkspace-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-walworkspace-tag-syntax.json"></a>

```
{
  "[Key](#cfn-emr-walworkspace-tag-key)" : {{String}},
  "[Value](#cfn-emr-walworkspace-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-emr-walworkspace-tag-syntax.yaml"></a>

```
  [Key](#cfn-emr-walworkspace-tag-key): {{String}}
  [Value](#cfn-emr-walworkspace-tag-value): {{String}}
```

## Properties
<a name="aws-properties-emr-walworkspace-tag-properties"></a>

`Key`  <a name="cfn-emr-walworkspace-tag-key"></a>
A user-defined key, which is the minimum required information for a valid tag. For more information, see [Tag](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-emr-walworkspace-tag-value"></a>
A user-defined value, which is optional in a tag. For more information, see [Tag Clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html).
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
