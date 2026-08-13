---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-location-job-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Location::Job Tag
<a name="aws-properties-location-job-tag"></a>

<a name="aws-properties-location-job-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::Location::Job](aws-resource-location-job.md).

## Syntax
<a name="aws-properties-location-job-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-location-job-tag-syntax.json"></a>

```
{
  "[Key](#cfn-location-job-tag-key)" : {{String}},
  "[Value](#cfn-location-job-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-location-job-tag-syntax.yaml"></a>

```
  [Key](#cfn-location-job-tag-key): {{String}}
  [Value](#cfn-location-job-tag-value): {{String}}
```

## Properties
<a name="aws-properties-location-job-tag-properties"></a>

`Key`  <a name="cfn-location-job-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-location-job-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
