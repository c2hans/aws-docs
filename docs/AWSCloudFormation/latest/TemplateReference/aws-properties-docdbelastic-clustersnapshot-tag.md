---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-docdbelastic-clustersnapshot-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DocDBElastic::ClusterSnapshot Tag
<a name="aws-properties-docdbelastic-clustersnapshot-tag"></a>

<a name="aws-properties-docdbelastic-clustersnapshot-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::DocDBElastic::ClusterSnapshot](aws-resource-docdbelastic-clustersnapshot.md).

## Syntax
<a name="aws-properties-docdbelastic-clustersnapshot-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-docdbelastic-clustersnapshot-tag-syntax.json"></a>

```
{
  "[Key](#cfn-docdbelastic-clustersnapshot-tag-key)" : {{String}},
  "[Value](#cfn-docdbelastic-clustersnapshot-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-docdbelastic-clustersnapshot-tag-syntax.yaml"></a>

```
  [Key](#cfn-docdbelastic-clustersnapshot-tag-key): {{String}}
  [Value](#cfn-docdbelastic-clustersnapshot-tag-value): {{String}}
```

## Properties
<a name="aws-properties-docdbelastic-clustersnapshot-tag-properties"></a>

`Key`  <a name="cfn-docdbelastic-clustersnapshot-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-docdbelastic-clustersnapshot-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
