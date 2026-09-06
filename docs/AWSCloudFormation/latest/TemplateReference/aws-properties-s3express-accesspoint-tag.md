---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3express-accesspoint-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::AccessPoint Tag
<a name="aws-properties-s3express-accesspoint-tag"></a>

A key-value pair that you use to label your access points. You can add tags to new access points when you create them, or you can add tags to existing access points. Tags can help you organize and control access to access points. For more information, see [Using tags for attribute-based access control (ABAC)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#using-tags-for-abac).

## Syntax
<a name="aws-properties-s3express-accesspoint-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3express-accesspoint-tag-syntax.json"></a>

```
{
  "[Key](#cfn-s3express-accesspoint-tag-key)" : {{String}},
  "[Value](#cfn-s3express-accesspoint-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3express-accesspoint-tag-syntax.yaml"></a>

```
  [Key](#cfn-s3express-accesspoint-tag-key): {{String}}
  [Value](#cfn-s3express-accesspoint-tag-value): {{String}}
```

## Properties
<a name="aws-properties-s3express-accesspoint-tag-properties"></a>

`Key`  <a name="cfn-s3express-accesspoint-tag-key"></a>
The key of the tag. Tags are key-value pairs that you use to label your access points. Tags can help you organize and control access to access points. For more information, see [Tagging S3 resources for cost allocation or attribute-based access control (ABAC)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html).
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:.*)([\p{L}\p{Z}\p{N}_.:=+\/\-@%]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-s3express-accesspoint-tag-value"></a>
The value of the tag. Tags are key-value pairs that you use to label your access points. Tags can help you organize and control access to access points. For more information, see [Tagging S3 resources for cost allocation or attribute-based access control (ABAC)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html).
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:=+\/\-@%]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
