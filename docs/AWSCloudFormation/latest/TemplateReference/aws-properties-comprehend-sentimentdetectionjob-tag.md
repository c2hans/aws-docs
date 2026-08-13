---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-comprehend-sentimentdetectionjob-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::SentimentDetectionJob Tag
<a name="aws-properties-comprehend-sentimentdetectionjob-tag"></a>

A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with the key-value pair ‘Department’:’Sales’ might be added to a resource to indicate its use by a particular department.

## Syntax
<a name="aws-properties-comprehend-sentimentdetectionjob-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-comprehend-sentimentdetectionjob-tag-syntax.json"></a>

```
{
  "[Key](#cfn-comprehend-sentimentdetectionjob-tag-key)" : {{String}},
  "[Value](#cfn-comprehend-sentimentdetectionjob-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-comprehend-sentimentdetectionjob-tag-syntax.yaml"></a>

```
  [Key](#cfn-comprehend-sentimentdetectionjob-tag-key): {{String}}
  [Value](#cfn-comprehend-sentimentdetectionjob-tag-value): {{String}}
```

## Properties
<a name="aws-properties-comprehend-sentimentdetectionjob-tag-properties"></a>

`Key`  <a name="cfn-comprehend-sentimentdetectionjob-tag-key"></a>
The initial part of a key-value pair that forms a tag associated with a given resource. For instance, if you want to show which resources are used by which departments, you might use “Department” as the key portion of the pair, with multiple possible values such as “sales,” “legal,” and “administration.”
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-comprehend-sentimentdetectionjob-tag-value"></a>
 The second part of a key-value pair that forms a tag associated with a given resource. For instance, if you want to show which resources are used by which departments, you might use “Department” as the initial (key) portion of the pair, with a value of “sales” to indicate the sales department.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
