---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-osis-pipeline-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OSIS::Pipeline Tag
<a name="aws-properties-osis-pipeline-tag"></a>

A tag (key-value pair) for an OpenSearch Ingestion pipeline.

## Syntax
<a name="aws-properties-osis-pipeline-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-osis-pipeline-tag-syntax.json"></a>

```
{
  "[Key](#cfn-osis-pipeline-tag-key)" : {{String}},
  "[Value](#cfn-osis-pipeline-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-osis-pipeline-tag-syntax.yaml"></a>

```
  [Key](#cfn-osis-pipeline-tag-key): {{String}}
  [Value](#cfn-osis-pipeline-tag-value): {{String}}
```

## Properties
<a name="aws-properties-osis-pipeline-tag-properties"></a>

`Key`  <a name="cfn-osis-pipeline-tag-key"></a>
The tag key. Tag keys must be unique for the pipeline to which they are attached.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-osis-pipeline-tag-value"></a>
The value assigned to the corresponding tag key. Tag values can be null and don't have to be unique in a tag set. For example, you can have a key value pair in a tag set of `project : Trinity` and `cost-center : Trinity`
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
