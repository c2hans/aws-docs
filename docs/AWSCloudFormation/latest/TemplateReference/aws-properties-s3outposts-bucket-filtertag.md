---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3outposts-bucket-filtertag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Outposts::Bucket FilterTag
<a name="aws-properties-s3outposts-bucket-filtertag"></a>

<a name="aws-properties-s3outposts-bucket-filtertag-description"></a>The `FilterTag` property type specifies Property description not available. for an [AWS::S3Outposts::Bucket](aws-resource-s3outposts-bucket.md).

## Syntax
<a name="aws-properties-s3outposts-bucket-filtertag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3outposts-bucket-filtertag-syntax.json"></a>

```
{
  "[Key](#cfn-s3outposts-bucket-filtertag-key)" : {{String}},
  "[Value](#cfn-s3outposts-bucket-filtertag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3outposts-bucket-filtertag-syntax.yaml"></a>

```
  [Key](#cfn-s3outposts-bucket-filtertag-key): {{String}}
  [Value](#cfn-s3outposts-bucket-filtertag-value): {{String}}
```

## Properties
<a name="aws-properties-s3outposts-bucket-filtertag-properties"></a>

`Key`  <a name="cfn-s3outposts-bucket-filtertag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:=+\/\-@%]*)$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-s3outposts-bucket-filtertag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:=+\/\-@%]*)$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
