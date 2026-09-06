---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3express-directorybucket-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::DirectoryBucket Tag
<a name="aws-properties-s3express-directorybucket-tag"></a>

A key-value pair that you use to label your directory buckets. You can add tags to new directory buckets when you create them, or you can add tags to existing directory buckets. Tags can help you organize, track costs for, and control access to directory buckets. For more information, see [Using tags with directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html).

## Syntax
<a name="aws-properties-s3express-directorybucket-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3express-directorybucket-tag-syntax.json"></a>

```
{
  "[Key](#cfn-s3express-directorybucket-tag-key)" : {{String}},
  "[Value](#cfn-s3express-directorybucket-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3express-directorybucket-tag-syntax.yaml"></a>

```
  [Key](#cfn-s3express-directorybucket-tag-key): {{String}}
  [Value](#cfn-s3express-directorybucket-tag-value): {{String}}
```

## Properties
<a name="aws-properties-s3express-directorybucket-tag-properties"></a>

`Key`  <a name="cfn-s3express-directorybucket-tag-key"></a>
The key of the tag. Tags are key-value pairs that you use to label your directory buckets. Tags can help you organize, track costs for, and control access to directory buckets. For more information, see [Using tags with directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html).
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:.*)([\p{L}\p{Z}\p{N}_.:=+\/\-@%]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-s3express-directorybucket-tag-value"></a>
The value of the tag. Tags are key-value pairs that you use to label your directory buckets. Tags can help you organize, track costs for, and control access to directory buckets. For more information, see [Using tags with directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html).
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:=+\/\-@%]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
